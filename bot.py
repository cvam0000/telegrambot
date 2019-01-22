import telepot
from pprint import pprint
from telepot .loop import MessageLoop
bot=telepot.Bot("538862630:AAF8LlV3qBSOKLDgbx-I1ZdTZvdtEdtQcVU")
pprint(bot.getMe())
responce=bot.getUpdates()
pprint(responce)


#linux_puran -1001169337107
bot.sendMessage(499134543, 'Hey! bro ')