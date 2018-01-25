import re
source = open('melon.html', 'rt').read()

# <td>...</td> 요소를 찾기 위한 정규표현식
PATTERN_TD = re.compile(r'<td.*?>.*?</td>', re.DOTALL)
# 찾은 결과 리스트
td_list = re.findall(PATTERN_TD, source)
# 리스트를 순회
for index, td in enumerate(td_list):
    td_strip = re.sub(r'[\n\t]+|\s{2,}', '', td)
    # print(f'{index:02}: {td_strip}')

#인덱스 1번 ((순위))

td_rank_cover = td_list[1]
PATTERN_RANK = re.compile(r'<span class="rank ">(.*?)</span>',re.DOTALL)
ranknumber = re.search(PATTERN_RANK, td_rank_cover).group(1)
print(ranknumber)

# 인덱스 3번  (이미지)
# 에 해당하는 <td>...</td>가 커버이미지의 img태그를 가지고 있음
td_img_cover = td_list[3]
# img태그의 'src'내용을 가져오는 정규표현식
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)
# 정규표현식을 인덱스3번 td에 적용해 커버이미지 url을 가져옴
url_img_cover = re.search(PATTERN_IMG, td_img_cover).group(1)
print(url_img_cover)

# 인덱스 5번에 해당하는 td가 곡 제목, 가수명을 가지고 있음
td_title_author = td_list[5]
# div.rank01에 곡 제목이 있음
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# 'div.rank01 a'의 내용에 곡 제목 텍스트가 있음

PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">.*?</div>', re.DOTALL)

PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

# div.rank01부분을 가져옴
div_rank01 = re.search(PATTERN_DIV_RANK01, td_title_author).group()
div_rank02 = re.search(PATTERN_DIV_RANK02, td_title_author).group()
# div.rank01에서 a태그의 내용을 가져와 title에 할당
title = re.search(PATTERN_A_CONTENT, div_rank01).group(1)
author = re.search(PATTERN_A_CONTENT, div_rank02).group(1)
print(title)
print(author)


##인덱스 6번
td_album = td_list[6]
PATTERN_ALBUM = re.compile(r'<div class="ellipsis rank03">.*?</div>',re.DOTALL)
div_rank03 = re.search(PATTERN_ALBUM, td_album).group()
albumname = re.search(PATTERN_A_CONTENT, td_album).group(1)
print(albumname)
#
# match_list = re.finditer(PATTERN_ALBUM,source)
# for match_list in match_list:


# match_list = re.finditer(PATTERN_DIV_RANK01, source)
# for match_div_rank01 in match_list:
#     # 각 순회에서 매치된 전체 문자열 (<div clas... ~ </div>)부분을 가져옴
#     div_rank01_content = match_div_rank01.group()
#
#     # 부분 문자열에서 a태그의 내용을 title변수에 할당
#     match_title = re.search(PATTERN_A_CONTENT, div_rank01_content)
#     title = match_title.group(1)
#     print(title)