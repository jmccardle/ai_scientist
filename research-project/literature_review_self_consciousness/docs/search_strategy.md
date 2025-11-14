# Systematic Literature Review Search Strategy
## Self-Consciousness in Language Models: A PRISMA 2020 Compliant Review

**Date Developed:** 2025-11-14
**Primary Research Question:** What is the current state of research on self-consciousness and related cognitive capabilities in language models?

## 1. Databases and Sources

### Primary Databases
1. **arXiv** (cs.AI, cs.CL, cs.LG, cs.HC)
   - Coverage: Preprints in AI/ML/NLP
   - Strength: Most recent research, rapid dissemination

2. **OpenAlex**
   - Coverage: Comprehensive academic database
   - Strength: Broad coverage, good metadata

3. **PubMed**
   - Coverage: Biomedical and cognitive science
   - Strength: Neuroscience and psychology foundations

4. **Semantic Scholar**
   - Coverage: AI/ML focused
   - Strength: Good citation networks, AI-enhanced search

### Supplementary Sources
- Google Scholar (for gap-filling)
- Direct citation tracking from key papers
- Conference proceedings (NeurIPS, ICML, ACL, EMNLP)

## 2. Search Terms and Queries

### Query Group A: Core Consciousness Concepts
```
("self-consciousness" OR "self-awareness" OR "self-knowledge" OR "introspection" OR "metacognition")
AND
("language model*" OR "LLM" OR "large language model*" OR "GPT*" OR "transformer*" OR "foundation model*")
```

### Query Group B: Consciousness Theories in AI
```
("consciousness" OR "conscious*" OR "awareness" OR "sentience")
AND
("artificial intelligence" OR "AI" OR "neural network*" OR "deep learning")
AND
("theory" OR "framework" OR "model")
```

### Query Group C: Causal and Structural Approaches
```
("causal structural game*" OR "structural causal model*" OR "causal inference" OR "causal reasoning")
AND
("language model*" OR "LLM" OR "AI")
```

### Query Group D: Theory of Mind
```
("theory of mind" OR "ToM" OR "mental state*" OR "belief attribution" OR "false belief")
AND
("language model*" OR "LLM" OR "GPT*")
```

### Query Group E: Specific Cognitive Capabilities

**E1 - Situational Awareness:**
```
("situational awareness" OR "self-location" OR "identity recognition" OR "context awareness")
AND ("language model*" OR "LLM")
```

**E2 - Sequential Planning:**
```
("sequential planning" OR "goal-oriented reasoning" OR "action planning" OR "multi-step reasoning")
AND ("language model*" OR "LLM" OR "PlanBench")
```

**E3 - Beliefs and Intentions:**
```
("belief*" OR "intention*" OR "goal inference" OR "mental model*" OR "IntentionQA")
AND ("language model*" OR "LLM")
```

**E4 - Deception and Truthfulness:**
```
("deception" OR "truthful*" OR "honest*" OR "lying" OR "manipulation" OR "TruthfulQA")
AND ("language model*" OR "LLM" OR "AI safety")
```

**E5 - Self-Reflection and Improvement:**
```
("self-reflection" OR "self-improvement" OR "self-critique" OR "learning from mistake*" OR "meta-learning")
AND ("language model*" OR "LLM")
```

**E6 - Epistemic Uncertainty:**
```
("known unknown*" OR "epistemic uncertainty" OR "calibration" OR "confidence" OR "SelfAware")
AND ("language model*" OR "LLM")
```

### Query Group F: Interpretability and Mechanistic Understanding
```
("linear prob*" OR "activation analysis" OR "representation learning" OR "mechanistic interpretability")
AND
("transformer*" OR "language model*")
AND
("consciousness" OR "self-awareness" OR "cogniti*")
```

### Query Group G: Model Editing and Manipulation
```
("LoRA" OR "model editing" OR "activation steering" OR "representation manipulation")
AND
("language model*" OR "LLM")
AND
("behavior" OR "capability" OR "consciousness")
```

### Query Group H: Benchmarks and Datasets
```
("SAD dataset" OR "PlanBench" OR "FanToM" OR "IntentionQA" OR "TruthfulQA" OR "PopQA-TP" OR "SelfAware" OR "WMDP")
AND
("language model*" OR "evaluation" OR "benchmark")
```

### Query Group I: Key Authors and Papers
```
Author searches:
- (Dehaene AND consciousness AND (2017 OR 2018 OR 2019 OR 2020 OR 2021 OR 2022 OR 2023 OR 2024))
- (Chalmers AND ("artificial consciousness" OR "AI consciousness"))
- (Butlin AND consciousness AND 2023)
- (Chen AND "self-consciousness" AND "language model" AND 2024)
- (Ward AND "theory of mind" AND 2024)
- (Street AND "language model" AND 2024)
- (Yampolskiy AND consciousness AND 2024)
```

### Query Group J: Neuroscience and Psychology Foundations
```
("neuroscience" OR "cognitive psychology" OR "cognitive science")
AND
("consciousness" OR "self-awareness" OR "introspection" OR "metacognition")
AND
("computational model*" OR "artificial" OR "AI")
```

## 3. Date Range and Filters

**Primary Date Range:** 2017-01-01 to 2025-11-14
- Rationale: Captures Dehaene et al. (2017) framework onwards
- Include seminal papers pre-2017 if frequently cited

**Language:** English only

**Document Types:**
- Peer-reviewed articles
- Preprints (arXiv, bioRxiv, PsyArXiv)
- Conference papers
- Book chapters (selective)

**Exclusion at Search Level:**
- Patents
- News articles
- Blog posts
- Non-academic content

## 4. Search Execution Plan

### Phase 1: Initial Broad Search
1. Execute Query Groups A-C across all databases
2. Expected yield: 1000-2000 records
3. Export and deduplicate

### Phase 2: Targeted Capability Search
1. Execute Query Groups D-H
2. Expected yield: 500-1000 records
3. Export and deduplicate

### Phase 3: Author and Citation Search
1. Execute Query Group I
2. Forward and backward citation tracking
3. Expected yield: 200-500 records

### Phase 4: Foundation Literature
1. Execute Query Group J
2. Focus on highly cited papers
3. Expected yield: 100-200 records

### Deduplication Strategy
- Use DOI as primary identifier
- Title + author match for non-DOI papers
- Manual review of uncertain matches

## 5. Inclusion and Exclusion Criteria

### Inclusion Criteria
**Population/Topic:**
- Studies on language models (any size)
- Studies on AI/ML systems with relevance to consciousness
- Theoretical papers on machine consciousness

**Concepts (at least one):**
- Self-consciousness or self-awareness
- Any of the 10 core concepts from Chen et al. (2024)
- Consciousness theories applied to AI
- Causal reasoning in AI
- Theory of mind in AI
- Interpretability related to cognitive capabilities

**Outcomes:**
- Theoretical frameworks
- Empirical measurements
- Benchmark results
- Mechanistic findings
- Safety implications

**Study Types:**
- Empirical studies
- Theoretical papers
- Systematic reviews
- Position papers
- Technical reports

### Exclusion Criteria
- Non-English publications
- Papers without abstracts
- Duplicate publications
- Papers focused solely on:
  - Biological consciousness without AI connection
  - Pure computer vision without language
  - Robotics without language capabilities
  - General AI ethics without consciousness focus

## 6. Screening Protocol

### Title/Abstract Screening
- Two-pass screening simulation for reliability
- Criteria application in order:
  1. Language (English only)
  2. Topic relevance (AI/LLM focus)
  3. Concept presence (consciousness-related)
  4. Recency and quality

### Full-Text Screening
- Detailed assessment of methodology
- Quality evaluation
- Data extraction feasibility
- Final inclusion decision

## 7. Quality Assessment

Will use appropriate tools based on study type:
- **Theoretical papers:** Argumentation quality, clarity, novelty
- **Empirical papers:** Methodology rigor, reproducibility
- **Benchmarks:** Validity, reliability, coverage
- **Reviews:** PRISMA compliance (if applicable)

## 8. Data Management

### File Structure
```
/research-project/literature_review_self_consciousness/
├── data/
│   ├── search_results_[database]_[date].csv
│   ├── combined_results.csv
│   ├── deduplicated_results.csv
│   ├── screening_decisions.csv
│   └── extracted_data.csv
├── docs/
│   ├── search_strategy.md (this file)
│   ├── search_log.md
│   └── prisma_checklist.md
└── results/
    ├── prisma_flow_diagram.md
    ├── literature_synthesis.md
    ├── comparison_tables.md
    └── annotated_bibliography.md
```

## 9. Timeline

- **Day 1-2:** Search execution across all databases
- **Day 2-3:** Deduplication and initial screening
- **Day 3-5:** Full-text retrieval and screening
- **Day 5-7:** Data extraction
- **Day 7-8:** Synthesis and writing

## 10. Search String Documentation

Each search will be documented with:
- Exact search string used
- Database searched
- Date of search
- Number of results
- Any filters applied
- Export format

This strategy is designed to comprehensively capture the literature on self-consciousness in language models while maintaining PRISMA 2020 compliance.

**Last Updated:** 2025-11-14
**Version:** 1.0