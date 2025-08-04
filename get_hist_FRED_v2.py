#!D:\Documents\Python\NII_PROJECT\bankstress\Scripts\python.exe

from datetime import datetime, timedelta
from pathlib import Path
import os
import sys

import pandas as pd
import numpy as np

import requests
from fredapi import Fred
from dotenv import load_dotenv
from cachetools import TTLCache
print(os.getcwd())

# --------- CONFIG ----------------------------------------------------------- #

YEARS_BACK      = 10                      
OUTPUT_XLSX     = "macro_indicators.xlsx"


# Series IDs and the aggregation method to turn *raw* observations -> quarterly
SERIES = {
    # Activity & prices
    "REAL_GDP"             : ("GDPC1",      "mean"),
    "NOMINAL_GDP"          : ("GDP",        "mean"),
    "REAL_DPI"             : ("DSPIC96",    "mean"),
    "NOMINAL_DPI"          : ("DSPI",       "mean"),
    "UNEMPLOYMENT_RATE"    : ("UNRATE",     "mean"),
    "CPI"                  : ("CPIAUCSL",   "mean"),

    # Rates
    "T_BILL_3M"            : ("DTB3",       "mean"),
    "UST_5Y"               : ("DGS5",       "mean"),
    "UST_10Y"              : ("GS10",       "mean"),
    "BBB_YIELD"            : ("BAA",        "mean"),
    "MORTGAGE_30Y"         : ("MORTGAGE30US","mean"),
    "PRIME_RATE"           : ("MPRIME",     "mean"),

    # Asset prices
    "EQUITY_INDEX"         : ("DJIA",      "mean"), 
    "HOUSE_PRICE_INDEX"    : ("USSTHPI",    "mean"),
    "CRE_PRICE_INDEX"      : ("BOGZ1FL075035503Q", "mean"),
    "VIX_MAX"              : ("VIXCLS",     "max"),    # Fed uses Q.max
}

# --------- ENV & API -------------------------------------------------------- #

load_dotenv()
API_KEY   = os.getenv("FRED_API_KEY")
if not API_KEY:
    sys.exit(" FRED_API_KEY missing add it to .env")

fred      = Fred(api_key=API_KEY)
session   = requests.Session()               # re-use TCP socket
cache     = TTLCache(maxsize=1000, ttl=900)  # 15-min soft cache

# --------- HELPERS ---------------------------------------------------------- #

def fetch_series(series_id: str, start: datetime, end: datetime) -> pd.Series:
    """Get raw observations, honour simple caching, return a pd.Series."""
    cache_key = (series_id, start.date(), end.date())
    if cache_key in cache:
        return cache[cache_key]

    data = fred.get_series(series_id,
                           observation_start=start,
                           observation_end=end,
                           session=session)
    cache[cache_key] = data
    return data

def to_quarterly(raw: pd.Series, rule: str) -> pd.Series:
    """Down-sample to quarter-end; rule ∈ {'mean','max'} ."""
    # Ensure DateTimeIndex
    s = raw.copy()
    if s.index.tz:
        s.index = s.index.tz_localize(None)
    if not isinstance(s.index, pd.DatetimeIndex):
        s.index = pd.to_datetime(s.index)

    # Some series (e.g., USSTHPI) are already quarterly – guard against double resample
    if s.index.freq == 'QE':
        return s
    method = s.resample('QE')
    return method.mean() if rule == "mean" else method.max()

# --------- MAIN ------------------------------------------------------------- #

def build_dataset(years_back: int) -> pd.DataFrame:
    end   = datetime.today()
    start = end - timedelta(days=365 * years_back)

    qtr_frames   = {}
    first_dates  = []    # track earliest common point
    for pretty, (sid, agg) in SERIES.items():
        print(f"fetching {pretty} ({sid}) …", flush=True)
        raw        = fetch_series(sid, start, end)
        qt         = to_quarterly(raw, agg).rename(pretty)
        qtr_frames[pretty] = qt
        first_dates.append(qt.first_valid_index())

    # align on the *latest* first_valid_index so every series has data
    common_start = max(first_dates)
    aligned      = [s.loc[common_start:] for s in qtr_frames.values()]
    df           = pd.concat(aligned, axis=1).dropna(how="any")

    # sanity check
    if df.isna().any().any():
        raise ValueError("Still found NaNs investigate frequency handling.")

    df.index.name = "QuarterEnd"
    return df

if __name__ == "__main__":
    df = build_dataset(YEARS_BACK)

    growth_map = {
    "REAL_GDP"   : "REAL_GDP_G",
    "NOMINAL_GDP": "NOMINAL_GDP_G",
    "REAL_DPI"   : "REAL_DPI_G",
    "NOMINAL_DPI": "NOMINAL_DPI_G",
    "CPI"        : "CPI_G",
    }

    for level_col, growth_col in growth_map.items():
        # 400 * ln(X_t / X_{t-1})  ==> annualised percent
        df[growth_col] = 400 * np.log(df[level_col] / df[level_col].shift(1))

    # Drop first row (it has NaNs because of the shift)
    df = df.dropna().copy()


    df.to_excel(OUTPUT_XLSX)
    #df.to_csv(OUTPUT_CSV)
    print(f" SAVED {len(df)} rows ({df.columns.size} variables) to {OUTPUT_XLSX} ")



