import logging
import pickle
from samssimplescraper import LinksRetriever

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./logs/sitemap_scraper.log', filemode='w'
)

# instantiate LinksRetriever with the winemag sitemap
links_retriever = LinksRetriever(url='https://www.winemag.com/sitemap_index.xml', folders=True)

# get a list of the link using .get_sitemap_links method, filter for only wine review sitemaps
sitemap_links = links_retriever.get_sitemap_links(tag='loc', link_filter='wine_review-sitemap')
assert all(isinstance(s, str) for s in sitemap_links)
logging.info('the sitemap link list is %s links long', len(sitemap_links))

# scrape all the wine review links
total_links = links_retriever.get_next_links(links=sitemap_links, tag='loc')
assert all(isinstance(s, str) for s in total_links)
logging.info('The final web links list is %s links long', len(total_links))

# save list for use on multiple servers
with open('./data/pickled_lists/total_links_list.pkl', 'wb') as fp:
        pickle.dump(total_links, fp)
