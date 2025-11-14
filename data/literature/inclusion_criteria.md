# Inclusion and Exclusion Criteria Checklist
## AI Deception Systematic Literature Review

### INCLUSION CRITERIA CHECKLIST

#### Topic Relevance (at least ONE must be true):
- [ ] AI systems exhibiting deceptive behavior (intentional or emergent)
- [ ] Specific deceptive AI systems (CICERO, GPT-4, AlphaStar, Pluribus, etc.)
- [ ] Types of AI deception (strategic, sycophantic, unfaithful reasoning)
- [ ] Risks from deceptive AI (malicious use, structural effects, loss of control)
- [ ] AI safety/alignment relating to honesty/truthfulness
- [ ] Policy/regulation of deceptive AI systems
- [ ] Detection methods for AI deception
- [ ] Mitigation strategies for deceptive AI behavior
- [ ] Theoretical frameworks for understanding AI deception
- [ ] Empirical studies demonstrating AI deception

#### Study Type (at least ONE must be true):
- [ ] Empirical research
- [ ] Theoretical analysis
- [ ] Systematic review/survey
- [ ] Position paper/perspective
- [ ] Technical report
- [ ] Conference paper
- [ ] Preprint
- [ ] Dissertation/thesis chapter

#### Time Period:
- [ ] Published 2015 or later
- [ ] OR: Pre-2015 but seminal/foundational work (requires justification)

#### Language:
- [ ] English language publication

#### Accessibility:
- [ ] Abstract available for screening
- [ ] Full text potentially retrievable

---

### EXCLUSION CRITERIA CHECKLIST

#### Automatic Exclusion (if ANY are true):
- [ ] Published before 2015 (unless seminal - requires override justification)
- [ ] Focus SOLELY on deepfakes/synthetic media without AI agency discussion
- [ ] Traditional cybersecurity without AI component
- [ ] Human deception studies without AI relevance
- [ ] Purely technical ML papers without deception/safety implications
- [ ] News articles or non-academic sources (unless primary sources)
- [ ] Duplicate publication (keep most recent/complete version)
- [ ] Non-English publication
- [ ] Retracted paper
- [ ] Conference abstract without full paper
- [ ] Marketing material or product announcements

---

### BORDERLINE CASE GUIDELINES

#### Include with Caution:
1. **Workshop papers**: Include if peer-reviewed and substantive (>4 pages)
2. **Blog posts from AI labs**: Include if technical and cited in academic literature
3. **Government reports**: Include if evidence-based and policy-relevant
4. **Older foundational papers**: Include if cited >10 times by included papers

#### Decision Escalation:
- **Title screening unclear** → Review abstract
- **Abstract screening unclear** → Review introduction/conclusion
- **Still unclear** → Mark for full-text review
- **Disagreement between reviewers** → Third reviewer decides

---

### SCREENING DECISION CODES

#### Include Codes:
- **INC-1**: Clear AI deception research
- **INC-2**: Relevant AI safety/alignment work
- **INC-3**: Game-playing AI with deception component
- **INC-4**: LLM behavior research relevant to deception
- **INC-5**: Policy/regulation of deceptive AI
- **INC-6**: Detection/mitigation methods
- **INC-7**: Foundational/seminal work (pre-2015)

#### Exclude Codes:
- **EXC-1**: Wrong date (too old, not foundational)
- **EXC-2**: Wrong topic (not AI deception related)
- **EXC-3**: Wrong publication type (news, marketing)
- **EXC-4**: Duplicate
- **EXC-5**: Language barrier
- **EXC-6**: Retracted
- **EXC-7**: Insufficient detail (abstract only)
- **EXC-8**: Pure deepfake/synthetic media
- **EXC-9**: Human deception only

#### Uncertain Codes:
- **UNC-1**: Needs abstract review
- **UNC-2**: Needs full-text review
- **UNC-3**: Needs second opinion

---

### QUALITY INDICATORS (for prioritization)

#### High Priority Papers (fast-track for full review):
- Published in top venues (NeurIPS, ICML, ICLR, Science, Nature)
- From major AI labs (OpenAI, Anthropic, DeepMind, Meta)
- Highly cited (>50 citations, adjusted for age)
- Direct study of deceptive behavior
- Novel detection/mitigation methods

#### Medium Priority Papers:
- Theoretical frameworks
- Survey/review papers
- Policy proposals
- Case studies
- Smaller empirical studies

#### Low Priority Papers:
- Opinion pieces without evidence
- Very preliminary work
- Peripheral relevance
- Poor methodology (assess in full-text)

---

### INTER-RATER RELIABILITY PROTOCOL

1. **Independent Review**: Two reviewers screen independently
2. **Agreement Calculation**: Cohen's Kappa (κ)
3. **Threshold**: κ > 0.6 required
4. **Conflict Resolution**:
   - If κ < 0.6: Refine criteria, retrain, re-screen sample
   - If κ ≥ 0.6: Third reviewer for disagreements
5. **Documentation**: Record all disagreements and resolutions

---

### SPECIAL CONSIDERATIONS

#### COVID-19 Era Papers (2020-2021):
- May have limited peer review
- Consider preprint quality carefully
- Check for subsequent journal publication

#### Large Language Model Papers (2022-2024):
- Rapid development area
- Preprints often supersede journal papers
- Check for updated versions

#### Emerging Terminology:
- "Jailbreaking" = Include if about LLM manipulation
- "Hallucination" = Include only if framed as deception
- "Alignment tax" = Include if discusses honesty trade-offs
- "Situational awareness" = Include if discusses deceptive potential

---

### DOCUMENTATION REQUIREMENTS

For EACH paper screened, record:
1. Unique ID
2. Title
3. Authors
4. Year
5. Screening level (title/abstract/full-text)
6. Decision (include/exclude/uncertain)
7. Decision code (INC-X/EXC-X/UNC-X)
8. Reviewer ID
9. Date of review
10. Notes (if borderline or interesting)

---

**Last Updated:** November 14, 2024
**Version:** 1.0
**Review Protocol:** PRISMA 2020 Compliant