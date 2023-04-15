import os

print("String session generator hoşgeldiniz")
	
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = 1761415
API_HASH = "e989d7ca9dfbfe3da8ffb39e283dd9ce"
client = TelegramClient(StringSession(), APP_ID, API_HASH)
client.start()
session_str = client.session.save()
	
s_m = client.send_message("me", session_str)
s_m.reply(("⬆️ String sessionunuz "))
	
print("Lütfen telegram kayıtlı mesajlarınızı kontrol ediniz. ")

