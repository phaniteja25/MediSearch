# MediSearch 

> A production-grade RAG system over peer-reviewed mental health 
> literature — enabling clinicians and researchers to query 
> clinical evidence in natural language with full source traceability.

## Status
🚧 In active development — [follow progress on LinkedIn](#)

## Problem
Clinicians and health startup teams spend hours manually searching 
PubMed to answer clinical questions. MediSearch lets them query a 
curated corpus of peer-reviewed mental health research in natural 
language and get cited, evidence-grounded answers — with source 
traceability for every claim.

## Planned Architecture
- **Ingestion:** PubMed API → Chunking → Embedding → Qdrant
- **Retrieval:** Hybrid search (dense + BM25) + Cross-encoder reranking
- **Generation:** Gemini 2.0 Flash with citation-grounded prompting
- **API:** FastAPI with Pydantic v2 request/response schemas
- **Evaluation:** RAGAS (Faithfulness, Answer Relevancy, Context Precision)
- **Deployment:** Render + Qdrant Cloud + GitHub Actions CI

## Tech Stack
| Layer | Technology |
|-------|-----------|
| API | FastAPI + Uvicorn |
| Vector DB | Qdrant |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| LLM | Gemini 2.0 Flash |
| Evaluation | RAGAS |
| Observability | Loguru |
| Containerization | Docker + Docker Compose |

## Project Structure
```
medisearch/
├── docs/               # Architecture, ADRs, eval results
├── src/
│   ├── core/           # Business logic (retriever, generator, rewriter)
│   ├── api/            # FastAPI routes and middleware
│   ├── ingestion/      # PubMed client, chunker, embedder
│   └── evaluation/     # RAGAS eval harness
├── tests/              # Unit and integration tests
├── infrastructure/     # Docker, docker-compose
└── .github/workflows/  # CI pipeline
```

## Local Setup
> Coming soon — full setup instructions once core pipeline is complete.

## Evaluation Results
> Coming soon — RAGAS scores will be documented here after Week 2.

## Author
Built by [Your Name] as part of an AI Engineering portfolio.  
Mentored under a structured SDLC approach mirroring production 
AI engineering workflows.

[LinkedIn](#) · [Portfolio](#)