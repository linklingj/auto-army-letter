from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from summarize_text import summarize_article
import re
import requests

#네이버 뉴스의 특정 언론사에서 크롤링
def send_press():
    yesterday = datetime.today() - timedelta(days=1)
    base_address = 'https://media.naver.com/press/437/ranking?type=section&date=' + yesterday.strftime('%Y%m%d')
    output = 'News Summary : ' + yesterday.strftime('%Y%m%d') + '\n'

    def get(url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_body_text(article, chars=700):
        html = str(article.find('div', {'id': 'dic_area'}))
        edited_html = re.sub('<br/>', '\n', html)
        content = BeautifulSoup(edited_html, 'html.parser').text
        formatted = re.sub('\n', ' ', content)
        formatted = re.sub('\t', '', formatted)
        formatted = re.sub(' +', ' ', formatted)
        return formatted[:chars].strip()


    soup = get(base_address)
    sections = soup.find_all('div', {'class': 'press_ranking_box'})
    for section in sections:
        try:
            section_name = section.find('strong', {'class': 'press_ranking_tit'}).get_text()
            article = section.find('li', {'class': 'as_thumb'})
            title = article.find('strong', {'class': 'list_title'}).get_text()
            view = article.find('span', {'class': 'list_view'})
            view_cnt = int(re.findall(r'\d+', view.get_text().replace(',',''))[0])
            url = section.find('a').get('href')

            if view_cnt < 200:
                continue
            
            #print(f'[{section_name}]')
            output += '#' + section_name + '\n'
            #print(title + f' (view:{view_cnt})')
            output += title + f' (v:{view_cnt})' + '\n'

            article_soup = get(url)
            article_text = get_body_text(article_soup)
            #print(article_text[:100])
            output += summarize_article(article_text) + '\n'

        except:
            continue

    return output + '\n'
