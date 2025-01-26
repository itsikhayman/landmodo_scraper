# page/property_link_scraper.py

import requests
from bs4 import BeautifulSoup

class PropertyLinkScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"Accept": "text/html"}
        self.property_links = []

    def scrape_links(self):
        page = 1
        while True:
            url = self.base_url.format(page=page)
            response = requests.get(url, headers=self.headers)
            parsed_response = BeautifulSoup(response.text, "html.parser")

            # Check for no search results
            no_results = parsed_response.find("div", class_="no_search_results_posts")
            if no_results:
                break

            # find total results
            if page == 1:
                result_nu = parsed_response.find('span', class_='total__js').text.strip()
                print(f"Total results: {result_nu}")

            # Find all property links on the page
            results = parsed_response.find_all("a", class_="col-sm-5")
            links = [f"https://www.landmodo.com{a_element.get('href')}" for a_element in results if a_element.get('href')]
            self.property_links.extend(links)

            print(f"Page {page}: Collected {len(links)} links.")

            page += 1

        return self.property_links
