# Support Ticket Similarity Assistant

A Python-based utility designed for Solari Analytics support agents to automatically match incoming tickets with historical resolutions, reducing resolution times and improving response consistency.

---

## Project Overview

This tool processes incoming customer support tickets and computes similarity scores against a historical database of resolved tickets.

### Features
* **Automated Keyword Overlap Matching:** Uses token normalization and Jaccard-style overlap scoring to surface top historical resolutions.
* **Escalation Threshold Handling:** Gracefully detects novel issues (e.g., new infrastructure or Snowflake integration failures) that lack sufficient historical precedents, flagging them for Tier-2 engineering escalation.
* **Zero External Dependencies:** Built purely using standard Python libraries for instant local sandbox execution.

---

## Repository Structure

```text
.
├── main.py                 # Primary execution script for processing incoming tickets
├── ticket_utils.py         # Data loading, tokenization, and scoring utilities
├── SOLUTION_DESIGN.md      # Detailed architectural trade-offs & technical decisions
├── case-study-brief.md     # Customer problem statement and requirements
└── starter_kit/            # Raw historical and sample dataset files
    └── data/
        ├── tickets.json               # 40 synthetic historical support tickets
        └── new_tickets_example.json   # 4 incoming test tickets


**Quick Start Guide**
1. **Prerequisites**
 -> Python 3.8 or higher. No external pip packages required.

2. **Execution**
 -> Run the main script from the root directory:
    python main.py

3. **Expected Output**
 -> The assistant evaluates the 4 test cases in new_tickets_example.json:

    **NT-1, NT-2, NT-3:** Matches with high confidence past resolutions (Password reset, blank chart, duplicate billing).

    **NT-4:** Detects a low similarity score (< 0.22) for a new Snowflake integration issue and prompts the agent to escalate to Tier 2.

4. **Limitations & Future Improvements**
  -> **Synonym Support:** Pure keyword matching does not recognize synonyms (e.g., "log in" vs. "sign in").
    Future iterations can incorporate vector embeddings (sentence-transformers).

  -> **Data Store:** Currently operates on local JSON files. Future enhancements could connect to a vector database (e.g., Pinecone/Qdrant)
    or REST API (Zendesk / Jira Service Management).













