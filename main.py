from bs4 import BeautifulSoup
import re
import utils
from utils import get_top100_list
from utils import get_song_detail

if __name__ == '__main__' :
    # result = get_top100_list(True)
    # for i in result:
    #     print(i)
    result_detail = get_song_detail(True)
    print(result_detail)
