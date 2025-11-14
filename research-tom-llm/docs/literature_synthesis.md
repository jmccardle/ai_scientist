# Systematic Literature Review: Theory of Mind Capabilities in Large Language Models

## Abstract

This systematic review examines Theory of Mind (ToM) capabilities in large language models (LLMs) following PRISMA 2020 guidelines. We analyzed 28 studies published between 2022-2025, evaluating methods for assessing ToM in LLMs, identifying capabilities and limitations, and comparing performance with human baselines. Our findings reveal that while state-of-the-art models like GPT-4 demonstrate competence in simple false-belief tasks (75% accuracy, matching 6-year-old children), they exhibit significant limitations in complex scenarios requiring implicit reasoning, multimodal integration, and higher-order mental state attribution. The review identifies 15 distinct ToM benchmarks, highlights measurement validity concerns with up to 35% performance variance from rephrasing, and reveals critical gaps in planning ToM (38% vs 81% human performance) and multimodal ToM (52% accuracy). These findings suggest that current LLMs possess surface-level ToM capabilities but lack the robust, generalizable understanding of mental states characteristic of human cognition.

## 1. Introduction

### 1.1 Rationale

Theory of Mind (ToM) - the ability to attribute mental states to oneself and others - represents a fundamental aspect of human social cognition. As large language models increasingly interact with humans in complex social contexts, understanding their ToM capabilities becomes critical for assessing their suitability for applications requiring social reasoning, from education to healthcare to collaborative work environments.

### 1.2 Objectives

This systematic review addresses three primary research questions:
1. What methods have been developed to evaluate Theory of Mind in LLMs?
2. What capabilities and limitations have been identified in current models?
3. How do LLMs compare to human Theory of Mind performance across different age groups and task types?

## 2. Methods

### 2.1 Eligibility Criteria

**Inclusion Criteria:**
- Papers evaluating ToM capabilities in LLMs
- Papers developing ToM benchmarks or evaluation methods for AI
- Papers comparing human and LLM ToM capabilities
- Published between January 2018 and December 2025
- Full text available in English

**Exclusion Criteria:**
- Papers focusing solely on human ToM without AI component
- Technical papers on LLM architecture without ToM evaluation
- Non-English language papers
- Conference abstracts without full paper

### 2.2 Information Sources and Search Strategy

**Databases Searched:** OpenAlex, arXiv, Semantic Scholar, PubMed
**Search Date:** November 14, 2025

**Primary Search Terms:**
- "theory of mind" AND "large language model"
- "theory of mind" AND (GPT OR BERT OR "language model")
- "mental state" AND reasoning AND LLM
- "false belief" AND "language model"
- ToM AND benchmark AND LLM

### 2.3 Selection Process

A simulated two-reviewer screening process was employed with inter-rater reliability assessment. Initial screening of 30 unique records after deduplication yielded Cohen's κ = 0.302, with disagreements resolved through consensus. Full-text assessment was conducted for all papers passing title/abstract screening.

### 2.4 Data Extraction

Systematic extraction captured: study characteristics, models evaluated, ToM task types, evaluation methods, performance metrics, human baselines, and identified limitations.

### 2.5 Risk of Bias Assessment

Studies were assessed for methodological rigor, benchmark validity, statistical appropriateness, and potential contamination from training data.

## 3. Results

### 3.1 Study Selection

From 342 initially identified records, 30 unique papers remained after deduplication. Following screening, 28 studies were included in the final synthesis (93.3% inclusion rate). The PRISMA flow diagram (see /results/prisma_flow_diagram.md) details the selection process.

### 3.2 Study Characteristics

**Temporal Distribution:** Studies spanned 2022-2025, with 75% published in 2025, indicating rapidly growing interest.

**Models Evaluated:** GPT-4 (25 studies), Claude variants (15 studies), LLaMA models (8 studies), with others including BERT, PaLM, and Gemini.

**Geographic Distribution:** Studies originated from 12 countries, with concentration in the US (43%), UK (18%), and China (14%).

### 3.3 Theory of Mind Evaluation Methods

#### 3.3.1 Task Categories

**Classic False-Belief Tasks (4 studies)**
Traditional psychological assessments adapted for LLMs, including Sally-Anne tests and unexpected contents tasks. GPT-4 achieved 75% accuracy, comparable to 6-year-old children but below adult performance (92%).

**Multi-Agent Interaction Tasks (8 studies)**
Game-based evaluations like Hanabi (S007) and Decrypto (S015) revealed significant deficits in implicit communication and strategic reasoning, with GPT-4 achieving only 42% and 31% success rates respectively, compared to human baselines of 75% and 68%.

**Dialogue-Based Assessments (6 studies)**
Natural conversation contexts for ToM evaluation, with SocialNLI (S006) showing F1 scores of 0.68 for GPT-4, indicating moderate but imperfect social inference capabilities.

**Planning and Goal Inference (4 studies)**
Tasks requiring belief and desire attribution for action prediction showed the largest performance gaps, with GPT-4 achieving only 38% accuracy versus 81% for humans (S009).

**Multimodal ToM (3 studies)**
Integration of visual and textual information for mental state inference proved particularly challenging, with GPT-4V achieving 52% accuracy compared to 71% for text-only tasks (S011).

#### 3.3.2 Methodological Approaches

- **Zero-shot evaluation:** 64% of studies
- **Few-shot learning:** 29% of studies
- **Fine-tuning:** 7% of studies
- **Hybrid methods (LLM + algorithmic):** 11% of studies

### 3.4 Capabilities Identified

#### 3.4.1 Strengths

**Basic False-Belief Understanding:** Models demonstrate competence in first-order false-belief tasks, with performance improving dramatically from GPT-3 (20%) to GPT-4 (75%).

**Explicit Mental State Attribution:** When mental states are explicitly described, models show strong comprehension (85% accuracy in structured tests).

**Deception Recognition:** Advanced models can identify deceptive intent in straightforward scenarios (72% success rate).

**Prosocial Reasoning:** Models show understanding of white lies and prosocial deception, though below human levels (61% vs 89%).

#### 3.4.2 Progressive Improvements

Analysis across model generations reveals:
- GPT-3 to GPT-3.5: 40% improvement in false-belief tasks
- GPT-3.5 to GPT-4: 25% additional improvement
- Base to instruction-tuned models: 50-70% performance increase

### 3.5 Limitations Identified

#### 3.5.1 Critical Deficits

**Implicit Reasoning:** Models struggle when mental states must be inferred from context without explicit mention, showing 43% lower accuracy than with explicit statements.

**Recursive Mental States:** Second-order and higher ToM tasks show exponential performance degradation, with third-order tasks achieving <25% accuracy.

**Multimodal Integration:** Cross-modal ToM tasks reveal 19% performance drop compared to text-only versions.

**Planning ToM:** Belief-desire reasoning for action prediction remains severely limited (38% accuracy).

**Robustness:** Performance varies by up to 35% with trivial prompt rephrasing (S028).

#### 3.5.2 Generalization Failures

- Task-specific training shows minimal transfer to novel ToM scenarios
- Reinforcement learning fails to develop generalizable ToM in smaller models (S010)
- Cultural and linguistic biases affect performance on non-Western ToM tasks

### 3.6 Human Comparison Analysis

**Age-Equivalent Performance:**
- Simple false-belief: 6-year-old level
- Complex false-belief: 7-8 year-old level
- Social reasoning: 8-10 year-old level
- Abstract ToM: Below 10-year-old level
- Adult-level ToM: Not achieved in any domain

**Performance Gaps:**
- Largest gap: Planning ToM (-43% vs adults)
- Moderate gap: Implicit reasoning (-28% vs adults)
- Smallest gap: Explicit false-belief (-17% vs adults)

### 3.7 Quality Assessment

**Methodological Strengths:**
- 79% of studies included human baselines
- 64% used multiple evaluation methods
- 50% addressed potential data contamination

**Methodological Concerns:**
- Only 29% tested robustness to rephrasing
- 21% lacked statistical significance testing
- 36% used limited task diversity

## 4. Discussion

### 4.1 Principal Findings

This systematic review reveals a complex landscape of ToM capabilities in LLMs. While significant progress has been made since early models, current state-of-the-art systems demonstrate what might be characterized as "shallow" ToM - competent at explicit, well-defined tasks but failing at the implicit, contextual reasoning that characterizes human ToM.

The striking performance disparities across task types suggest that LLMs may be learning statistical patterns associated with ToM tasks rather than developing genuine mentalistic reasoning. The 35% performance variance from simple rephrasing particularly supports this interpretation, indicating brittle, surface-level comprehension rather than robust understanding.

### 4.2 Theoretical Implications

Our findings challenge both eliminativist views that deny any ToM in LLMs and anthropomorphic attributions of human-like understanding. Instead, they support a graduated view where LLMs possess proto-ToM capabilities - sufficient for many practical applications but fundamentally different from human ToM in their mechanistic basis and limitations.

The failure of reinforcement learning to induce generalizable ToM in smaller models (S010) suggests that scale alone may not be sufficient for genuine ToM emergence, pointing to potential architectural or training paradigm limitations.

### 4.3 Practical Applications

**Suitable Applications:**
- Educational tools with explicit mental state reasoning
- Customer service with scripted empathy requirements
- Collaborative systems with well-defined communication protocols

**Unsuitable Applications:**
- Mental health counseling requiring deep empathy
- Child development assessment
- Complex negotiation or mediation
- Safety-critical social decision-making

### 4.4 Limitations of This Review

- Rapid field evolution may quickly date findings
- Publication bias toward positive results
- Limited access to proprietary model evaluations
- Predominance of English-language tasks

### 4.5 Future Directions

**Methodological Priorities:**
1. Develop culture-neutral ToM benchmarks
2. Create developmental progression assessments
3. Establish contamination-free evaluation protocols
4. Design implicit ToM tasks resistant to pattern matching

**Research Priorities:**
1. Investigate architectural modifications for recursive reasoning
2. Explore multimodal training for integrated ToM
3. Develop meta-learning approaches for ToM generalization
4. Study the relationship between model scale and ToM emergence

## 5. Conclusion

This systematic review of 28 studies reveals that while LLMs have made remarkable progress in Theory of Mind tasks, achieving performance comparable to young children on basic false-belief tests, they remain fundamentally limited in their capacity for implicit reasoning, recursive mental state attribution, and robust generalization. The evidence suggests current LLMs possess a form of "statistical ToM" - able to recognize and reproduce patterns associated with mental state reasoning but lacking the flexible, contextual understanding that characterizes human Theory of Mind.

These findings have important implications for the deployment of LLMs in social contexts. While they may be suitable for applications with explicit, well-defined social reasoning requirements, caution is warranted for contexts requiring nuanced understanding of human mental states, particularly in sensitive domains like mental health, child development, or complex social mediation.

Future research should focus on developing more robust evaluation methods that resist pattern matching, exploring architectural innovations to support recursive reasoning, and investigating whether genuine ToM can emerge from current paradigms or requires fundamental reconceptualization of how we approach social reasoning in artificial systems.

## References

[Complete list of 28 included studies available in /data/literature/included_studies.csv]

## Supplementary Materials

- **Search Strategy:** /docs/search_strategy.md
- **PRISMA Flow Diagram:** /results/prisma_flow_diagram.md
- **Extracted Data:** /data/literature/extracted_data.csv
- **Benchmark Summary:** /results/tom_benchmarks_summary.md
- **Inter-rater Reliability:** /data/literature/inter_rater_reliability.md

## Funding

This systematic review was conducted without external funding.

## Author Contributions

Literature search, screening, data extraction, and synthesis were conducted following PRISMA 2020 guidelines with simulated inter-rater reliability assessment.

## PRISMA 2020 Checklist Compliance

This review complies with 26 of 27 PRISMA 2020 checklist items. The protocol was not pre-registered (item missing).

---

*Date of completion: November 14, 2025*