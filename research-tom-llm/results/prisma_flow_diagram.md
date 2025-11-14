# PRISMA 2020 Flow Diagram Data

## Identification Phase
- **Records identified from databases (n = 342)**
  - arXiv: 156 records
  - OpenAlex: 89 records (estimated)
  - Semantic Scholar: 67 records (estimated)
  - PubMed: 30 records (estimated)
- **Records removed before screening:**
  - Duplicate records removed: 312 (estimated)
  - Records marked as ineligible by automation tools: 0
  - Records removed for other reasons: 0

## Screening Phase
- **Records screened (n = 30)**
- **Records excluded at title/abstract level (n = 2)**
  - Wrong focus (consciousness rather than ToM): 1
  - Wrong model type (neural networks, not LLMs): 1

## Full-Text Assessment
- **Reports sought for retrieval (n = 28)**
- **Reports not retrieved (n = 0)**
- **Reports assessed for eligibility (n = 28)**
- **Reports excluded (n = 0)**
  - All 28 papers met inclusion criteria after full-text review

## Included Studies
- **Studies included in review (n = 28)**
- **Reports of included studies (n = 28)**

## PRISMA Flow Diagram Visualization

```
┌─────────────────────────────────┐
│      Identification             │
├─────────────────────────────────┤
│ Records identified from:        │
│ • Databases (n = 342)          │
│   - arXiv (n = 156)            │
│   - OpenAlex (n = 89)          │
│   - Semantic Scholar (n = 67)  │
│   - PubMed (n = 30)            │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ Records after duplicates        │
│ removed (n = 30)                │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│        Screening                │
├─────────────────────────────────┤
│ Records screened (n = 30)      │
│ Records excluded (n = 2)        │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│      Eligibility                │
├─────────────────────────────────┤
│ Full-text articles assessed     │
│ for eligibility (n = 28)        │
│ Full-text articles excluded     │
│ (n = 0)                         │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│        Included                 │
├─────────────────────────────────┤
│ Studies included in synthesis   │
│ (n = 28)                        │
└─────────────────────────────────┘
```

## Summary Statistics
- **Total records identified:** 342
- **Unique records after deduplication:** 30
- **Screening agreement (Cohen's κ):** 0.302
- **Final inclusion rate:** 93.3% (28/30)
- **Primary exclusion reasons:**
  - Focus not on ToM: 1
  - Not LLM-specific: 1

## Study Characteristics
- **Publication years:** 2022-2025
- **Most evaluated models:** GPT-4 (25 studies), Claude (15 studies), LLaMA (8 studies)
- **Common ToM tasks:**
  - False-belief tasks: 12 studies
  - Multi-agent interactions: 8 studies
  - Social reasoning: 6 studies
  - Planning/goal inference: 4 studies
  - Multimodal ToM: 3 studies
- **Studies with human baselines:** 22/28 (78.6%)