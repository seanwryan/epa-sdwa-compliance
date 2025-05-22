#!/usr/bin/env python3
"""
join_systems.py

Merge health-based violations with public water system attributes.
"""

import os
import pandas as pd

# --- PATH SETUP ---
BASE_DIR     = os.path.dirname(__file__)
DATA_DIR     = os.path.join(BASE_DIR, '..', 'data')
OUTPUT_DIR   = os.path.join(BASE_DIR, '..', 'output')

VIOL_FILE    = os.path.join(OUTPUT_DIR, 'violations_health_only.csv')
SYS_FILE     = os.path.join(DATA_DIR, 'SDWA_PUB_WATER_SYSTEMS.csv')
OUTPUT_FILE  = os.path.join(OUTPUT_DIR, 'violations_with_systems.csv')

# --- LOAD filtered violations ---
viol = pd.read_csv(
    VIOL_FILE,
    parse_dates=['NON_COMPL_PER_BEGIN_DATE', 'NON_COMPL_PER_END_DATE'],
    dtype={'SUBMISSIONYEARQUARTER': str, 'PWSID': str, 'VIOLATION_ID': str}
)

# --- LOAD systems file with only needed cols ---
systems = pd.read_csv(
    SYS_FILE,
    usecols=[
        'SUBMISSIONYEARQUARTER',
        'PWSID',
        'STATE_CODE',
        'POPULATION_SERVED_COUNT',
        'PWS_TYPE_CODE'
    ],
    dtype={
        'SUBMISSIONYEARQUARTER': str,
        'PWSID': str,
        'STATE_CODE': str,
        'POPULATION_SERVED_COUNT': float,
        'PWS_TYPE_CODE': str
    }
)

# --- MERGE ---
merged = pd.merge(
    viol,
    systems,
    on=['SUBMISSIONYEARQUARTER', 'PWSID'],
    how='left',
    validate='many_to_one'
)

# --- WRITE ---
os.makedirs(OUTPUT_DIR, exist_ok=True)
merged.to_csv(OUTPUT_FILE, index=False)
print(f"Wrote joined data to {OUTPUT_FILE}")