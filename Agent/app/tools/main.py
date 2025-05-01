import requests
from fastapi import FastAPI, Request
from tools.call_arxiv import search_papers
import tools.call_pdf_extract as pdf_extract
from tools.call_summarizer import summarize_paper
from tools.call_flashcards import generate_flashcards

app = FastAPI()

@app.post("/agent")
async def agent(request: Request):
    # Get the request body
    body = await request.json()
    query = body['query']
    print(f"Query: {query}")

    # Search for the query
    papers = search_papers(query)

    # Retrieve Query Results and summarise them
    k=5
    summaries = []
    for paper in papers:
        pdf_text= pdf_extract.extract_pdf_text(paper['link'], paper['title'])
        # Summarize the paper
        summary = summarize_paper(paper,pdf_text)
        summaries.append(summary)
    print(f"Summaries: {summaries}")

    # Generate Flashcards
    all_text = "\n".join(summaries)
    flashcards = generate_flashcards(all_text)

    # Return the flashcards
    return {"flashcards": flashcards}