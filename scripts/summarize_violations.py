#!/usr/bin/env python3
"""
summarize_violations.py

Generate summary tables and static plots of health-based violations:
  - violations per state
  - violations per year
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# --- PATH SETUP ---
BASE_DIR     = os.path.dirname(__file__)
OUTPUT_DIR   = os.path.join(BASE_DIR, '..', 'output')
PLOTS_DIR    = os.path.join(OUTPUT_DIR, 'plots')

INPUT_FILE   = os.path.join(OUTPUT_DIR, 'violations_with_systems.csv')
STATE_SUM_CSV= os.path.join(OUTPUT_DIR, 'summary_violations_by_state.csv')
YEAR_SUM_CSV = os.path.join(OUTPUT_DIR, 'summary_violations_by_year.csv')

STATE_PLOT   = os.path.join(PLOTS_DIR, 'violations_per_state.png')
YEAR_PLOT    = os.path.join(PLOTS_DIR, 'violations_trend_by_year.png')

# --- READ DATA ---
df = pd.read_csv(
    INPUT_FILE,
    parse_dates=['NON_COMPL_PER_BEGIN_DATE', 'NON_COMPL_PER_END_DATE'],
    dtype={'STATE_CODE': str}
)

# --- SUMMARY BY STATE ---
state_summary = (
    df
    .groupby('STATE_CODE')
    .size()
    .reset_index(name='violation_count')
    .sort_values('violation_count', ascending=False)
)

# Save CSV
state_summary.to_csv(STATE_SUM_CSV, index=False)

# --- PLOT: Violations per State ---
os.makedirs(PLOTS_DIR, exist_ok=True)
plt.figure(figsize=(10, 6))
plt.bar(state_summary['STATE_CODE'], state_summary['violation_count'])
plt.title('Health-based Violations by State')
plt.xlabel('State')
plt.ylabel('Number of Violations')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(STATE_PLOT)
plt.close()

# --- SUMMARY BY YEAR ---
# extract year from the begin date
df['year'] = df['NON_COMPL_PER_BEGIN_DATE'].dt.year.fillna(0).astype(int)
year_summary = (
    df[df['year'] > 0]
    .groupby('year')
    .size()
    .reset_index(name='violation_count')
    .sort_values('year')
)

# Save CSV
year_summary.to_csv(YEAR_SUM_CSV, index=False)

# --- PLOT: Violations Trend by Year ---
plt.figure(figsize=(10, 6))
plt.bar(year_summary['year'].astype(str), year_summary['violation_count'])
plt.title('Health-based Violations Trend by Year')
plt.xlabel('Year')
plt.ylabel('Number of Violations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(YEAR_PLOT)
plt.close()

print(f"Wrote summaries to:\n  • {STATE_SUM_CSV}\n  • {YEAR_SUM_CSV}")
print(f"Wrote plots to:\n  • {STATE_PLOT}\n  • {YEAR_PLOT}")