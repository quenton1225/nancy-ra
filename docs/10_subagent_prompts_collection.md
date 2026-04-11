# Subagent Prompt Pack: Collection Phase (Pilot Round)

## Usage
- Use these prompts with Explore-style subagents for structured collection tasks.
- Target for pilot: 20 records per query family, total 60.
- Apply rules from docs/08_phase0_subagent_spec.md strictly.

---

## Prompt A: Neurodivergent + Education (20 records)
Task:
Collect 20 candidate papers (year >= 2020) focusing on neurodivergent learners in education/learning contexts.

Must output columns:
record_id,title,authors,year,venue,publication_type,doi,arxiv_id,source_url,citation_count,citation_date,domain_neurodivergent,domain_education,domain_adaptive,study_type,sample_size,population_type,input_signal,ai_method,prediction_target,evaluation_metrics,notes

Rules:
1. domain_neurodivergent=1 and domain_education=1.
2. domain_adaptive can be 0 or 1.
3. Skip records with missing core metadata (title/authors/year/venue/source).
4. Prioritize peer-reviewed sources.
5. Keep data factual; do not invent DOI or citation_count.

Output format:
- Return CSV rows only.
- notes should include short source provenance (publisher, DOI page, arXiv, etc.).

---

## Prompt B: Neurodivergent + Adaptive Systems (20 records)
Task:
Collect 20 candidate papers (year >= 2020) focusing on neurodivergent users and adaptive systems/personalization.

Must output columns:
record_id,title,authors,year,venue,publication_type,doi,arxiv_id,source_url,citation_count,citation_date,domain_neurodivergent,domain_education,domain_adaptive,study_type,sample_size,population_type,input_signal,ai_method,prediction_target,evaluation_metrics,notes

Rules:
1. domain_neurodivergent=1 and domain_adaptive=1.
2. domain_education can be 0 or 1.
3. Exclude diagnosis-only papers without adaptation value.
4. Keep at least 5 review/method papers for landscape coverage.
5. Keep data factual; do not invent unavailable metadata.

Output format:
- Return CSV rows only.
- notes include why selected in one short phrase.

---

## Prompt C: Education + Adaptive Systems (20 records)
Task:
Collect 20 candidate papers (year >= 2020) on adaptive learning systems, preference modeling, or personalization in education.

Must output columns:
record_id,title,authors,year,venue,publication_type,doi,arxiv_id,source_url,citation_count,citation_date,domain_neurodivergent,domain_education,domain_adaptive,study_type,sample_size,population_type,input_signal,ai_method,prediction_target,evaluation_metrics,notes

Rules:
1. domain_education=1 and domain_adaptive=1.
2. domain_neurodivergent can be 0 or 1.
3. Include empirical and high-quality review balance.
4. Prioritize papers with explicit evaluation metrics.
5. Keep data factual; do not hallucinate missing values.

Output format:
- Return CSV rows only.
- notes include primary contribution (e.g., RL policy, log modeling, NLP personalization).

---

## Prompt D: Single-Domain Must-Read (10-15 records, optional in pilot)
Task:
Collect 10-15 single-domain flagship or highly cited must-read papers from any one of the three domains.

Rules:
1. Must satisfy at least one:
- flagship venue, or
- high citation for age.
2. For 2024-2026 papers, do not reject purely for low citation count.
3. Mark exactly one domain as 1 when truly single-domain.

Output:
- Same CSV columns as above.

---

## Suggested Record ID Prefix
- PNE### for Neurodivergent+Education
- PNA### for Neurodivergent+Adaptive
- PEA### for Education+Adaptive
- PMS### for Must-read single domain
