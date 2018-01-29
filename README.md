# EAAScraper

This is a demo of obtaining data from submitting forms using brute-force. Please note that this project is purely for academic purpose, any data obtained form the sample website belongs to its owner. DO NOT NUKE THE WEBSITE.

This scraper scrapes from [Estate Agents Authority](http://www.eaa.org.hk/en-us/licence-search) to look for real estate agents in Hong Kong.

![licence-search-empty](Images/empty-form.png)

After inputting a valid licence number, you get the result.

![licence-search-result](Images/result.png)

The spider loops through all possible licence number and submit form requests. For the sake of demonstration purpose, we only loop on one alphabet by default.

## Quickstart
```bash
cd EAAScraper
pip install -r requirements.txt
scrapy crawl eaa
```

## Explanation
### Key techniques
1. Submit multipart/form-data
2. Notice that the site uses pre-negotiated values for form requests
3. Use generators instead of pre-computed list to obtain all possible input
4. Insert valid records into MongoDB using pipelines