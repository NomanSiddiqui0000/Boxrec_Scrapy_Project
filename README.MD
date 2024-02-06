
## Boxrec_profile_ scraper_using_scrapy
The websites contain data about boxers' profiles, their scheduled matches, and more. However, scraping data directly using the Scrapy framework is challenging because these websites aggressively use anti-bot measures. They can detect proxies and scrutinize the behavior of user agents, as well as the way requests are sent, including the duration of requests. Therefore, we need to use other third-party services like proxy rotation and user agents. For this project, I recommend obtaining credentials from ScrapeOps. They will provide you with 1000 free proxies and user agents. If you want access to more features, you can opt for the premium package.
This scraper is expected to gather approximately 24,000 or more records.
Gathering maximum data will take some time due to the implementation of the time library, which pauses the scraper for random durations after each request to mimic human behavior.

## Installation
Python
```bash
  pip install Python
```
Scrapy framework
```bash
  pip install scrapy
```

## Deployment
Clone the project.
```bash
  git clone https://github.com/NomanSiddiqui0000/Boxrec_Scrapy_Project.git
```
This project requires an API key to utilize cloud-based functionalities such as proxy rotation and user agents. You'll jusut need to add your API key to the given location into the `setting.py` file.
```bash
SCRAPEOPS_API_KEY = 'Your_API_KEY_HERE'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    'pbo.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
}

```



Ensure that you must be in project directory.
```bash
  cd <project directory>
```
For crawling the spider use this command.The second one will save your scraped data into the given file format seperately.
```bash
  scrapy crawl pw
  OR
  scrapy crawl -O pw <file name with extension .csv or .json>
```


## Items
This scraper will scrape **26** items or features which is given below.

Name, picture_link, Wikipedia_Link, division, rating, bouts, rounds, KOs, Career, Debut, vada, titles, ID, Birth Name, sex, Alias, Age, Nationality, Stance, Height, Reach, Residence, Birth Place, Win, Lose, Draw
