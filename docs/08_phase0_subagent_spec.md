# Phase 0 Spec for Multi-Subagent Literature Pipeline

## 1) Objective
Build a high-quality literature pool for three domains:
- Neurodivergent research
- Education/Learning
- Adaptive systems

Primary target:
- At least 100 validated records after cleaning
- Focus on papers covering any 2-domain combination
- Include a small set of single-domain must-read papers (flagship + highly cited)

## 2) Scope and Priority
### In scope
- Empirical studies and review papers related to any of:
  - Neurodivergent learners and functional needs
  - AI/ML-driven learning support and preference modeling
  - Adaptive learning/HCI systems
- 2-domain combinations are primary
- Single-domain top papers are secondary but required

### Out of scope
- Pure clinical diagnosis pipelines without learning/adaptation relevance
- Opinion-only pieces without data or methodological contribution
- Non-peer-reviewed noise sources

## 3) Hard Inclusion/Exclusion Rules
### Inclusion rules (all required unless marked optional)
1. Year >= 2020
2. Peer-reviewed venue preferred (journal/conference)
3. Must provide at least one stable source:
- DOI or
- arXiv ID or
- stable publisher/library URL
4. Topic relevance must satisfy at least one:
- Neurodivergent + Education
- Neurodivergent + Adaptive Systems
- Education + Adaptive Systems
- Single-domain paper that is clearly top-tier

### Exclusion rules
1. No accessible abstract/metadata after 2 retrieval attempts
2. Clinical diagnosis-only framing with no adaptation/learning transfer value
3. Duplicate record (exact or near-duplicate after normalization)
4. Missing critical metadata after validation:
- title
- authors
- year
- venue
- source link

## 4) Single-Domain Must-Read Criteria
A paper can be included as single-domain must-read if it satisfies at least one:
1. Flagship venue criterion:
- Top conference or top journal in that domain
2. High-citation criterion:
- Strong citation impact for its age window

Operational note:
- New papers (2024-2026) are protected from low-citation bias
- Do not reject new top-venue papers only because citation count is still low

## 5) Required CSV Schema (v1)
Use one unified CSV with the following columns in order:

record_id,title,authors,year,venue,publication_type,doi,arxiv_id,source_url,citation_count,citation_date,
domain_neurodivergent,domain_education,domain_adaptive,
study_type,sample_size,population_type,input_signal,ai_method,prediction_target,evaluation_metrics,
quality_rigor,quality_transfer,quality_repro_ethics,
decision,decision_reason,dedup_group,reviewer,review_date,notes

## 6) Field Definitions
### publication_type
- journal
- conference
- review_article
- thesis
- preprint

### domain one-hot encoding
- domain_neurodivergent: 0/1
- domain_education: 0/1
- domain_adaptive: 0/1

Rule:
- At least one domain must be 1
- Primary pool should prioritize records where sum >= 2

### study_type
- empirical
- review
- methodological
- theoretical

### population_type
- neurodivergent
- neurotypical
- mixed
- not_applicable

## 7) Quality Control Rules
### Dedup (two-pass)
1. Exact dedup by DOI or normalized title + year
2. Near dedup by high title similarity + overlapping author set + close year

### Metadata validation
A record is valid only if these are confirmed:
- title
- authors
- year
- venue
- source_url or doi or arxiv_id

### Citation handling
- Record citation_date together with citation_count
- Citation is supportive, not absolute
- For 2024-2026 papers, use venue strength and method relevance as co-equal signals

## 8) Scoring Framework (Balanced Weighting)
Use three scores, each 1-5:
1. quality_rigor
- design quality, venue credibility, reporting clarity
2. quality_transfer
- transfer value to your research goals and experimental design
3. quality_repro_ethics
- reproducibility signals and ethics transparency

Balanced policy:
- Keep balanced importance across the three dimensions
- Do not let citation count dominate ranking

## 9) Decision Labels
Use one of:
- keep_high
- keep_medium
- maybe
- exclude

Minimum decision rule:
- keep_high: consistently strong in at least two quality dimensions and no red flags
- exclude: fails scope or metadata validity or dedup check

## 10) Subagent Roles and I/O Contract
### Agent A: Collection
Input:
- query packs and scope rules
Output:
- raw candidate CSV with required core metadata

### Agent B: Metadata and Dedup
Input:
- raw candidate CSV
Output:
- normalized CSV with dedup_group and cleaned metadata

### Agent C: Quality Audit
Input:
- normalized CSV
Output:
- corrected/removed records with issue log

### Agent D/E/F: Reading and Scoring (parallel by domain emphasis)
Input:
- quality-approved CSV
Output:
- per-record 3-score assessment + decision suggestion

### Agent G: Ranking and Synthesis
Input:
- all scored records
Output:
- domain ranking tables + cross-domain ranking + final shortlist

## 11) Deliverables Checklist
1. validated_master.csv (>=100 records)
2. dedup_report.md
3. quality_audit_report.md
4. ranked_by_domain.csv
5. ranked_overall.csv
6. top20_must_read.md

## 12) Quick Start Execution Order
1. Freeze this Phase 0 spec
2. Launch collection agents in parallel
3. Run normalization + dedup
4. Run quality audit
5. Launch reading/scoring agents
6. Generate ranked outputs and shortlist
