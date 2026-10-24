# AI Engineering — RAG & LangChain Live Course

> A hands-on repository covering Retrieval-Augmented Generation (RAG) fundamentals, embedding-based search, vector databases, and LLM integration patterns.

[![Python](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/uv-0.5+-purple.svg)](https://docs.astral.sh/uv/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🎯 Learning Journey

This course is delivered in progressive phases. Each phase builds on the previous one and includes runnable code, real-world analogies, and a growing FAQ document.

- **Phase 1 — Foundations of RAG & LLM Interaction** ✅ *Current*
- Phase 2 — LangChain, Agents & Production Patterns *(upcoming)*

---

## 📚 Phase 1: Foundations of RAG & LLM Interaction

### What you will learn

By the end of this phase, you should be able to:

- [x] Call a hosted LLM with both single-turn and streaming responses.
- [x] Explain the role of embeddings in semantic search.
- [x] Convert raw text into dense vectors using a local embedding model.
- [x] Compare vectors with cosine similarity and Euclidean distance.
- [x] Build a simple Top-K retrieval pipeline from scratch.
- [x] Store and query vectors using **Qdrant**.
- [x] Configure vector collections, payloads, and scalar quantization.

---

## 🗂️ Repository Structure

```text
ai-engg-rag-live/
├── src/ai_engg_rag_live/
│   ├── 1_call_llm/                         # LLM API interaction
│   │   ├── call_llm_single_response.py     # Single complete response
│   │   └── call_llm_stream_response.py     # Token-by-token streaming
│   └── 2_learn_rag_basics/
│       └── 1_rag_basics.ipynb              # RAG fundamentals notebook
├── Frequently Asked Questions.txt          # Curated Q&A from the cohort
├── pyproject.toml                          # Project dependencies
└── README.md                               # This file
```

---

## 🚀 Quick Start

1. Install dependencies with `uv`:

   ```bash
   uv sync
   ```

2. Create a `.env` file with your credentials:

   ```bash
   OLLAMA_API_KEY=your_ollama_or_openrouter_key_here
   OLLAMA_MODEL=kimi-k2.7-code:cloud   # or any hosted model you prefer
   ```

3. Run an LLM example:

   ```bash
   uv run python src/ai_engg_rag_live/1_call_llm/call_llm_single_response.py
   ```

4. Launch the RAG notebook:

   ```bash
   uv run jupyter lab src/ai_engg_rag_live/2_learn_rag_basics/1_rag_basics.ipynb
   ```

---

## 🧩 Phase 1 Modules

Click each module below to expand the concepts, code references, and checkpoints.

---

<details open>
<summary><h3 style="display:inline">Module 1 — Calling LLMs: Single vs. Streaming</h3></summary>

Understanding the two most common interaction patterns with large language models.

#### Concepts covered

| Concept | Description |
| --- | --- |
| **Single response** | Send one prompt, wait for the full completion, then return it. |
| **Streaming response** | Receive generated tokens progressively as they are produced. |
| **Usage metadata** | Capture prompt and completion token counts from the final chunk. |
| **Async clients** | Use `ollama.AsyncClient` for non-blocking I/O. |

#### Code references

- [`src/ai_engg_rag_live/1_call_llm/call_llm_single_response.py`](src/ai_engg_rag_live/1_call_llm/call_llm_single_response.py)
- [`src/ai_engg_rag_live/1_call_llm/call_llm_stream_response.py`](src/ai_engg_rag_live/1_call_llm/call_llm_stream_response.py)

#### Checkpoints

- [x] Can send a question and receive a complete answer.
- [x] Can stream a response and print tokens as they arrive.
- [x] Can extract prompt/completion token usage from a streaming final chunk.

</details>

---

<details open>
<summary><h3 style="display:inline">Module 2 — RAG Fundamentals & Embeddings</h3></summary>

Building the retrieval layer of a RAG pipeline without any vector database first.

#### Concepts covered

| Concept | Description |
| --- | --- |
| **Documents** | Raw text records with metadata (topic, level). |
| **Embeddings** | Dense vectors produced by a sentence-transformer-style model. |
| **Semantic similarity** | Finding text that means the same thing even when wording differs. |
| **Cosine similarity** | Measures the angle between two vectors; higher is better. |
| **Euclidean distance** | Measures straight-line distance between vectors; lower is better. |
| **Top-K retrieval** | Selecting the K highest-scoring candidates for downstream use. |

#### Code references

- [`src/ai_engg_rag_live/2_learn_rag_basics/1_rag_basics.ipynb`](src/ai_engg_rag_live/2_learn_rag_basics/1_rag_basics.ipynb)

#### Practical flow

1. Prepare 20 technology-learning documents.
2. Embed all documents with a local model (`mxbai-embed-large:latest` / `nomic-embed-text:v1.5`).
3. Embed a natural-language query.
4. Score every document against the query using **cosine similarity**.
5. Return the **Top-K** most relevant documents.

#### Checkpoints

- [x] Can generate embeddings for a list of texts.
- [x] Can compare a query embedding against document embeddings.
- [x] Can rank results by similarity.
- [x] Understands the difference between cosine and Euclidean metrics.

</details>

---

<details open>
<summary><h3 style="display:inline">Module 3 — Vector Databases with Qdrant</h3></summary>

Moving from in-memory NumPy-style search to a production-grade vector store.

#### Concepts covered

| Concept | Description |
| --- | --- |
| **Qdrant client** | Connecting to a local Qdrant server (`http://localhost:6333`). |
| **Collection** | A named container of points with a fixed vector configuration. |
| **Vector params** | `size` (dimension) and `distance` metric (COSINE, DOT, EUCLID). |
| **Point** | A record containing `id`, `vector`, and `payload` metadata. |
| **Upsert** | Insert or update points in a collection. |
| **Query points** | Search a collection by vector similarity. |
| **Scalar quantization** | Compress vectors to reduce memory while keeping search quality. |

#### Code references

- [`src/ai_engg_rag_live/2_learn_rag_basics/1_rag_basics.ipynb`](src/ai_engg_rag_live/2_learn_rag_basics/1_rag_basics.ipynb)

#### Practical flow

1. Start Qdrant locally (Docker or binary).
2. Create a collection with vector parameters matching the embedding dimension.
3. Upsert points: each point holds a document vector plus topic/level payload.
4. Query with `query_points(...)` using the same embedding space.
5. Observe payload and score for each retrieved result.
6. Create a second collection with **INT8 scalar quantization** and compare results.

#### Checkpoints

- [x] Can create a Qdrant collection with correct dimension and distance metric.
- [x] Can upsert points with vectors and payloads.
- [x] Can query a collection and interpret `score`, `payload`, and `vector`.
- [x] Understands that the embedding model must match the collection dimension.
- [x] Can configure scalar quantization to compress stored vectors.

</details>

---

## 🧠 Key Takeaways

> Phase 1 teaches the core building blocks of a RAG system: **LLM interaction**, **text embeddings**, **similarity math**, **Top-K retrieval**, and **vector database persistence**.

- RAG does **not** train the LLM on your documents; it retrieves relevant snippets at query time.
- The embedding model and generation model are independent, but the query and documents must use the **same embedding space**.
- Similarity metrics matter: use the metric recommended by your embedding model.
- Vector databases such as Qdrant let you scale retrieval, attach metadata payloads, and tune memory/quality trade-offs.

---

## 📖 FAQ

A curated list of questions from the cohort is available in [`Frequently Asked Questions.txt`](Frequently%20Asked%20Questions.txt). It covers:

- RAG vs. LLM
- Embeddings, dimensions, and providers
- Cosine / dot product / Euclidean distance
- HNSW, exact vs. ANN search
- Chunking and retrieval strategy
- Streaming, API keys, and production patterns

---

## ✅ Phase 1 Completion Checklist

Use this checklist to confirm you have completed Phase 1 before moving on.

- [x] Module 1 — Called an LLM in single-response mode.
- [x] Module 1 — Streamed an LLM response and captured usage metadata.
- [x] Module 2 — Embedded documents and a query with a local model.
- [x] Module 2 — Computed cosine similarity and Euclidean distance manually.
- [x] Module 2 — Implemented Top-K retrieval from scratch.
- [x] Module 3 — Connected to Qdrant and created a collection.
- [x] Module 3 — Upserted vector points with payloads.
- [x] Module 3 — Queried Qdrant and retrieved relevant documents.
- [x] Module 3 — Experimented with scalar quantization/compression.

---

## 🔭 Phase 2 Preview

Phase 2 will introduce:

- LangChain abstractions for chains, loaders, and retrievers.
- Document chunking strategies and overlap.
- Hybrid search (dense + sparse).
- Reranking with cross-encoders.
- Agentic retrieval and tool-calling patterns.

---

## 🤝 Contributions

This is a personal learning repository. If you are following the cohort, feel free to open issues or discussions for clarification and add new FAQ entries as new questions come up.

---

*Phase 1 complete — ready for LangChain.*
