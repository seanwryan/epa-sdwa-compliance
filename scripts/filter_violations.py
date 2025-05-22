#!/usr/bin/env python3
"""
filter_violations.py

Read the EPA violations CSV in chunks, keep only health-based violations
(as indicated by IS_HEALTH_BASED_IND == 'Y'), and write to a clean CSV
including the SUBMISSIONYEARQUARTER field for downstream joins.
"""

import os
import pandas as pd

# --- CONFIG ---
BASE_DIR    = os.path.dirname(__file__)
DATA_DIR    = os.path.join(BASE_DIR, '..', 'data')
OUTPUT_DIR  = os.path.join(BASE_DIR, '..', 'output')

INPUT_FILE  = os.path.join(DATA_DIR, 'SDWA_VIOLATIONS_ENFORCEMENT.csv')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'violations_health_only.csv')

USECOLS = [
    'SUBMISSIONYEARQUARTER',    # snapshot key for merging
    'PWSID',
    'VIOLATION_ID',
    'VIOLATION_CATEGORY_CODE',
    'NON_COMPL_PER_BEGIN_DATE',
    'NON_COMPL_PER_END_DATE',
    'VIOLATION_STATUS',
    'IS_HEALTH_BASED_IND'
]

CHUNK_SIZE = 200_000

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    first_chunk = True

    for chunk in pd.read_csv(
        INPUT_FILE,
        usecols=USECOLS,
        parse_dates=['NON_COMPL_PER_BEGIN_DATE', 'NON_COMPL_PER_END_DATE'],
        date_parser=lambda col: pd.to_datetime(col, errors='coerce'),
        chunksize=CHUNK_SIZE,
        low_memory=False,
        dtype={'SUBMISSIONYEARQUARTER': str, 'PWSID': str, 'VIOLATION_ID': str}
    ):
        # keep only rows flagged as health-based
        health_only = chunk[chunk['IS_HEALTH_BASED_IND'] == 'Y']

        # write header on first chunk, then append
        if first_chunk:
            health_only.to_csv(OUTPUT_FILE, index=False, mode='w')
            first_chunk = False
        else:
            health_only.to_csv(OUTPUT_FILE, index=False, header=False, mode='a')

    print(f"Wrote filtered violations to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()