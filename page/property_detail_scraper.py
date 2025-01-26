# pages/property_detail_scraper.py

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import threading  # To manage thread safety

class PropertyDetailScraper:
    def __init__(self):
        self.headers = {"Accept": "text/html"}
        self.counter = 1
        self.counter_lock = threading.Lock()  # Lock to ensure thread safety

    def get_property_details(self, url):
        response = requests.get(url, headers=self.headers)
        parsed_response = BeautifulSoup(response.text, "html.parser")
        details = {
            'URL': url,
            'APN number': self.get_text_from_html(parsed_response, 'span', 'textbox textbox-apn'),
            'Acreage': self.get_text_from_html(parsed_response, 'span', 'textbox textbox-property_acreage'),
            'Price': self.get_text_from_html(parsed_response, 'span', 'pricebox pricebox-post_promo'),
            'Agency': self.get_text_from_html(parsed_response, 'h2', 'h4 inline-block bold author-name'),
        }
        with self.counter_lock:
            print(f"{self.counter}. Scraping from {url}")
            self.counter += 1
        return details

    @staticmethod
    def get_text_from_html(soup, tag, class_name):
        element = soup.find(tag, class_=class_name)
        return element.text.strip() if element else 'N/A'

    def scrape_multiple_properties(self, urls):
        max_workers = min(len(urls), 1000)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.get_property_details, urls))
        return results
