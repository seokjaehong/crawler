import requests
import re

__all__ = (
    'get_tag_attribute',
    'get_tag_content'
)

def save_melon():
    """
    멜론사이트의 인기차트 에해당하는 페이지를 melon.html 로저장
    :return: None
    """

    response = requests.get('https://www.melon.com/chart/index.htm')
    source = response.text
    with open('melon.html', 'wt') as f:
        f.write(source)

def get_tag_attribute(attirbute_name, tag_string) :
    p = re.compile(r'^.*?<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
        attribute_name=attirbute_name
    ),re.DOTALL)
    m=re.search(p,tag_string)
    if m:
        return m.group('value')
    return ''


def get_tag_content (tag_string) :
    #p = re.compile(r'<.*?>(?P<value>.*)<.*?>',re.DOTALL)
    p = re.compile(r'<.*?>(?P<value>.*)<.*?>',re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        # return m.group('value')
        return get_tag_content(m)
    elif re.search(r'[<>]', tag_string):
        return ''
    else :
        return tag_string

def find_tag(tag, tag_string , class_=None) :
    """
    tag_string에서 tag요소를 찾아 리턴

    :param tag: 찾 을tag
    :param tag_string: 검색 할tag문자 열
    :return: 첫번째 로찾 은tag 문자열
    """
    p = re.compile(r'.*?(<{tag}.*?{class_}.*?>.*?</{tag}>)'.format(
        tag=tag,
        class_ =f'class=".*{class_}.*?"' if class_ else '',
    ),re.DOTALL)
    m = re.search(p,tag_string)
    if m:
        return m.group(1)
    return None
