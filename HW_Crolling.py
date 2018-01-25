import re
source = open('melon.html', 'rt').read()

# 노래제목찾기
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">(.*?)</div>', re.DOTALL)
# <a href=....>(내용)</a>
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

match_list = PATTERN_DIV_RANK01.finditer(source)

title_list = list()

for match in match_list:
    #PATTERN_A_CONTENT.search( PATTERN_A_CONTENT,PATTERN_DIV_RANK01)
    result = PATTERN_A_CONTENT.search(match.group())
    title_list.append(result.group(1))

# print(title_list)

#가수찾기

PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">(.*?)</div>', re.DOTALL)
found_list = PATTERN_DIV_RANK02.finditer(source)

artist_list = list()
for match in found_list:
    result = PATTERN_A_CONTENT.search(match.group())
    artist_list.append(result.group(1))

# print(artist_list)

#앨 범 찾 기


PATTERN_DIV_RANK03 = re.compile(r'<div class="ellipsis rank03">(.*?)</div>', re.DOTALL)

found_list = PATTERN_DIV_RANK03.finditer(source)

album_list = list()
for i in found_list:
    result = PATTERN_A_CONTENT.search(i.group())
    album_list.append(result.group(1))

result_list = list(zip(title_list,artist_list,album_list))

final_list =list()

count = 1

for i in result_list:
    result_dict = dict()
    result_dict["rank"] = count
    result_dict["title"] = i[0]
    result_dict["singer"] = i[1]
    result_dict["album"] =i[2]
    final_list.append(result_dict)
    count += 1

for i in final_list :
    print(i)

