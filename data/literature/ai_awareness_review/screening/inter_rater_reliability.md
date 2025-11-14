# Inter-Rater Reliability Analysis
## Title/Abstract Screening

### Agreement Matrix

|                    | Reviewer 2: Include | Reviewer 2: Exclude | Total |
|--------------------|--------------------|--------------------|--------|
| **Reviewer 1: Include** | 77                 | 6                  | 83     |
| **Reviewer 1: Exclude** | 8                  | 9                  | 17     |
| **Total**              | 85                 | 15                 | 100    |

### Cohen's Kappa Calculation

**Observed Agreement (Po):**
- Both reviewers agreed: 77 (both include) + 9 (both exclude) = 86
- Po = 86/100 = 0.86

**Expected Agreement by Chance (Pe):**
- Probability Reviewer 1 includes: 83/100 = 0.83
- Probability Reviewer 1 excludes: 17/100 = 0.17
- Probability Reviewer 2 includes: 85/100 = 0.85
- Probability Reviewer 2 excludes: 15/100 = 0.15

- Expected both include: 0.83 × 0.85 = 0.7055
- Expected both exclude: 0.17 × 0.15 = 0.0255
- Pe = 0.7055 + 0.0255 = 0.731

**Cohen's Kappa:**
κ = (Po - Pe) / (1 - Pe)
κ = (0.86 - 0.731) / (1 - 0.731)
κ = 0.129 / 0.269
**κ = 0.48**

### Interpretation
- κ = 0.48 indicates **moderate agreement** (0.41-0.60 range)
- This is below our target of κ > 0.6 for substantial agreement

### Disagreement Analysis

**Cases where Reviewer 1 included but Reviewer 2 excluded (6 cases):**
1. Study 008: Constitutional AI - Reviewer 2 focused on safety vs awareness
2. Study 013: Vision-Language Models - Reviewer 2 considered out of scope
3. Study 027: Synthetic Data for Sycophancy - Reviewer 2 saw as training method
4. Study 030: Reversal Curse - Reviewer 2 saw as learning limitation
5. Study 037: Zero-Shot Planning - Reviewer 2 didn't connect planning to awareness
6. Study 043: Self-Training - Reviewer 2 focused on training vs metacognition

**Cases where Reviewer 2 included but Reviewer 1 excluded (8 cases):**
1. Study 019: Red Teaming - Reviewer 2 saw awareness testing aspect
2. Study 024: Geometry of Truth - Reviewer 2 connected to self-awareness
3. Study 033: Learning to Listen - Reviewer 2 identified social awareness
4. Study 040: Mechanistic Interpretability - Reviewer 2 saw mechanism importance
5. Study 046: Emergent Semantics - Reviewer 2 connected to semantic awareness
6. Study 050: Social Biases - Reviewer 2 identified social awareness aspect
7. Study 062: Planning for Code - Reviewer 2 saw metacognitive planning
8. Study 088: Measure of Intelligence - Reviewer 2 included awareness component

### Resolution Strategy

Given the moderate agreement (κ = 0.48), a third reviewer perspective was simulated to resolve conflicts:

**Resolution Criteria Applied:**
1. Include if paper directly examines any of the four awareness dimensions
2. Include if paper provides evaluation methods for awareness
3. Include if paper discusses risks/implications of awareness
4. Include if paper contributes theoretical frameworks
5. Exclude if paper is purely technical without awareness relevance

**Final Decisions After Resolution:**
- 14 conflicts resolved
- Final included: 85 papers
- Final excluded: 15 papers

### Refined Screening Criteria

Based on disagreements, we refined our criteria:
1. **Metacognition**: Include all papers on reasoning, self-correction, planning, or self-improvement that involve reflection on cognitive processes
2. **Self-awareness**: Include papers on knowledge boundaries, uncertainty, self-recognition, or limitations awareness
3. **Social awareness**: Include ToM, social norms, perspective-taking, and social interaction understanding
4. **Situational awareness**: Include context understanding, environmental awareness, and evaluation detection
5. **Risks**: Include deception, manipulation, safety implications of awareness

### Quality Assurance

To improve reliability in future rounds:
1. Developed explicit coding manual with examples
2. Created decision tree for borderline cases
3. Established hierarchy of inclusion criteria
4. Documented rationale for all disagreements

---
**Conclusion:** While initial κ = 0.48 was below target, the resolution process and criteria refinement resulted in a robust set of 85 included papers for full-text screening.