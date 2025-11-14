# Systematic Literature Search Strategy

## Databases to Search

### Primary Databases
1. **OpenAlex** - Comprehensive multidisciplinary coverage
2. **arXiv** - Preprints in AI, computer science, and neuroscience
3. **PubMed** - Biomedical and neuroscience literature
4. **PhilPapers** - Philosophy literature (if available via web search)

### Supplementary Sources
- Semantic Scholar - Citations and related papers
- Google Scholar - Grey literature and cited-by searches
- Direct references from Chalmers (2023) paper

## Search Terms by Concept

### Consciousness Theories Block
```
("Global Workspace Theory" OR "Global Neuronal Workspace" OR GWT OR GNW OR "Baars" OR "Dehaene")
OR
("Integrated Information Theory" OR IIT OR "phi metric" OR "Tononi")
OR
("Higher-Order Thought" OR HOT OR "Higher-Order Perception" OR HOP OR "Rosenthal" OR "Gennaro")
OR
("Recurrent Processing Theory" OR RPT OR "Lamme" OR "recurrent feedback")
OR
("Attention Schema Theory" OR AST OR "Graziano")
OR
("functionalism" AND consciousness)
OR
("embodied cognition" OR "enactive" OR "sensorimotor" AND consciousness)
```

### AI/LLM Block
```
("large language model" OR LLM OR "language model" OR GPT OR "transformer" OR "neural network")
OR
("artificial intelligence" OR AI OR "machine consciousness" OR "artificial consciousness")
OR
("deep learning" OR "neural architecture")
```

### Combined Searches

#### Search 1: Consciousness Theories + LLMs
```
(
  "Global Workspace Theory" OR GWT OR
  "Integrated Information Theory" OR IIT OR
  "Higher-Order Thought" OR HOT OR
  "Recurrent Processing Theory" OR
  "Attention Schema Theory" OR AST OR
  functionalism OR
  "embodied cognition"
)
AND
(
  "large language model" OR LLM OR
  "artificial intelligence" OR AI OR
  consciousness OR awareness
)
```

#### Search 2: Specific Consciousness Requirements
```
(
  "recurrent processing" OR
  "global workspace" OR
  "unified agency" OR
  "binding problem" OR
  "symbol grounding" OR
  embodiment OR
  "attention mechanism"
)
AND
(
  "language model" OR
  "neural network" OR
  "artificial intelligence"
)
AND
(consciousness OR sentience OR awareness)
```

#### Search 3: Key Authors
```
(
  Chalmers OR Baars OR Dehaene OR
  Tononi OR Rosenthal OR Gennaro OR
  Lamme OR Graziano OR Harnad
)
AND
(
  "artificial intelligence" OR
  "language model" OR
  consciousness OR
  "computational theory"
)
```

#### Search 4: Architectural Features
```
(
  transformer OR "attention mechanism" OR
  "recurrent neural network" OR RNN OR
  "feedback loop" OR "self-model" OR
  metacognition
)
AND
(
  consciousness OR awareness OR sentience
)
```

## Database-Specific Queries

### OpenAlex Query
```
(title.search:"consciousness" OR abstract.search:"consciousness")
AND
(title.search:"language model" OR abstract.search:"artificial intelligence")
AND
publication_year:>1988
```

### arXiv Query
```
(ti:consciousness OR abs:consciousness)
AND
(ti:"language model" OR ti:"artificial intelligence" OR abs:"neural network")
AND
cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR cat:q-bio.NC
```

### PubMed Query (MeSH + Keywords)
```
(
  "Consciousness"[Mesh] OR "Models, Theoretical"[Mesh] OR
  "Neural Networks, Computer"[Mesh]
)
AND
(
  "artificial intelligence"[tiab] OR "language model"[tiab] OR
  "global workspace"[tiab] OR "integrated information"[tiab]
)
AND
("1988/01/01"[PDAT] : "2025/12/31"[PDAT])
```

## Citation Tracking

### Backward Citation Chaining
Extract and review all references from:
- Chalmers, D.J. (2023). Could a Large Language Model be Conscious? arXiv:2303.07103

### Forward Citation Tracking
Find all papers that cite:
- Chalmers (2023) paper
- Key seminal works:
  - Baars (1988) - A Cognitive Theory of Consciousness
  - Tononi (2004) - An information integration theory of consciousness
  - Dehaene et al. (2001) - Towards a cognitive neuroscience of consciousness
  - Lamme (2006) - Towards a true neural stance on consciousness

## Search Filters

**Date Range:** 1988-01-01 to 2025-12-31

**Publication Types:**
- Journal articles
- Conference proceedings
- Preprints (arXiv, bioRxiv, PhilPapers)
- Book chapters (if relevant)

**Language:** English

**Availability:** Abstracts required minimum; full text preferred

## Expected Yield

**Estimated Results per Database:**
- OpenAlex: ~2,000-5,000 records
- arXiv: ~500-1,000 records
- PubMed: ~300-800 records
- Total before deduplication: ~3,000-7,000 records
- Expected after deduplication: ~2,500-5,000 unique records
- Expected after screening: ~100-300 included studies

## Quality Control

1. **Search reproducibility:** Document exact query strings, database versions, search dates
2. **Pilot testing:** Test queries on small samples before full execution
3. **Sensitivity checks:** Verify known key papers are retrieved
4. **Deduplication protocol:** Use DOI, title, and author matching

## Update Strategy

Given the rapidly evolving field:
- Document exact search dates
- Plan for potential update searches before publication
- Monitor key journals/conferences for new relevant papers

---

**Search Protocol Version:** 1.0
**Date:** 2025-11-14
**Estimated Completion:** 1-2 weeks for full search and screening
**Librarian Consultation:** N/A (automated via MCP servers)
