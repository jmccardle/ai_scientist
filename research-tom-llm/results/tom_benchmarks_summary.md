# Theory of Mind Benchmarks and Evaluation Methods Summary

## Major ToM Benchmarks Identified

### 1. Classic False-Belief Tasks
- **Papers using:** S001, S004, S010
- **Task types:** Sally-Anne test, Unexpected contents, Location change
- **Best performance:** GPT-4 (75% accuracy)
- **Human baseline:** 6-year-old children (75%), Adults (92%)

### 2. Advanced Multi-Order ToM Tests
- **Papers using:** S002
- **Task types:** Second-order beliefs, Recursive mental states
- **Best performance:** GPT-4 (85% accuracy)
- **Human baseline:** 7-10 year old children (varies by task)

### 3. Game-Based Benchmarks

#### LLM-Hanabi (S007)
- **Task:** Cooperative card game requiring implicit communication
- **Performance:** GPT-4 (42% win rate) vs Humans (75%)
- **Key limitation:** Poor implicit mental state inference

#### Decrypto Benchmark (S015)
- **Task:** Clue-giving and guessing with opponent modeling
- **Performance:** GPT-4 (31% success) vs Humans (68%)
- **Key limitation:** Strategic ToM reasoning deficits

### 4. Novel Specialized Benchmarks

#### SocialNLI (S006)
- **Focus:** Social inference from dialogue
- **Metric:** F1 scores (GPT-4: 0.68)
- **Innovation:** Natural conversation context

#### TactfulToM (S008)
- **Focus:** White lie understanding
- **Performance:** GPT-4 (61%) vs Humans (89%)
- **Innovation:** Prosocial deception assessment

#### MOMENTS (S011)
- **Focus:** Multimodal ToM (vision + text)
- **Performance:** GPT-4V (52%) vs text-only GPT-4 (71%)
- **Innovation:** Cross-modal mental state inference

#### Planning ToM - PToM (S009)
- **Focus:** Belief and desire inference for planning
- **Performance:** GPT-4 (38%) vs Humans (81%)
- **Innovation:** Goal-directed ToM reasoning

#### SoMi-ToM (S013)
- **Focus:** Multi-perspective taking in embodied scenarios
- **Performance:** GPT-4 (48%) vs Humans (76%)
- **Innovation:** Multiple agent perspective tracking

### 5. Safety and Application-Oriented Assessments

#### ToM-Safety Suite (S017)
- **Focus:** Malicious use of ToM capabilities
- **Finding:** 43% manipulation success rate
- **Concern:** Potential for social engineering

#### ProToM Framework (S022)
- **Focus:** Prosocial behavior facilitation
- **Finding:** 23% cooperation increase with ToM feedback
- **Application:** Multi-agent collaboration

#### MIST Framework (S030)
- **Focus:** Bias detection through ToM
- **Finding:** 73% bias detection rate
- **Application:** Fairness evaluation

## Evaluation Methods Taxonomy

### 1. Prompting Strategies
- **Zero-shot:** Most common (18 studies)
- **Few-shot:** Used in 8 studies
- **Fine-tuning:** Limited use (2 studies)

### 2. Human Baseline Comparisons
- **Children (4-10 years):** 5 studies
- **Adult performance:** 17 studies
- **No human baseline:** 6 studies

### 3. Methodological Approaches
- **Direct evaluation:** Traditional ToM tasks (10 studies)
- **Game-based:** Interactive scenarios (4 studies)
- **Dialogue-based:** Conversational context (5 studies)
- **Multimodal:** Vision + language (3 studies)
- **Hybrid methods:** LLM + other techniques (3 studies)
- **Agent-based:** Multi-agent interactions (5 studies)

## Performance Patterns by Model

### GPT-4 (Most Evaluated)
- **Strengths:**
  - Best at classic false-belief tasks (75%)
  - Strong on structured ToM tests (85%)
  - Reasonable dialogue-based inference (F1: 0.68)
- **Weaknesses:**
  - Poor planning ToM (38%)
  - Limited multimodal ToM (52%)
  - Weak implicit communication (42% in Hanabi)

### Claude Series
- **Performance:** Generally 5-10% below GPT-4
- **Tested in:** 15 studies
- **Notable:** Better at safety-oriented tasks

### LLaMA Models
- **Performance:** Significantly below GPT-4 (typically 20-40% lower)
- **Finding:** Base models show minimal ToM (S002)
- **Limitation:** Poor generalization after RL training (S010)

## Key Methodological Innovations

1. **Synthetic Story Generation (S016)**
   - Programmable complexity levels
   - Performance drops from 78% (simple) to 41% (complex)

2. **Dual-Process Framework (S027)**
   - Multi-scale ToM modeling
   - 41% collaboration efficiency improvement

3. **Validity Testing (S028)**
   - Revealed 35% variance with rephrasing
   - Highlights measurement reliability issues

4. **Hybrid Approaches (S020, S029)**
   - LLM + inverse planning: 74% vs 58% LLM-only
   - Structured representations boost performance

## Critical Gaps Identified

1. **Robustness:** High sensitivity to prompt variations
2. **Generalization:** Task-specific performance, limited transfer
3. **Implicit reasoning:** Poor at unstated mental states
4. **Multimodal integration:** Vision-language alignment issues
5. **Higher-order ToM:** Recursive reasoning remains challenging
6. **Cultural bias:** Western-centric task design
7. **Developmental trajectory:** No clear learning progression