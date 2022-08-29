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
    var = var[0] +' '+ var[-1]
    return var      

def search(fighter):
    page = r.get('http://ufcstats.com/statistics/fighters/search?query=' + Name(fighter))
    search = re.findall('http://ufcstats.com/fighter-details/.{16}', page.text)
    search = search[0]
    fighterpage = r.get(search)
    fightername = re.findall('title-highlight">\W*.*', fighterpage.text)
    fightername = fightername[0]
    fightername = fightername.split("\n                ")
    fightername = fightername[-1]

    height = re.findall('Height:'+ spacex + '"', fighterpage.text)
    weight = re.findall('Weight:'+ spacex + 'lbs', fighterpage.text)
    reach = re.findall('Reach:'+ spacex + '"', fighterpage.text)
    record = re.findall('Record:.*', fighterpage.text)
    record = record[0]
    global result
    result = 'Name: '+fightername+'\n'+splitter(height)+'\n'+ splitter(weight)+'\n'+ splitter(reach)+'\n'+ splitter(height)+'\n'+record
    
    

