from bs4 import BeautifulSoup
from os.path import expanduser, join
import requests


#import asyncio
#import aiohttp

class AppLogic:
    def __init__(self):
        self.Header =  {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0'}
        self.Data = dict()
        self.ItemPageUrl = "https://pastebin.com/archive"
        self.RootUrl = "https://pastebin.com/"
        self.Urls = ["https://pastebin.com/archive", 
                     "https://pastebin.com/archive/python",
                     "https://pastebin.com/archive/php",
                     "https://pastebin.com/archive/csharp",
                     "https://pastebin.com/archive/c",
                     "https://pastebin.com/archive/cpp",
                     "https://pastebin.com/archive/java",
                     "https://pastebin.com/archive/lua",
                     "https://pastebin.com/archive/html5",
                     "https://pastebin.com/archive/json",
                     "https://pastebin.com/archive/bash",
                     "https://pastebin.com/archive/javascript",
                   ]
    
    def GetItemsFromArchive(self, url="https://pastebin.com/archive"):
        try:
            Req = requests.get(url, headers=self.Header)
            store = list()
            if Req.status_code == 200:
                bs = BeautifulSoup(Req.text, "html.parser")
                table = bs.table
                raw_items = table.find_all("tr")
                for item in raw_items:
                    link = item.find_all("a")
                    if len(link) == 2:
                       d = dict()
                       d["Title"] = link[0].text
                       d["Url"] = link[0].get('href')
                       d["Syntax"] = link[1].text
                       store.append(d)
                       if len(store) > 25:
                           break
                return store
            else:
                return None

        except Exception as e:
            print(str(e))
    
    def GetRawData(self, url):
        FullRawUrl = self.RootUrl + 'raw' + url
        Req = requests.get(FullRawUrl, headers=self.Header)
        try:
            if Req.status_code == 200:
                return Req.text
            return None
        except Exception as e:
            return None
    
    def  GetAllData(self ):
        holder = dict()
        for url in self.Urls:
            data = self.GetItemsFromArchive(url)
            name = url.split('/')
            holder[name[-1]] = data

        return holder


    ##########

#   async def AsyncGetItemsFromArchive(self, session, url="https://pastebin.com/archive"):
#       holder = list()
#       async with session.get(url) as response:
#           if response.status == 200:
#               html = await response.text()
#               bs = BeautifulSoup(html, "html.parser")
#               table = bs.table
#               raw_items = table.find_all("tr")
#               for item in raw_items:
#                   link = item.find_all("a")
#                   if len(link) == 2:
#                      d = dict()
#                      d["Title"] = link[0].text
#                      d["Url"] = link[0].get('href')
#                      d["Syntax"] = link[1].text
#                      holder.append(d)
#               name = url.split('/')
#               self.Data[name[-1]] = holder
#
#   
#   async def AsyncGetAllData(self):
#       tasks = []
#       async with aiohttp.ClientSession() as session:
#           for url in self.Urls:
#               task = asyncio.ensure_future(self.AsyncGetItemsFromArchive(session, url))
#               tasks.append(task)
#           await asyncio.gather(*tasks, return_exceptions=True)
#       
#     
#   def Run(self):
#       asyncio.get_event_loop().run_until_complete(self.AsyncGetAllData())