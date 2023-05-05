from datetime import datetime
from bs4 import BeautifulSoup
import re
import requests

def send_sports_data(date):
    base_address = {
        'nba': 'https://sports.news.naver.com/basketball/schedule/index?category=nba',
        'kbl': 'https://sports.news.naver.com/basketball/schedule/index?category=kbl',
        'epl': 'https://sports.news.naver.com/wfootball/schedule/index?category=epl',
        'champs': 'https://sports.news.naver.com/wfootball/schedule/index?category=champs'
    }
    output = 'Sports ' + date[4:] + '\n'

    def get(url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    for game_type in ['nba', 'kbl']:
        try:
            soup = get(base_address[game_type] + '&date=' + date)
            today = soup.find('div', {'class': 'sch_vs'})

            games = today.find_all('div', {'class': 'end'})

            if len(games) == 0:
                #print(f'NO {game_type} GAME TODAY')
                output += f'NO {game_type} GAME\n'
                continue

            for game in games:
                teams = game.find_all('span', {'class': 'vs_team'})
                #print(teams[0].get_text().strip() + ' vs ' + teams[1].get_text().strip())
                output += teams[0].get_text().strip() + ' vs ' + teams[1].get_text().strip() + '\n'
                scores = game.find_all('strong', {'class': 'vs_num'})
                #print(scores[0].get_text().strip() + ' : ' + scores[1].get_text().strip())
                output += scores[0].get_text().strip() + ' : ' + scores[1].get_text().strip() + '\n'
        except:
            continue

    return output + '\n'
