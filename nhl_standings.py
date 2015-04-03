from bs4 import BeautifulSoup as bs
import urllib2
from jinja2 import Environment, FileSystemLoader


def parse_it(d, team):
    n = i.attrs['team']
    d[n] = {}
    d[n]['conf'] = i.parent.parent.parent.parent.parent.parent.attrs['name']
    d[n]['divi'] = i.parent.parent.parent.attrs['heading']
    d[n]['abrev'] = i.attrs['tricode']
    e = i.statsgroup.attrs
    d[n]['gp'] = e['stat0']
    d[n]['w'] = e['stat1']
    d[n]['l'] = e['stat2']
    d[n]['otl'] = e['stat3']
    d[n]['points'] = e['stat4']


if __name__ == "__main__":
    url = "http://app.cgy.nhl.yinzcam.com/V2/Stats/Standings"
    a = urllib2.urlopen(url).read()

    soup = bs(a)

    teams = {}
    test = ['a', 'b', 'c']

    for i in soup.findAll('standing'):
        parse_it(teams, i)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')

    with open('pages/standings.html', 'w') as nh:
        nh.write(template.render(standings=teams))
