
import requests
from bs4 import BeautifulSoup
import sqlite3
import re
from item.models import *
from datetime import datetime

class CrawlBaykoreans():
    def __init__(self):
        self.url_format = 'https://baykoreans.link/index.php'
        #self.link_list = ['drama', 'drama_fin', 'entertain', 'movie']
        self.link_list = ['drama', 'drama_fin']

    def get_last_page(self, link):
        payload = {'mid': link, 'page': 1}
        res = requests.get(self.url_format, params=payload)
        soup = BeautifulSoup(res.content)

        page_regex = re.compile(r'page=(?P<page>\d*)')

        last_page = soup.find('ul',{'class':'pagination'}).findAll('li')[-1]
        last_page_url = last_page.find('a')['href']

        result = page_regex.search(last_page_url)

        if result:
            page_str = result.group()

            last_page = page_str.split('=')[1]
            return last_page
        else:
            raise Exception('Can not find last page in {}'.format(link))


    def get_drama_list(self, link, page):
        payload = {'mid': link, 'page': page}
        res = requests.get(self.url_format, params=payload)
        soup = BeautifulSoup(res.content)

        data_table = soup.find('table', {'class':'boardList'})
        data_list = data_table.find('tbody').findAll('tr')
        for data in data_list:
            try:
                title = data.findAll('td')[1].text.strip()
                title_split = title.split(' ')
                brodcasting_date = title_split[0]

                title_regex = re.compile(r'제\d*회')
                title_episode = ' '.join(title_split[1:])
                episode_idx = title_regex.search(title_episode).start()
                title = title_episode[:episode_idx].strip()
                episode = title_episode[episode_idx:].strip()
                if episode.find('\n') > 0:
                    episode = episode[:episode.find('\n')]

                self.insert_drama_insert(link, title, episode, brodcasting_date)

            except:
                continue


    def insert_drama_insert(self, link, drama, episode, episode_date):

        category = Category.objects.filter(link=link).first()
        d, created = Drama.objects.get_or_create(category=category,name=drama)

        brodcasting_date = datetime.strptime(episode_date,'%m%d%y') 

        epi = DramaEpisode.objects.get_or_create(drama=d, name=episode, brodcasting_date=brodcasting_date) 


    def processing(self):
        for link in self.link_list:

            for page in range(100, 0, -1):
                self.get_drama_list(link, page)
            

def run():
    crawl = CrawlBaykoreans()
    crawl.processing()


if __name__ == '__main__':
    crawl = CrawlBaykoreans()
    crawl.processing()
