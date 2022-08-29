import requests as r
import re
        
spacex = '\W*.\W*.*'
def Name(prename):
        
    name = ''
    for i in prename:
        if i == "'":
            i = "%27"
        name += i
        
    return name

def splitter(var):
    var = var[0]
    var = var.split("\n      ")
    var = var[0] + var[-1]
    return var

def search(fighter):
    page = r.get('http://ufcstats.com/statistics/fighters/search?query=' + Name(fighter))
    search = re.findall('http://ufcstats.com/fighter-details/.{16}', page.text)
    search = search[0]
    fighterpage = r.get(search)
    height = re.findall('Height:'+ spacex + '"', fighterpage.text)
    splitter(height)
    print (height)


search('Kamaru')