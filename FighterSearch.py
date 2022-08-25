import requests as r
import re

def Name(prename):
    global name
    name = ''
    for i in prename:
        if i == "'":
            i = "%27"
        name += i
    
    return name

page = r.get('http://ufcstats.com/statistics/fighters/search?query=' + Name("amanda nunes"))
fighter = re.search('http://ufcstats.com/fighter-details/................', page.text)
print(fighter)