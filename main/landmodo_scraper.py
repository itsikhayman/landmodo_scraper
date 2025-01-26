# main/landmodo_scraper

import pyinputplus as pyip
from landmodo_API.page.property_link_scraper import PropertyLinkScraper
from landmodo_API.page.property_detail_scraper import PropertyDetailScraper
from landmodo_API.common.transfer_to_excel import TransferToExcel
from landmodo_API.common.play_ringtone import RingtonePlayer

def main():
    print("Welcome to Landmodo Scraper v250120252006b5")
    ringtone_file = "tada.wav"
    # Get the URL template from user input using pyinputplus
    url_template = pyip.inputURL("Enter the search URL (e.g., https://www.landmodo.com/properties...): ") + "&page={page}"

    # Initialize PropertyLinkScraper with the user-provided URL template
    link_scraper = PropertyLinkScraper(base_url=url_template)
    all_property_links = link_scraper.scrape_links()

    # Initialize PropertyDetailScraper and scrape property details in parallel
    detail_scraper = PropertyDetailScraper()
    all_property_details = detail_scraper.scrape_multiple_properties(all_property_links)

    # Initialize the RingtonePlayer and play the sound when finish scraping
    ringtone_player = RingtonePlayer(ringtone_file)
    ringtone_player.play_finish_ringtone()

    # Save all collected property details to an Excel file using the transfer_to_excel module
    transfer_to_excel = TransferToExcel()
    transfer_to_excel.save_to_excel(all_property_details)

if __name__ == "__main__":
    main()
