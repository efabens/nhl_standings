from bs4 import BeautifulSoup as bs
import urllib2


def parse_it(d, team):
    print i.attrs
    n = i.attrs['team']
    d[n]={}
    d[n]['conf'] = i.parent.parent.parent.parent.parent.parent.attrs['name']
    d[n]['divi'] = i.parent.parent.parent.attrs['heading']
    d[n]['abrev'] = i.attrs['tricode']


if __name__ == "__main__":
    url = "http://app.cgy.nhl.yinzcam.com/V2/Stats/Standings"
    a = urllib2.urlopen(url).read()

    soup = bs(a)

    teams = {}

    for i in soup.findAll('standing'):
        parse_it(teams, i)
