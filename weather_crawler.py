from datetime import datetime
from bs4 import BeautifulSoup
import re
import requests

def send_weather_data(date):
    base_address = 'https://weather.naver.com/today/02111598'
    output = 'Weather\n'

    def get(url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    try:
        soup = get(base_address)
        card = soup.find('div', {'class': 'card_week'})
        days = card.find_all('div', {'class': 'day_data'})

        for i in range(2):
            day = days[i].find('span', {'class': 'date_inner'})
            output += day.get_text().replace('\n','') + '\n'

            weather = days[i].find_all('span', {'class': 'weather_inner'})
            am1 = '���� ' + weather[0].find('span', {'class': 'rainfall'}).get_text().replace('\n',' ').replace('����Ȯ��','')
            am2 = weather[0].find('span', {'class': 'weather_text'}).get_text()
            pm1 = '���� ' + weather[1].find('span', {'class': 'rainfall'}).get_text().replace('\n',' ').replace('����Ȯ��','')
            pm2 = weather[1].find('span', {'class': 'weather_text'}).get_text()
            output += am1 + ' ' + am2 + '|' + pm1 + ' ' + pm2 + '|'

            output += days[i].find('strong' ,{'class', 'temperature'}).get_text().replace('\n', '').replace('�������',' ').replace('�ְ���',' ') + '\n'
    except:
        pass

    return output + '\n'


#��ȱ� ����2��02111598