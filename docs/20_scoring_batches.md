# Scoring Batch Plan

## Batch Files
- docs/20_batch_pne.csv (18 records)
- docs/21_batch_pna.csv (16 records)
- docs/22_batch_pea.csv (20 records)

## Scoring Output Contract
Each record must return:
- record_id
- quality_rigor (1-5)
- quality_transfer (1-5)
- quality_repro_ethics (1-5)
- decision (keep_high/keep_medium/maybe/exclude)
- decision_reason (<= 25 words)
