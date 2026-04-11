# Next Actions: Scale from Pilot to 100+ Validated Records

## Current Pilot Baseline
- Curated and scored records: 54
- Decision distribution:
  - keep_high: 19
  - keep_medium: 16
  - maybe: 12
  - exclude: 7

## Scale-Up Target
- Candidate pool: 120-150
- After QC/curation: >=100 validated records

## Execution Plan (Immediate)
1. Run second collection round with expanded query packs per domain pair.
2. Keep same QC pipeline:
- dedup pass
- off-topic exclusion pass
- metadata audit
3. Merge with current pilot scored set.
4. Launch scoring batches for newly added records only.
5. Regenerate ranked outputs.

## Query Expansion Suggestions
- Add synonyms for neurodivergence:
  - ASD, ADHD, dyslexia, dyspraxia, executive dysfunction
- Add adaptive system terms:
  - user modeling, intervention policy, recommendation, intelligent tutoring
- Add educational context terms:
  - LMS logs, classroom intervention, learning outcome, engagement

## Acceptance Gates for Scale-Up
1. Core metadata completeness >= 95%
2. Duplicate ratio <= 20% after normalization
3. Off-topic ratio <= 15%
4. At least 30% records from each domain-pair bucket before final balancing
