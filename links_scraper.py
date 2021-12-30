import pickle
import logging
from logging.handlers import SMTPHandler
from config import config
from samssimplescraper import Scraper

logger = logging.getLogger()

log_format = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

local_handler = logging.FileHandler(
                filename='./logs/links_scraper.log',
                mode='w'
)
local_handler.setFormatter(log_format)
local_handler.setLevel(logging.INFO)
logger.addHandler(local_handler)

email_handler = SMTPHandler(mailhost=config['mailhost'],
                fromaddr=config['fromaddr'],
                toaddrs=config['toaddrs'],
                subject='Instance 1 scraper done.',
                credentials=config['credentials'],
                secure=())
email_handler.setFormatter(log_format)
email_handler.setLevel(logging.INFO)
logger.addHandler(email_handler)


ROOT_URL = "https://www.winemag.com/buying-guide/"

with open('./data/pickled_lists/total_links_list.pkl', 'rb') as fpick:
        links = pickle.load(fpick)

scraper = Scraper(link_list=links[0:5], root_url=ROOT_URL, folders=True)

scraper.get_html()
logger.warning('Scraper on instance 1 is finished!')
