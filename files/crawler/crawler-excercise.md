## Python Clawler

1. Webtoon Class, Episode Class 구현

```python
import requests
import os
import re
from bs4 import BeautifulSoup
from urllib import parse

class Webtoon:
    '''
    webtoon_id
    no:
    url_thumbnail
    title
    rating
    created_date
    url을 받아 파싱해주는 클래스
    '''
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.no = []
        self.url_thumbnail = []
        self.title = []
        self.rating = []
        self.created_date = []

    def update(self):

        payload = {
            'titleId': self.webtoon_id
        }

        webtoon_url = 'https://comic.naver.com/webtoon/list.nhn'
        url_result = requests.get(webtoon_url, payload)

        soup = BeautifulSoup(url_result.text, 'lxml')

        table = soup.select_one('table.viewList')

        tr_list = soup.select('tr')

        for index, tr in enumerate(tr_list[1:]):
            if tr.get('class'):
                continue

            url_thumbnail = tr.select_one('td:nth-of-type(1) img').get('src')
            title = tr.select_one('td:nth-of-type(2) > a').get_text(strip=True)
            rating = tr.select_one('td:nth-of-type(3) strong').get_text(strip=True)
            created_date = tr.select_one('td:nth-of-type(4)').get_text(strip=True)
            href = tr.select_one('td:nth-of-type(2) > a').get('href')
            no = dict(parse.parse_qsl(parse.urlsplit(href).query))

            self.url_thumbnail.append(url_thumbnail)
            self.title.append(title)
            self.rating.append(rating)
            self.created_date.append(created_date)
            self.no.append(no.get('no'))


    @property
    def return_url(self):
        return self.url

death = Webtoon('703845')
death.update()
print(death.title)

```
