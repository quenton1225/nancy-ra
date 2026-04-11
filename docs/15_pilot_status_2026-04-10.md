# Pilot Status (2026-04-10)

## Completed
1. Phase 0 specification finalized.
2. Unified master CSV template created.
3. Subagent prompt packs created (collection + QC/scoring).
4. Pilot collection executed via OpenAlex (3 groups x 20 target).
5. Dedup QC executed (exact DOI/title-year).
6. Hard off-topic exclusion pass executed.

## Output Files
- docs/08_phase0_subagent_spec.md
- docs/09_validated_master_template.csv
- docs/10_subagent_prompts_collection.md
- docs/11_subagent_prompts_qc_scoring.md
- docs/12_pilot_candidates_raw.csv
- docs/12_pilot_candidates_cleaned.csv
- docs/12_pilot_candidates_curated.csv
- docs/13_pilot_collection_log.md
- docs/14_pilot_qc_report.md
- docs/16_pilot_exclusion_log.md

## Current Counts
- raw: 60
- cleaned (dedup): 57
- curated (off-topic excluded): 54

Group balance in curated set:
- PNE: 18
- PNA: 16
- PEA: 20

## Notes
- Dedup removals were primarily duplicate DOI records.
- Off-topic removals captured clear false positives (e.g., hardware quantization / CI-CD engineering noise).
- Current curated set is suitable for pilot scoring and relevance auditing.

## Recommended Immediate Next Step
1. Run Domain Scoring agents on docs/12_pilot_candidates_curated.csv (PNE/PNA/PEA split).
2. Produce ranked_by_domain.csv and ranked_overall.csv.
3. Use pilot findings to tighten query constraints before scaling to 120-150 candidates.
