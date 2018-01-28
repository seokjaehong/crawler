
#from utils.models import MelonCrawler
from HW_melon_utils import *

from utils.Models import *

if __name__ == '__main__':
    crawler = MelonCrawler()

    # q = input('검색할 곡 명을 입력해주세요: ')
    # result = crawler.search_song(q)
    # result1=result[0]
    # print(result1.title)
    # print(result1.artist)
    # print(result1.lyrics)



    result3 = crawler.search_artist('아이유')
    # result4 = result3.get_detail('True')
    # print(result3.birthdate)
    # print(result4)
    result2 = result3[0]
    print(result2.name)
    print(result2.gubun)
    birthdate = result2.birthdate
    print(birthdate)
    #
    # # artist_list = crawler.search_artist('아이유')
    # art = Artist(261143,'아이유','솔로','Balld,Dance,Drama')
    # # art.artist_id=261143
    # # art.name='아이유'
    # # art.gubun='솔로'
    # # art.genre = 'Ballad, Dance, Drama'
    # detail=art.get_detail('False')
    # print(detail.birthdate)
    #
    # print(artist_list)


    #for artist in artist_list:
    #    print(artist)

    # artist1 = artist_list[1]
    # print(artist1.name,artist1.genre)
    # print(artist1.debutdate)





    #print(get_song_detail(True))