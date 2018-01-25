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
