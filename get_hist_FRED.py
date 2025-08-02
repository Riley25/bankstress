from fredapi import Fred
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

# ------------------------
# USER SETTINGS
# ------------------------

FRED_API_KEY = os.getenv("FRED_API_KEY")

YEARS_BACK = 10  # set to 10, 15, or 20
OUTPUT_FILE = "macro_28_indicators.xlsx"

# ------------------------
# 28 Indicator Series IDs from Federal Reserve's Supervisory Scenarios
# ------------------------

FRED_SERIES_IDS = {
    # Activity & prices
    "Real_GDP": "GDPC1",
    "Nominal_GDP": "GDP",
    "Real_DPI": "DSPIC96",
    "Nominal_DPI": "DSPI",
    "Unemployment_Rate": "UNRATE",
    "CPI": "CPIAUCSL",

    # Rates
    "TBill_3m": "DTB3",
    "UST_5y": "DGS5",
    "UST_10y": "GS10",
    "BBB_Yield": "BAA10Y",
    "Mortgage_30y": "MORTGAGE30US",
    "Prime_Rate": "MPRIME",

    # Asset prices
    "Equity_Index": "SP500",         
    "House_Price_Index": "BOGZ1FL075035243Q",
    "CRE_Price_Index": "BOGZ1FL075035503Q",
    "VIX": "VIXCLS",
}


# ------------------------
# Pull Data
# ------------------------

def fetch_macro_data(years_back: int):
    fred = Fred(api_key=FRED_API_KEY)

    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * years_back)

    all_data = pd.DataFrame()

    for name, series_id in FRED_SERIES_IDS.items():
        try:
            print(f"Fetching {name} ({series_id})...")
            data = fred.get_series(series_id, observation_start=start_date, observation_end=end_date)
            data = data.rename(name)
            all_data = pd.concat([all_data, data], axis=1)
        except Exception as e:
            print(f"⚠️ Error fetching {name}: {e}")

    return all_data


# ------------------------
# Save to CSV
# ------------------------

if __name__ == "__main__":
    df = fetch_macro_data(YEARS_BACK)
    df.index.name = "Date"
    df.to_excel(OUTPUT_FILE)

    print(f"\n✅ Done. Saved to {OUTPUT_FILE}")


