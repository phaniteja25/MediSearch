import requests
import logging
import os

'''
This module contains the PubMedClient class, 
which talks to two API endpoints of the NCBI E-utilities API:

1. ESearch: To search for articles based on a query and retrieve their IDs.
2. EFetch: To fetch detailed information about articles using their IDs in the form of XML.
The XML response from EFetch is then parsed into Paper objects, which are used in the rest of the application.

Note: The client could fail when the network is down, the API is down, or if the API key is invalid or 
the XML is not parsed correctly
'''
class PubMedClient:


    def __init__(self):
        self.session = requests.Session()
        self.BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


    def search_pubmed(self, query: str, max_results: int = 300) -> list[str]:
        '''
        Search PubMed via ESearch and return list of related PMID's
    
    Args:
    query : type string to fetch the specific topic papers
    max_results : type int, maximum number of articles to return
    
    Returns:
    List of PMIDS
    
    Raises
    request.HTTP error if network call fails 
    '''
    
    #1. Build the params dictionary for calling the api with db : pubmed, term : query, retmax : max_results, retmode : json
    #2. Load the api key 
    #3. perform GET call to esearch.fcgi
    #4. extract idlist from response json 
    #5. log the idlist found
    #6. return the id list. 
        params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
        }

        api_key = os.getenv("NCBI_API_KEY")
        
        if api_key:
            params["api_key"] = api_key

        try:
            response = requests.get(f"{self.BASE_URL}esearch.fcgi", params=params)
            response.raise_for_status()
            
            data = response.json()
            id_list = data.get("esearchresult", {}).get("idlist", [])
            
            logging.info(f"Found {len(id_list)} PMIDs for query: {query}")
            
            return id_list
        except requests.RequestException as e:
            logging.error(f"API request failed: {e}")
            raise
    

if __name__ == "__main__":
    # Example usage
    client = PubMedClient()
    query = "machine learning in healthcare"
    pmids = client.search_pubmed(query)
    print(pmids)

