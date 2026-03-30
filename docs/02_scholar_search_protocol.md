# Google Scholar Search Protocol (v1)

## Goal
Produce a reproducible preliminary literature review before next meeting.

## Timebox
- Total: 2-4 working days for first round
- Target output: 12-18 core papers + evidence summary

## Databases (Phase 1)
- Google Scholar (mandatory first pass)

## Query Sets (copy and run directly)

### Set A: AI + neurodivergent identification in learning/HCI
1. "neurodivergent" "artificial intelligence" "learning" "user modeling"
2. "autism" OR "ADHD" "machine learning" "adaptive learning"
3. "neurodiversity" "HCI" "AI" "personalization"

### Set B: AI + preference identification
1. "user preference" "machine learning" "adaptive interface"
2. "learning preference" "AI" "personalized learning system"
3. "preference inference" "human-computer interaction" "eye tracking"

### Set C: Observable signals -> cognitive/affective/behavioral needs
1. "eye tracking" "machine learning" "cognitive state" "learning"
2. "behavioral signals" "AI" "user state inference"
3. "interaction logs" "preference prediction" "educational technology"

## Screening Rules
- Year priority: 2020+
- Keep if:
  - Has empirical evaluation
  - Uses AI/ML for inference/modeling
  - Can transfer to learning/HCI adaptation
- Exclude if:
  - Pure clinical diagnosis without adaptation relevance
  - Opinion-only or conceptual-only without data
  - Irrelevant domain with no transferable method

## Workflow
1. Run each query and inspect first 50 results.
2. Save candidates to extraction table.
3. Mark each candidate: keep / maybe / exclude.
4. Keep at least 10 candidates per query set initially.
5. Deduplicate by title + year + first author.
6. Select final 12-18 core papers.

## Quality Triage Labels
- Direct: directly answers RQ1/RQ2 in learning/HCI context
- Adjacent: method transferable but context different
- Background: useful theory/context only

## Deliverables
- `03_literature_extraction_template.csv` filled with first-round records
- 1-page evidence conclusion
- 1-page recommendation for Route A vs Route B
