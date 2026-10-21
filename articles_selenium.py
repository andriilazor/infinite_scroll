import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "https://infiniteajaxscroll.com/examples/articles/"
OUTPUT = "articles_selenium.json"


def scroll_to_end(driver, pause=1.5, max_idle=3):
    count = len(driver.find_elements(By.CSS_SELECTOR, "div.article"))
    idle = 0
    while idle < max_idle:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        new_count = len(driver.find_elements(By.CSS_SELECTOR, "div.article"))
        if new_count == count:
            idle += 1
        else:
            idle, count = 0, new_count


def extract(driver):
    js_text = "return arguments[0].textContent;"
    items = []
    for article in driver.find_elements(By.CSS_SELECTOR, "div.article"):
        paragraphs = article.find_elements(By.CSS_SELECTOR, "p")
        items.append({
            "title": article.find_element(By.CSS_SELECTOR, "h1").get_attribute("textContent"),
            "text": " ".join(driver.execute_script(js_text, p) for p in paragraphs),
            "images": [img.get_attribute("src") for img in article.find_elements(By.CSS_SELECTOR, "img")],
        })
    return items


def main():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(URL)
        scroll_to_end(driver)
        items = extract(driver)
    finally:
        driver.quit()

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(items)} articles to {OUTPUT}")


if __name__ == "__main__":
    main()
