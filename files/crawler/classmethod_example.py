import os
import requests
from bs4 import BeautifulSoup
import re


# 웹툰을 이름으로 검색하여 인스턴스를 리스트로 가지고 사용자가 크롤링할 웹툰을 선택한다.
class Taskmanager:

    # 검색의 대상이 될 리스트
    webtoon_list = []

    # 검색결과 리스트
    request_list = []

    def __init__(self, webtoon_id, webtoon_title):
        self.webtoon_id = webtoon_id
        self.webtoon_title = webtoon_title

    @classmethod
    def start(cls):

        # requeset로 목록을 요청하여 html파일에 담고 저장
        file_path = 'data/webtoon_list.html'

        webtoon_url = 'http://comic.naver.com/webtoon/weekday.nhn'

        # 파일이 없을경우 request.get으로 요청한 text를 파일로 저장
        # 파일이 있을 경우 해당 파일을 열고 내용을 html 변수에 할당
        if not os.path.exists(file_path):

            response = requests.get(webtoon_url)

            html = response.text

            open(file_path, 'wt').write(html)

        else:
            html = open(file_path, 'rt').read()

        soup = BeautifulSoup(html, 'lxml')

        # 웹툰의 전체리스트의 정보를 가져온다.
        webtoon_list = soup.select('div.thumb > a img')

        # 웹툰의 전체리스트에서 title과 id값을 추출하여 인스턴스를 만들고 list에 저장한다.
        for webtoon in webtoon_list:
            item_title = webtoon.get('title')
            item_id = re.findall(r'webtoon/(\d*)', webtoon.get('src'))

            if item_title is not None:
                cls.webtoon_list.append(cls(webtoon_title=item_title, webtoon_id=item_id))

    # webtoon의 검색어를 입력받아 일치하는 검색결과를 request리스트에 추가 한다.
    @classmethod
    def search(cls, keyword):

        # search 메서드 호출시 검색기록이 있으면 검색결과 초기화
        if cls.request_list:
            cls.request_list = []

        # 검색결과와 매치되는 인스턴스를 request리스트에 append 한다.
        for item in cls.webtoon_list:
            if keyword in item.webtoon_title:
                cls.request_list.append(item)

        # 검색결과를 프린트 해준다.
        if cls.request_list:
            print(f'요청하신 "{keyword}"와 일치하는 검색결과:')
            for i, result in enumerate(cls.request_list):
                print(f'{i + 1}. {result.webtoon_title}')
        else:
            print(f'"{keyword}"와 매칭되는 만화는 없습니다.')


Taskmanager.start()
Taskmanager.search('신')
