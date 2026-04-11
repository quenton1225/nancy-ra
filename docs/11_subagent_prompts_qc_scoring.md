# Subagent Prompt Pack: QC and Scoring Phase

## Prompt E: Metadata + Dedup QC
Task:
Given candidate CSV rows, perform two-pass quality control:
1. Exact dedup: DOI or normalized title+year.
2. Near dedup: high title similarity + overlapping author set + close year.

Output:
- cleaned CSV rows (same schema)
- issue log table with: record_id,issue_type,action,reason

Rules:
1. Remove duplicates with clear rationale.
2. Keep one canonical record per dedup_group.
3. Do not fabricate missing metadata.

---

## Prompt F: Accuracy Audit (Spot Check)
Task:
Randomly audit at least 20% of cleaned records for metadata correctness.

Check fields:
- title, authors, year, venue, DOI/source_url, domain one-hot

Output:
- audit report with pass/fail per checked record
- corrected rows for failed records

Rules:
1. If source is unverifiable, downgrade decision to maybe.
2. Track confidence per record: high/medium/low.

---

## Prompt G: Reading + Scoring
Task:
Read abstract/method/results (full text if available), then score each record:
- quality_rigor (1-5)
- quality_transfer (1-5)
- quality_repro_ethics (1-5)

Output:
- scored CSV rows (same schema, include decision + decision_reason)
- short ranking summary by domain pair

Decision guidance:
- keep_high: strong in at least 2 score dimensions and no red flags
- keep_medium: useful but with limitations
- maybe: partial relevance or uncertain reliability
- exclude: out-of-scope or unverifiable

---

## Prompt H: Ranking + Synthesis
Task:
Create two rankings:
1. ranked_by_domain
2. ranked_overall

Output files (or equivalent tables):
- ranked_by_domain.csv
- ranked_overall.csv
- top20_must_read.md

Rules:
1. Use balanced weighting across the three quality scores.
2. Citation count is supportive, not dominant.
3. Include a short risk note for each top-10 record.
