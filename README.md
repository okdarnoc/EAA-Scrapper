# EAAScraper

This is a demo of obtaining data from submitting forms using brute-force. Please note that this project is purely for academic purpose, any data obtained form the sample website belongs to its owner. DO NOT NUKE ANY WEBSITE.

## Quickstart
```bash
cd EAAScraper
pip install -r requirements.txt
scrapy crawl eaa
```

## Explanation
### Key technqiues
1. Submitting multipart/form-data
2. Noticing that the site uses pre-negotiated values for form requests
3. Use generators instead of pre-computed list to obtain all possible input
