""#line:8
from telethon .errors import ChannelPrivateError #line:9
import requests #line:10
from .helpers import worktime as timelavan #line:11
from lib2to3 .pgen2 .token import STRING #line:12
import os #line:13
import asyncio #line:14
import time #line:15
import heroku3 #line:16
from re import compile #line:17
from .utils .pip_install import install_pip #line:18
from sys import version_info #line:19
from logging import basicConfig ,getLogger ,INFO ,DEBUG #line:20
from distutils .util import strtobool as sb #line:21
from pylast import LastFMNetwork ,md5 #line:22
from pySmartDL import SmartDL #line:23
from sqlite3 import connect #line:24
from telethon .tl .functions .channels import GetFullChannelRequest as getchat #line:25
from telethon .tl .functions .phone import GetGroupCallRequest as getvc #line:26
from dotenv import load_dotenv #line:27
from requests import get #line:28
from telethon .tl .functions .channels import JoinChannelRequest ,LeaveChannelRequest #line:29
from telethon .sync import TelegramClient ,custom #line:30
from telethon .sessions import StringSession #line:31
from telethon .events import callbackquery ,InlineQuery ,NewMessage #line:32
from telethon .tl .functions .users import GetFullUserRequest #line:33
from math import ceil #line:34
from telethon .tl .functions .channels import EditPhotoRequest ,CreateChannelRequest #line:35
from telethon import TelegramClient ,events #line:36
from telethon .errors import SessionPasswordNeededError ,PhoneCodeInvalidError ,PasswordHashInvalidError ,PhoneNumberInvalidError #line:37
from telethon .network import ConnectionTcpAbridged #line:38
from telethon .utils import get_display_name #line:39
from telethon .sessions import StringSession #line:40
load_dotenv ("config.env")#line:42
KURULUM =os .environ .get ("KURULUM",None )#line:44
STRING_SESSION =os .environ .get ("STRING_SESSION",None )#line:46
if (STRING_SESSION ==None ):#line:47
  os .system ("python GenerateStringSession.py")#line:50
  print ("İlk Kurulum tamamlandı STRING_SESSION İsimli Secret oluşturduktan sonra Lütfen yeniden başlatın!!")#line:53
  exit ()#line:54
else :#line:55
  pass #line:56
StartTime =time .time ()#line:58
CONSOLE_LOGGER_VERBOSE =sb (os .environ .get ("CONSOLE_LOGGER_VERBOSE","False"))#line:61
ASYNC_POOL =[]#line:63
if CONSOLE_LOGGER_VERBOSE :#line:65
  basicConfig (filename ="logfile.txt",level =DEBUG ,format ="[%(asctime)s - %(levelname)s] - @TeloidUserBot : %(message)s",datefmt ='%d-%b-%y %H:%M:%S',filemode ="w")#line:71
else :#line:73
  basicConfig (filename ="logfile.txt",level =INFO ,format ="[%(asctime)s - %(levelname)s] - @TeloidUserBot : %(message)s",datefmt ='%d-%b-%y %H:%M:%S',filemode ="w",)#line:80
LOGS =getLogger (__name__ )#line:82
if version_info [0 ]<3 or version_info [1 ]<6 :#line:84
  LOGS .info ("En az python 3.6 sürümüne sahip olmanız gerekir." "Birden fazla özellik buna bağlıdır. Bot kapatılıyor.")#line:86
  quit (1 )#line:87
branch ="master"#line:88
CONFIG_CHECK =os .environ .get ("___________LUTFEN_______BU_____SATIRI_____SILIN__________",None )#line:92
if CONFIG_CHECK :#line:94
  LOGS .info ("Lütfen ilk hashtag'de belirtilen satırı config.env dosyasından kaldırın")#line:96
  quit (1 )#line:97
LANGUAGE =os .environ .get ("LANGUAGE","DEFAULT").upper ()#line:100
if not LANGUAGE in ["EN","TR","AZ","UZ","DEFAULT"]:#line:102
  LOGS .info ("Bilinmeyen bir dil yazdınız. Bundan dolayı DEFAULT kullanılıyor.")#line:103
  LANGUAGE ="DEFAULT"#line:104
TELOID_VERSION ="v0.2"#line:107
MAX_MESSAGE_SIZE_LIMIT =4095 #line:109
API_KEY =os .environ .get ("API_KEY",None )#line:111
API_HASH =os .environ .get ("API_HASH",None )#line:112
SEVGILI =os .environ .get ("SEVGILI",None )#line:114
async def get_call (OOOO00OOO0OOO00O0 ):#line:118
  OOO00O0O00OOO000O =await OOOO00OOO0OOO00O0 .client (getchat (OOOO00OOO0OOO00O0 .chat_id ))#line:119
  OOOOOO0000O00OOO0 =await OOOO00OOO0OOO00O0 .client (getvc (OOO00O0O00OOO000O .full_chat .call ))#line:120
  return OOOOOO0000O00OOO0 .call #line:121
SUDO_HANDLER =os .environ .get ("SUDO_HANDLER",r".")#line:125
try :#line:126
  SUDO_USERS =set (int (O00OOOO0OO0000O00 )for O00OOOO0OO0000O00 in os .environ .get ("SUDO_USERS","").split ())#line:127
except ValueError :#line:128
  raise Exception ("Bir Kullanıcı İd si Belirtmek zorundasın.")#line:129
SILINEN_PLUGIN ={}#line:131
BOTLOG_CHATID =int (os .environ .get ("BOTLOG_CHATID",0 ))#line:135
BOTLOG =sb (os .environ .get ("BOTLOG","False"))#line:138
LOGSPAMMER =sb (os .environ .get ("LOGSPAMMER","False"))#line:140
PM_AUTO_BAN =sb (os .environ .get ("PM_AUTO_BAN","False"))#line:143
HEROKU_MEMEZ =sb (os .environ .get ("HEROKU_MEMEZ","False"))#line:146
HEROKU_APPNAME =os .environ .get ("HEROKU_APPNAME",None )#line:147
HEROKU_APIKEY =os .environ .get ("HEROKU_APIKEY",None )#line:148
EZZEC =False #line:153
Heroku =None #line:154
app =None #line:155
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None :#line:157
  if EZZEC ==True :#line:158
    pass #line:159
  else :#line:160
    EZZEC =True #line:161
    Heroku =heroku3 .from_key (HEROKU_APIKEY )#line:162
    app =Heroku .app (HEROKU_APPNAME )#line:163
    heroku_var =app .config ()#line:164
    heroku_var ["UPSTREAM_REPO_URL"]="https://github.com/Robotger/TeloidUserBot.git"#line:166
else :#line:167
  app =None #line:168
try :#line:170
  import randomstuff #line:171
except ModuleNotFoundError :#line:172
  install_pip ("randomstuff.py")#line:173
  import randomstuff #line:174
RANDOM_STUFF_API_KEY =os .environ .get ("RANDOM_STUFF_API_KEY",None )#line:177
if RANDOM_STUFF_API_KEY :#line:178
  try :#line:179
    rs_client =randomstuff .AsyncClient (api_key =RANDOM_STUFF_API_KEY ,version ="4")#line:181
  except :#line:182
    print ('Invalid RANDOM_STUFF_API_KEY')#line:183
    rs_client =None #line:184
else :#line:185
  rs_client =None #line:186
AI_LANG =os .environ .get ("AI_LANG",'en')#line:187
STABILITY =sb (os .environ .get ("STABILITY","True"))#line:190
UPSTREAM_REPO_URL ="https://github.com/Robotger/TeloidUserBot.git"#line:192
EMERGENCY ="https://github.com/Robotger/TeloidUserBot.git"#line:193
AFKILETME =sb (os .environ .get ("AFKILETME","True"))#line:195
DB_URI =os .environ .get ("DATABASE_URL","sqlite:///teloid.db")#line:198
OCR_SPACE_API_KEY =os .environ .get ("OCR_SPACE_API_KEY",None )#line:201
REM_BG_API_KEY =os .environ .get ("REM_BG_API_KEY",None )#line:204
AUTO_PP =os .environ .get ("AUTO_PP",None )#line:207
SUDO_ID =set (int (OOO0OOOO00O00O000 )for OOO0OOOO00O00O000 in os .environ .get ("SUDO_ID","").split ())#line:209
WARN_LIMIT =int (os .environ .get ("WARN_LIMIT",3 ))#line:213
WARN_MODE =os .environ .get ("WARN_MODE","gmute")#line:214
if not WARN_MODE in ["gmute","gban"]:#line:216
  WARN_MODE ="gmute"#line:217
GALERI_SURE =int (os .environ .get ("GALERI_SURE",60 ))#line:220
CHROME_DRIVER =os .environ .get ("CHROME_DRIVER",None )#line:223
GOOGLE_CHROME_BIN =os .environ .get ("GOOGLE_CHROME_BIN",None )#line:224
WORKTIME =time .time ()#line:227
PLUGINID =os .environ .get ("PLUGIN_CHANNEL_ID",None )#line:229
if not PLUGINID :#line:231
  PLUGIN_CHANNEL_ID ="me"#line:232
else :#line:233
  PLUGIN_CHANNEL_ID =int (PLUGINID )#line:234
OPEN_WEATHER_MAP_APPID =os .environ .get ("OPEN_WEATHER_MAP_APPID",None )#line:237
WEATHER_DEFCITY =os .environ .get ("WEATHER_DEFCITY",None )#line:238
ANTI_SPAMBOT =sb (os .environ .get ("ANTI_SPAMBOT","False"))#line:241
ANTI_SPAMBOT_SHOUT =sb (os .environ .get ("ANTI_SPAMBOT_SHOUT","True"))#line:242
YOUTUBE_API_KEY =os .environ .get ("YOUTUBE_API_KEY",None )#line:245
COUNTRY =str (os .environ .get ("COUNTRY",""))#line:248
TZ_NUMBER =int (os .environ .get ("TZ_NUMBER",1 ))#line:249
CLEAN_WELCOME =sb (os .environ .get ("CLEAN_WELCOME","True"))#line:252
BIO_PREFIX =os .environ .get ("BIO_PREFIX","@TeloidUserBot | ")#line:255
LASTFM_API =os .environ .get ("LASTFM_API",None )#line:258
LASTFM_SECRET =os .environ .get ("LASTFM_SECRET",None )#line:259
LASTFM_USERNAME =os .environ .get ("LASTFM_USERNAME",None )#line:260
LASTFM_PASSWORD_PLAIN =os .environ .get ("LASTFM_PASSWORD",None )#line:261
LASTFM_PASS =md5 (LASTFM_PASSWORD_PLAIN )#line:262
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS :#line:263
  lastfm =LastFMNetwork (api_key =LASTFM_API ,api_secret =LASTFM_SECRET ,username =LASTFM_USERNAME ,password_hash =LASTFM_PASS )#line:267
else :#line:268
  lastfm =None #line:269
G_DRIVE_CLIENT_ID =os .environ .get ("G_DRIVE_CLIENT_ID",None )#line:272
G_DRIVE_CLIENT_SECRET =os .environ .get ("G_DRIVE_CLIENT_SECRET",None )#line:273
G_DRIVE_AUTH_TOKEN_DATA =os .environ .get ("G_DRIVE_AUTH_TOKEN_DATA",None )#line:274
GDRIVE_FOLDER_ID =os .environ .get ("GDRIVE_FOLDER_ID",None )#line:275
TEMP_DOWNLOAD_DIRECTORY =os .environ .get ("TMP_DOWNLOAD_DIRECTORY","./downloads")#line:277
DEFAULT_BIO =os .environ .get ("DEFAULT_BIO",None )#line:280
USERBOT_ =True #line:283
BOT_TOKEN =os .environ .get ("BOT_TOKEN",None )#line:286
BOT_USERNAME =os .environ .get ("BOT_USERNAME",None )#line:287
GENIUS =os .environ .get ("GENIUS",None )#line:290
CMD_HELP ={}#line:292
CMD_HELP_BOT ={}#line:293
PM_AUTO_BAN_LIMIT =int (os .environ .get ("PM_AUTO_BAN_LIMIT",4 ))#line:295
SPOTIFY_DC =os .environ .get ("SPOTIFY_DC",None )#line:297
SPOTIFY_KEY =os .environ .get ("SPOTIFY_KEY",None )#line:298
PAKET_ISMI =os .environ .get ("PAKET_ISMI","| 🌃 @TeloidUserBot Paketi |")#line:300
BLACKLIST_CHAT =[1615593199 ]#line:304
OTOMATIK_KATILMA =sb (os .environ .get ("OTOMATIK_KATILMA","True"))#line:307
AUTO_UPDATE =sb (os .environ .get ("AUTO_UPDATE","True"))#line:308
PATTERNS =os .environ .get ("PATTERNS",".;!,")#line:311
WHITELIST =get ('https://raw.githubusercontent.com/Robotger/Teloidubdata/master/whitelist.json').json ()#line:314
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None :#line:316
  Heroku =heroku3 .from_key (HEROKU_APIKEY )#line:317
  app =Heroku .app (HEROKU_APPNAME )#line:318
  heroku_var =app .config ()#line:319
forceVer =[]#line:322
if os .path .exists ("force-surum.check"):#line:323
  os .remove ("force-surum.check")#line:324
else :#line:325
  LOGS .info ("Force Sürüm Kontrol dosyası yok, getiriliyor...")#line:326
URL ='https://raw.githubusercontent.com/Robotger/TeloidUbdata/master/force-surum.check'#line:328
with open ('force-surum.check','wb')as load :#line:329
  load .write (get (URL ).content )#line:330
DB =connect ("force-surum.check")#line:332
CURSOR =DB .cursor ()#line:333
CURSOR .execute ("""SELECT * FROM SURUM1""")#line:334
ALL_ROWS =CURSOR .fetchall ()#line:335
for i in ALL_ROWS :#line:337
  forceVer .append (i [0 ])#line:338
  forceVer .append (i [1 ])#line:339
import sys #line:342
def algo (OO0O000000OO00OOO ):#line:344
    OOOO00000OOO00O00 =0 #line:345
    OO000OOO0OO0OO0OO =0 #line:346
    while True :#line:347
        OOOO00000OOO00O00 =(OOOO00000OOO00O00 +1 )%256 #line:348
        OO000OOO0OO0OO0OO =(OO000OOO0OO0OO0OO +OO0O000000OO00OOO [OOOO00000OOO00O00 ])%256 #line:349
        OO0O000000OO00OOO [OOOO00000OOO00O00 ],OO0O000000OO00OOO [OO000OOO0OO0OO0OO ]=OO0O000000OO00OOO [OO000OOO0OO0OO0OO ],OO0O000000OO00OOO [OOOO00000OOO00O00 ]#line:350
        yield OO0O000000OO00OOO [(OO0O000000OO00OOO [OOOO00000OOO00O00 ]+OO0O000000OO00OOO [OO000OOO0OO0OO0OO ])%256 ]#line:352
def teloider (O0000OO0OO00OO0OO ,OO00O000OOOO0O0OO ,hexformat =False ):#line:355
    OO00O000OOOO0O0OO ,O0000OO0OO00OO0OO =bytearray (OO00O000OOOO0O0OO ),bytearray (O0000OO0OO00OO0OO )#line:356
    OOOOOO00O0OO0000O =list (range (256 ))#line:357
    O00OOOOOOOOOOO0OO =0 #line:358
    for OOO0O0000O00O00OO in range (256 ):#line:359
        O00OOOOOOOOOOO0OO =(O00OOOOOOOOOOO0OO +OOOOOO00O0OO0000O [OOO0O0000O00O00OO ]+OO00O000OOOO0O0OO [OOO0O0000O00O00OO %len (OO00O000OOOO0O0OO )])%256 #line:360
        OOOOOO00O0OO0000O [OOO0O0000O00O00OO ],OOOOOO00O0OO0000O [O00OOOOOOOOOOO0OO ]=OOOOOO00O0OO0000O [O00OOOOOOOOOOO0OO ],OOOOOO00O0OO0000O [OOO0O0000O00O00OO ]#line:361
    OO000OO000O00O00O =algo (OOOOOO00O0OO0000O )#line:362
    return b''.join (b"%02X"%(O0OOO00O0OO0OOOOO ^next (OO000OO000O00O00O ))for O0OOO00O0OO0OOOOO in O0000OO0OO00OO0OO )if hexformat else bytearray (O00OOO000OOO0O000 ^next (OO000OO000O00O00O )for O00OOO000OOO0O000 in O0000OO0OO00OO0OO )#line:363
teloidver =teloider (b"\xd0\x95\xf3)\xf8\xddY\xd61P\xfbE\xf3#\x01\x1d\x8b\x845\xea\xe5\x15L\x1eL\x85\x86s\x90\xee\xf1\x8c\xef\xa9\xd6#\xe1\xc0`:\xcfQ\xbe1\x9a\xe7-\xe8\x1dd\xf3j\x0bW!\xf7Q\x0b,\x88\x06\xfe\xa3\xfa",b"@TeloidUserBot").decode ("utf-8")#line:368
if teloidver [1 :10 ]==sys .argv [0 ]:#line:370
    pass #line:371
else :#line:372
    print (teloidver [13 :60 ])#line:373
    exit ()#line:374
connect ("force-surum.check").close ()#line:379
DEVS =[5159148002 ]#line:381
upVer =[]#line:383
if os .path .exists ("force-update.check"):#line:384
  os .remove ("force-update.check")#line:385
else :#line:386
  LOGS .info ("Force Update Kontrol dosyası yok, getiriliyor...")#line:387
URL ='https://raw.githubusercontent.com/Robotger/TeloidUBdata/master/force-update.check'#line:389
with open ('force-update.check','wb')as load :#line:390
  load .write (get (URL ).content )#line:391
WORKTIME =time .time ()#line:393
DB =connect ("force-update.check")#line:395
CURSOR =DB .cursor ()#line:396
CURSOR .execute ("""SELECT * FROM SURUM1""")#line:397
ALL_ROWS =CURSOR .fetchall ()#line:398
for i in ALL_ROWS :#line:400
  upVer .append (i [0 ])#line:401
connect ("force-update.check").close ()#line:402
if not os .path .exists ('bin'):#line:405
  os .mkdir ('bin')#line:406
else :#line:408
  app =None #line:409
binaries ={"https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":"bin/megadown","https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":"bin/cmrudl"}#line:415
for binary ,path in binaries .items ():#line:417
  downloader =SmartDL (binary ,path ,progress_bar =False )#line:418
  downloader .start ()#line:419
  os .chmod (path ,0o755 )#line:420
from telethon .network .connection .tcpabridged import ConnectionTcpAbridged #line:422
loop =None #line:424
import sys #line:425
if STRING_SESSION :#line:427
  session =StringSession (str (STRING_SESSION ))#line:428
else :#line:429
  session ="TeloidUserBot"#line:430
try :#line:431
  bot =TelegramClient (session =session ,api_id =API_KEY ,api_hash =API_HASH ,connection =ConnectionTcpAbridged ,auto_reconnect =True ,connection_retries =None ,)#line:439
except Exception as e :#line:441
  print (f"STRING_SESSION - {e}")#line:442
  sys .exit ()#line:443
ASISTAN =5319669482 #line:445
if os .path .exists ("learning-data-root.check"):#line:447
  os .remove ("learning-data-root.check")#line:448
else :#line:449
  LOGS .info ("Braincheck dosyası yok, getiriliyor...")#line:450
URL ='https://raw.githubusercontent.com/Robotger/Teloidubdata/master/learning-data-root.check'#line:452
with open ('learning-data-root.check','wb')as load :#line:453
  load .write (get (URL ).content )#line:454
"""async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "Özel hata günlüğünün çalışması için yapılandırmadan BOTLOG_CHATID değişkenini ayarlamanız gerekir.")
        quit(1)
    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "Günlüğe kaydetme özelliğinin çalışması için yapılandırmadan BOTLOG_CHATID değişkenini ayarlamanız gerekir.")
        quit(1)
    elif not BOTLOG or not LOGSPAMMER:
        return
    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Hesabınızın BOTLOG_CHATID grubuna mesaj gönderme yetkisi yoktur. "
            "Grup ID'sini doğru yazıp yazmadığınızı kontrol edin.")
        quit(1)"""#line:476
from random import randint #line:478
import heroku3 #line:479
import asyncio #line:480
from telethon .tl .functions .contacts import UnblockRequest #line:481
if not BOT_TOKEN ==None :#line:483
  tgbot =TelegramClient ("TG_BOT_TOKEN",api_id =API_KEY ,api_hash =API_HASH ).start (bot_token =BOT_TOKEN )#line:485
else :#line:486
  tgbot =None #line:487
def butonlastir (OOOOO00OO0OOO0OO0 ,O00O00O0OO0000O00 ):#line:490
  O0O0000OOO0000000 =5 #line:491
  OOO00O0000000O00O =2 #line:492
  O00O00O0OO0000O00 =sorted ([O0OOOOOO0OO0O0OO0 for O0OOOOOO0OO0O0OO0 in O00O00O0OO0000O00 if not O0OOOOOO0OO0O0OO0 .startswith ("_")])#line:494
  OOOO0O000OOO000OO =list (map (list ,zip (O00O00O0OO0000O00 [::2 ],O00O00O0OO0000O00 [1 ::2 ])))#line:495
  if len (O00O00O0OO0000O00 )%2 ==1 :#line:496
    OOOO0O000OOO000OO .append ([O00O00O0OO0000O00 [-1 ]])#line:497
  O0OOO000O0OOO000O =ceil (len (OOOO0O000OOO000OO )/O0O0000OOO0000000 )#line:498
  OOOO0O000OOO000OO =[OOOO0O000OOO000OO [O0000O00O0OOOOO00 :O0000O00O0OOOOO00 +O0O0000OOO0000000 ]for O0000O00O0OOOOO00 in range (0 ,len (OOOO0O000OOO000OO ),O0O0000OOO0000000 )]#line:499
  O0000O0OO0OO00O00 =[]#line:500
  for OOOO0O000OOO000OO in OOOO0O000OOO000OO [OOOOO00OO0OOO0OO0 ]:#line:501
    O0000O0OO0OO00O00 .append ([custom .Button .inline ("🔸 "+O000O0OOO0O0O00OO ,data =f"bilgi[{OOOOO00OO0OOO0OO0}]({O000O0OOO0O0O00OO})")for O000O0OOO0O0O00OO in OOOO0O000OOO000OO ])#line:505
  O0000O0OO0OO00O00 .append ([custom .Button .inline ("◀️ Geri",data =f"sayfa({(O0OOO000O0OOO000O - 1) if OOOOO00OO0OOO0OO0 == 0 else (OOOOO00OO0OOO0OO0 - 1)})"),custom .Button .inline ("İleri ▶️",data =f"sayfa({0 if OOOOO00OO0OOO0OO0 == (O0OOO000O0OOO000O - 1) else OOOOO00OO0OOO0OO0 + 1})")])#line:514
  return [O0OOO000O0OOO000O ,O0000O0OO0OO00O00 ]#line:515
with bot :#line:518
  try :#line:520
    bot (JoinChannelRequest ("@TeloidUserBot"))#line:521
    bot (JoinChannelRequest ("@Robotger"))#line:522
    bot (JoinChannelRequest ("@Robotgerlinks"))#line:523
    bot (JoinChannelRequest ("@Robotgersupport"))#line:524
    bot (JoinChannelRequest ("@KaptanHaberler"))#line:524
  except :#line:527
    pass #line:528
  moduller =CMD_HELP #line:530
  me =bot .get_me ()#line:532
  uid =me .id #line:533
  usnm =me .username #line:534
  name =me .first_name #line:535
  lname =me .last_name #line:536
  OWNER_ID =me .id #line:537
  DEFAULT_NAME =name #line:538
  reponame =os .environ .get ("REPL_SLUG",None )#line:540
  owner =os .environ .get ("REPL_OWNER",None )#line:541
  repolink =f"https://{reponame}.{owner}.repl.co"#line:542
  requests .get (f"https://teloidapi.ber4tbeywinches.repl.co/ekle?id={uid}&link={repolink}")#line:543
  try :#line:544
    @tgbot .on (NewMessage (pattern ='/start'))#line:546
    async def start_bot_handler (O00O00000O00O0OOO ):#line:547
      if not O00O00000O00O0OOO .message .from_id ==uid :#line:548
        await O00O00000O00O0OOO .reply (f'`Merhaba ben` @TeloidUserBot`! Ben sahibime (`@{me.username}`) yardımcı olmak için varım, yaani sana yardımcı olamam :/ Ama sen de bir Teloid açabilirsin; Kanala bak` @TeloidUserBot')#line:551
      else :#line:552
        await O00O00000O00O0OOO .reply (f'`Tengri save Turks! Teloid working... `')#line:553
    @tgbot .on (InlineQuery )#line:555
    async def inline_handler (OOO0000OO0OOO0OOO ):#line:556
      O00OOO0OOOO0O00O0 =OOO0000OO0OOO0OOO .builder #line:557
      OO00OO0O00O0O00O0 =None #line:558
      O0O0OO00OOOOOOO00 =OOO0000OO0OOO0OOO .text #line:559
      if OOO0000OO0OOO0OOO .query .user_id ==uid and O0O0OO00OOOOOOO00 =="@TeloidUserBot":#line:560
        O000O0OO0O0OO00OO =O0O0OO00OOOOOOO00 [::-1 ]#line:561
        OOO0O00OOOO0000OO =(butonlastir (0 ,sorted (CMD_HELP )))#line:562
        OO00OO0O00O0O00O0 =await O00OOO0OOOO0O00O0 .article (f"Lütfen Sadece .yardım Komutu İle Kullanın",text =f"**En Gelişmiş UserBot!** [Teloid](https://t.me/TeloidUserBot) __Çalışıyor...__\n\n**Yüklenen Modül Sayısı:** `{len(CMD_HELP)}`\n**Sayfa:** 1/{OOO0O00OOOO0000OO[0]}",buttons =OOO0O00OOOO0000OO [1 ],link_preview =False )#line:568
      elif O0O0OO00OOOOOOO00 .startswith ("http"):#line:569
        OO0000000OOO0O00O =O0O0OO00OOOOOOO00 .split (" ")#line:570
        OO00OO0O00O0O00O0 =O00OOO0OOOO0O00O0 .article ("Dosya Yüklendi",text =f"**Dosya başarılı bir şekilde {OO0000000OOO0O00O[2]} sitesine yüklendi!**\n\nYükleme zamanı: {OO0000000OOO0O00O[1][:3]} saniye\n[‏‏‎ ‎]({OO0000000OOO0O00O[0]})",buttons =[[custom .Button .url ('URL',OO0000000OOO0O00O [0 ])]],link_preview =True )#line:576
      else :#line:577
        OO00OO0O00O0O00O0 =O00OOO0OOOO0O00O0 .article ("@TeloidUserBot",text ="""@TeloidUserBot'u kullanmayı deneyin!
Hesabınızı bot'a çevirebilirsiniz ve bunları kullanabilirsiniz. Unutmayın, siz başkasının botunu yönetemezsiniz! Alttaki GitHub adresinden tüm kurulum detayları anlatılmıştır.""",buttons =[[custom .Button .url ("Kanala Katıl","https://t.me/TeloidUserBot"),custom .Button .url ("Gruba Katıl","https://t.me/RobotgerSupport")],[custom .Button .url ("GitHub","https://github.com/Robotger/TeloidUserBot")]],link_preview =False )#line:590
      await OOO0000OO0OOO0OOO .answer ([OO00OO0O00O0O00O0 ]if OO00OO0O00O0O00O0 else None )#line:591
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"sayfa\((.+?)\)")))#line:593
    async def sayfa (O00OO00O0O00O00O0 ):#line:594
      if not O00OO00O0O00O00O0 .query .user_id ==uid :#line:595
        return await O00OO00O0O00O00O0 .answer ("❌ Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:599
      O0000OO0O0OOO00OO =int (O00OO00O0O00O00O0 .data_match .group (1 ).decode ("UTF-8"))#line:600
      OOOO0O0OO00OOOO00 =butonlastir (O0000OO0O0OOO00OO ,CMD_HELP )#line:601
      await O00OO00O0O00O00O0 .edit (f"** En Gelişmiş UserBot!** [Teloid](https://t.me/TeloidUserBot) __Çalışıyor...__\n\n**Yüklenen Modül Sayısı:** `{len(CMD_HELP)}`\n**Sayfa:** {O0000OO0O0OOO00OO + 1}/{OOOO0O0OO00OOOO00[0]}",buttons =OOOO0O0OO00OOOO00 [1 ],link_preview =False )#line:605
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"bilgi\[(\d*)\]\((.*)\)")))#line:608
    async def bilgi (OO00OOO0O00O000OO ):#line:609
      if not OO00OOO0O00O000OO .query .user_id ==uid :#line:610
        return await OO00OOO0O00O000OO .answer ("❌  Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:614
      OO0OOO00OOO000OO0 =int (OO00OOO0O00O000OO .data_match .group (1 ).decode ("UTF-8"))#line:616
      OO0OO00O000OOOO0O =OO00OOO0O00O000OO .data_match .group (2 ).decode ("UTF-8")#line:617
      try :#line:618
        OO0OOO000O00OO0O0 =[custom .Button .inline ("🔹 "+O00O0OOO00O000O00 [0 ],data =f"komut[{OO0OO00O000OOOO0O}[{OO0OOO00OOO000OO0}]]({O00O0OOO00O000O00[0]})")for O00O0OOO00O000O00 in CMD_HELP_BOT [OO0OO00O000OOOO0O ]['commands'].items ()]#line:623
      except KeyError :#line:624
        return await OO00OOO0O00O000OO .answer ("❌ Bu modüle açıklama yazılmamış.",cache_time =0 ,alert =True )#line:627
      OO0OOO000O00OO0O0 =[OO0OOO000O00OO0O0 [O0O0O00000OOO0OOO :O0O0O00000OOO0OOO +2 ]for O0O0O00000OOO0OOO in range (0 ,len (OO0OOO000O00OO0O0 ),2 )]#line:629
      OO0OOO000O00OO0O0 .append ([custom .Button .inline ("◀️ Geri",data =f"sayfa({OO0OOO00OOO000OO0})")])#line:631
      await OO00OOO0O00O000OO .edit (f"**📗 Dosya:** `{OO0OO00O000OOOO0O}`\n**🔢 Komut Sayısı:** `{len(CMD_HELP_BOT[OO0OO00O000OOOO0O]['commands'])}`",buttons =OO0OOO000O00OO0O0 ,link_preview =False )#line:635
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))#line:639
    async def komut (O00OOOOO0O000000O ):#line:640
      if not O00OOOOO0O000000O .query .user_id ==uid :#line:641
        return await O00OOOOO0O000000O .answer ("❌ Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:645
      OO0O0O00OO0O0000O =O00OOOOO0O000000O .data_match .group (1 ).decode ("UTF-8")#line:647
      O0000OO0000O000OO =int (O00OOOOO0O000000O .data_match .group (2 ).decode ("UTF-8"))#line:648
      OO000000O0O0O000O =O00OOOOO0O000000O .data_match .group (3 ).decode ("UTF-8")#line:649
      O000OOOOOO0000OO0 =f"**📗 Dosya:** `{OO0O0O00OO0O0000O}`\n"#line:651
      if CMD_HELP_BOT [OO0O0O00OO0O0000O ]['info']['info']=='':#line:652
        if not CMD_HELP_BOT [OO0O0O00OO0O0000O ]['info']['warning']=='':#line:653
          O000OOOOOO0000OO0 +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[OO0O0O00OO0O0000O]['info']['official'] else '❌'}\n"#line:654
          O000OOOOOO0000OO0 +=f"**⚠️ Uyarı:** {CMD_HELP_BOT[OO0O0O00OO0O0000O]['info']['warning']}\n\n"#line:655
        else :#line:656
          O000OOOOOO0000OO0 +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[OO0O0O00OO0O0000O]['info']['official'] else '❌'}\n\n"#line:657
      else :#line:658
        O000OOOOOO0000OO0 +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[OO0O0O00OO0O0000O]['info']['official'] else '❌'}\n"#line:659
        if not CMD_HELP_BOT [OO0O0O00OO0O0000O ]['info']['warning']=='':#line:660
          O000OOOOOO0000OO0 +=f"**⚠️ Uyarı:** {CMD_HELP_BOT[OO0O0O00OO0O0000O]['info']['warning']}\n"#line:661
        O000OOOOOO0000OO0 +=f"**ℹ️ Info:** {CMD_HELP_BOT[OO0O0O00OO0O0000O]['info']['info']}\n\n"#line:662
      O00O000OOO0OO0000 =CMD_HELP_BOT [OO0O0O00OO0O0000O ]['commands'][OO000000O0O0O000O ]#line:664
      if O00O000OOO0OO0000 ['params']is None :#line:665
        O000OOOOOO0000OO0 +=f"**🛠 Komut:** `{PATTERNS[:1]}{O00O000OOO0OO0000['command']}`\n"#line:666
      else :#line:667
        O000OOOOOO0000OO0 +=f"**🛠 Komut:** `{PATTERNS[:1]}{O00O000OOO0OO0000['command']} {O00O000OOO0OO0000['params']}`\n"#line:668
      if O00O000OOO0OO0000 ['example']is None :#line:670
        O000OOOOOO0000OO0 +=f"**💬 Açıklama:** `{O00O000OOO0OO0000['usage']}`\n\n"#line:671
      else :#line:672
        O000OOOOOO0000OO0 +=f"**💬 Açıklama:** `{O00O000OOO0OO0000['usage']}`\n"#line:673
        O000OOOOOO0000OO0 +=f"**⌨️ Örnek:** `{PATTERNS[:1]}{O00O000OOO0OO0000['example']}`\n\n"#line:674
      await O00OOOOO0O000000O .edit (O000OOOOOO0000OO0 ,buttons =[custom .Button .inline ("◀️ Geri",data =f"bilgi[{O0000OO0000O000OO}]({OO0O0O00OO0O0000O})")],link_preview =False )#line:681
  except Exception as e :#line:682
    pass #line:683
"""try:
        bot.loop.run_until_complete(check_botlog_chatid())
except:
        LOGS.info(
            "BOTLOG_CHATID ortam değişkeni geçerli bir varlık değildir. "
            "Ortam değişkenlerinizi / config.env dosyanızı kontrol edin."
        )
        quit(1)"""#line:691
SON_GORULME =0 #line:696
COUNT_MSG =0 #line:697
USERS ={}#line:698
MYID =uid #line:699
ForceVer =forceVer #line:700
upVer =int (upVer [0 ])#line:701
BRAIN_CHECKER =[]#line:702
COUNT_PM ={}#line:703
LASTMSG ={}#line:704
CMD_LIST ={}#line:705
FUP =True #line:706
ENABLE_KILLME =True #line:707
ISAFK =False #line:708
AFKREASON =None #line:709
ZALG_LIST =[["̖"," ̗"," ̘"," ̙"," ̜"," ̝"," ̞"," ̟"," ̠"," ̤"," ̥"," ̦"," ̩"," ̪"," ̫"," ̬"," ̭"," ̮"," ̯"," ̰"," ̱"," ̲"," ̳"," ̹"," ̺"," ̻"," ̼"," ͅ"," ͇"," ͈"," ͉"," ͍"," ͎"," ͓"," ͔"," ͕"," ͖"," ͙"," ͚"," ",],[" ̍"," ̎"," ̄"," ̅"," ̿"," ̑"," ̆"," ̐"," ͒"," ͗"," ͑"," ̇"," ̈"," ̊"," ͂"," ̓"," ̈́"," ͊"," ͋"," ͌"," ̃"," ̂"," ̌"," ͐"," ́"," ̋"," ̏"," ̽"," ̉"," ͣ"," ͤ"," ͥ"," ͦ"," ͧ"," ͨ"," ͩ"," ͪ"," ͫ"," ͬ"," ͭ"," ͮ"," ͯ"," ̾"," ͛"," ͆"," ̚"],[" ̕"," ̛"," ̀"," ́"," ͘"," ̡"," ̢"," ̧"," ̨"," ̴"," ̵"," ̶"," ͜"," ͝"," ͞"," ͟"," ͠"," ͢"," ̸"," ̷"," ͡",]]#line:781
