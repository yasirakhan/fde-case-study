# Support Ticket Similarity Assistant - Solution Design

## Overview & Objective
Solari Analytics' support team handles ~150 tickets daily. Agents often spend too much time resolving recurring issues or give inconsistent answers. This tool matches incoming customer tickets against historical support records to instantly surface similar past tickets and proven resolutions.

## Core Assumptions
- **Volume & Scale:** Initial seed dataset is small (~35 tickets), but the design must scale smoothly as ticket history grows.
- **Latency:** Agents need instant recommendations during active customer chats (sub-second execution).
- **Novel/Unmatched Tickets:** Tickets like new data warehouse integrations (e.g., Snowflake) will not have historical matches. These must be caught by a similarity threshold check and flagged for tier-2 escalation.

## Proposed Architecture & Tech Stack
- **Stack:** Python 3 standard library (`json`, `re`), requiring zero external dependencies or heavy vector databases. This makes it extremely portable for local sandbox execution or quick deployment.
- **Matching Algorithm:** 
  1. Text normalization (lowercase, remove punctuation, token set generation).
  2. Jaccard/keyword-overlap scoring between incoming text and historical tickets.
  3. Ranking results to return the top 3 most relevant past tickets.

## Key Trade-Offs
- **Keyword Overlap vs. Semantic Embeddings:** 
  * Chosen: Naive keyword overlap. It is completely transparent, lightning-fast, and requires no external API keys or complex model infrastructure.
  * Trade-off: It may miss strict synonyms, but it offers high reliability and zero maintenance overhead for an initial v1 release.

## Future Improvements (With More Time)
- Upgrade to semantic vector embeddings (e.g., sentence-transformers) to handle synonyms better.
- Add an LLM summarization step to condense multi-paragraph resolution notes into a single bullet point for agents.
- Wrap the script in a lightweight REST API (Flask/FastAPI) and integrate it directly into the support helpdesk UI.