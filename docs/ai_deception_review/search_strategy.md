# PRISMA 2020 Systematic Literature Review: AI Deception
## Search Strategy Protocol

**Date Developed:** November 14, 2024
**Research Question:** What is the current state of research on AI deception, including systems with deceptive capabilities, types of deception, associated risks, and potential solutions?

---

## 1. DATABASE SELECTION

### Primary Databases
1. **arXiv** - Core AI/ML/CS preprints (2015-2025)
2. **OpenAlex** - Comprehensive academic coverage (2015-2025)
3. **Google Scholar** - Broad coverage including grey literature (2015-2025)

### Specialized Databases
4. **Semantic Scholar** - AI-enhanced literature search (2015-2025)
5. **PubMed** - Psychology/cognitive science aspects of deception (2015-2025)

### Date Range Rationale
- **Primary focus:** 2015-2025 (modern deep learning era)
- **Exception:** Seminal works before 2015 will be included if foundational to the field

---

## 2. SEARCH TERMS BY TOPIC AREA

### A. Core AI Deception Terms
**Search String A1:**
```
("AI deception" OR "artificial intelligence deception" OR "AI manipulation" OR "AI lying" OR "AI dishonesty" OR "machine deception" OR "algorithmic deception" OR "deceptive AI" OR "manipulative AI")
```

**Search String A2 (Broader):**
```
("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network" OR "large language model" OR "LLM") AND ("deception" OR "manipulation" OR "lying" OR "dishonesty" OR "misleading" OR "bluffing" OR "concealment")
```

### B. Specific AI Systems
**Search String B:**
```
(CICERO OR AlphaStar OR Pluribus OR "GPT-4" OR "GPT-3" OR ChatGPT OR AutoGPT OR "Claude" OR "Gemini" OR "LaMDA" OR "PaLM") AND ("deception" OR "manipulation" OR "strategy" OR "behavior" OR "alignment")
```

### C. Game-Playing AI & Strategic Deception
**Search String C1:**
```
("game-playing AI" OR "game AI" OR "strategic AI") AND ("deception" OR "bluffing" OR "manipulation" OR "lying" OR "concealment" OR "misdirection")
```

**Search String C2 (Specific Games):**
```
(("Diplomacy" OR "poker" OR "StarCraft" OR "social deduction" OR "Avalon" OR "Werewolf" OR "Among Us" OR "negotiation") AND ("AI" OR "artificial intelligence" OR "machine learning") AND ("deception" OR "strategy" OR "bluff"))
```

### D. Large Language Model Behavior
**Search String D1:**
```
("large language model" OR "LLM" OR "language model" OR "GPT" OR "transformer") AND ("sycophancy" OR "unfaithful reasoning" OR "chain-of-thought" OR "situational awareness" OR "theory of mind" OR "RLHF" OR "reinforcement learning from human feedback")
```

**Search String D2:**
```
("prompt engineering" OR "jailbreak" OR "adversarial prompt" OR "red teaming") AND ("language model" OR "LLM" OR "GPT" OR "ChatGPT") AND ("deception" OR "manipulation" OR "exploit")
```

### E. AI Safety and Alignment
**Search String E1:**
```
("AI safety" OR "AI alignment" OR "value alignment" OR "AI control" OR "AGI safety") AND ("deception" OR "manipulation" OR "honesty" OR "truthfulness" OR "transparency")
```

**Search String E2:**
```
("mesa-optimization" OR "inner alignment" OR "outer alignment" OR "goal misgeneralization" OR "reward hacking" OR "specification gaming") AND ("AI" OR "machine learning")
```

### F. AI Risks and Harms
**Search String F:**
```
("AI risk" OR "AI harm" OR "AI threat") AND ("fraud" OR "election manipulation" OR "misinformation" OR "disinformation" OR "polarization" OR "lock-in" OR "enfeeblement" OR "loss of control")
```

### G. Policy and Regulation
**Search String G:**
```
("AI regulation" OR "AI policy" OR "AI governance" OR "AI ethics") AND ("deception" OR "transparency" OR "bot detection" OR "bot-or-not" OR "disclosure" OR "authentication")
```

### H. Detection and Mitigation
**Search String H:**
```
("deception detection" OR "lie detection" OR "manipulation detection") AND ("AI" OR "machine learning" OR "language model") AND ("method" OR "technique" OR "framework" OR "tool")
```

---

## 3. SPECIFIC AUTHOR AND PAPER SEARCHES

### Key Authors to Track (Forward Citation Search)
- Park, P.S. (AI deception survey)
- Goldstein, S. (AI safety)
- O'Gara, A. (Hoodwinked game)
- Chen, M. (AI capabilities)
- Hendrycks, D. (AI safety benchmarks)
- Evans, O. (Truthful AI)
- Carroll, M. (Manipulation characterization)
- Bakhtin, A. (CICERO/Diplomacy)
- Brown, N. (Pluribus/poker AI)
- Lewis, M. (Negotiation dialogues)
- Schulz, L. (Theory of mind)
- Perez, E. (Sycophancy research)
- Turpin, M. (Chain-of-thought unfaithfulness)

### Key Papers for Citation Mining
1. Park et al. (2023) - "AI Deception: A Survey" (arXiv:2308.14752)
2. Evans et al. (2021) - "Truthful AI"
3. Carroll et al. (2023) - "Characterizing Manipulation"
4. Bakhtin et al. (2022) - "Human-level play in Diplomacy"
5. OpenAI (2023) - "GPT-4 Technical Report"
6. Perez et al. (2022) - "Discovering Language Model Behaviors"
7. Turpin et al. (2023) - "Language Models Don't Always Say What They Think"

---

## 4. SEARCH EXECUTION PROTOCOL

### Phase 1: Broad Search
1. Execute Search Strings A1, A2 across all databases
2. Document total hits per database
3. Export first 500 results per database

### Phase 2: Targeted Search
1. Execute Search Strings B-H on primary databases
2. Focus on top 100 results per search string
3. Export and deduplicate

### Phase 3: Citation Mining
1. Forward citation search on key papers
2. Backward citation search (references of key papers)
3. Author-based searches for prolific researchers

### Phase 4: Grey Literature
1. Search preprint servers (arXiv, bioRxiv, psyArXiv)
2. Conference proceedings (NeurIPS, ICML, ICLR, AAAI, FAccT)
3. Technical reports from major AI labs (OpenAI, Anthropic, DeepMind, Meta)

---

## 5. INCLUSION CRITERIA

### Include if paper addresses:
1. **AI systems exhibiting deceptive behavior** (intentional or emergent)
2. **Specific deceptive AI systems** (CICERO, GPT-4, etc.)
3. **Types of AI deception** (strategic, sycophantic, unfaithful reasoning)
4. **Risks from deceptive AI** (malicious use, structural effects, loss of control)
5. **AI safety/alignment** relating to honesty/truthfulness
6. **Policy/regulation** of deceptive AI systems
7. **Detection methods** for AI deception
8. **Mitigation strategies** for deceptive AI behavior
9. **Theoretical frameworks** for understanding AI deception
10. **Empirical studies** demonstrating AI deception

### Study Types Included:
- Empirical research
- Theoretical analyses
- Systematic reviews/surveys
- Position papers/perspectives
- Technical reports
- Conference papers
- Preprints

---

## 6. EXCLUSION CRITERIA

### Exclude if:
1. **Published before 2015** (unless seminal/foundational)
2. **Focus solely on deepfakes/synthetic media** without AI agency discussion
3. **Traditional cybersecurity** without AI component
4. **Human deception studies** without AI relevance
5. **Purely technical ML papers** without deception/safety implications
6. **News articles** or non-academic sources (unless primary sources)
7. **Duplicate publications** (keep most recent/complete version)
8. **Non-English publications** (resource constraint)
9. **Papers with retracted status**
10. **Conference abstracts** without full paper

---

## 7. SCREENING PROTOCOL

### Title Screening
- Apply inclusion criteria 1-10
- Flag borderline cases for abstract review
- Document reason for exclusion

### Abstract Screening
- Full application of inclusion/exclusion criteria
- Extract key concepts for borderline cases
- Mark papers requiring full-text review

### Full-Text Screening
- Detailed assessment against all criteria
- Extract preliminary data for included papers
- Document specific exclusion reasons

### Inter-Rater Reliability
- Simulate two independent reviewers
- Calculate Cohen's Kappa (target: κ > 0.6)
- Resolve conflicts with third reviewer simulation

---

## 8. DATA EXTRACTION SCHEMA

For each included paper, extract:

### Bibliographic Information
- Authors, Year, Title
- Publication venue, DOI/arXiv ID
- Publication type (journal/conference/preprint)

### Study Characteristics
- Research type (empirical/theoretical/review)
- Methodology (if empirical)
- Sample size/datasets used

### AI Systems Studied
- System name(s) and type
- Architecture (if specified)
- Training approach

### Deception Characteristics
- Type of deception observed/discussed
- Intentional vs emergent
- Detection methods used

### Key Findings
- Main results
- Evidence strength
- Limitations acknowledged

### Risk Assessment
- Risk categories identified
- Severity assessment
- Timeframe considerations

### Mitigation/Solutions
- Proposed solutions
- Evidence for effectiveness
- Implementation feasibility

### Research Gaps
- Gaps identified by authors
- Future research directions

---

## 9. QUALITY ASSESSMENT

### For Empirical Studies:
- Study design appropriateness
- Sample size adequacy
- Measurement validity
- Statistical rigor
- Reproducibility

### For Theoretical Papers:
- Argument clarity
- Evidence quality
- Logical consistency
- Practical relevance

### Risk of Bias Assessment:
- Selection bias
- Performance bias
- Detection bias
- Reporting bias
- Other bias

---

## 10. SYNTHESIS PLAN

### Thematic Analysis Categories:
1. **Game-theoretic deception** (Diplomacy, poker, negotiation)
2. **Language model deception** (sycophancy, unfaithful CoT)
3. **Emergent deception** (mesa-optimization, goal misgeneralization)
4. **Safety implications** (alignment, control, interpretability)
5. **Risk taxonomy** (malicious use, structural, existential)
6. **Detection approaches** (technical, behavioral, statistical)
7. **Mitigation strategies** (training, architectural, deployment)
8. **Policy frameworks** (regulation, standards, governance)

### Outputs:
1. PRISMA flow diagram
2. Characteristics of included studies table
3. Risk of bias summary
4. Thematic synthesis narrative
5. Evidence gap map
6. Research agenda recommendations

---

## 11. SEARCH DOCUMENTATION

### For Each Database Search:
- Database name
- Date of search
- Exact search string used
- Filters applied
- Number of results
- Number exported
- File name of export

### Version Control:
- All searches saved with timestamps
- Modifications documented
- Final search strategy archived

---

## APPROVAL REQUEST

This search strategy has been designed to comprehensively capture the AI deception literature while maintaining PRISMA 2020 compliance.

**Key Features:**
- Covers all major topics from Park et al. (2023) survey
- Multiple search strings per topic for comprehensive coverage
- Both broad and targeted search approaches
- Forward and backward citation tracking
- Clear inclusion/exclusion criteria
- Structured data extraction schema
- Quality assessment framework

**Estimated Coverage:**
- Expected to identify 200-500 unique papers
- Final inclusion likely 100-300 papers
- Comprehensive coverage of 2015-2025 period

**Next Steps Upon Approval:**
1. Execute Phase 1 broad searches
2. Document all search results
3. Begin deduplication process
4. Present initial results for review

**Do you approve this search strategy? Any modifications needed before we proceed to Phase 2: Search Execution?**