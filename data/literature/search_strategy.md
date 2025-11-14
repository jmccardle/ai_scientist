# Systematic Literature Review Search Strategy
## Paper: "Looking Inward: Language Models Can Learn About Themselves by Introspection"

---

## Research Question

**Primary Question:** What is the current state of knowledge regarding language model introspection, self-knowledge, and related capabilities in AI systems?

**Secondary Questions:**
1. How do LLMs demonstrate self-awareness or situational awareness?
2. What methods exist for model interpretability and understanding internal states?
3. What are the safety and alignment implications of self-aware AI systems?
4. How does model introspection relate to broader concepts of AI consciousness and moral status?

---

## Search Protocol

### 1. Databases to Search

**Primary Databases:**
- **arXiv** (Computer Science categories: cs.AI, cs.CL, cs.LG, cs.CY)
  - Rationale: Primary source for cutting-edge AI research preprints
  - Coverage: 2018-2024

- **OpenAlex** (formerly Microsoft Academic)
  - Rationale: Comprehensive academic coverage across disciplines
  - Coverage: All years, focus on 2018-2024

- **Semantic Scholar**
  - Rationale: Strong AI/ML coverage with citation network analysis
  - Coverage: All years, focus on 2018-2024

**Secondary Databases (for specific topics):**
- **PubMed** (for consciousness, cognition, and philosophical works)
- **PhilPapers** (for philosophical perspectives on AI consciousness)
- **Google Scholar** (for citation tracking and grey literature)

### 2. Search Terms and Boolean Logic

#### Core Search String (Adapted for Each Database)

**Search String A - LLM Introspection Focus:**
```
("language model*" OR "LLM" OR "GPT*" OR "transformer*" OR "foundation model*" OR "large model*")
AND
("introspect*" OR "self-knowledge" OR "self-aware*" OR "self-predict*" OR "self-model*" OR "self-understand*" OR "meta-cognit*" OR "self-reflect*")
```

**Search String B - Situational Awareness and Interpretability:**
```
("language model*" OR "LLM" OR "GPT*" OR "transformer*")
AND
("situational aware*" OR "context aware*" OR "environment detect*" OR "interpretab*" OR "explainab*" OR "internal state*" OR "representation learn*" OR "attention mechanism*")
```

**Search String C - AI Alignment and Safety:**
```
("language model*" OR "LLM" OR "GPT*" OR "AI system*")
AND
("alignment" OR "deception" OR "honesty" OR "truthful*" OR "scheming" OR "misalignment" OR "constitutional AI" OR "alignment faking" OR "safety")
```

**Search String D - Model Behavior and Calibration:**
```
("language model*" OR "LLM" OR "GPT*")
AND
("calibrat*" OR "self-consist*" OR "behavior* predict*" OR "sycophancy" OR "confirmation bias" OR "weak-to-strong" OR "chain-of-thought" OR "reasoning transparen*")
```

**Search String E - Model Finetuning and Adaptation:**
```
("language model*" OR "LLM" OR "GPT*")
AND
("finetun*" OR "LoRA" OR "adaptation" OR "behavior* modif*" OR "transfer learn*" OR "parameter efficient")
```

**Search String F - AI Consciousness and Moral Status:**
```
("artificial intelligence" OR "AI" OR "language model*" OR "machine")
AND
("consciousness" OR "sentience" OR "moral status" OR "self-report*" OR "phenomenal*" OR "subjective experience")
```

### 3. Specific Author Searches

**Key Authors to Track (based on paper references):**
- Owain Evans (UC Berkeley): situational awareness, truthful AI
- Ethan Perez (Anthropic): model evaluations, alignment
- Miles Turpin (Scale AI): chain-of-thought, interpretability
- Tomek Korbak: alignment, fine-tuning
- Collin Burns: weak-to-strong generalization
- Samuel Bowman: model capabilities
- Dan Hendrycks: MMLU, benchmarks
- Eric Schwitzgebel: philosophy of introspection

### 4. Specific Paper Tracking

**Must Include Papers from Original References:**
1. Allen-Zhu & Li (2024) - "Physics of Language Models"
2. Berglund et al. (2023) - "Taken Out of Context"
3. Burns et al. (2023) - "Weak-to-Strong Generalization"
4. Carlsmith (2023) - "Scheming AIs"
5. Chen et al. (2024) - "Self-Consistency Improves Chain of Thought"
6. Kadavath et al. (2022) - "Language Models (Mostly) Know What They Know"
7. Lin et al. (2022) - "Teaching Models to Express Their Uncertainty"
8. Perez et al. (2023) - "Discovering Language Model Behaviors"
9. Sharma et al. (2023) - "Towards Understanding Sycophancy"
10. Hendrycks et al. (2021) - "Measuring Massive Multitask Language Understanding"

### 5. Citation Tracking Strategy

**Forward Citations:**
- Papers citing arXiv:2410.13787 (the introspection paper)
- Use Semantic Scholar and Google Scholar APIs

**Backward Citations:**
- All 60+ references from the introspection paper
- Key references from highly cited related papers

### 6. Inclusion and Exclusion Criteria

**Inclusion Criteria:**
- **Population:** Studies on large language models (>1B parameters) OR theoretical work on AI systems
- **Intervention/Exposure:** Any method for assessing, improving, or understanding:
  - Self-knowledge/introspection
  - Interpretability
  - Alignment
  - Behavioral prediction
  - Situational awareness
- **Comparator:** Not required (include descriptive studies)
- **Outcomes:** Any measure of model capability, behavior, or understanding
- **Study Design:**
  - Empirical studies (experiments, evaluations)
  - Theoretical analyses
  - Philosophical arguments
  - Method papers
- **Publication Type:**
  - Peer-reviewed articles
  - Preprints (arXiv, bioRxiv)
  - Conference papers
  - Technical reports
  - Books/book chapters
- **Language:** English
- **Date:** Primary focus 2018-2024; include seminal earlier works

**Exclusion Criteria:**
- Pure application papers without relevance to core concepts
- Hardware/infrastructure papers
- Papers on models <1B parameters unless theoretically relevant
- News articles, blog posts (unless containing original research)
- Duplicate publications (keep most complete version)

### 7. Search Execution Plan

**Phase 1: Primary Database Search (Days 1-2)**
1. Execute all 6 search strings in arXiv
2. Execute all 6 search strings in OpenAlex
3. Execute all 6 search strings in Semantic Scholar
4. Document counts for PRISMA diagram

**Phase 2: Author and Paper Tracking (Day 3)**
1. Search for all key authors' recent publications
2. Verify inclusion of all 60+ referenced papers
3. Forward citation search on introspection paper
4. Backward citation search on key papers

**Phase 3: Specialized Searches (Day 4)**
1. Philosophy databases for consciousness/moral status
2. PubMed for cognitive science perspectives
3. Google Scholar for grey literature

**Phase 4: Deduplication (Day 5)**
1. Merge all search results
2. Remove duplicates by DOI/title matching
3. Export to screening database

### 8. Data Management

**Fields to Extract:**
- Bibliographic: Authors, Title, Year, Journal/Venue, DOI
- Study characteristics: Model type, Model size, Evaluation method
- Key findings: Primary results, Effect sizes (if applicable)
- Theoretical contribution: Framework, Concepts introduced
- Relevance: Primary research area (1-12 from scope)

**File Formats:**
- CSV for screening and extraction
- BibTeX for references
- Markdown for synthesis

### 9. Quality Assurance

**Inter-rater Reliability (Simulated):**
- Two independent screening passes
- Calculate Cohen's Kappa
- Target κ > 0.6 for substantial agreement
- Third reviewer for conflicts

**Search Reproducibility:**
- Document exact search strings
- Record search dates
- Save search results before screening
- Version control all data files

### 10. Expected Outputs

**Quantitative Estimates:**
- Expected papers identified: 2,000-3,000
- Expected after deduplication: 1,500-2,000
- Expected after title/abstract screening: 300-400
- Expected after full-text screening: 150-200
- Expected final inclusion: 100-150

**Deliverables:**
1. PRISMA 2020 flow diagram
2. Comprehensive reference database
3. Thematic synthesis (12 research areas)
4. Gap analysis
5. Comparison tables
6. Risk of bias assessment
7. Complete bibliography

---

## Approval Request

**Please review and approve this search strategy before I proceed with execution.**

Key decisions for approval:
1. ✓ Database selection (arXiv, OpenAlex, Semantic Scholar primary)
2. ✓ Search terms (6 search strings covering all topics)
3. ✓ Inclusion/exclusion criteria
4. ✓ Date range (2018-2024 with exceptions for seminal works)
5. ✓ Quality standards (κ > 0.6, PRISMA compliance)

**Modifications needed? Please specify any changes to:**
- Additional databases
- Modified search terms
- Different inclusion criteria
- Alternative date ranges

---

*Search strategy developed following PRISMA 2020 guidelines*
*Date: November 14, 2024*
*Reviewer: Literature Review Agent (ASSISTANT Mode)*