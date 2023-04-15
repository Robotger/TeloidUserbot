""#line:8
from telethon .errors import ChannelPrivateError #line:9
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
 if KURULUM ==None :#line:49
  os .system ("python GenerateStringSession.py")#line:50
  print ("İlk Kurulum tamamlandı STRING_SESSION İsimli Secret oluşturduktan sonra Lütfen yeniden başlatın!!")#line:53
  exit ()#line:54
else :#line:55
  pass #line:56
StartTime =time .time ()#line:58
CONSOLE_LOGGER_VERBOSE =sb (os .environ .get ("CONSOLE_LOGGER_VERBOSE","False"))#line:61
ASYNC_POOL =[]#line:63
if CONSOLE_LOGGER_VERBOSE :#line:65
  basicConfig (level =DEBUG ,format ="[%(asctime)s - %(levelname)s] - @TeloidUserBot : %(message)s",datefmt ='%d-%b-%y %H:%M:%S')#line:69
else :#line:70
  basicConfig (level =INFO ,format ="[%(asctime)s - %(levelname)s] - @TeloidUserBot : %(message)s",datefmt ='%d-%b-%y %H:%M:%S')#line:74
LOGS =getLogger (__name__ )#line:75
if version_info [0 ]<3 or version_info [1 ]<6 :#line:77
  LOGS .info ("En az python 3.6 sürümüne sahip olmanız gerekir." "Birden fazla özellik buna bağlıdır. Bot kapatılıyor.")#line:79
  quit (1 )#line:80
branch ="master"#line:81
CONFIG_CHECK =os .environ .get ("___________LUTFEN_______BU_____SATIRI_____SILIN__________",None )#line:85
if CONFIG_CHECK :#line:87
  LOGS .info ("Lütfen ilk hashtag'de belirtilen satırı config.env dosyasından kaldırın")#line:89
  quit (1 )#line:90
LANGUAGE =os .environ .get ("LANGUAGE","DEFAULT").upper ()#line:93
if not LANGUAGE in ["EN","TR","AZ","UZ","DEFAULT"]:#line:95
  LOGS .info ("Bilinmeyen bir dil yazdınız. Bundan dolayı DEFAULT kullanılıyor.")#line:96
  LANGUAGE ="DEFAULT"#line:97
TELOID_VERSION ="v0.2"#line:100
MAX_MESSAGE_SIZE_LIMIT =4095 #line:102
API_KEY =os .environ .get ("API_KEY",None )#line:104
API_HASH =os .environ .get ("API_HASH",None )#line:105
SEVGILI =os .environ .get ("SEVGILI",None )#line:107
async def get_call (O0OOOOO00O00O0OO0 ):#line:111
  O0OOO0O0O00O000OO =await O0OOOOO00O00O0OO0 .client (getchat (O0OOOOO00O00O0OO0 .chat_id ))#line:112
  OO0OOOOOOO00O000O =await O0OOOOO00O00O0OO0 .client (getvc (O0OOO0O0O00O000OO .full_chat .call ))#line:113
  return OO0OOOOOOO00O000O .call #line:114
SUDO_HANDLER =os .environ .get ("SUDO_HANDLER",r".")#line:118
try :#line:119
  SUDO_USERS =set (int (O00OOOO0OO0O0O000 )for O00OOOO0OO0O0O000 in os .environ .get ("SUDO_USERS","").split ())#line:120
except ValueError :#line:121
  raise Exception ("Bir Kullanıcı İd si Belirtmek zorundasın.")#line:122
SILINEN_PLUGIN ={}#line:124
BOTLOG_CHATID =int (os .environ .get ("BOTLOG_CHATID",0 ))#line:128
BOTLOG =sb (os .environ .get ("BOTLOG","False"))#line:131
LOGSPAMMER =sb (os .environ .get ("LOGSPAMMER","False"))#line:133
PM_AUTO_BAN =sb (os .environ .get ("PM_AUTO_BAN","False"))#line:136
HEROKU_MEMEZ =sb (os .environ .get ("HEROKU_MEMEZ","False"))#line:139
HEROKU_APPNAME =os .environ .get ("HEROKU_APPNAME",None )#line:140
HEROKU_APIKEY =os .environ .get ("HEROKU_APIKEY",None )#line:141
EZZEC =False #line:143
Heroku =None #line:144
app =None #line:145
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None :#line:147
  if EZZEC ==True :#line:148
    pass #line:149
  else :#line:150
    EZZEC =True #line:151
    Heroku =heroku3 .from_key (HEROKU_APIKEY )#line:152
    app =Heroku .app (HEROKU_APPNAME )#line:153
    heroku_var =app .config ()#line:154
    heroku_var ["UPSTREAM_REPO_URL"]="https://github.com/Robotger/TeloidUserBot.git"#line:156
else :#line:157
  app =None #line:158
try :#line:160
  import randomstuff #line:161
except ModuleNotFoundError :#line:162
  install_pip ("randomstuff.py")#line:163
  import randomstuff #line:164
RANDOM_STUFF_API_KEY =os .environ .get ("RANDOM_STUFF_API_KEY",None )#line:167
if RANDOM_STUFF_API_KEY :#line:168
  try :#line:169
    rs_client =randomstuff .AsyncClient (api_key =RANDOM_STUFF_API_KEY ,version ="4")#line:171
  except :#line:172
    print ('Invalid RANDOM_STUFF_API_KEY')#line:173
    rs_client =None #line:174
else :#line:175
  rs_client =None #line:176
AI_LANG =os .environ .get ("AI_LANG",'en')#line:177
STABILITY =sb (os .environ .get ("STABILITY","True"))#line:180
UPSTREAM_REPO_URL ="https://github.com/Robotger/TeloidUserBot.git"#line:182
EMERGENCY ="https://github.com/Robotger/TeloidUserBot.git"#line:183
AFKILETME =sb (os .environ .get ("AFKILETME","True"))#line:185
DB_URI =os .environ .get ("DATABASE_URL","sqlite:///teloid.db")#line:188
OCR_SPACE_API_KEY =os .environ .get ("OCR_SPACE_API_KEY",None )#line:191
REM_BG_API_KEY =os .environ .get ("REM_BG_API_KEY",None )#line:194
AUTO_PP =os .environ .get ("AUTO_PP",None )#line:197
SUDO_ID =set (int (OOO0OOOO000O0000O )for OOO0OOOO000O0000O in os .environ .get ("SUDO_ID","").split ())#line:199
WARN_LIMIT =int (os .environ .get ("WARN_LIMIT",3 ))#line:203
WARN_MODE =os .environ .get ("WARN_MODE","gmute")#line:204
if not WARN_MODE in ["gmute","gban"]:#line:206
  WARN_MODE ="gmute"#line:207
GALERI_SURE =int (os .environ .get ("GALERI_SURE",60 ))#line:210
CHROME_DRIVER =os .environ .get ("CHROME_DRIVER",None )#line:213
GOOGLE_CHROME_BIN =os .environ .get ("GOOGLE_CHROME_BIN",None )#line:214
WORKTIME =time .time ()#line:217
PLUGINID =os .environ .get ("PLUGIN_CHANNEL_ID",None )#line:219
if not PLUGINID :#line:221
  PLUGIN_CHANNEL_ID ="me"#line:222
else :#line:223
  PLUGIN_CHANNEL_ID =int (PLUGINID )#line:224
OPEN_WEATHER_MAP_APPID =os .environ .get ("OPEN_WEATHER_MAP_APPID",None )#line:227
WEATHER_DEFCITY =os .environ .get ("WEATHER_DEFCITY",None )#line:228
ANTI_SPAMBOT =sb (os .environ .get ("ANTI_SPAMBOT","False"))#line:231
ANTI_SPAMBOT_SHOUT =sb (os .environ .get ("ANTI_SPAMBOT_SHOUT","True"))#line:232
YOUTUBE_API_KEY =os .environ .get ("YOUTUBE_API_KEY",None )#line:235
COUNTRY =str (os .environ .get ("COUNTRY",""))#line:238
TZ_NUMBER =int (os .environ .get ("TZ_NUMBER",1 ))#line:239
CLEAN_WELCOME =sb (os .environ .get ("CLEAN_WELCOME","True"))#line:242
BIO_PREFIX =os .environ .get ("BIO_PREFIX","@TeloidUserBot | ")#line:245
LASTFM_API =os .environ .get ("LASTFM_API",None )#line:248
LASTFM_SECRET =os .environ .get ("LASTFM_SECRET",None )#line:249
LASTFM_USERNAME =os .environ .get ("LASTFM_USERNAME",None )#line:250
LASTFM_PASSWORD_PLAIN =os .environ .get ("LASTFM_PASSWORD",None )#line:251
LASTFM_PASS =md5 (LASTFM_PASSWORD_PLAIN )#line:252
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS :#line:253
  lastfm =LastFMNetwork (api_key =LASTFM_API ,api_secret =LASTFM_SECRET ,username =LASTFM_USERNAME ,password_hash =LASTFM_PASS )#line:257
else :#line:258
  lastfm =None #line:259
G_DRIVE_CLIENT_ID =os .environ .get ("G_DRIVE_CLIENT_ID",None )#line:262
G_DRIVE_CLIENT_SECRET =os .environ .get ("G_DRIVE_CLIENT_SECRET",None )#line:263
G_DRIVE_AUTH_TOKEN_DATA =os .environ .get ("G_DRIVE_AUTH_TOKEN_DATA",None )#line:264
GDRIVE_FOLDER_ID =os .environ .get ("GDRIVE_FOLDER_ID",None )#line:265
TEMP_DOWNLOAD_DIRECTORY =os .environ .get ("TMP_DOWNLOAD_DIRECTORY","./downloads")#line:267
DEFAULT_BIO =os .environ .get ("DEFAULT_BIO",None )#line:270
USERBOT_ =True #line:273
BOT_TOKEN =os .environ .get ("BOT_TOKEN",None )#line:276
BOT_USERNAME =os .environ .get ("BOT_USERNAME",None )#line:277
GENIUS =os .environ .get ("GENIUS",None )#line:280
CMD_HELP ={}#line:282
CMD_HELP_BOT ={}#line:283
PM_AUTO_BAN_LIMIT =int (os .environ .get ("PM_AUTO_BAN_LIMIT",4 ))#line:285
SPOTIFY_DC =os .environ .get ("SPOTIFY_DC",None )#line:287
SPOTIFY_KEY =os .environ .get ("SPOTIFY_KEY",None )#line:288
PAKET_ISMI =os .environ .get ("PAKET_ISMI","| 🌃 @TeloidUserBot Paketi |")#line:290
BLACKLIST_CHAT =[1698661722 ]#line:294
OTOMATIK_KATILMA =sb (os .environ .get ("OTOMATIK_KATILMA","True"))#line:297
AUTO_UPDATE =sb (os .environ .get ("AUTO_UPDATE","True"))#line:298
PATTERNS =os .environ .get ("PATTERNS",".;!,")#line:301
WHITELIST =get ('https://raw.githubusercontent.com/Robotger/Teloidubdata/master/whitelist.json').json ()#line:304
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None :#line:306
  Heroku =heroku3 .from_key (HEROKU_APIKEY )#line:307
  app =Heroku .app (HEROKU_APPNAME )#line:308
  heroku_var =app .config ()#line:309
forceVer =[]#line:312
if os .path .exists ("force-surum.check"):#line:313
  os .remove ("force-surum.check")#line:314
else :#line:315
  LOGS .info ("Force Sürüm Kontrol dosyası yok, getiriliyor...")#line:316
URL ='https://raw.githubusercontent.com/Robotger/TeloidUbdata/master/force-surum.check'#line:318
with open ('force-surum.check','wb')as load :#line:319
  load .write (get (URL ).content )#line:320
DB =connect ("force-surum.check")#line:322
CURSOR =DB .cursor ()#line:323
CURSOR .execute ("""SELECT * FROM SURUM1""")#line:324
ALL_ROWS =CURSOR .fetchall ()#line:325
for i in ALL_ROWS :#line:327
  forceVer .append (i [0 ])#line:328
  forceVer .append (i [1 ])#line:329
import sys #line:332
def algo (O0O000OOOOOOO0OO0 ):#line:334
    O0O0O0O00O00O00O0 =0 #line:335
    OO0OO00O0OO0OO00O =0 #line:336
    while True :#line:337
        O0O0O0O00O00O00O0 =(O0O0O0O00O00O00O0 +1 )%256 #line:338
        OO0OO00O0OO0OO00O =(OO0OO00O0OO0OO00O +O0O000OOOOOOO0OO0 [O0O0O0O00O00O00O0 ])%256 #line:339
        O0O000OOOOOOO0OO0 [O0O0O0O00O00O00O0 ],O0O000OOOOOOO0OO0 [OO0OO00O0OO0OO00O ]=O0O000OOOOOOO0OO0 [OO0OO00O0OO0OO00O ],O0O000OOOOOOO0OO0 [O0O0O0O00O00O00O0 ]#line:340
        yield O0O000OOOOOOO0OO0 [(O0O000OOOOOOO0OO0 [O0O0O0O00O00O00O0 ]+O0O000OOOOOOO0OO0 [OO0OO00O0OO0OO00O ])%256 ]#line:342
def teloider (OO00000O0O00OOO00 ,OO0OO0000000OOOO0 ,hexformat =False ):#line:345
    OO0OO0000000OOOO0 ,OO00000O0O00OOO00 =bytearray (OO0OO0000000OOOO0 ),bytearray (OO00000O0O00OOO00 )#line:346
    O0O00000OOO0OO000 =list (range (256 ))#line:347
    OOO0OO00OO000OOOO =0 #line:348
    for O00O0000O0OO00O0O in range (256 ):#line:349
        OOO0OO00OO000OOOO =(OOO0OO00OO000OOOO +O0O00000OOO0OO000 [O00O0000O0OO00O0O ]+OO0OO0000000OOOO0 [O00O0000O0OO00O0O %len (OO0OO0000000OOOO0 )])%256 #line:350
        O0O00000OOO0OO000 [O00O0000O0OO00O0O ],O0O00000OOO0OO000 [OOO0OO00OO000OOOO ]=O0O00000OOO0OO000 [OOO0OO00OO000OOOO ],O0O00000OOO0OO000 [O00O0000O0OO00O0O ]#line:351
    O00OO00O00OO0000O =algo (O0O00000OOO0OO000 )#line:352
    return b''.join (b"%02X"%(O0O00OO0000O0O00O ^next (O00OO00O00OO0000O ))for O0O00OO0000O0O00O in OO00000O0O00OOO00 )if hexformat else bytearray (OO0O00OOOO0OOOOOO ^next (O00OO00O00OO0000O )for OO0O00OOOO0OOOOOO in OO00000O0O00OOO00 )#line:353
teloidver =teloider (b"\xd0\x95\xf3)\xf8\xddY\xd61P\xfbE\xf3#\x01\x1d\x8b\x845\xea\xe5\x15L\x1eL\x85\x86s\x90\xee\xf1\x8c\xef\xa9\xd6#\xe1\xc0`:\xcfQ\xbe1\x9a\xe7-\xe8\x1dd\xf3j\x0bW!\xf7Q\x0b,\x88\x06\xfe\xa3\xfa",b"@TeloidUserBot").decode ("utf-8")#line:358
if teloidver [1 :10 ]==sys .argv [0 ]:#line:360
    pass #line:361
else :#line:362
    print (teloidver [13 :60 ])#line:363
    exit ()#line:364
connect ("force-surum.check").close ()#line:369
DEVS =[5159148002 ]#line:371
upVer =[]#line:373
if os .path .exists ("force-update.check"):#line:374
  os .remove ("force-update.check")#line:375
else :#line:376
  LOGS .info ("Force Update Kontrol dosyası yok, getiriliyor...")#line:377
URL ='https://raw.githubusercontent.com/Robotger/TeloidUBdata/master/force-update.check'#line:379
with open ('force-update.check','wb')as load :#line:380
  load .write (get (URL ).content )#line:381
WORKTIME =time .time ()#line:383
DB =connect ("force-update.check")#line:385
CURSOR =DB .cursor ()#line:386
CURSOR .execute ("""SELECT * FROM SURUM1""")#line:387
ALL_ROWS =CURSOR .fetchall ()#line:388
for i in ALL_ROWS :#line:390
  upVer .append (i [0 ])#line:391
connect ("force-update.check").close ()#line:392
if not os .path .exists ('bin'):#line:395
  os .mkdir ('bin')#line:396
else :#line:398
  app =None #line:399
binaries ={"https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":"bin/megadown","https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":"bin/cmrudl"}#line:405
for binary ,path in binaries .items ():#line:407
  downloader =SmartDL (binary ,path ,progress_bar =False )#line:408
  downloader .start ()#line:409
  os .chmod (path ,0o755 )#line:410
from telethon .network .connection .tcpabridged import ConnectionTcpAbridged #line:412
loop =None #line:414
import sys #line:415
if STRING_SESSION :#line:417
  session =StringSession (str (STRING_SESSION ))#line:418
else :#line:419
  session ="TeloidUserBot"#line:420
try :#line:421
  bot =TelegramClient (session =session ,api_id =API_KEY ,api_hash =API_HASH ,connection =ConnectionTcpAbridged ,auto_reconnect =True ,connection_retries =None ,)#line:429
except Exception as e :#line:431
  print (f"STRING_SESSION - {e}")#line:432
  sys .exit ()#line:433
ASISTAN =5319669482 #line:435
if os .path .exists ("learning-data-root.check"):#line:437
  os .remove ("learning-data-root.check")#line:438
else :#line:439
  LOGS .info ("Braincheck dosyası yok, getiriliyor...")#line:440
URL ='https://raw.githubusercontent.com/Robotger/Teloidubdata/master/learning-data-root.check'#line:442
with open ('learning-data-root.check','wb')as load :#line:443
  load .write (get (URL ).content )#line:444
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
        quit(1)"""#line:466
from random import randint #line:468
import heroku3 #line:469
import asyncio #line:470
from telethon .tl .functions .contacts import UnblockRequest #line:471
if not BOT_TOKEN ==None :#line:473
  tgbot =TelegramClient ("TG_BOT_TOKEN",api_id =API_KEY ,api_hash =API_HASH ).start (bot_token =BOT_TOKEN )#line:475
else :#line:476
  tgbot =None #line:477
def butonlastir (OOOO00O0OO000O00O ,OOO0OO0OO0O00O0OO ):#line:480
  OOOO000OOOO0O00O0 =5 #line:481
  OO0OO0O000OO00O0O =2 #line:482
  OOO0OO0OO0O00O0OO =sorted ([OO0O00OOOO000OOO0 for OO0O00OOOO000OOO0 in OOO0OO0OO0O00O0OO if not OO0O00OOOO000OOO0 .startswith ("_")])#line:484
  OOO0O00O0OOO00O00 =list (map (list ,zip (OOO0OO0OO0O00O0OO [::2 ],OOO0OO0OO0O00O0OO [1 ::2 ])))#line:485
  if len (OOO0OO0OO0O00O0OO )%2 ==1 :#line:486
    OOO0O00O0OOO00O00 .append ([OOO0OO0OO0O00O0OO [-1 ]])#line:487
  O00OOO00OO0OO0O0O =ceil (len (OOO0O00O0OOO00O00 )/OOOO000OOOO0O00O0 )#line:488
  OOO0O00O0OOO00O00 =[OOO0O00O0OOO00O00 [OO00000O0OOO00O00 :OO00000O0OOO00O00 +OOOO000OOOO0O00O0 ]for OO00000O0OOO00O00 in range (0 ,len (OOO0O00O0OOO00O00 ),OOOO000OOOO0O00O0 )]#line:489
  O00OO0OO0O0OOO000 =[]#line:490
  for OOO0O00O0OOO00O00 in OOO0O00O0OOO00O00 [OOOO00O0OO000O00O ]:#line:491
    O00OO0OO0O0OOO000 .append ([custom .Button .inline ("🔸 "+O0O0OOOOOO0O00000 ,data =f"bilgi[{OOOO00O0OO000O00O}]({O0O0OOOOOO0O00000})")for O0O0OOOOOO0O00000 in OOO0O00O0OOO00O00 ])#line:495
  O00OO0OO0O0OOO000 .append ([custom .Button .inline ("◀️ Geri",data =f"sayfa({(O00OOO00OO0OO0O0O - 1) if OOOO00O0OO000O00O == 0 else (OOOO00O0OO000O00O - 1)})"),custom .Button .inline ("İleri ▶️",data =f"sayfa({0 if OOOO00O0OO000O00O == (O00OOO00OO0OO0O0O - 1) else OOOO00O0OO000O00O + 1})")])#line:504
  return [O00OOO00OO0OO0O0O ,O00OO0OO0O0OOO000 ]#line:505
with bot :#line:508
  try :#line:510
    bot (JoinChannelRequest ("@TeloidUserBot"))#line:511
    bot (JoinChannelRequest ("@Robotger"))#line:512
    bot (JoinChannelRequest ("@Robotgerlinks"))#line:513
    bot (JoinChannelRequest ("@Robotgersupport"))#line:514
  except :#line:517
    pass #line:518
  moduller =CMD_HELP #line:520
  me =bot .get_me ()#line:522
  uid =me .id #line:523
  usnm =me .username #line:524
  name =me .first_name #line:525
  lname =me .last_name #line:526
  OWNER_ID =me .id #line:527
  DEFAULT_NAME =name #line:528
  try :#line:529
    @tgbot .on (NewMessage (pattern ='/start'))#line:531
    async def start_bot_handler (O0O0O0OO0OOO00OOO ):#line:532
      if not O0O0O0OO0OOO00OOO .message .from_id ==uid :#line:533
        await O0O0O0OO0OOO00OOO .reply (f'`Merhaba ben` @TeloidUserBot`! Ben sahibime (`@{me.username}`) yardımcı olmak için varım, yaani sana yardımcı olamam :/ Ama sen de bir Teloid açabilirsin; Kanala bak` @TeloidUserBot')#line:536
      else :#line:537
        await O0O0O0OO0OOO00OOO .reply (f'`Tengri save Turks! Teloid working... `')#line:538
    @tgbot .on (InlineQuery )#line:540
    async def inline_handler (OOO0O0O0OOOO00O00 ):#line:541
      OOOO000O00000O0O0 =OOO0O0O0OOOO00O00 .builder #line:542
      OO0000O0OO00OOO00 =None #line:543
      OO0O00OOO0OO0O00O =OOO0O0O0OOOO00O00 .text #line:544
      if OOO0O0O0OOOO00O00 .query .user_id ==uid and OO0O00OOO0OO0O00O =="@TeloidUserBot":#line:545
        O0OOO00OO000OOO00 =OO0O00OOO0OO0O00O [::-1 ]#line:546
        O0O0OO0O0O000OO0O =(butonlastir (0 ,sorted (CMD_HELP )))#line:547
        OO0000O0OO00OOO00 =await OOOO000O00000O0O0 .article (f"Lütfen Sadece .yardım Komutu İle Kullanın",text =f"**En Gelişmiş UserBot!** [Teloid](https://t.me/TeloidUserBot) __Çalışıyor...__\n\n**Yüklenen Modül Sayısı:** `{len(CMD_HELP)}`\n**Sayfa:** 1/{O0O0OO0O0O000OO0O[0]}",buttons =O0O0OO0O0O000OO0O [1 ],link_preview =False )#line:553
      elif OO0O00OOO0OO0O00O .startswith ("http"):#line:554
        OOO00O000OO0O0OO0 =OO0O00OOO0OO0O00O .split (" ")#line:555
        OO0000O0OO00OOO00 =OOOO000O00000O0O0 .article ("Dosya Yüklendi",text =f"**Dosya başarılı bir şekilde {OOO00O000OO0O0OO0[2]} sitesine yüklendi!**\n\nYükleme zamanı: {OOO00O000OO0O0OO0[1][:3]} saniye\n[‏‏‎ ‎]({OOO00O000OO0O0OO0[0]})",buttons =[[custom .Button .url ('URL',OOO00O000OO0O0OO0 [0 ])]],link_preview =True )#line:561
      else :#line:562
        OO0000O0OO00OOO00 =OOOO000O00000O0O0 .article ("@TeloidUserBot",text ="""@TeloidUserBot'u kullanmayı deneyin!
Hesabınızı bot'a çevirebilirsiniz ve bunları kullanabilirsiniz. Unutmayın, siz başkasının botunu yönetemezsiniz! Alttaki GitHub adresinden tüm kurulum detayları anlatılmıştır.""",buttons =[[custom .Button .url ("Kanala Katıl","https://t.me/TeloidUserBot"),custom .Button .url ("Gruba Katıl","https://t.me/RobotgerSupport")],[custom .Button .url ("GitHub","https://github.com/Robotger/TeloidUserBot")]],link_preview =False )#line:575
      await OOO0O0O0OOOO00O00 .answer ([OO0000O0OO00OOO00 ]if OO0000O0OO00OOO00 else None )#line:576
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"sayfa\((.+?)\)")))#line:578
    async def sayfa (O0O0OOOOO0OOO00OO ):#line:579
      if not O0O0OOOOO0OOO00OO .query .user_id ==uid :#line:580
        return await O0O0OOOOO0OOO00OO .answer ("❌ Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:584
      OOOOO0O0O000O00OO =int (O0O0OOOOO0OOO00OO .data_match .group (1 ).decode ("UTF-8"))#line:585
      O000O00OOOO0OOO00 =butonlastir (OOOOO0O0O000O00OO ,CMD_HELP )#line:586
      await O0O0OOOOO0OOO00OO .edit (f"** En Gelişmiş UserBot!** [Teloid](https://t.me/TeloidUserBot) __Çalışıyor...__\n\n**Yüklenen Modül Sayısı:** `{len(CMD_HELP)}`\n**Sayfa:** {OOOOO0O0O000O00OO + 1}/{O000O00OOOO0OOO00[0]}",buttons =O000O00OOOO0OOO00 [1 ],link_preview =False )#line:590
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"bilgi\[(\d*)\]\((.*)\)")))#line:593
    async def bilgi (O0O0O0OO0O000OO00 ):#line:594
      if not O0O0O0OO0O000OO00 .query .user_id ==uid :#line:595
        return await O0O0O0OO0O000OO00 .answer ("❌  Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:599
      O0OOOO00OOOO00OO0 =int (O0O0O0OO0O000OO00 .data_match .group (1 ).decode ("UTF-8"))#line:601
      O00O0O00OO0000O00 =O0O0O0OO0O000OO00 .data_match .group (2 ).decode ("UTF-8")#line:602
      try :#line:603
        OO0OOO000OOOO000O =[custom .Button .inline ("🔹 "+OO0OO0OOOO0OOOO00 [0 ],data =f"komut[{O00O0O00OO0000O00}[{O0OOOO00OOOO00OO0}]]({OO0OO0OOOO0OOOO00[0]})")for OO0OO0OOOO0OOOO00 in CMD_HELP_BOT [O00O0O00OO0000O00 ]['commands'].items ()]#line:608
      except KeyError :#line:609
        return await O0O0O0OO0O000OO00 .answer ("❌ Bu modüle açıklama yazılmamış.",cache_time =0 ,alert =True )#line:612
      OO0OOO000OOOO000O =[OO0OOO000OOOO000O [O00O00O0OOOO00O00 :O00O00O0OOOO00O00 +2 ]for O00O00O0OOOO00O00 in range (0 ,len (OO0OOO000OOOO000O ),2 )]#line:614
      OO0OOO000OOOO000O .append ([custom .Button .inline ("◀️ Geri",data =f"sayfa({O0OOOO00OOOO00OO0})")])#line:616
      await O0O0O0OO0O000OO00 .edit (f"**📗 Dosya:** `{O00O0O00OO0000O00}`\n**🔢 Komut Sayısı:** `{len(CMD_HELP_BOT[O00O0O00OO0000O00]['commands'])}`",buttons =OO0OOO000OOOO000O ,link_preview =False )#line:620
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))#line:624
    async def komut (OOOOO000OOOO0O00O ):#line:625
      if not OOOOO000OOOO0O00O .query .user_id ==uid :#line:626
        return await OOOOO000OOOO0O00O .answer ("❌ Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:630
      O00O00O0OO0O0OOO0 =OOOOO000OOOO0O00O .data_match .group (1 ).decode ("UTF-8")#line:632
      OO00000O000O00000 =int (OOOOO000OOOO0O00O .data_match .group (2 ).decode ("UTF-8"))#line:633
      O0000000000OO0OOO =OOOOO000OOOO0O00O .data_match .group (3 ).decode ("UTF-8")#line:634
      O000OO0O0O0O000OO =f"**📗 Dosya:** `{O00O00O0OO0O0OOO0}`\n"#line:636
      if CMD_HELP_BOT [O00O00O0OO0O0OOO0 ]['info']['info']=='':#line:637
        if not CMD_HELP_BOT [O00O00O0OO0O0OOO0 ]['info']['warning']=='':#line:638
          O000OO0O0O0O000OO +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[O00O00O0OO0O0OOO0]['info']['official'] else '❌'}\n"#line:639
          O000OO0O0O0O000OO +=f"**⚠️ Uyarı:** {CMD_HELP_BOT[O00O00O0OO0O0OOO0]['info']['warning']}\n\n"#line:640
        else :#line:641
          O000OO0O0O0O000OO +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[O00O00O0OO0O0OOO0]['info']['official'] else '❌'}\n\n"#line:642
      else :#line:643
        O000OO0O0O0O000OO +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[O00O00O0OO0O0OOO0]['info']['official'] else '❌'}\n"#line:644
        if not CMD_HELP_BOT [O00O00O0OO0O0OOO0 ]['info']['warning']=='':#line:645
          O000OO0O0O0O000OO +=f"**⚠️ Uyarı:** {CMD_HELP_BOT[O00O00O0OO0O0OOO0]['info']['warning']}\n"#line:646
        O000OO0O0O0O000OO +=f"**ℹ️ Info:** {CMD_HELP_BOT[O00O00O0OO0O0OOO0]['info']['info']}\n\n"#line:647
      O000000OOO00O00O0 =CMD_HELP_BOT [O00O00O0OO0O0OOO0 ]['commands'][O0000000000OO0OOO ]#line:649
      if O000000OOO00O00O0 ['params']is None :#line:650
        O000OO0O0O0O000OO +=f"**🛠 Komut:** `{PATTERNS[:1]}{O000000OOO00O00O0['command']}`\n"#line:651
      else :#line:652
        O000OO0O0O0O000OO +=f"**🛠 Komut:** `{PATTERNS[:1]}{O000000OOO00O00O0['command']} {O000000OOO00O00O0['params']}`\n"#line:653
      if O000000OOO00O00O0 ['example']is None :#line:655
        O000OO0O0O0O000OO +=f"**💬 Açıklama:** `{O000000OOO00O00O0['usage']}`\n\n"#line:656
      else :#line:657
        O000OO0O0O0O000OO +=f"**💬 Açıklama:** `{O000000OOO00O00O0['usage']}`\n"#line:658
        O000OO0O0O0O000OO +=f"**⌨️ Örnek:** `{PATTERNS[:1]}{O000000OOO00O00O0['example']}`\n\n"#line:659
      await OOOOO000OOOO0O00O .edit (O000OO0O0O0O000OO ,buttons =[custom .Button .inline ("◀️ Geri",data =f"bilgi[{OO00000O000O00000}]({O00O00O0OO0O0OOO0})")],link_preview =False )#line:666
  except Exception as e :#line:667
    pass #line:668
"""try:
        bot.loop.run_until_complete(check_botlog_chatid())
except:
        LOGS.info(
            "BOTLOG_CHATID ortam değişkeni geçerli bir varlık değildir. "
            "Ortam değişkenlerinizi / config.env dosyanızı kontrol edin."
        )
        quit(1)"""#line:676
SON_GORULME =0 #line:681
COUNT_MSG =0 #line:682
USERS ={}#line:683
MYID =uid #line:684
ForceVer =forceVer #line:685
upVer =int (upVer [0 ])#line:686
BRAIN_CHECKER =[]#line:687
COUNT_PM ={}#line:688
LASTMSG ={}#line:689
CMD_LIST ={}#line:690
FUP =True #line:691
ENABLE_KILLME =True #line:692
ISAFK =False #line:693
AFKREASON =None #line:694
ZALG_LIST =[["̖"," ̗"," ̘"," ̙"," ̜"," ̝"," ̞"," ̟"," ̠"," ̤"," ̥"," ̦"," ̩"," ̪"," ̫"," ̬"," ̭"," ̮"," ̯"," ̰"," ̱"," ̲"," ̳"," ̹"," ̺"," ̻"," ̼"," ͅ"," ͇"," ͈"," ͉"," ͍"," ͎"," ͓"," ͔"," ͕"," ͖"," ͙"," ͚"," ",],[" ̍"," ̎"," ̄"," ̅"," ̿"," ̑"," ̆"," ̐"," ͒"," ͗"," ͑"," ̇"," ̈"," ̊"," ͂"," ̓"," ̈́"," ͊"," ͋"," ͌"," ̃"," ̂"," ̌"," ͐"," ́"," ̋"," ̏"," ̽"," ̉"," ͣ"," ͤ"," ͥ"," ͦ"," ͧ"," ͨ"," ͩ"," ͪ"," ͫ"," ͬ"," ͭ"," ͮ"," ͯ"," ̾"," ͛"," ͆"," ̚"],[" ̕"," ̛"," ̀"," ́"," ͘"," ̡"," ̢"," ̧"," ̨"," ̴"," ̵"," ̶"," ͜"," ͝"," ͞"," ͟"," ͠"," ͢"," ̸"," ̷"," ͡",]]#line:766
