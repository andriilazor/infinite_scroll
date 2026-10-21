# Infinite Scroll Scraper

Two ways of scraping the articles from the
[Infinite Ajax Scroll example blog](https://infiniteajaxscroll.com/examples/articles/):

- `articles_spider.py` – a Scrapy spider that follows the pagination links (`a.pager__next`).
- `articles_selenium.py` – a headless Chrome script that scrolls the page until no new articles load.

Both extract the `title`, `text` and `images` of every article.

## Requirements

- Python 3
- Google Chrome (for the Selenium script)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Scrapy spider:

```bash
scrapy runspider articles_spider.py -O articles_spider.json
```

Selenium script (writes `articles_selenium.json`):

```bash
python articles_selenium.py
```

## Output

Each item is a JSON object:

```json
{
  "title": "...",
  "text": "...",
  "images": ["https://..."]
}
```
