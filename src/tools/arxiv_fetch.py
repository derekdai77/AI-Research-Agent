import arxiv

def fetch_papers(topic, api_url):
    '''
    Fetch a small set of ArXiv papers relevant to the topic.
    '''
    search = arxiv.Search(
        query=topic,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )
    papers = []
    for result in search.results():
        papers.append({
            'title': result.title,
            'summary': result.summary[:300] + '...',
            'url': result.entry_id
        })
    return papers
