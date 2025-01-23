def retrieve_information(search_results, papers):
    '''
    Combine search results and paper summaries in a rudimentary way.
    In a real RAG system, you'd store vectors in Pinecone, retrieve, etc.
    '''
    text = "=== Combined Search Results ===\n"
    for result in search_results:
        text += f"Title: {result['title']}\nSnippet: {result['snippet']}\nLink: {result['link']}\n\n"

    text += "\n=== Relevant Papers ===\n"
    for paper in papers:
        text += f"Title: {paper['title']}\nSummary: {paper['summary']}\nURL: {paper['url']}\n\n"

    return text
