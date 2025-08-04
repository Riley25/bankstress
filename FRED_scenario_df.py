
import pandas as pd


ADVERSE_DOMESTIC_2023 = pd.DataFrame({ 'Scenario Name': [ 'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse'],
    'Date': ['2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1'],
    'Real GDP growth': [-12.5, -6.7, -8.0, -5.9, -1.8, 0.6, 0.9, 6.3, 5.9, 5.6, 5.3, 5.0, 4.7],
    'Nominal GDP growth': [-10.1, -5.3, -7.0, -4.9, -0.7, 1.9, 2.2, 7.6, 7.2, 6.4, 6.3, 6.1, 6.0],
    'Real disposable income growth': [-7.9, -3.0, -3.4, -2.1, 0.3, 1.5, 1.7, 5.3, 5.3, 5.1, 4.8, 4.5, 4.2],
    'Nominal disposable income growth': [-5.8, -1.8, -2.4, -0.9, 1.6, 2.8, 2.9, 6.6, 6.7, 6.5, 6.3, 6.0, 5.7],
    'Unemployment rate': [5.6, 6.8, 8.1, 9.2, 9.7, 9.9, 10.0, 9.5, 9.0, 8.6, 8.2, 7.8, 7.5],
    'CPI inflation rate': [2.3, 1.5, 1.3, 1.3, 1.4, 1.4, 1.4, 1.5, 1.5, 1.5, 1.6, 1.6, 1.6],
    '3-month Treasury rate': [1.7, 1.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    '5-year Treasury yield': [1.2, 0.9, 0.8, 0.8, 0.9, 0.9, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1],
    '10-year Treasury yield': [1.1, 0.8, 0.8, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.3, 1.4, 1.5, 1.5],
    'BBB corporate yield': [5.8, 6.3, 6.5, 6.6, 6.4, 6.1, 5.8, 5.5, 5.1, 4.8, 4.5, 4.1, 3.8],
    'Mortgage rate': [4.0, 3.7, 3.8, 3.8, 3.8, 3.7, 3.5, 3.4, 3.3, 3.2, 3.1, 3.1, 3.1],
    'Prime rate': [4.7, 4.0, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1],
    'Dow Jones Total Stock Market Index (Level)': [24338.0, 22131.8, 21501.5, 21186.3, 21816.7, 22762.2, 24022.8, 25598.7, 27489.7, 29380.7, 32217.2, 35368.9, 38520.6],
    'House Price Index (Level)': [248.8, 228.6, 212.9, 201.7, 194.3, 189.5, 186.1, 191.2, 196.4, 201.6, 206.7, 211.7, 215.9],
    'Commercial Real Estate Price Index (Level)': [347.6, 336.9, 322.5, 301.0, 276.7, 255.2, 233.7, 215.0, 217.7, 220.4, 223.1, 225.7, 228.3],
    'Market Volatility Index (Level)': [70.0, 75.0, 65.4, 58.0, 52.1, 47.4, 43.6, 40.6, 38.2, 36.2, 34.7, 33.4, 32.4]})

clean = ADVERSE_DOMESTIC_2023["Date"].str.replace(" ", "")  
periods = pd.PeriodIndex(clean, freq="Q") 
ADVERSE_DOMESTIC_2023["Date"] = periods.to_timestamp("Q")


# --------- 2023 BASELINE ---------------------------------------------------------- #

BASELINE_DOMESTIC_2023 = pd.DataFrame({'Scenario Name': ['Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline'],
    'Date': ['2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1'],
    'Real GDP growth': [-0.5, -0.9, 0.0, 0.9, 1.5, 1.9, 2.2, 2.3, 2.2, 2.1, 2.1, 2.1, 2.0],
    'Nominal GDP growth': [2.9, 2.1, 2.6, 3.4, 3.9, 4.1, 4.3, 4.4, 4.4, 3.9, 3.8, 3.8, 3.9],
    'Real disposable income growth': [1.8, 0.7, 1.5, 2.0, 2.4, 2.4, 2.4, 2.4, 2.1, 2.0, 2.0, 2.0, 2.0],
    'Nominal disposable income growth': [5.1, 3.5, 4.0, 4.3, 4.6, 4.5, 4.3, 4.4, 4.2, 4.1, 4.0, 4.0, 4.0],
    'Unemployment rate': [3.9, 4.3, 4.6, 4.8, 4.9, 4.9, 4.8, 4.7, 4.6, 4.6, 4.6, 4.6, 4.6],
    'CPI inflation rate': [3.2, 2.9, 2.7, 2.4, 2.2, 2.1, 2.2, 2.1, 2.2, 2.2, 2.2, 2.2, 2.2],
    '3-month Treasury rate': [4.7, 4.8, 4.6, 4.4, 4.0, 3.7, 3.3, 3.1, 3.0, 3.0, 3.0, 3.0, 3.0],
    '5-year Treasury yield': [4.0, 4.0, 3.9, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0, 3.0, 2.9],
    '10-year Treasury yield': [3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.3, 3.3, 3.3, 3.3, 3.2, 3.2],
    'BBB corporate yield': [5.9, 5.8, 5.6, 5.5, 5.4, 5.3, 5.3, 5.2, 5.2, 5.2, 5.2, 5.2, 5.2],
    'Mortgage rate': [6.2, 5.9, 5.6, 5.4, 5.2, 5.0, 4.9, 4.9, 4.8, 4.8, 4.8, 4.8, 4.8],
    'Prime rate': [7.4, 7.6, 7.4, 7.2, 6.8, 6.5, 6.2, 6.0, 5.9, 5.9, 5.9, 5.9, 5.9],
    'Dow Jones Total Stock Market Index (Level)': [38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6, 38520.6],
    'House Price Index (Level)': [301.3, 302.8, 304.3, 305.8, 307.4, 308.9, 310.4, 312.0, 313.5, 315.1, 316.6, 318.2, 319.8],
    'Commercial Real Estate Price Index (Level)': [361.0, 363.7, 366.4, 369.1, 371.9, 374.6, 377.4, 380.2, 383.0, 385.9, 388.7, 391.6, 394.5],
    'Market Volatility Index (Level)': [30.7, 29.0, 27.2, 28.4, 28.5, 28.6, 28.4, 28.4, 28.5, 28.5, 28.5, 28.5, 28.4]}) 


clean = BASELINE_DOMESTIC_2023["Date"].str.replace(" ", "")  
periods = pd.PeriodIndex(clean, freq="Q") 
BASELINE_DOMESTIC_2023["Date"] = periods.to_timestamp("Q")


# --------- 2024 ADVERSE ---------------------------------------------------------- #

ADVERSE_DOMESTIC_2024 = pd.DataFrame({'Scenario Name': ['Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse'],
    'Date': ['2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1', '2026 Q2', '2026 Q3', '2026 Q4', '2027 Q1'],
    'Real GDP growth': [-11.6, -6.7, -8.0, -5.9, -1.8, 0.6, 0.9, 6.5, 6.1, 5.7, 5.4, 5.1, 4.8],
    'Nominal GDP growth': [-9.9, -5.7, -7.1, -5.1, -0.7, 1.9, 2.1, 7.6, 7.5, 6.6, 6.5, 6.3, 6.2],
    'Real disposable income growth': [-7.8, -4.0, -4.2, -2.9, -0.1, 1.2, 1.7, 5.3, 5.6, 5.3, 5.0, 4.8, 4.5],
    'Nominal disposable income growth': [-6.0, -2.8, -3.2, -1.8, 1.1, 2.4, 2.9, 6.6, 7.1, 6.9, 6.6, 6.4, 6.1],
    'Unemployment rate': [5.6, 6.8, 8.1, 9.2, 9.7, 9.9, 10.0, 9.5, 9.0, 8.5, 8.1, 7.8, 7.4],
    'CPI inflation rate': [2.3, 1.5, 1.3, 1.3, 1.4, 1.4, 1.4, 1.5, 1.5, 1.5, 1.6, 1.6, 1.6],
    '3-month Treasury rate': [2.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    '5-year Treasury yield': [0.4, 0.3, 0.4, 0.5, 0.5, 0.6, 0.7, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2],
    '10-year Treasury yield': [1.1, 0.8, 0.8, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.3, 1.4, 1.5, 1.5],
    'BBB corporate yield': [5.8, 6.3, 6.5, 6.6, 6.4, 6.1, 5.8, 5.5, 5.1, 4.8, 4.5, 4.1, 3.8],
    'Mortgage rate': [4.0, 3.7, 3.8, 3.8, 3.8, 3.7, 3.5, 3.4, 3.3, 3.2, 3.1, 3.1, 3.1],
    'Prime rate': [5.1, 3.2, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1],
    'Dow Jones Total Stock Market Index (Level)': [26130.6, 22761.8, 21799.3, 21318.0, 22280.5, 23724.3, 25649.4, 28055.7, 30943.3, 33830.8, 38162.2, 42974.8, 47787.5],
    'House Price Index (Level)': [261.4, 241.1, 225.4, 214.0, 206.8, 202.0, 198.8, 204.3, 210.0, 215.7, 221.3, 226.9, 232.3],
    'Commercial Real Estate Price Index (Level)': [338.5, 328.0, 314.0, 293.1, 269.4, 248.4, 227.5, 209.4, 211.4, 213.4, 215.3, 217.3, 219.2],
    'Market Volatility Index (Level)': [65.0, 70.0, 61.4, 54.5, 49.1, 44.8, 41.5, 38.8, 36.6, 34.9, 33.6, 32.5, 31.7]})

clean = ADVERSE_DOMESTIC_2024["Date"].str.replace(" ", "")  
periods = pd.PeriodIndex(clean, freq="Q") 
ADVERSE_DOMESTIC_2024["Date"] = periods.to_timestamp("Q")


# --------- 2024 BASELINE ---------------------------------------------------------- #

BASELINE_DOMESTIC_2024 = pd.DataFrame({'Scenario Name': ['Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline'],
    'Date': ['2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1', '2026 Q2', '2026 Q3', '2026 Q4', '2027 Q1'],
    'Real GDP growth': [1.0, 0.7, 0.9, 1.5, 1.8, 2.0, 2.1, 2.1, 2.1, 2.0, 2.0, 1.9, 1.9],
    'Nominal GDP growth': [3.2, 2.9, 3.1, 3.6, 4.1, 4.2, 4.3, 4.3, 4.3, 3.9, 3.9, 3.9, 3.9],
    'Real disposable income growth': [2.5, 1.8, 1.8, 2.0, 2.4, 2.3, 2.2, 2.2, 2.2, 2.0, 1.9, 1.9, 2.0],
    'Nominal disposable income growth': [4.6, 4.0, 4.0, 4.1, 4.5, 4.3, 4.3, 4.2, 4.3, 4.2, 4.1, 4.1, 4.1],
    'Unemployment rate': [3.9, 4.1, 4.2, 4.3, 4.3, 4.2, 4.2, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1],
    'CPI inflation rate': [2.4, 2.3, 2.4, 2.3, 2.2, 2.2, 2.3, 2.3, 2.2, 2.2, 2.2, 2.2, 2.2],
    '3-month Treasury rate': [5.3, 5.0, 4.6, 4.2, 3.9, 3.6, 3.4, 3.2, 3.2, 3.2, 3.2, 3.2, 3.1],
    '5-year Treasury yield': [4.2, 4.0, 3.9, 3.8, 3.6, 3.6, 3.5, 3.4, 3.3, 3.3, 3.2, 3.2, 3.1],
    '10-year Treasury yield': [4.1, 4.0, 3.9, 3.8, 3.7, 3.7, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6],
    'BBB corporate yield': [5.8, 5.7, 5.7, 5.6, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5],
    'Mortgage rate': [6.5, 6.1, 5.8, 5.6, 5.4, 5.3, 5.3, 5.2, 5.2, 5.2, 5.2, 5.1, 5.1],
    'Prime rate': [8.4, 8.1, 7.7, 7.3, 7.0, 6.7, 6.4, 6.3, 6.2, 6.2, 6.2, 6.2, 6.2],
    'Dow Jones Total Stock Market Index (Level)': [47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5, 47787.5],
    'House Price Index (Level)': [311.6, 312.8, 313.9, 315.1, 316.3, 317.5, 318.6, 319.8, 321.0, 322.2, 323.4, 324.6, 325.8],
    'Commercial Real Estate Price Index (Level)': [350.2, 351.5, 352.8, 354.2, 355.5, 356.8, 358.1, 359.5, 360.8, 362.2, 363.5, 364.9, 366.2],
    'Market Volatility Index (Level)': [24.6, 26.0, 26.8, 27.2, 27.5, 27.7, 27.9, 28.0, 28.1, 28.2, 28.2, 28.3, 28.3]})

clean = BASELINE_DOMESTIC_2024["Date"].str.replace(" ", "")  
periods = pd.PeriodIndex(clean, freq="Q") 
BASELINE_DOMESTIC_2024["Date"] = periods.to_timestamp("Q")


# --------- 2025 ADVERSE ---------------------------------------------------------- #

ADVERSE_DOMESTIC_2025 = pd.DataFrame({'Scenario Name': ['Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse',
                         'Supervisory Severely Adverse'],
    'Date': ['2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1', '2026 Q2', '2026 Q3', '2026 Q4', '2027 Q1', '2027 Q2', '2027 Q3', '2027 Q4', '2028 Q1'],
    'Real GDP growth': [-8.9, -6.7, -8.0, -5.9, -1.8, 0.6, 0.9, 6.4, 6.0, 5.7, 5.3, 5.0, 4.8],
    'Nominal GDP growth': [-8.0, -6.0, -7.2, -5.1, -0.7, 1.7, 2.1, 7.8, 7.4, 6.8, 6.7, 6.5, 6.2],
    'Real disposable income growth': [-6.0, -3.5, -3.5, -2.3, 0.5, 1.6, 1.8, 5.5, 5.4, 5.2, 5.1, 4.9, 4.6],
    'Nominal disposable income growth': [-4.5, -2.2, -2.4, -1.1, 1.6, 2.7, 3.0, 6.8, 6.8, 6.8, 6.6, 6.5, 6.3],
    'Unemployment rate': [5.6, 6.8, 8.1, 9.2, 9.7, 9.9, 10.0, 9.5, 9.0, 8.6, 8.2, 7.8, 7.5],
    'CPI inflation rate': [2.0, 1.5, 1.3, 1.3, 1.4, 1.4, 1.4, 1.5, 1.5, 1.5, 1.6, 1.6, 1.6],
    '3-month Treasury rate': [1.8, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    '5-year Treasury yield': [0.6, 0.5, 0.6, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.5, 1.6],
    '10-year Treasury yield': [1.4, 1.0, 1.0, 1.1, 1.2, 1.2, 1.3, 1.4, 1.5, 1.5, 1.6, 1.6, 1.7],
    'BBB corporate yield': [5.2, 5.7, 6.0, 6.0, 6.0, 5.8, 5.5, 5.2, 4.8, 4.6, 4.3, 4.0, 3.7],
    'Mortgage rate': [4.0, 3.7, 3.8, 3.8, 3.8, 3.7, 3.6, 3.6, 3.5, 3.4, 3.3, 3.3, 3.2],
    'Prime rate': [4.8, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1],
    'Dow Jones Total Stock Market Index (Level)': [34508.6, 30792.3, 29730.5, 29199.6, 30261.4, 31854.1, 33977.7, 36632.3, 39817.7, 43003.1, 47781.2, 53090.2, 58399.3],
    'House Price Index (Level)': [275.1, 255.2, 239.9, 228.9, 222.0, 217.5, 214.4, 220.4, 226.5, 232.6, 238.6, 244.7, 250.6],
    'Commercial Real Estate Price Index (Level)': [302.4, 295.4, 286.1, 272.2, 256.4, 242.5, 228.6, 216.5, 218.2, 219.9, 221.5, 223.2, 224.8],
    'Market Volatility Index (Level)': [60.0, 65.0, 57.3, 51.2, 46.4, 42.6, 39.5, 37.1, 35.2, 33.7, 32.6, 31.6, 30.9]})

clean = ADVERSE_DOMESTIC_2025["Date"].str.replace(" ", "")  
periods = pd.PeriodIndex(clean, freq="Q") 
ADVERSE_DOMESTIC_2025["Date"] = periods.to_timestamp("Q")


# --------- 2025 BASELINE ---------------------------------------------------------- #

BASELINE_DOMESTIC_2025 = pd.DataFrame({'Scenario Name': ['Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline',
                         'Supervisory Baseline'],
    'Date': ['2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1', '2026 Q2', '2026 Q3', '2026 Q4', '2027 Q1', '2027 Q2', '2027 Q3', '2027 Q4', '2028 Q1'],
    'Real GDP growth': [2.1, 1.9, 1.9, 1.9, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.9, 1.9],
    'Nominal GDP growth': [4.5, 4.4, 4.4, 4.5, 4.7, 4.2, 4.2, 4.3, 4.2, 4.0, 4.0, 4.0, 4.0],
    'Real disposable income growth': [2.4, 2.1, 2.5, 2.3, 2.6, 2.2, 2.1, 2.3, 2.1, 2.0, 2.0, 2.0, 2.0],
    'Nominal disposable income growth': [4.9, 4.6, 5.0, 4.8, 5.2, 4.6, 4.3, 4.5, 4.3, 4.2, 4.1, 4.1, 4.1],
    'Unemployment rate': [4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.3, 4.2, 4.2, 4.2, 4.2, 4.2],
    'CPI inflation rate': [2.8, 2.7, 2.6, 2.6, 2.8, 2.6, 2.4, 2.4, 2.3, 2.2, 2.2, 2.1, 2.2],
    '3-month Treasury rate': [4.3, 4.0, 3.9, 3.8, 3.7, 3.6, 3.6, 3.5, 3.4, 3.4, 3.4, 3.4, 3.4],
    '5-year Treasury yield': [4.2, 4.1, 4.0, 4.0, 4.0, 3.9, 3.8, 3.7, 3.7, 3.6, 3.6, 3.5, 3.5],
    '10-year Treasury yield': [4.4, 4.4, 4.3, 4.3, 4.2, 4.2, 4.2, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1],
    'BBB corporate yield': [5.6, 5.7, 5.8, 5.8, 5.8, 5.9, 5.8, 5.9, 5.9, 5.9, 5.9, 5.9, 5.9],
    'Mortgage rate': [6.4, 6.2, 6.1, 6.0, 5.9, 5.8, 5.7, 5.7, 5.7, 5.6, 5.6, 5.6, 5.6],
    'Prime rate': [7.6, 7.4, 7.2, 7.0, 6.9, 6.8, 6.7, 6.6, 6.6, 6.5, 6.5, 6.5, 6.5],
    'Dow Jones Total Stock Market Index (Level)': [58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3, 58399.3],
    'House Price Index (Level)': [323.7, 325.4, 327.0, 328.6, 330.2, 331.9, 333.5, 335.2, 336.8, 338.5, 340.2, 341.9, 343.6],
    'Commercial Real Estate Price Index (Level)': [310.9, 312.4, 314.0, 315.5, 317.1, 318.7, 320.2, 321.8, 323.4, 325.0, 326.6, 328.3, 329.9],
    'Market Volatility Index (Level)': [26.7, 26.6, 26.6, 26.8, 27.0, 27.2, 27.4, 27.5, 27.6, 27.8, 27.9, 28.0, 28.1]})


clean = BASELINE_DOMESTIC_2025["Date"].str.replace(" ", "")  
periods = pd.PeriodIndex(clean, freq="Q") 
BASELINE_DOMESTIC_2025["Date"] = periods.to_timestamp("Q")


