from pyrogram import Client, idle, enums
import json
from userbot import app, Db
from config import BOTLOG
import sys
import requests
from random import choice

ALIVE_MSG = [
     "{username}, `XUserBot {worktime} zamandır çalışıyor...`\n——————————————\n**Pyrogram sürümü :** `{pyrogram}`\n**Userbot sürümü  :** `{xver}`\n**Python sürümü    :** `{python}`\n**Plugin sayısı :** `{plugin}`\n——————————————\n**Emrine amadeyim dostum... 😇**",
    "`Userbotunuz çalışıyor ve sana bişey demek istiyor.. Seni seviyorum` **{xsahip}** ❤️ \n Bot Versiyonu: {xver} ",
    "🎆 `Endişelenme! Seni yanlız bırakmam.` **{xsahip}**, `xverUserBot çalışıyor.` \n Bot Versiyonu: {xver} ",
    "`⛈️ Elimden gelenin en iyisini yapmaya hazırım`, **{xsahip}** \n Bot Versiyonu: {xver} ",
    "✨ `xverUserBot sahibinin emirlerine hazır...` \n Bot Versiyonu: {xver} ",
    "`Şuan en gelişmiş userbotun düzenlediği mesajı okuyor olmalısın` **{xsahip}**. \n Bot Versiyonu: {xver} ",
    "`Benimi Aramıştın ❓ Ben Buradayım Merak Etme` \n Bot Versiyonu: {xver} ",
    "Merhaba {xsahip} , Ben senin tarafından seçilmiş, sana durmaksızın hizmet eden bir sekreterim👩🏻‍💻.",
    "**Hey** {xsahip} \n \n✨ __Yüklenen Plugin Sayısı__ ** {plugin} **\n \n👨🏼‍💻 __Python Sürümü__ ** {python} **\n \n⚡️__Pyrogram Sürüm__ ** {pyrogram} **\n \n__Botun Sapa Sağlam Çalışıyor iyi günler :)__☄️\n\n\n         __xver Sürüm__ ** {xver} **"
]



if len(sys.argv) > 1:
    resp = requests.get("https://ixelizm.dev/changelog")
    content = resp.text
    text = "`Bot Başarıyla Güncellendi!`"
    app.edit_message_text(int(sys.argv[-2]), int(sys.argv[-1]), text)


  
PLUGIN_MESAJLAR = {}
ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_MSG))}"}

PLUGIN_MESAJLAR_TURLER = ["alive"]
for mesaj in PLUGIN_MESAJLAR_TURLER:
    PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
    for i in Db.data['messages']:
        if mesaj in i:
                PLUGIN_MESAJLAR[mesaj] = i[mesaj]
app.start()
me = app.get_me() 





idle()
