import requests
import xml.etree.ElementTree as ET

def search_papers(query):
    base_url = "http://export.arxiv.org/api/query?search_query=ti:"
    search_url = f"{base_url}{query}&start=0&max_results=5"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        # Parse XML response
        root = ET.fromstring(response.content)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = []
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text.strip()
            summary = entry.find('atom:summary', ns).text.strip()
            pdf_link = entry.find('atom:link[@type="application/pdf"]', ns)
            link = pdf_link.get('href') if pdf_link is not None else None
            authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
            
            entries.append({
                'title': title,
                'summary': summary,
                'link': link,
                'authors': authors
            })
        
        return entries
    else:
        raise Exception(f"Error fetching papers: {response.status_code} - {response.text}")
