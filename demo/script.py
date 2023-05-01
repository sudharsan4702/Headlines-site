import poplib
import requests
from bs4 import BeautifulSoup
# websites to scrape
imdb_news = "https://www.empireonline.com/movies/news/"  # movie site
tech_news = "https://techcrunch.com/"  # techcrunch site
game_news = "https://www.gameinformer.com/news"  # game informer site
economic_news = "https://www.moneycontrol.com/news/business/economy/"  # money control site
cricket_news = "https://www.cricbuzz.com/cricket-news/latest-news"  # cricbuzz site
# requests
response_imdb = requests.get(imdb_news)
response_tech = requests.get(tech_news)
response_game = requests.get(game_news)
response_economy = requests.get(economic_news)
response_cricket = requests.get(cricket_news)
# parser
soup_imdb = BeautifulSoup(response_imdb.text, 'html.parser')
soup_tech = BeautifulSoup(response_tech.text, 'html.parser')
soup_game = BeautifulSoup(response_game.text, 'html.parser')
soup_economy = BeautifulSoup(response_economy.text, 'html.parser')
soup_cricket = BeautifulSoup(response_cricket.text, 'html.parser')
# head_lines list
imdb_head_lines = []
tech_head_lines = []
game_head_lines = []
economy_head_lines = []
cricket_head_lines = []


def scrape_imdb():

    section = soup_imdb.find(
        'div', class_='jsx-2979979908 content').find_all('h3', class_='jsx-2519753491')
    for title in section:
        imdb_head_lines.append(title.text.strip())


def scrape_tech():

    tech_title = soup_tech.find_all('h2', class_='post-block__title')
    for t_title in tech_title:
        tech_head_lines.append(t_title.text.strip())


def scrape_game():

    game_title = soup_game.find(
        'div', class_='views-infinite-scroll-content-wrapper clearfix').find_all('h2', class_='page-title')
    for g_title in game_title:
        game_head_lines.append(g_title.text.strip())


def scrape_economy():

    economy_title = soup_economy.find('ul', id='cagetory').find_all('h2')
    for e_title in economy_title:
        economy_head_lines.append(e_title.text)


def scrape_cricket():

    cricket_title = soup_cricket.find('div', id='news-list').find_all('h2')
    for c_title in cricket_title:
        cricket_head_lines.append(c_title.text)


scrape_imdb()
scrape_tech()
scrape_game()
scrape_economy()
scrape_cricket()
