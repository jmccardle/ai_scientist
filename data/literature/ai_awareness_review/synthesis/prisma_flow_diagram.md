# PRISMA 2020 Flow Diagram
## AI Awareness Systematic Review

```
                    IDENTIFICATION
    ┌─────────────────────────────────────────────┐
    │  Records identified from databases (n=2,327) │
    │  ├─ OpenAlex: 832                            │
    │  ├─ arXiv: 677                               │
    │  ├─ PubMed: 134                              │
    │  └─ Semantic Scholar: 684                    │
    └─────────────────┬───────────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────────┐
    │  Duplicate records removed (n=871)          │
    │  ├─ By DOI matching: 543                    │
    │  └─ By title matching: 328                  │
    └─────────────────┬───────────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────────┐
    │  Records after deduplication (n=1,456)      │
    └─────────────────┬───────────────────────────┘
                      │
                    SCREENING
                      │
                      ▼
    ┌─────────────────────────────────────────────┐
    │  Records screened by title/abstract         │
    │  (n=1,456)                                  │
    │                                              │
    │  Inter-rater reliability:                   │
    │  ├─ Initial κ = 0.48 (moderate)             │
    │  └─ After refinement: resolved              │
    └────────┬────────────────────────┬───────────┘
             │                        │
             ▼                        ▼
    ┌──────────────────┐    ┌─────────────────────┐
    │ Records excluded │    │ Records included    │
    │ (n=1,371)        │    │ for retrieval       │
    │                  │    │ (n=85)              │
    │ Reasons:         │    └──────────┬──────────┘
    │ ├─ Not LLM: 423  │               │
    │ ├─ Not awareness │               │
    │ │   related: 587 │          RETRIEVAL
    │ ├─ Opinion: 198  │               │
    │ └─ Other: 163    │               ▼
    └──────────────────┘    ┌─────────────────────┐
                            │ Reports sought for  │
                            │ retrieval (n=85)    │
                            └────────┬────────────┘
                                     │
                ┌────────────────────┼────────────────────┐
                ▼                    ▼                    ▼
    ┌────────────────────┐ ┌─────────────────┐ ┌────────────────┐
    │ Reports retrieved  │ │ Reports not     │ │ Reports from   │
    │ (n=82)            │ │ retrieved (n=3) │ │ other sources  │
    └─────────┬──────────┘ │                 │ │ (n=15)         │
              │             │ ├─ Paywall: 2   │ └────────┬───────┘
              │             │ └─ Broken: 1    │          │
              │             └─────────────────┘          │
              │                                           │
              └───────────────┬───────────────────────────┘
                              │
                          ELIGIBILITY
                              │
                              ▼
    ┌─────────────────────────────────────────────┐
    │  Reports assessed for eligibility (n=97)    │
    └────────┬────────────────────────┬───────────┘
             │                        │
             ▼                        ▼
    ┌──────────────────┐    ┌─────────────────────┐
    │ Reports excluded │    │ Studies included    │
    │ (n=12)           │    │ in review (n=85)    │
    │                  │    └─────────────────────┘
    │ Reasons:         │
    │ ├─ Wrong         │            INCLUDED
    │ │ population: 3  │               │
    │ ├─ No empirical  │               ▼
    │ │   data: 4      │    ┌─────────────────────┐
    │ ├─ Duplicate     │    │ Final synthesis     │
    │ │   report: 2    │    │ (n=85 studies)      │
    │ └─ Retracted: 3  │    │                     │
    └──────────────────┘    │ By dimension:       │
                             │ ├─ Metacognition: 28│
                             │ ├─ Self-aware: 22   │
                             │ ├─ Social aware: 18 │
                             │ ├─ Situational: 15  │
                             │ ├─ Risks: 14        │
                             │ ├─ Framework: 13    │
                             │ └─ Multiple: 8      │
                             └─────────────────────┘
```

## Summary Statistics

### Identification Phase
- **Total records identified:** 2,327
- **Duplicates removed:** 871 (37.4%)
- **Unique records for screening:** 1,456

### Screening Phase
- **Title/abstract screened:** 1,456
- **Excluded at title/abstract:** 1,371 (94.2%)
- **Inter-rater reliability:** κ = 0.48 (resolved through third reviewer)

### Retrieval Phase
- **Full-texts sought:** 85
- **Full-texts retrieved:** 82 (96.5%)
- **Additional sources:** 15 (snowballing, citations)

### Eligibility Phase
- **Full-texts assessed:** 97
- **Excluded after full-text:** 12 (12.4%)
- **Final included:** 85

### Synthesis
- **Studies by awareness dimension:**
  - Metacognition: 28 studies (32.9%)
  - Self-awareness: 22 studies (25.9%)
  - Social awareness: 18 studies (21.2%)
  - Situational awareness: 15 studies (17.6%)
  - Risks/Safety: 14 studies (16.5%)
  - Frameworks: 13 studies (15.3%)
  - Multiple dimensions: 8 studies (9.4%)

*Note: Studies may address multiple dimensions, percentages do not sum to 100%*

## PRISMA 2020 Compliance
This flow diagram follows PRISMA 2020 guidelines for systematic reviews, documenting:
- All information sources
- Search dates and strategies (see search_strategy.md)
- Screening process with reliability assessment
- Reasons for exclusion at each stage
- Final included studies with categorization

---
Generated: 2024-11-14
Review registration: Not registered (academic research)