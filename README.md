EPA SDWA Compliance Analysis

Overview\
This project uses Python scripts (no notebooks) to process and analyze health-based violations under the Safe Drinking Water Act (SDWA) for U.S. public water systems.

Project Structure\
epa-sdwa-compliance/\
- data/\
 -- SDWA_EVENTS_MILESTONES.csv\
 -- SDWA_FACILITIES.csv\
 -- SDWA_GEOGRAPHIC_AREAS.csv\
 -- SDWA_LCR_SAMPLES.csv\
 -- SDWA_PN_VIOLATION_ASSOC.csv\
 -- SDWA_PUB_WATER_SYSTEMS.csv\
 -- SDWA_REF_ANSI_AREAS.csv\
 -- SDWA_REF_CODE_VALUES.csv\
 -- SDWA_SERVICE_AREAS.csv\
 -- SDWA_SITE_VISITS.csv\
 -- SDWA_VIOLATIONS_ENFORCEMENT.csv

- scripts/\
 -- filter_violations.py   Reads SDWA_VIOLATIONS_ENFORCEMENT in chunks, filters for IS_HEALTH_BASED_IND == 'Y', outputs violations_health_only.csv\
 -- join_systems.py   Merges violations_health_only.csv with SDWA_PUB_WATER_SYSTEMS on SUBMISSIONYEARQUARTER and PWSID, outputs violations_with_systems.csv\
 -- summarize_violations.py Generates summary_violations_by_state.csv and summary_violations_by_year.csv, and creates plots/violations_per_state.png and plots/violations_trend_by_year.png

- output/\
 -- violations_health_only.csv\
 -- violations_with_systems.csv\
 -- summary_violations_by_state.csv\
 -- summary_violations_by_year.csv\
 -- plots/\
  - violations_per_state.png\
  - violations_trend_by_year.png

Getting Started

1.  Place all unzipped EPA CSVs into the data/ folder.

2.  Install dependencies (in a virtual environment):\
    - pandas\
    - matplotlib

Step 1: Filter Health-Based Violations\
- Run filter_violations.py\
- Reads SDWA_VIOLATIONS_ENFORCEMENT.csv in chunks\
- Keeps only rows where IS_HEALTH_BASED_IND == 'Y'\
- Writes output/violations_health_only.csv

Step 2: Join System Attributes\
- Run join_systems.py\
- Merges violations_health_only.csv with SDWA_PUB_WATER_SYSTEMS.csv on SUBMISSIONYEARQUARTER and PWSID\
- Includes STATE_CODE, POPULATION_SERVED_COUNT, PWS_TYPE_CODE\
- Writes output/violations_with_systems.csv

Step 3: Summarize and Plot\
- Run summarize_violations.py\
- Produces:\
  -- summary_violations_by_state.csv (counts per STATE_CODE)\
  -- summary_violations_by_year.csv (annual counts from NON_COMPL_PER_BEGIN_DATE)\
  -- plots/violations_per_state.png\
  -- plots/violations_trend_by_year.png

Results Preview\
- Heatmap of violations by state shows highest counts in TX, OH, PA, WA\
- Time-series trend reveals a sharp rise in health-based violations through the early 2000s, then a gradual decline

Data Source & License\
- Data from EPA ECHO SDWA downloads (July 2021 release, refreshed quarterly)\
- Code released under the MIT License
