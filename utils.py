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
    # utils가 있는
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

    # 1~50, 50~100위 웹페이지 주소
    url_chart_realtime = 'https://www.melon.com/chart/index.htm'

    # 1~100위에 해당하는 웹페이지 HTML을
    # data/chart_realtime_50.html 에 저장
    # 'xt'모드와 try-except를 쓸 경우
    file_path = os.path.join(path_data_dir, 'chart_realtime.html')
    try:
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode) as f:
            response = requests.get(url_chart_realtime)
            source = response.text
            f.write(source)
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')
