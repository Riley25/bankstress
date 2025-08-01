from fredapi import Fred
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# ------------------------
# USER SETTINGS
# ------------------------

FRED_API_KEY = os.getenv("FRED_API_KEY") or "fc29b91df570ee581c1ff199dc2c1097"
YEARS_BACK = 15  # set to 10, 15, or 20
OUTPUT_FILE = "macro_28_indicators.csv"

# ------------------------
# 28 Indicator Series IDs from Federal Reserve's Supervisory Scenarios
# ------------------------

FRED_SERIES_IDS = {
    "Real_GDP": "GDPC1",
    "CPI": "CPIAUCSL",
    "Unemployment_Rate": "UNRATE",
    "3mo_Treasury": "GS3M",
    "5yr_Treasury": "GS5",
    "10yr_Treasury": "GS10",
    "BBB_Corporate_Yield": "BAA10Y",
    "Mortgage_Rate": "MORTGAGE30US",
    "House_Price_Index": "USSTHPI",
    "Dow_Jones": "DJIA",
    "S&P_500": "SP500",
    "Nominal_GDP": "GDP",
    "Fed_Funds": "FEDFUNDS",
    "Oil_Price_WTI": "DCOILWTICO",
    "Dollar_Index": "DTWEXBGS",
    "Consumer_Confidence": "UMCSENT",
    "VIX": "VIXCLS",
    "Prime_Rate": "MPRIME",
    "Credit_Card_Rate": "TERMCBCCALLNS",
    "Auto_Loan_Rate": "TERMCBAUTO48NS",
    "Industrial_Production": "INDPRO",
    "Retail_Sales": "RSAFS",
    "Payroll_Employment": "PAYEMS",
    "PCE_Inflation": "PCEPI",
    "Net_Exports": "NETEXP",
    "Total_Reserves": "TREAST",
    "Bank_Credit": "TOTBKCR"
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
    df.to_csv(OUTPUT_FILE)
    print(f"\n✅ Done. Saved to {OUTPUT_FILE}")


