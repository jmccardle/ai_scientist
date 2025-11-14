# Systematic Literature Review Search Strategy
## Constitutional AI and Related Foundations

### 1. Research Question
What are the foundational concepts, methods, and related work surrounding Constitutional AI and its approach to training harmless AI systems through self-improvement and AI feedback?

### 2. Databases to Search
- **OpenAlex** - Comprehensive academic database
- **arXiv** - Preprints in AI/ML, Computer Science
- **Semantic Scholar** - AI-focused academic search
- **PubMed** - For human-computer interaction and safety studies
- **Google Scholar** - Supplementary search for grey literature

### 3. Search Terms and Boolean Logic

#### Core Search String Components:

**Group A - Constitutional AI and RLHF:**
- ("constitutional AI" OR "constitutional artificial intelligence")
- ("reinforcement learning from human feedback" OR RLHF OR "RL from human feedback")
- ("reinforcement learning from AI feedback" OR RLAIF OR "RL from AI feedback")
- ("preference learning" OR "preference modeling")
- ("reward modeling" OR "reward model")

**Group B - AI Alignment and Safety:**
- ("AI alignment" OR "AI safety" OR "aligned AI")
- ("harmless AI" OR "harmful outputs" OR "AI harm")
- ("helpful honest harmless" OR HHH)
- ("value alignment" OR "human values")
- ("safe AI" OR "AI risk")

**Group C - Methods and Techniques:**
- ("chain of thought" OR "chain-of-thought" OR CoT)
- ("self-critique" OR "self-criticism" OR "self-improvement")
- ("red teaming" OR "adversarial testing")
- ("scalable oversight" OR "scalable supervision")
- ("constitutional principles" OR "rule-based AI")

**Group D - Language Models:**
- ("language model" OR "large language model" OR LLM)
- ("GPT" OR "BERT" OR "transformer model")
- ("conversational AI" OR "dialogue system" OR "chatbot")
- ("assistant AI" OR "AI assistant")

### 4. Search Queries by Database

#### OpenAlex Query:
```
(("constitutional AI" OR "reinforcement learning from human feedback" OR RLHF OR "reinforcement learning from AI feedback")
AND
("AI alignment" OR "AI safety" OR "harmless AI" OR "helpful honest harmless")
AND
("language model" OR LLM OR GPT))
OR
(("chain of thought" OR "self-critique" OR "red teaming")
AND
("AI safety" OR "AI alignment")
AND
publication_year:2015-2024)
```

#### arXiv Query:
```
cat:cs.AI OR cat:cs.LG OR cat:cs.CL
AND
(abstract:"constitutional AI" OR abstract:RLHF OR abstract:"reinforcement learning from human feedback"
OR abstract:"AI alignment" OR abstract:"AI safety"
OR abstract:"chain of thought" OR abstract:"self-critique" OR abstract:"red teaming")
AND
submittedDate:[2015 TO 2024]
```

#### PubMed Query:
```
("artificial intelligence"[MeSH] OR "machine learning"[MeSH])
AND
("safety"[Title/Abstract] OR "alignment"[Title/Abstract] OR "ethics"[Title/Abstract])
AND
("reinforcement learning"[Title/Abstract] OR "feedback"[Title/Abstract])
AND
("2015/01/01"[PDat] : "2024/12/31"[PDat])
```

### 5. Known Key Papers to Include (from Constitutional AI references)

#### RLHF Foundations:
1. Christiano et al. (2017) - Deep reinforcement learning from human preferences
2. Stiennon et al. (2020) - Learning to summarize from human feedback
3. Ouyang et al. (2022) - Training language models to follow instructions (InstructGPT)
4. Bai et al. (2022) - Training a helpful and harmless assistant

#### AI Alignment and Safety:
5. Askell et al. (2021) - A general language assistant as a lab for alignment
6. Ganguli et al. (2022) - Red teaming language models
7. Perez et al. (2022) - Red teaming language models with language models
8. Glaese et al. (2022) - Improving alignment of dialogue agents (Sparrow)

#### Chain-of-Thought and Reasoning:
9. Nye et al. (2021) - Show your work: Scratchpads
10. Wei et al. (2022) - Chain of thought prompting
11. Kojima et al. (2022) - Large language models are zero-shot reasoners

#### Self-Supervision and Critique:
12. Saunders et al. (2022) - Self-critiquing models for assisting human evaluators
13. Scheurer et al. - Training language models with language feedback
14. Madaan et al. (2023) - Self-refine: Iterative refinement with self-feedback

#### Scaling and Oversight:
15. Irving et al. (2018) - AI safety via debate
16. Christiano et al. (2018) - Supervising strong learners by amplifying weak experts
17. Bowman et al. (2022) - Measuring progress on scalable oversight

#### Evaluation and Capabilities:
18. Kadavath et al. (2022) - Language models (mostly) know what they know
19. Srivastava et al. (2022) - Beyond the imitation game (BIG-bench)
20. Thoppilan et al. (2022) - LaMDA: Language models for dialog applications

### 6. Search Execution Plan

**Phase 1 - Initial Database Search (Week 1):**
- Execute searches in all databases
- Export results to reference manager
- Document search date and result counts

**Phase 2 - Deduplication (Week 1):**
- Remove duplicate records
- Verify complete capture of known key papers

**Phase 3 - Title/Abstract Screening (Week 2):**
- Apply inclusion/exclusion criteria
- Double-screen 20% for reliability
- Calculate Cohen's Kappa

**Phase 4 - Full-Text Retrieval (Week 2-3):**
- Obtain full-text articles
- Document unavailable papers

**Phase 5 - Full-Text Screening (Week 3-4):**
- Detailed eligibility assessment
- Extract key information

**Phase 6 - Data Extraction (Week 4-5):**
- Structured data extraction
- Quality assessment

**Phase 7 - Synthesis (Week 5-6):**
- Thematic analysis
- PRISMA flow diagram
- Narrative synthesis

### 7. Quality Assurance

- **Search Reproducibility:** All searches documented with date/time
- **Inter-rater Reliability:** Target κ > 0.6
- **PRISMA Compliance:** Follow 27-item checklist
- **Version Control:** Git tracking of all decisions
- **Audit Trail:** Complete documentation of excluded papers with reasons

### 8. Search Dates
- **Initial Search:** November 14, 2024
- **Update Search:** To be conducted before final synthesis
- **Search Coverage:** January 2015 - November 2024

### 9. Language Restrictions
- English language publications only
- Justified by focus on English-language AI systems

### 10. Grey Literature
- Conference proceedings included (NeurIPS, ICML, ACL, etc.)
- Preprints from arXiv included
- Technical reports from major AI labs included if peer-reviewed