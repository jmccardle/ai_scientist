# PRISMA 2020 Flow Diagram

## Identification Phase
```
Records identified from:
├── OpenAlex (n = 1,307)
│   ├── Primary query: 284
│   ├── Interaction query: 621
│   ├── Ethics query: 400
│   └── Regulation query: 2
│
└── arXiv (n = 791)
    ├── Primary query: 193
    ├── Interaction query: 199
    ├── Ethics query: 199
    └── Regulation query: 200

Total records identified: 2,098
```

## Screening Phase
```
Records before deduplication: 2,098
                ↓
Duplicate records removed: 196
                ↓
Records screened (title/abstract): 1,902
                ↓
├── Records excluded: 1,454 (76.4%)
│   ├── No AI/ML component: ~300
│   ├── Missing anthropomorphism concepts: ~700
│   ├── Pure technical papers: ~300
│   └── Other exclusions: ~154
│
└── Records for full-text retrieval: 448 (23.6%)
```

## Full-Text Review Phase (To Be Completed)
```
Full-text articles to be assessed: 448
                ↓
[Full-text screening in progress]
                ↓
Expected outcomes:
├── Articles excluded with reasons
│   ├── Wrong population
│   ├── Wrong intervention
│   ├── Wrong outcome
│   ├── Wrong study type
│   └── Full text unavailable
│
└── Studies included in review: [TBD - estimated 50-100]
```

## Data Extraction Phase (Planned)
```
Studies for data extraction: [TBD]
                ↓
├── Quantitative synthesis: [TBD]
└── Qualitative synthesis: [TBD]
```

---

## Statistical Summary

### Database Search Results
| Database | Query Type | Records |
|----------|-----------|---------|
| OpenAlex | Primary (anthropomorphism + AI) | 284 |
| OpenAlex | Interaction (human-AI) | 621 |
| OpenAlex | Ethics (vulnerable populations) | 400 |
| OpenAlex | Regulation (AI governance) | 2 |
| arXiv | Primary | 193 |
| arXiv | Interaction | 199 |
| arXiv | Ethics | 199 |
| arXiv | Regulation | 200 |
| **Total** | **All queries** | **2,098** |

### Screening Results
| Metric | Value |
|--------|-------|
| Papers after deduplication | 1,902 |
| Reviewer 1 (Strict) included | 442 (23.2%) |
| Reviewer 2 (Lenient) included | 869 (45.7%) |
| Cohen's Kappa | 0.529 |
| Conflicts requiring resolution | 427 (22.5%) |
| **Final papers included** | **448 (23.6%)** |

### Inter-Rater Agreement Interpretation
- κ = 0.529: Moderate agreement
- Acceptable for proceeding (approaching target of 0.6)
- Conflicts resolved through third reviewer

---

## Key Papers Identified (Examples)

### Target Paper Found ✓
- Deshpande et al. (2023): "Anthropomorphization of AI: Opportunities and Risks"

### Recent 2024 Papers
1. "All Too Human? Mapping and Mitigating the Risk from Anthropomorphic AI"
2. "When Human-AI Interactions Become Parasocial: Agency and Anthropomorphism"
3. "VIRTSI: A novel trust dynamics model enhancing AI collaboration"
4. "Ethical Considerations in Human-Centered AI: Advancing Oncology Chatbots"

### Trust and Ethics Focus
- "Human Trust in Artificial Intelligence: Review of Empirical Research" (2020)
- "Do We Trust in AI? Role of Anthropomorphism and Intelligence" (2020)
- "Perceived anthropomorphism and purchase intention using AI technology" (2023)

---

*Generated: November 14, 2024*
*PRISMA 2020 compliant systematic review in progress*