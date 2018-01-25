import re

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
    # 프로젝트 컨테이너 폴더 경로
    path_module = os.path.abspath(__name__)
    print(f'path_module: \n{path_module}')
    root_dir = os.path.dirname(path_module)
    print(f'root_dir: \n{root_dir}')

    # data/ 폴더 경로
    path_data_dir = os.path.join(root_dir, 'data')
    print(f'path_data_dir: \n{path_data_dir}')

    print(path_data_dir)

    # if not os.path.exists(path_data_dir) :
    #     os.makedirs(path_data_dir)

    os.makedirs(path_data_dir,exist_ok=True)

    # 1~50, 50~100위 웹페이지 주소
    url_chart_realtime_50 = 'https://www.melon.com/chart/index.htm'
    url_chart_realtime_100 = 'https://www.melon.com/chart/index.htm#params%5Bidx%5D=51'
    file_path = os.path.join(path_data_dir,'chart_realtime_50.html')
    #try-except
    try :
        with open(file_path, 'wt') as f:
            f.write(source)
            response = requests.get(url_chart_realtime_50)
            source = response.text
    except FileExistsError :
        print(f'"{file_path}" file is already exists!')

    # with open('data/chart_realtime_50.html', 'wt') as f:
    #     f.write(source)

    #file exist
    file_path = os.path.join(path_data_dir, 'chart_realtime_100.html')

    # file no exist
    if not os.path.exists(file_path) :
            response = requests.get(url_chart_realtime_100)
            source = response.text
            with open('data/char_realtime_100.html', 'wt') as f:
                f.write(source)
    else :
        print(f'"{file_path}" file is already exists!')

    #file_path = os.path.join(path_data_dir, 'abc.txt')
    #print(f'file_path: \n{file_path}')

    # result = []
    # for tr in soup.find_all('tr', class_='lst50'):
    #     rank = tr.find('span', class_='rank').text
    #     title = tr.find('div', class_='rank01').find('a').text
    #     artist = tr.find('div', class_='rank02').find('a').text
    #     album = tr.find('div', class_='rank03').find('a').text
    #     url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
    #     # http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/120/quality/80/optimize
    #     # .* -> 임의 문자의 최대 반복
    #     # \. -> '.' 문자
    #     # .*?/ -> '/'이 나오기 전까지의 최소 반복
    #     p = re.compile(r'(.*\..*?)/')
    #     url_img_cover = re.search(p, url_img_cover).group(1)
    #
    #     result.append({
    #         'rank': rank,
    #         'title': title,
    #         'url_img_cover': url_img_cover,
    #         'artist': artist,
    #         'album': album,
    #     })
    #