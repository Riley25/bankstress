### Bank Stress

A Streamlit-powered web app that lets anyone pull public data, apply Fed scenarios, and instantly stress-test any U.S. bank’s balance-sheet.

### What it does
- Fetches data automatically

- Call-Report & UBPR fields via the FDIC Bank Financials API 

- 28 macro drivers from FRED with fredapi 

- Annual Baseline & Severely-Adverse scenario CSVs from the Fed’s stress-test page Federal Reserve

- Computes product-level loan yields, deposit betas, NCO ratios, and other model inputs.

- Runs a 13-quarter projection engine for balances, NII, losses, ACL, and capital.

- Shows results in interactive Altair/Plotly charts plus CSV / JSON audit downloads (SR 11-7 traceability).

