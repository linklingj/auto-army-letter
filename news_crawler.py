from datetime import datetime
from bs4 import BeautifulSoup
from summarize_text import summarize_article
import re
import requests

#네이버 뉴스에서 크롤링
def send_news():
    base_address = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=10'

    def get(url):
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except:
            pass

    def get_body_text(article, chars=1000):
        try:
            html = str(article.find('div', {'id': 'dic_area'}))
            edited_html = re.sub('<br/>', '\n', html)
            content = BeautifulSoup(edited_html, 'html.parser').text
            formatted = re.sub('\n', ' ', content)
            formatted = re.sub('\t', '', formatted)
            formatted = re.sub(' +', ' ', formatted)
            return formatted[:chars].strip()
        except:
            pass

    #0 정치 1 경제 2 사회 3 생활/문화 4 세계 5 IT/과학
    article_per_subject = {0 : 1, 1 : 1, 2 : 1, 4 : 1, 5 : 1}
    for i in [0, 1, 2, 4, 5]:
        max_cnt = article_per_subject[i]
        soup = get(base_address + str(i))
        section_name = soup.find('title').text.split(' ')[0]
        print(section_name)
        articles = soup.find_all('dt', {'class': ''})

        article_cnt = 0
        for item in articles:
            try:
                item = item.find('a', {'class': 'nclicks(fls.list)'})
                title = re.sub('\t', '', item.text)
                url = re.sub('\t', '', item.attrs['href'])
                print(title)
                article_soup = get(url)
                article = get_body_text(article_soup)
                print(article[:100])
                #summarize_article(article)

                article_cnt += 1
            except:
                continue
            if article_cnt == max_cnt:
                break

