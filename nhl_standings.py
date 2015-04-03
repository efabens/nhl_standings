from bs4 import BeautifulSoup as bs
import urllib2
from jinja2 import Environment, FileSystemLoader
import json


if __name__ == "__main__":
    url = "https://api.thescore.com/nhl/standings"
    teams = json.load(urllib2.urlopen(url))

    test = ['1', '2','3']

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')

    with open('pages/standings.html', 'w') as nh:
        nh.write(template.render(standings=teams, test=test))
