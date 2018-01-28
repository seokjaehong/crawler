import re
from bs4 import BeautifulSoup
import os
import requests

def get_top100_list(refresh_html=False):
    """
    실시간 차트 1~100위의 리스트 반환
    파일위치:
        현재 파일(모듈)의 위치를 사용한 상위 디렉토리 경로 (crawler디렉토리):
            os.path.dirname(os.path.abspath(__name__))
        1~50위:   data/chart_realtime_50.html
        51~100위: data/chart_realtime_100.html
    :return:
    """
    # utils가 있는
    global source
    path_module = os.path.abspath(__name__)
    print(f'path_module: \n{path_module}')

    # 프로젝트 컨테이너 폴더 경로
    root_dir = os.path.dirname(path_module)
    print(f'root_dir: \n{root_dir}')

    # data/ 폴더 경로
    path_data_dir = os.path.join(root_dir, 'data')
    print(f'path_data_dir: \n{path_data_dir}')

    # 만약에 path_data_dir에 해당하는 폴더가 없을 경우 생성해준다
    os.makedirs(path_data_dir, exist_ok=True)

    # 실시간 1~100위 웹페이지 주소
    url_chart_realtime = 'https://www.melon.com/chart/index.htm'

    # 실시간 1~100위 웹페이지 HTML을 data/chart_realtime.html 에 저장
    file_path = os.path.join(path_data_dir, 'chart_realtime.html')
    try:
        # refresh_html매개변수가 True일 경우, wt모드로 파일을 열어 새로 파일을 다운받도록 함
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode) as f:
            response = requests.get(url_chart_realtime)
            source = response.text
            f.write(source)
    # xt모드에서 있는 파일을 열려고 한 경우 발생하는 예외
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')

    file_path = os.path.join(path_data_dir, 'abc.txt')
    print(f'file_path: \n{file_path}')


    soup = BeautifulSoup(source, 'lxml')
    #soup = BeautifulSoup(source,'xml')
    #soup =BeautifulSoup(source, 'html.parser')
    #soup = BeautifulSoup(source,'lxml-xml')



    result = []
    for tr in soup.find_all('tr', class_=['lst50','lst100']):
        rank = tr.find('span', class_='rank').text
        title = tr.find('div', class_='rank01').find('a').text
        artist = tr.find('div', class_='rank02').find('a').text
        album = tr.find('div', class_='rank03').find('a').text
        url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
        # http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/120/quality/80/optimize
        # .* -> 임의 문자의 최대 반복
        # \. -> '.' 문자
        # .*?/ -> '/'이 나오기 전까지의 최소 반복

        p = re.compile(r'(.*\..*?)/')
        url_img_cover = re.search(p, url_img_cover).group(1)

        result.append({
            'rank': rank,
            'title': title,
            'url_img_cover': url_img_cover,
            'artist': artist,
            'album': album,
        })
    return result



#    for i in result :
#        print(i)



def get_song_detail(refresh_html=False):

    global source_song_detail
    path_module = os.path.abspath(__file__)
    root_dir = os.path.dirname(path_module)
    path_data_dir = os.path.join(root_dir, 'data')
    os.makedirs(path_data_dir, exist_ok=True)

    url_song_detail = 'https://www.melon.com/song/detail.htm?songId=30512671'
    file_path = os.path.join(path_data_dir, 'song_detail.html')

    try:
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode) as f:
            response = requests.get(url_song_detail)
            source_song_detail = response.text
            f.write(source_song_detail)
        # xt모드에서 있는 파일을 열려고 한 경우 발생하는 예외
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')

    #file_path = os.path.join(path_data_dir, 'abc.txt')
    #print(f'file_path: \n{file_path}')
    # print(source_song_detail)

    soup_song_detail = BeautifulSoup(source_song_detail, 'lxml')
    result = []
    for div in soup_song_detail.find_all('div', class_=['section_info']):

        songname_pattern = div.find('div', class_='song_name').text
        r1 = re.compile(r'.*?\w.*\t(\w.*?)\r',re.DOTALL)
        songname= re.search(r1,songname_pattern).group(1)

        artist = div.find('div', class_='artist').find('a').text
        album =div.find('div', class_='meta').find('dd').find('a').text
        song_info_detail_meta= div.find('div', class_='meta').find('dl').text

        r2 = re.compile(r'.*?\n(.*?)',re.DOTALL)
        song_date = r2.search(r2, song_info_detail_meta).group(1)
        #genre = r2.search(r2, song_info_detail_meta).group(2)
        #flac = r2.search(r2, song_info_detail_meta).group(3)



        #r2 = re.complie(r'',re.DOTALL)
        result.append({
            'songname': songname,
            'artist': artist,
            'album': album,
            'songdate': song_date,
         #   'genre': genre,
         #   'flac' : flac,

        })
    for div in soup_song_detail.find_all('div', class_='section_lyric'):
        lyrics = div.find('div', class_='lyric').text
        #pwkrrhdrk = div.find('div', class_='ellipsis').find('a', class_='artist_name').text
        result.append({
            'lyrics': lyrics,
         #   '작곡' : pwkrrhdrk,
        })

    return result
