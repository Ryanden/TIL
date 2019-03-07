from utils import Webtoon, Episode
import os
import requests
from bs4 import BeautifulSoup
import re


# WebtoonCrawler의 클래스메서드를 사용하여 모든 웹툰의 데이터를 Webtoon_list에 인스턴스로 저장
class WebtoonCrawler:
    # 검색의 대상이 될 리스트
    webtoon_list = []

    # 검색결과 리스트
    request_list = []

    # 유저가 선택한 번호를 저장할 변수
    user_request = 0

    # 웹툰의 아이디와 제목 속성을 가진 인스턴스를 생성
    def __init__(self, webtoon_id, webtoon_title):
        self.webtoon_id = webtoon_id
        self.webtoon_title = webtoon_title
        self.episode_list = []

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
    def search(cls):

        # search 메서드 호출시 검색기록이 있으면 검색결과 초기화
        if cls.request_list:
            cls.request_list = []

        print('Ctrl+C로 종료합니다.')
        keyword = input(f'검색할 웹툰명을 입력해주세요:')

        # 검색결과와 매치되는 인스턴스를 request리스트에 append 한다.
        for item in cls.webtoon_list:
            if keyword in item.webtoon_title:
                cls.request_list.append(item)

        # 검색결과의 매치되는 인스턴스가 있다면 인스턴스 목록을 출력한다.
        if cls.request_list:
            print(f'요청하신 "{keyword}"와 일치하는 검색결과:')
            # 리퀘스트 목록을 출력하는 메서드 호출
            cls.show_request_list()
        else:
            print(f'"{keyword}"와 매칭되는 만화는 없습니다.')

    # keyword에서 입력받은 정보를 기준으로 검색결과를 프린트 해준다.
    @classmethod
    def show_request_list(cls):

        # 키워드와 매칭되는 인스턴스의 몰록을 프린트
        for i, result in enumerate(cls.request_list):
            print(f'{i + 1}. {result.webtoon_title}')

    # 선택된 웹툰으로 정보를 보거나 웹툰의 이미지를 저장하거나 되돌아갈수 있다.
    @classmethod
    def choice(cls):

        print('현재 검색결과를 출력합니다.')
        cls.show_request_list()

        print(f'상위 목록에서 열람을 희망하는 웹툰 번호를 선택 해 주세요.')
        user_request = input(f'선택 :')

        # 유저의 입력을 받아 요청과 매치되는 인스턴스를 리스트에서 추출
        for i, webtoon in enumerate(cls.request_list):
            if user_request != str(i + 1):
                continue
            else:
                # 목록에서 선택한 번호와 요청한 번호가 같은 인스턴스만 할당
                selected_webtoon = webtoon
                break

        print('1. 웹툰 정보 보기 \n'
              '2. 웹툰 저장하기 \n' 
              '3. 다른 웹툰 검색해서 선택하기 '
        )
        user_request = input(f'선택 :')

        if user_request is '1':
            # 웹툰클래스에 요청한 인스턴스의 id를 매개변수로 전달하여 인스턴스 생성
            webtoon_info = Webtoon(webtoon_id=selected_webtoon.webtoon_id)

            # webtoon_info 인스턴스에 기본 속성을 셋팅
            # webtoon_info.html프로퍼티로 webtoon_info 인스턴스의 html을 자신의 속성으로 사용
            webtoon_info.html

            # webtoon_info의 title프로퍼티로 title, author, description을 셋팅
            webtoon_info.title

            webtoon_info.episode_list

            # webtoon_info 인스턴스의 기본정보를 출력
            webtoon_info.show_info()

            print(f'다른정보를 조회하려면 1번, 종료하려면 2번을 입력해주세요.')
            user_request = input(f'선택 :')

            # 정보를 출력하고 다시 메서드 호출로 돌아감
            if user_request is '1':
                cls.choice()
            else:
                print('이용해주셔서 감사합니다. 크롤러를 종료합니다.')

        elif user_request is '2':
            pass
        elif user_request is '3':
            # search 메서드 호출로 다른 웹툰의 정보를 사용자에게 입력받도록 함
            cls.search()
        else:
            # 1,2,3번 만 입력받도록 함
            print('입력이 올바르지 않습니다. \n'
                  '1,2,3 번의 메뉴에 해당하는 번호를 입력 해 주세요.'
            )
            cls.choice()


WebtoonCrawler.start()
WebtoonCrawler.search()
WebtoonCrawler.choice()
