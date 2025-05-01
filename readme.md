## Research Assistant
This project outlines the flow for a research assist that uses accessess and search arxiv to collect research papers and build flash cards on them.
This Should be achieved utilising agentic flow+multiple docker containers.

## Plan
User → Frontend/CLI
        ↓
     Agent (llm-agent container)
        ↓ (issues Tool Calls)
1. arxiv-search-api → gets paper links
2. pdf-downloader   → downloads & extracts text
3. summarizer       → condenses paper into key ideas
4. flashcard-generator → formats Q/A markdown
        ↓
     Agent aggregates all into output frame
        ↓
     Flashcard.md file is saved or returned to user


## Services
- Agent - Fastapi
- LLM - Ollama
- Search Tool - Arxiv API
- Pdf Downloader - PymuPDF
- Summariser
- Flash Card Generator

## Agent 
Responsible for calling the tools the orchestration of flow

## Search Arxiv
Use Arxiv api to get pdf_links of papers which have title matching to query.

##
