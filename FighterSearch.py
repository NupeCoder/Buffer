import requests as r
import re
class Search:
    def __init__(self):
        self.name = ''
        

    def Name(self, prename):
        
        self.name = ''
        for i in prename:
            if i == "'":
                i = "%27"
            self.name += i
        
        return self.name
    
    def Search(self, name):
        page = r.get('http://ufcstats.com/statistics/fighters/search?query=' + self.Name(name))
        search = re.findall('http://ufcstats.com/fighter-details/.{16}', page.text)
        search = search[0]
        fighterpage = r.get(search)


