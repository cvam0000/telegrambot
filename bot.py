import telepot
from pprint import pprint
bot=telepot.Bot("538862630:AAF8LlV3qBSOKLDgbx-I1ZdTZvdtEdtQcVU")
pprint(bot.getMe())
responce=bot.getUpdates()
pprint(responce)