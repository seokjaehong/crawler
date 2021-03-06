"""
아티스트 검색
http://www.melon.com/search/artist/index.htm?q=%EC%95%84%EC%9D%B4%EC%9C%A0&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=&ipath=srch_form
검색 결과를
def search_artist(q):
    return class Artist의 목록
아티스트 상세 정보
http://www.melon.com/artist/detail.htm?artistId=261143
artist_detail_{artist_id}.html
Artist의 인스턴스 메서드
    def get_detail(self)
        return 없이 자신의 속성 채우기
아티스트의 곡
http://www.melon.com/artist/song.htm?artistId=261143
Artist의 인스턴스 메서드
    def get_songs(self)
        return Song의 list
"""
import os
import re

import requests
from bs4 import BeautifulSoup, NavigableString

# utils가 있는
PATH_MODULE = os.path.abspath(__file__)

# 프로젝트 컨테이너 폴더 경로
ROOT_DIR = os.path.dirname(os.path.dirname(PATH_MODULE))

# data/ 폴더 경로
DATA_DIR = os.path.join(ROOT_DIR, 'data')

print(PATH_MODULE)
print(ROOT_DIR)
print(DATA_DIR)


class MelonCrawler:

    def search_artist(self, q):
        """
        http://www.melon.com/search/artist/index.htm?q=%EC%95%84%EC%9D%B4%EC%9C%A0&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=&ipath=srch_form
        예시)아이유
        :param q: 검색할 가수명
        :return: 결과 dict 가수리스트
        """
        url = 'https://www.melon.com/search/artist/index.htm?'
        #항상 url에 https 로 입려되었는지 확인
        params = {
            'q': q,
            'section' : '',
            'searchGnbYn' : 'Y',
            'kkoSpl' : 'N',
            'kkoDpType':'',
            'ipath':'srch_form',
        }
        #파라미터가 6개로 section, kkoDpTYpe은 입력 받는 변수가 빈칸
        response = requests.get(url, params)
        # melon artist 사이트에 6개의 파라미터를 전달해서 site html 전닮받고
        soup = BeautifulSoup(response.text, 'lxml')
        #beutifulsoup을 통해 soup으로 퍼다담음
        tr_list = soup.select('div#pageList div > ul > li')

        #가수의 일반정보 :이름, 국적, 성별, 솔로/그룹 여부 , 장르 ,유명곡 정보를 한번에 받아오기 위해 li 까지만 내려받음
        result = []
        #결과를 result에 내려받는 for 문
        for tr in tr_list:
            #< a href = "javascript:searchLog('web_artist','ARTIST','AR','아이유','261143');melon.link.goArtistDetail('261143');"title = "아이유 - 페이지 이동"class ="ellipsis" > < b > 아이유 < / b > < / a >

            artist_info = tr.find('div',class_= 'wrap_atist12').find('div', class_='atist_info')
            source = tr.find('div',class_='wrap_atist12').find('a', class_='thumb')

            #print(source)
            #print(type(source))
            #source = artist_info.select_one('a:nth-of-type(1) href').get('value')

            #r1 = re.compile(r'.*?\;.*?\'(\d.*)\'', re.DOTALL)

            artist_id = re.search(r"searchLog\(.*'(\d+)'\)",source.get('href')).group(1)
            artistname = artist_info.find('a', class_='ellipsis').text
            artistname_gubun= artist_info.find('dd', class_='gubun').get_text(strip=True)
            artist_genre = artist_info.find('dd', class_='gnr').find('div',class_='fc_strong').get_text(strip=True)

            artist= Artist(artist_id=artist_id, name=artistname, gubun=artistname_gubun, genre=artist_genre)
            result.append(artist)

        return result

    def search_song(self, q):
        """
        곡 명으로 멜론에서 검색한 결과 리스트를 리턴
        :param q: 검색할 곡 명
        :return: 결과 dict리스트
        """
        """
        1. http://www.melon.com/search/song/index.htm
            에 q={q}, section=song으로 parameter를 준 URL에
            requests를 사용해 요청
        2. response.text를 사용해 BeautifulSoup인스턴스 soup생성
        3. soup에서 적절히 결과를 가공
        4. 결과 1개당 Song인스턴스 한개씩
        5. 전부 리스트에 넣어 반환
        6. 완☆성
        """
        url = 'https://www.melon.com/search/song/index.htm'
        params = {
            'q': q,
            'section': 'song',
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        tr_list = soup.select('form#frm_defaultList table > tbody > tr ')
        # tr_list = soup.find('form', id='frm_defaultList').find('table').fi ㅜㅜnd('tbody').find_all('tr')

        result = []
        for tr in tr_list:
            # <a href="javascript:searchLog('web_song','SONG','SO','빨간맛','30512671');melon.play.playSong('26020103',30512671);" class="fc_gray" title="빨간 맛 (Red Flavor)">빨간 맛 (Red Flavor)</a>
            # song_id = re.search(r"searchLog\(.*'(\d+)'\)", tr.select_one('td:nth-of-type(3) a.fc_gray').get('href')).group(1)
            song_id = tr.select_one('td:nth-of-type(1) input[type=checkbox]').get('value')
            title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
            artist = tr.select_one('td:nth-of-type(4) span.checkEllipsisSongdefaultList').get_text(
                strip=True)
            album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

            song = Song(song_id=song_id, title=title, artist=artist, album=album)
            result.append(song)
        return result

class Artist:
    def __init__(self,artist_id,name,gubun,genre):
        self.artist_id = artist_id
        self.name = name
        self.gubun = gubun
        self.genre = genre
        ## detail 추가할것
        self._debutdate = None
        self._birthdate = None
        self._acttype = None
        self._company = None
        self._gettitle = None

        self._info = {}
        self._award_history = []
        self._introduction = {}
        self._activity_information = {}
        self._personal_information = {}

    def __str__(self):
        return f'{self.name} (구분:{self.gubun}, 장르:{self.genre})'

    def get_detail(self,refresh_html=False):
        """
                자신의 데뷔일 , 생일 , 활동유형, 소속사 수상이력 채운다
                :return: 없음
        """
        # 파일위치는 data/artist_detail_{artist_id}.html
        file_path = os.path.join(DATA_DIR, f'artist_detail_{self.artist_id}.html')
        try:
            file_mode = 'wt' if refresh_html else 'xt'
            with open(file_path, file_mode) as f:
                # url과 parameter구분해서 requests사용
                url = f'https://www.melon.com/artist/detail.htm'
                params = {
                    'artistId': self.artist_id,
                }
                response = requests.get(url, params)
                source = response.text
                # 만약 받은 파일의 길이가 지나치게 짧을 경우 예외를 일으키고
                # 예외 블럭에서 기록한 파일을 삭제하도록 함
                file_length = f.write(source)
                if file_length < 10:
                    raise ValueError('파일이 너무 짧습니다')
        except FileExistsError:
            print(f'"{file_path}" file is already exists!')
        except ValueError:
            # 파일이 너무 짧은 경우
            os.remove(file_path)
            return

        source = open(file_path, 'rt').read()
        soup = BeautifulSoup(source, 'lxml')
        # div.song_name의 자식 strong요소의 바로 다음 형제요소의 값을 양쪽 여백을 모두 잘라낸다
        # 아래의 HTML과 같은 구조
        # <div class="song_name">
        #   <strong>곡명</strong>
        #
        #              Heart Shaker
        # </div>

        #기본정보

        div_entry = soup.find('div', class_ ='wrap_atist_info')
        artistname = soup.find('p', class_='title_atist').strong.next_sibling.strip()
        dl = div_entry.find('dl', class_='atist_info clfix')
        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it,it))

        debutdate = dl.find('dd').find('span', class_='gubun').text

        birthdate=description_dict.get('생일')
        acttype=description_dict.get('활동유형')
        company=description_dict.get('소속사')
        gettitle=description_dict.get('수상이력')

        div_detail_entry = soup.find('div', id='conts')


        #수상이력
        award_history_meta=div_detail_entry.find('div', class_='section_atistinfo01')
        dl2 = award_history_meta.find('dl', class_='list_define').text
        award_history= dl2.splitlines()

        #가수소개
        introduction_meta = div_detail_entry.find('div', class_='section_atistinfo02')
        introduction = introduction_meta.find('div', class_='atist_insdc').get_text(strip=True)

        #활동정보
        activity_information_meta = div_detail_entry.find('div', class_='section_atistinfo03')
        dl3= activity_information_meta.find('dl', class_='list_define clfix')
        items = [item.get_text(strip=True) for item in dl3.contents if not isinstance(item, str)]
        it = iter(items)
        activity_information = dict(zip(it, it))

        #개인정보
        personal_information_meta = div_detail_entry.find('div', class_='section_atistinfo04')
        dl4 = personal_information_meta.find('dl', class_='list_define clfix')
        items = [item.get_text(strip=True) for item in dl4.contents if not isinstance(item, str)]
        it = iter(items)
        personal_information = dict(zip(it, it))

        # 리턴하지말고 데이터들을 자신의 속성으로 할당
        self.name = artistname
        #self.gubun = gubun
        #self.genre = genre
        self._debutdate = debutdate
        self._birthdate = birthdate
        self._acttype = acttype
        self._company = company
        self._gettitle = gettitle
        self._award_history = award_history
        self._introduction = introduction
        self._activity_information = activity_information
        self._personal_information = personal_information


    @property
    def award_history(self):
        # 만약 가지고 있는 생일정보 없다면
        if not self._award_history:
            # 받아와서 할당
            self.get_detail()
        # 그리고 birthdate
        return self._award_history
    @property
    def introduction(self):
        if not self._introduction:
            self.get_detail()
        return self._introduction

    @property
    def activity_information(self):
        if not self._activity_information:
            self.get_detail()
        return self._activity_information

    @property
    def personal_information(self):
        if not self._personal_information:
            self.get_detail()
        return self._personal_information

    @property
    def birthdate(self):
        # 만약 가지고 있는 생일정보 없다면
        if not self._birthdate:
            # 받아와서 할당
            self.get_detail()
        # 그리고 birthdate
        return self._birthdate
    @property
    def debutdate(self):
        if not self._debutdate:
            self.get_detail()
        return self._debutdate

    @property
    def acttype(self):
        if not self._acttype:
            self.get_detail()
        return self._acttype

    @property
    def company(self):
        if not self._company:
            self.get_detail()
        return self._company

    @property
    def gettitle(self):
        if not self._gettitle:
            self.get_detail()
        return self._gettitle

    def get_song(self,refresh_html='False'):
        """
                        자신의 노래리스트를 채움 (노래제목, 가수, 앨범, 장르)          :return: 없음
                """
        # 파일위치는 data/artist_detail_{artist_id}.html
        file_path = os.path.join(DATA_DIR, f'artist_song_detail_{self.artist_id}.html')
        try:
            file_mode = 'wt' if refresh_html else 'xt'
            with open(file_path, file_mode) as f:
                # url과 parameter구분해서 requests사용
                url = f'https://www.melon.com/artist/song.htm'
                params = {
                    'artistId': self.artist_id,
                }
                response = requests.get(url, params)
                source = response.text
                # 만약 받은 파일의 길이가 지나치게 짧을 경우 예외를 일으키고
                # 예외 블럭에서 기록한 파일을 삭제하도록 함
                file_length = f.write(source)
                if file_length < 10:
                    raise ValueError('파일이 너무 짧습니다')
        except FileExistsError:
            print(f'"{file_path}" file is already exists!')
        except ValueError:
            # 파일이 너무 짧은 경우
            os.remove(file_path)
            return

        source = open(file_path, 'rt').read()
        soup = BeautifulSoup(source, 'lxml')

        tr_list = soup.select('form#frm table > tbody > tr ')
        # tr_list = soup.find('form', id='frm_defaultList').find('table').fi ㅜㅜnd('tbody').find_all('tr')

        result = []
        for tr in tr_list:
            # <a href="javascript:searchLog('web_song','SONG','SO','빨간맛','30512671');melon.play.playSong('26020103',30512671);" class="fc_gray" title="빨간 맛 (Red Flavor)">빨간 맛 (Red Flavor)</a>
            # song_id = re.search(r"searchLog\(.*'(\d+)'\)", tr.select_one('td:nth-of-type(3) a.fc_gray').get('href')).group(1)
            song_id = tr.select_one('td:nth-of-type(1) input[type=checkbox]').get('value')
            title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
            artist = tr.select_one('td:nth-of-type(4) span.checkEllipsis').get_text(
                strip=True)
            album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

            song = Song(song_id=song_id, title=title, artist=artist, album=album)
            result.append(song)

        return result



        # # 아티스트의 곡
        # # http://www.melon.com/artist/song.htm?artistId=261143
        # # Artist의 인스턴스 메서드
        #     def get_songs(self)
        #         return Song의 list'''


class Song:
    def __init__(self, song_id, title, artist, album):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album

        self._release_date = None
        self._lyrics = None
        self._genre = None
        self._producers = None

    def __str__(self):
        return f'{self.title} (아티스트: {self.artist}, 앨범: {self.album})'

    def get_detail(self, refresh_html=False):
        """
        자신의 _release_date, _lyrics, _genre, _producers를 채운다
        :return:
        """
        # 파일위치는 data/song_detail_{song_id}.html
        file_path = os.path.join(DATA_DIR, f'song_detail_{self.song_id}.html')
        try:
            file_mode = 'wt' if refresh_html else 'xt'
            with open(file_path, file_mode) as f:
                # url과 parameter구분해서 requests사용
                url = f'https://www.melon.com/song/detail.htm'
                params = {
                    'songId': self.song_id,
                }
                response = requests.get(url, params)
                source = response.text
                # 만약 받은 파일의 길이가 지나치게 짧을 경우 예외를 일으키고
                # 예외 블럭에서 기록한 파일을 삭제하도록 함
                file_length = f.write(source)
                if file_length < 10:
                    raise ValueError('파일이 너무 짧습니다')
        except FileExistsError:
            print(f'"{file_path}" file is already exists!')
        except ValueError:
            # 파일이 너무 짧은 경우
            os.remove(file_path)
            return

        source = open(file_path, 'rt').read()
        soup = BeautifulSoup(source, 'lxml')
        # div.song_name의 자식 strong요소의 바로 다음 형제요소의 값을 양쪽 여백을 모두 잘라낸다
        # 아래의 HTML과 같은 구조
        # <div class="song_name">
        #   <strong>곡명</strong>
        #
        #              Heart Shaker
        # </div>
        div_entry = soup.find('div', class_='entry')
        title = div_entry.find('div', class_='song_name').strong.next_sibling.strip()
        artist = div_entry.find('div', class_='artist').get_text(strip=True)
        # 앨범, 발매일, 장르...에 대한 Description list
        dl = div_entry.find('div', class_='meta').find('dl')
        # isinstance(인스턴스, 클래스(타입))
        # items = ['앨범', '앨범명', '발매일', '발매일값', '장르', '장르값']
        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        album = description_dict.get('앨범')
        release_date = description_dict.get('발매일')
        genre = description_dict.get('장르')

        div_lyrics = soup.find('div', id='d_video_summary')

        lyrics_list = []
        for item in div_lyrics:
            if item.name == 'br':
                lyrics_list.append('\n')
            elif type(item) is NavigableString:
                lyrics_list.append(item.strip())
        lyrics = ''.join(lyrics_list)

        # 리턴하지말고 데이터들을 자신의 속성으로 할당
        self.title = title
        self.artist = artist
        self.album = album
        self._release_date = release_date
        self._genre = genre
        self._lyrics = lyrics
        self._producers = {}

    @property
    def lyrics(self):
        # 만약 가지고 있는 가사정보가 없다면
        if not self._lyrics:
            # 받아와서 할당
            self.get_detail()
        # 그리고 가사정보 출력
        return self._lyrics

    @property
    def genre(self):
        # 만약 가지고 있는 가사정보가 없다면
        if not self._genre:
            # 받아와서 할당
            self.get_detail()
        # 그리고 가사정보 출력
        return self._genre

    @property
    def release_date(self):
        # 만약 가지고 있는 가사정보가 없다면
        if not self._release_date:
            # 받아와서 할당
            self.get_detail()
        # 그리고 가사정보 출력
        return self._release_date