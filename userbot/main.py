# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 
""" UserBot başlangıç noktası """
import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, TELOID_VERSION, PATTERNS, DEFAULT_NAME, BOT_TOKEN,BOTLOG_CHATID
from .modules import ALL_MODULES
from .asisstant.modules import ALL_MODULE
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from pySmartDL import SmartDL
from telethon.tl import functions
from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp
import glob

ALIVE_MSG = [
     "{username}, `Teloid {worktime} zamandır çalışıyor...`\n——————————————\n**Telethon sürümü :** `{telethon}`\n**Userbot sürümü  :** `{teloid}`\n**Python sürümü    :** `{python}`\n**Plugin sayısı :** `{plugin}`\n——————————————\n**Emrine amadeyim dostum... 😇**",
    "`Userbotunuz çalışıyor ve sana bişey demek istiyor.. Seni seviyorum` **{teloidsahip}** ❤️ \n Bot Versiyonu: {teloid} ",
 
    "🎆 `Endişelenme! Seni yanlız bırakmam.` **{teloidsahip}**, `TeloidUserBot çalışıyor.` \n Bot Versiyonu: {teloid} ",
    "`⛈️ Elimden gelenin en iyisini yapmaya hazırım`, **{teloidsahip}** \n Bot Versiyonu: {teloid} ",
    "✨ `TeloidUserBot sahibinin emirlerine hazır...` \n Bot Versiyonu: {teloid} ",
    "`Şuan en gelişmiş userbotun düzenlediği mesajı okuyor olmalısın` **{teloidsahip}**. \n Bot Versiyonu: {teloid} ",
    "`Benimi Aramıştın ❓ Ben Buradayım Merak Etme` \n Bot Versiyonu: {teloid} ",
    "Merhaba {teloidsahip} , Ben senin tarafından seçilmiş, sana durmaksızın hizmet eden bir sekreterim👩🏻‍💻.",
    "**Hey** {teloidsahip} \n \n✨ __Yüklenen Plugin Sayısı__ ** {plugin} **\n \n👨🏼‍💻 __Python Sürümü__ ** {python} **\n \n⚡️__Telethon Sürüm__ ** {telethon} **\n \n__Botun Sapa Sağlam Çalışıyor iyi günler :)__☄️\n\n\n         __Teloid Sürüm__ ** {teloid} **"
]

DIZCILIK_STR = [
    "Çıkartmayı dızlıyorum...",
    "Çaldım Gitti Geçmiş Olsun 🤭",
    "Yaşasın dızcılık...",
    "Bu çıkartmayı kendi paketime davet ediyorum...",
    "Bunu dızlamam lazım...",
    "Hey bu güzel bir çıkartma!\nHemen dızlıyorum..",
    "Çıkartmanı dızlıyorum\nhahaha.",
    "Hey şuraya bak. (☉｡☉)!→\nBen bunu dızlarken...",
    "Güller kırmızı menekşeler mavi, bu çıkartmayı paketime dızlayarak havalı olacağım...",
    "Çıkartma hapsediliyor...",
    "Bay dızcı bu çıkartmayı dızlıyor... ",
    "Bu güzel çıkartma neden benim paketimde de olmasın🤭",
    "**Trrek çıkartmanı dızladım adam ol**"
]

AFKSTR = [
    "🥸 Merhaba {first_name}!\n📴 Aradığınız kişi şu anda telefona cevap verememektedir.\n🤫 En son {last_seen_long} önce buradaydı.\n🔈 Sinyal tonundan sonra, mesajınızı tarifeniz üzerinden bırakabilirsiniz.\n\n💸 Mesaj ücreti ₺0.69'dir.\n\n 🔉 biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiip!",
    "🔻Merhaba {mention} 🤡.\n🔻Şu an burada değilim.\n🔻Bekle beni👤, 👻ansızın gelebilirim.\n🔻Son görülmem: {last_seen_long} ..\n🔻Ne zaman gelirim: bilemem, belkide hiç bir zaman.",
    "Şu an acele işim var, daha sonra mesaj atsan olmaz mı? Zaten yine geleceğim.",
    "Aradığınız kişi şu anda telefona cevap veremiyor. Sinyal sesinden sonra kendi tarifeniz üzerinden mesajınızı bırakabilirsiniz. Mesaj ücreti 49 kuruştur. \n`biiiiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "Birkaç dakika içinde geleceğim. Fakat gelmezsem...\ndaha fazla bekle.",
    "Şu an burada değilim, ama muhtemelen başka bir yerdeyim.",
    "Güller kırmızı\nMenekşeler mavi\nBana bir mesaj bırak\nVe sana döneceğim.",
    "Bazen hayattaki en iyi şeyler beklemeye değer…\nHemen dönerim.",
    "Hemen dönerim,\nama eğer geri dönmezsem,\ndaha sonra dönerim.",
    "Henüz anlamadıysan,\nburada değilim.",
    "Merhaba, uzak mesajıma hoş geldiniz, bugün sizi nasıl görmezden gelebilirim?",
    "7 deniz ve 7 ülkeden uzaktayım,\n7 su ve 7 kıta,\n7 dağ ve 7 tepe,\n7 ovala ve 7 höyük,\n7 havuz ve 7 göl,\n7 bahar ve 7 çayır,\n7 şehir ve 7 mahalle,\n7 blok ve 7 ev...\n\nMesajların bile bana ulaşamayacağı bir yer!",
    "Şu anda klavyeden uzaktayım, ama ekranınızda yeterince yüksek sesle çığlık atarsanız, sizi duyabilirim.",
    "Şu yönde ilerliyorum\n---->",
    "Şu yönde ilerliyorum\n<----",
    "Lütfen mesaj bırakın ve beni zaten olduğumdan daha önemli hissettirin.",
    "Sahibim burada değil, bu yüzden bana yazmayı bırak.",
    "Burada olsaydım,\nSana nerede olduğumu söylerdim.\n\nAma ben değilim,\ngeri döndüğümde bana sor...",
    "Uzaklardayım!\nNe zaman dönerim bilmiyorum !\nUmarım birkaç dakika sonra!",
    "Sahibim şuan da müsait değil. Adınızı, numarınızı ve adresinizi verirseniz ona iletibilirm ve böylelikle geri döndüğü zaman.",
    "Üzgünüm, sahibim burada değil.\nO gelene kadar benimle konuşabilirsiniz.\nSahibim size sonra döner.",
    "Bahse girerim bir mesaj bekliyordun!",
    "Hayat çok kısa, yapacak çok şey var...\nOnlardan birini yapıyorum...",
    "Şu an burada değilim....\nama öyleysem ...\n\nbu harika olmaz mıydı?",
    "Beni hatırladığına sevindim ama şuanda klavye bana çok uzak",
    "Belki İyiyim, Belki Kötüyüm Bilmiyorsun Ama AFK Olduğumu Görebiliyorsun"
]

KICKME_MSG = [
    "Güle güle ben gidiyorum 👋🏻",
    "Sessizce çıkıyorum 🥴",
    "Haberin olmadan çıkarsam bir gün benim grupta olmadığı farkedeceksin.. O yüzden bu mesajı bırakıyorum🚪",
    "Hemen burayı terk etmeliyim🤭"
    "**Ops Ben Kaçtım Bye bYe..**"
]

CV_MSG = [
    "**{DEFAULT_NAME}** `Fazla Bi Bilgi Ayarlamamış Ama Şunu Biliyorum Kendisi Baya Zevkli Birisi Çünkü Teloid Userbot Kullanıyor.` 😁",
    "`Üzgünüm sana vercek bir bilgim yok.`"
]

UNAPPROVED_MSG = ("`Hey olduğun yerde kal,!👨‍💻 Ben Teloid. Endişelenme!\n\n`"
                  "`Sahibim sana mesaj atma izni vermedi o yüzden sahibim seni onaylayana kadar bu mesajı alacaksın.. `"
                  "`Lütfen sahibimin aktif olmasını bekleyin, o genellikle PM'leri onaylar.\n\n`"
                  "`Bildiğim kadarıyla o kafayı yemiş insanlara PM izni vermiyor.`")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()



INVALID_PH = '\nHATA: Girilen telefon numarası geçersiz' \
             '\n  Ipucu: Ülke kodunu kullanarak numaranı gir' \
             '\n   Telefon numaranızı tekrar kontrol edin'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()
BRAIN_CHECKER = BRAIN_CHECKER[0]


def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komutları Alıyoruz #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # lavanPY
            lavanpy = re.search('\"\"\"TeloidPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not lavanpy == None:
                lavanpy = lavanpy.group(0)
                for Satir in lavanpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin dışarıdan yüklenmiştir. Herhangi bir açıklama tanımlanmamıştır.')
            CmdHelp.add()
             

try:
    bot.start()
    idim = bot.get_me().id
    lavanbl = requests.get('https://raw.githubusercontent.com/Robotger/TeloidUbData/master/blacklist.json').json()
    if idim in lavanbl:
        bot.send_message("me", f"`❌ Teloid yöneticileri sizi bottan yasakladı! Bot kapatılıyor...`")
        LOGS.error("Teloid yöneticileri sizi bottan yasakladı! Bot kapatılıyor...")
        bot.disconnect()
    # ChromeDriver'ı Ayarlayalım #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Galeri için değerler
    GALERI = {}

    # PLUGIN MESAJLARI AYARLIYORUZ
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_MSG))}", "afk": f"`{str(choice(AFKSTR))}`", "kickme": f"`{str(choice(KICKME_MSG))}`", "pm": str(UNAPPROVED_MSG), "dızcı": str(choice(DIZCILIK_STR)), "cv": str(choice(CV_MSG)), "ban": "🌀 {mention}`, Banlandı!!`", "mute": "🌀 {mention}`, sessize alındı!`", "approve": "`Merhaba` {mention}`, artık bana mesaj gönderebilirsin!`", "disapprove": "{mention}`, artık bana mesaj gönderemezsin!`", "block": "{mention}`, bunu bana mecbur bıraktın! Seni engelledim!`"}


    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "cv", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("🔄 Pluginler Yükleniyor..")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Onsuzda Yüklüdür " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`[×] Yükleme Başarısız! Plugin Hatalı!!\n\nHata: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Lütfen pluginlerin kalıcı olması için PLUGIN_CHANNEL_ID'i ayarlayın.`")



except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALERI_SQL.TUM_GALERI[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False
#LOOP.run_until_complete(lavan_userbot_on())
#if not BOTLOG_CHATID:
    #LOOP.run_until_complete(autopilot())
#if not BOT_TOKEN:
    #LOOP.run_until_complete(autobot())
    
for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)
if BOT_TOKEN:
  
 for module_name in ALL_MODULE:
    imported_module = import_module("userbot.asisstant.modules." + module_name)    

os.system("clear")

LOGS.info("+===========================================================+")
LOGS.info("|                     ✨Teloid Userbot✨                    |")
LOGS.info("+==============+==============+==============+==============+")
LOGS.info("|                                                            |")
LOGS.info("Botunuz çalışıyor! Herhangi bir sohbete .alive yazarak Test edin."
          " Yardıma İhtiyacınız varsa, Destek grubumuza gelin t.me/RobotgerSupport")
LOGS.info(f"Bot versiyonunuz ==> {TELOID_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
