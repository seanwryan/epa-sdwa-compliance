EPA SDWA Compliance Analysis

Overview\
This repository contains a Python-script only pipeline to process and analyze health-based violations under the Safe Drinking Water Act (SDWA) for U.S. public water systems. No notebooks are used---everything runs from the command line.

Project Structure\
epa-sdwa-compliance/\
data/\
-- (Full EPA CSVs; not tracked in Git)\
- SDWA_EVENTS_MILESTONES.csv\
- SDWA_FACILITIES.csv\
- SDWA_GEOGRAPHIC_AREAS.csv\
- SDWA_LCR_SAMPLES.csv\
- SDWA_PN_VIOLATION_ASSOC.csv\
- SDWA_PUB_WATER_SYSTEMS.csv\
- SDWA_REF_ANSI_AREAS.csv\
- SDWA_REF_CODE_VALUES.csv\
- SDWA_SERVICE_AREAS.csv\
- SDWA_SITE_VISITS.csv\
- SDWA_VIOLATIONS_ENFORCEMENT.csv

scripts/\
filter_violations.py -- Reads SDWA_VIOLATIONS_ENFORCEMENT.csv in chunks, filters for IS_HEALTH_BASED_IND == 'Y', outputs violations_health_only.csv\
join_systems.py -- Merges violations_health_only.csv with SDWA_PUB_WATER_SYSTEMS.csv on SUBMISSIONYEARQUARTER and PWSID, outputs violations_with_systems.csv\
summarize_violations.py -- Aggregates merged data to produce summary CSVs and static plots

output/\
violations_health_only.csv -- Filtered health-based violations (intermediate; not tracked)\
violations_with_systems.csv -- Joined violations with system attributes (intermediate; not tracked)\
summary_violations_by_state.csv -- Counts of health-based violations by state\
summary_violations_by_year.csv -- Counts of health-based violations by year\
plots/\
violations_per_state.png -- Bar chart of violations by state\
violations_trend_by_year.png -- Bar chart of annual violations trend

requirements.txt -- Lists required Python packages (pandas, matplotlib)\
LICENSE -- MIT License\
README (this document)

Getting Started

1.  Obtain the EPA SDWA download ZIP from the ECHO SDWA Downloads page and extract all CSVs into the local data/ directory.

2.  Create and activate a Python virtual environment.

3.  Install dependencies:\
    pip install -r requirements.txt

Usage

Step 1: Filter for health-based violations\
python3 scripts/filter_violations.py\
-- Reads data/SDWA_VIOLATIONS_ENFORCEMENT.csv in chunks\
-- Keeps only rows where IS_HEALTH_BASED_IND == 'Y'\
-- Writes output/violations_health_only.csv

Step 2: Join with public water system attributes\
python3 scripts/join_systems.py\
-- Merges violations_health_only.csv with data/SDWA_PUB_WATER_SYSTEMS.csv\
-- Joins on SUBMISSIONYEARQUARTER and PWSID\
-- Includes STATE_CODE, POPULATION_SERVED_COUNT, PWS_TYPE_CODE\
-- Writes output/violations_with_systems.csv

Step 3: Summarize and plot results\
python3 scripts/summarize_violations.py\
-- Aggregates merged data by state and by year\
-- Produces summary_violations_by_state.csv and summary_violations_by_year.csv\
-- Saves bar-chart PNGs in output/plots/

Results Preview\
-- The annual violations trend plot shows how health-based violations evolved over time.\
-- The per-state violations chart highlights which states report the highest counts.

Data Source and License\
Raw data provided by the U.S. Environmental Protection Agency (ECHO SDWA downloads, July 2021 release, refreshed quarterly).\
All code in this repository is released under the MIT License.
