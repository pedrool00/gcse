# pip install google-api-python-client

#!/usr/bin/env python3
from googleapiclient.discovery import build
import argparse
import itertools

# Add API key and Google Custom Search Engine ID here
my_api_key = "Your_API_Key"
my_cse_id = "Your_CSE_ID" 

def google_search(search_query, api_key, cse_id, num_results, start_page=1, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_query, cx=cse_id, num=num_results, start=start_page, **kwargs).execute()
    if int(res['searchInformation']['totalResults']) > 0:
        return res['items']
    return []

# Use the -s to enter your search query.
# Optionally, use -n to change the number of results.
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--searchQuery", help="Enter the search query")
parser.add_argument("-n", "--numResults", type=int, default=3, help="Enter the number of results to fetch (max 10)")
args = parser.parse_args()

if args.searchQuery is None:
    print("Developed by Pedro, for Guardian.ai")
    parser.print_help()
    exit()

# Perform the search. Cap is set to 10 results.
searchQuery = args.searchQuery
numResults = min(args.numResults, 10) 

allResults = []
allResults.extend(google_search(
    searchQuery, my_api_key, my_cse_id, num_results=min(numResults, 10), start_page=1))

if len(allResults) == 0:
    print("No Results found")
else:
    for result in allResults:
        print(result['link'])
