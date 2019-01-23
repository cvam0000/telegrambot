import telepot
from pprint import pprint
from telepot .loop import MessageLoop
import requests
from requests import *
import json
import time 

from hn import HN #hacker news 

bot=telepot.Bot("538862630:AAF8LlV3qBSOKLDgbx-I1ZdTZvdtEdtQcVU")
pprint(bot.getMe())
#responce1=bot.getUpdates()
#pprint(responce1)


#linux_puran -1001169337107




#https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=API_KEY  techcrunch_API

url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e353c11878134fc28d81faf7eff3b941'

resp = requests.get(url).json()
#if resp.status_code != 200:
    # This means something went wrong.
    #print('hello')
    #raise ApiError('GET /tasks/ {}'.format(resp.status_code))

#response = requests.get(url)

for x in range(9):
    title=resp['articles'][x]['title']
    description=resp['articles'][x]['title']
    url=resp['articles'][x]['url']
    source = resp['articles'][x]['source']['name']
    output=  "***"+source +"***\n"+description+"\n"+url
    bot.sendMessage(499134543, output ,parse_mode= 'Markdown')
    time.sleep(100)


#print(resp['articles'][0]['title'])

#print(resp)



#bot.sendMessage(499134543, output ,parse_mode= 'Markdown')