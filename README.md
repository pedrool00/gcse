# GCSE
A simple Google Custom Search Engine meant for using Google Dorks and return the best results. 

The tool has been coded to return a max of 10 URLs from Google Search. Number can be modified up to 100 (max imposed by Google). 
Also, note that the limit of free daily searches is 100.  

This versatile tool developed with the goal of helping in OSINT investigations.

## Install

```bash
git clone https://github.com/pedrool00/gcse.git
cd gcse
pip install -r requirements.txt

cd gcse
python3 gcse.py
```

## Usage

```bash
python3 gcse.py -s "food" -n 3
```

```bash
python3 gcse.py -s "site:google.com filetype:pdf"
```

### Options

```
usage: gcse.py [-h] [-s SEARCHQUERY] [-n NUMRESULTS]

options:
  -h, --help            show this help message and exit
  -s SEARCHQUERY, --searchQuery SEARCHQUERY
                        Enter a search query
  -n NUMRESULTS, --numResults NUMRESULTS
                        Enter the number of results to fetch (max 10)
```

---

## Setup

You need:

* GOOGLE API Key
* GOOGLE CUSTOM SEARCH ENGINE ID

### Google API Key

Start going to [Google Cloud](https://console.cloud.google.com/)
To create your application's API key:

Create a new key:

1. Open the Google Cloud API Console.
2. Create or select a project.
3. On the Credentials page, get an existing API key or create a new one (Create credentials > API key). You can restrict the key by clicking Restrict key.

### Google Custom Search Engine ID

1. Go [here](https://programmablesearchengine.google.com/controlpanel/all)
2. Add a new search engine and click save after
3. Get your search engine ID  

Lastly, in the gcse.py file, replace the variables with your key and cse id. 

```python
my_api_key = "Your GOOGLE API KEY"
my_cse_id = "YOU Custom Search Engine ID"
```

You should now be ready to start searching! 


