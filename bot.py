import telepot
from pprint import pprint
from telepot .loop import MessageLoop
bot=telepot.Bot("538862630:AAF8LlV3qBSOKLDgbx-I1ZdTZvdtEdtQcVU")
pprint(bot.getMe())
responce=bot.getUpdates()
pprint(responce)


#linux_puran -1001169337107




#https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=API_KEY  techcrunch_API

url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e353c11878134fc28d81faf7eff3b941'
data=request.get(url)
print(data)
bot.sendMessage(499134543, data)