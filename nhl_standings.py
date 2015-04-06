import urllib2
from jinja2 import Environment, FileSystemLoader
import json
from ftplib import FTP

def process(a_list):
    highest_max=0

    for i in a_list:
        i['gl'] = 82-int(i['games_played'])
        i['max_p'] = i['gl']*2+int(i['points'])
        highest_max=max(i['points'], highest_max)

    return highest_max

if __name__ == "__main__":
    url = "https://api.thescore.com/nhl/standings"
    teams = json.load(urllib2.urlopen(url))

    test = ['1', '2','3']

    highest=process(teams)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.jinja')

    with open('pages/standings.html', 'w') as nh:
        nh.write(template.render(standings=teams, maxi=highest))

