from serpapi import GoogleSearch

def perform_search(query, api_key):
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    search_results = []

    for item in results.get('organic_results', []):
        search_results.append({
            'title': item.get('title'),
            'link': item.get('link'),
            'snippet': item.get('snippet')
        })
    return search_results
