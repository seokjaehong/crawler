
#from utils.models import MelonCrawler
from HW_melon_utils import *

from utils.Models import *

if __name__ == '__main__':
    crawler = MelonCrawler()
    #q = input('검색할 곡 명을 입력해주세요: ')
    #result = crawler.search_song(q)
    #detaillist = crawler.getdetail()

    crawler.search_artist('아이유')
    #crawler.search_song('기대해')



    #print(get_song_detail(True))