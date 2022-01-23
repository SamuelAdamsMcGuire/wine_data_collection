'''
Used to see how many webpages have been scraped and how many are left
'''
import pickle
from samssimplescraper import Scraper


ROOT_URL = "https://www.winemag.com/buying-guide/"

with open('./data/pickled_lists/total_links_list.pkl', 'rb') as fpick:
    links = pickle.load(fpick)

scraper = Scraper(link_list=links, root_url=ROOT_URL, folders=True)

scraper.check_status()
