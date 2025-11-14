# ACE Paper: Key References and Topics Extracted

## Paper Details
- **Title**: Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models
- **Authors**: Qizheng Zhang, Changran Hu, et al. (Stanford, SambaNova, UC Berkeley)
- **arXiv**: 2510.04618v1 [cs.LG] 6 Oct 2025

## Core Contributions
1. **ACE Framework**: Agentic Context Engineering for comprehensive context adaptation
2. **Addresses two key problems**:
   - Brevity bias: compression away of domain-specific knowledge
   - Context collapse: iterative degradation through monolithic rewriting
3. **Three-agent architecture**: Generator, Reflector, Curator
4. **Incremental delta updates**: Structured, itemized bullet-based context
5. **Grow-and-refine mechanism**: Prevents collapse while scaling

## Key Results
- **AppWorld agents**: +10.6% average improvement
- **Finance domain**: +8.6% average improvement
- **Efficiency**: 86.9% lower adaptation latency
- **AppWorld leaderboard**: Matches top-ranked GPT-4.1 agent using smaller open-source model

## Primary References from Paper

### Context Adaptation & Prompt Optimization
1. **GEPA [4]**: Agrawal et al. 2025 - Reflective prompt evolution via genetic-Pareto search
2. **MIPROv2 [36]**: Opsahl-Ong et al. 2024 - Joint optimization of instructions and demonstrations
3. **TextGrad [54]**: Yuksekgonul et al. 2024 - Automatic differentiation via text
4. **Reflexion [40]**: Shinn et al. 2023 - Verbal reinforcement learning for agents

### Agent Systems & Memory
5. **Dynamic Cheatsheet [41]**: Suzgun et al. 2025 - Test-time learning with adaptive memory
6. **A-MEM [48]**: Xu et al. 2025 - Agentic memory for LLM agents (Zettelkasten-inspired)
7. **Agent Workflow Memory [46]**: Wang et al. 2024 - Reusable workflows from trajectories
8. **AgentFly [59]**: Zhou et al. 2025 - Fine-tuning agents without fine-tuning LLMs
9. **ReAct [52]**: Yao et al. 2023 - Synergizing reasoning and acting
10. **SWE-Agent [49]**: Yang et al. 2024 - Agent-computer interfaces for software engineering

### In-Context Learning
11. **Many-shot ICL [3]**: Agarwal et al. 2024 - Many-shot in-context learning
12. **Few-shot learning [9]**: Brown et al. 2020 - Language models are few-shot learners

### RAG & Knowledge Integration
13. **Self-RAG [6]**: Asai et al. 2024 - Learning to retrieve, generate, and critique
14. **RAG [27]**: Lewis et al. 2020 - Retrieval-augmented generation for knowledge-intensive NLP
15. **RETRO [7]**: Borgeaud et al. 2022 - Improving language models by retrieving from trillions of tokens

### Long-Context LLMs
16. **YARN [39]**: Peng et al. 2023 - Efficient context window extension
17. **LIFT [34]**: Mao et al. 2024 - Improving long context understanding through fine-tuning
18. **Prompt Cache [17]**: Gim et al. 2024 - Modular attention reuse for low-latency inference
19. **CacheBlend [51]**: Yao et al. 2025 - Fast LLM serving for RAG with cached knowledge fusion
20. **CacheGen [30]**: Liu et al. 2024 - KV cache compression and streaming
21. **KiVi [32]**: Liu et al. 2024 - Tuning-free asymmetric 2bit quantization for KV cache
22. **InfiniGen [25]**: Lee et al. 2024 - Efficient generative inference with dynamic KV cache management

### Benchmarks & Evaluation
23. **AppWorld [43]**: Trivedi et al. 2024 - Controllable world of apps for benchmarking interactive agents
24. **FiNER [33]**: Loukas et al. 2022 - Financial numeric entity recognition for XBRL
25. **Formula [44]**: Wang et al. 2025 - Benchmarking LoRA methods for fine-tuning LLMs on financial datasets
26. **LegalBench [18]**: Guha et al. 2023 - Measuring legal reasoning in LLMs
27. **HotPotQA [50]**: Yang et al. 2018 - Multi-hop question answering
28. **Gorilla [38]**: Patil et al. 2024 - Large language model connected with massive APIs

### Chain-of-Thought & Reasoning
29. **CoT [47]**: Wei et al. 2022 - Chain-of-thought prompting elicits reasoning
30. **Self-Consistency [45]**: Wang et al. 2022 - Self-consistency improves CoT reasoning
31. **SelfElicit [31]**: Liu et al. 2025 - Language models know where relevant evidence is

### Compound AI Systems
32. **Compound AI Systems [55]**: Zaharia et al. 2024 - The shift from models to compound AI systems
33. **Decomposed Prompting [23]**: Khot et al. 2022 - Modular approach for solving complex tasks
34. **DSPy**: Framework for programming with foundation models

### Parameter-Efficient Methods
35. **LoRA [20]**: Hu et al. 2021 - Low-rank adaptation of large language models
36. **Prefix-Tuning [28]**: Li & Liang 2021 - Optimizing continuous prompts for generation
37. **PEFT [26]**: Lester et al. 2021 - Power of scale for parameter-efficient prompt tuning

### Machine Unlearning & Privacy
38. **Machine Unlearning [8]**: Bourtoule et al. 2021 - Making systems forget
39. **Unlearning LLMs [29]**: Liu et al. 2024 - Rethinking machine unlearning for LLMs
40. **GDPR Right to Erasure [1]**: EU Regulation 2016/679
41. **CCPA Right to Delete [2]**: California Civil Code 2018

### Transfer Learning & Domain Adaptation
42. **Transfer Learning Survey [60]**: Zhuang et al. 2019 - Comprehensive survey
43. **Transfer Learning [37]**: Pan & Yang 2010 - Survey on transfer learning
44. **Data Scarcity & Transfer [21]**: Hutchinson et al. 2017 - Overcoming data scarcity
45. **Domain Generalization [19]**: Gulrajani & Lopez-Paz 2021 - In search of lost domain generalization
46. **WILDS [24]**: Koh et al. 2021 - Benchmark of in-the-wild distribution shifts

### Code Generation & Program Synthesis
47. **Symbolic Language Generation [53]**: Ye et al. 2023 - Generating data for symbolic language
48. **Adaptive Self-Improvement [56]**: Zhang et al. 2025 - For ML library development
49. **Prompt Alchemist [16]**: Gao et al. 2025 - Automated LLM-tailored prompt optimization for test generation

### Systems & Efficiency
50. **Flora [11]**: Chen et al. 2025 - Effortless context construction to arbitrary length
51. **Long Context for NL2SQL [12]**: Chung et al. 2025 - Leveraging LLM extended context
52. **Putting All into Context [22]**: Jiang et al. 2025 - Simplifying agents with LCLMs
53. **Plan Caching [58]**: Zhang et al. 2025 - Cost-efficient serving via test-time plan caching
54. **Caravan [57]**: Zhang et al. 2024 - Practical online learning of in-network ML models

## Key Topics for Literature Review

### 1. Context Adaptation Methods
- In-context learning (few-shot, many-shot)
- Prompt engineering and optimization
- Natural language feedback
- Meta-prompting
- Context compression vs expansion
- Brevity bias in optimization

### 2. Agentic Systems
- LLM agents and multi-agent systems
- Agent memory and experience replay
- Tool use and API calling
- ReAct pattern (reasoning + acting)
- Agent planning and reflection
- Workflow learning

### 3. Self-Improving AI
- Test-time learning and adaptation
- Online learning for LLMs
- Continuous learning
- Self-reflection and self-correction
- Iterative refinement
- Feedback loops

### 4. Memory Systems
- External memory for LLMs
- Episodic vs semantic memory
- Memory retrieval and selection
- Memory organization (Zettelkasten, etc.)
- Dynamic memory updates
- Context windows and memory management

### 5. Long-Context LLMs
- Context window extension techniques
- KV cache optimization
- Attention mechanisms for long sequences
- Efficient inference for long contexts
- Position embeddings (RoPE, ALiBi, etc.)

### 6. Prompt Optimization
- Automatic prompt engineering
- Evolutionary prompt optimization
- Gradient-based prompt tuning
- Multi-objective optimization
- Prompt compression

### 7. Retrieval-Augmented Generation
- RAG architectures
- Self-RAG and adaptive retrieval
- Dense retrieval methods
- Retrieval-aware training

### 8. Financial NLP
- Financial entity recognition
- XBRL processing
- Numerical reasoning in finance
- Domain-specific LLM applications

### 9. Benchmarks for Agents
- Interactive coding environments
- Multi-turn task completion
- API understanding benchmarks
- Real-world agent evaluation

### 10. Efficiency & Systems
- KV cache reuse and compression
- Batching strategies
- Serving optimization
- Cost-performance tradeoffs

## Related Work Sections to Explore

### Brevity Bias in Optimization
- Convergence to generic prompts
- Loss of domain-specific detail
- Diversity in prompt optimization

### Context Collapse
- Monolithic rewriting issues
- Information loss over iterations
- Incremental vs full updates

### Modular Agent Architectures
- Separation of concerns (Generator/Reflector/Curator)
- Division of labor in compound AI systems
- Specialized vs general-purpose components

### Structured Context Representations
- Itemized bullets vs monolithic text
- Metadata-augmented context
- Hierarchical organization

### Grow-and-Refine Mechanisms
- Balancing expansion and pruning
- Deduplication strategies
- Semantic similarity-based merging
