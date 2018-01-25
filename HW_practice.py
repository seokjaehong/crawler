import re
#source = open('melon.html', 'rt').read()
source = '''
<div class="first-div">
    <div class="second-div">
        <span class="span-content">ABCD</span>
    </div>
</div>
'''

# def get_tag_attribute(attribute_name, tag_string):
#     return re.finditer(r'{attribute_name}',tag_string)
# example = '<a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>'
# get_tag_attribute('href', example)


example = '<a href="javascript:melon.play.playSong(,30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>'


#mycode
# def get_tag_attribute(attribute_name, tag_string) :
#     findlist = re.findall(r'<a '+ attribute_name +r'\=(.*?)"',tag_string,re.DOTALL)
#     return findlist
#
# value1=get_tag_attribute('href',example)
# print(value1)
# value2=get_tag_attribute('title',example)
# print(value2)

#instructor code

# # 키워드 인저로 넘겨야되 정규식 안
# def get_tag_attribute(attirbute_name, tag_string) :
#     p = re.compile(r'^.*?<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
#         attribute_name=attirbute_name
#     ),re.DOTALL)
#     m=re.search(p,tag_string)
#     if m:
#         return m.group('value')
#     return ''
#
#
# result = get_tag_attribute('class',source)
# print(result)

def get_tag_content (tag_string) :
    #p = re.compile(r'<.*?>(?P<value>.*)<.*?>',re.DOTALL)
    p = re.compile(r'<.*?>(?P<value>.*)<.*?>',re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        # return m.group('value')
        return get_tag_content(r)

    else :
        return tag_string

result2 = get_tag_content(source)
print(result2)