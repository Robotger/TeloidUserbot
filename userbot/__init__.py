""#line:8:""" UserBot hazırlanışı. """
from telethon .errors import ChannelPrivateError #line:9:from telethon.errors import ChannelPrivateError
from .helpers import worktime as timelavan #line:11:from .helpers import worktime as timelavan
from lib2to3 .pgen2 .token import STRING #line:12:from lib2to3.pgen2.token import STRING
import os #line:13:import os
import asyncio #line:14:import asyncio
import time #line:15:import time
import heroku3 #line:16:import heroku3
from re import compile #line:17:from re import compile
from .utils .pip_install import install_pip #line:18:from .utils.pip_install import install_pip
from sys import version_info #line:19:from sys import version_info
from logging import basicConfig ,getLogger ,INFO ,DEBUG #line:20:from logging import basicConfig, getLogger, INFO, DEBUG
from distutils .util import strtobool as sb #line:21:from distutils.util import strtobool as sb
from pylast import LastFMNetwork ,md5 #line:22:from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL #line:23:from pySmartDL import SmartDL
from sqlite3 import connect #line:24:from sqlite3 import connect
from telethon .tl .functions .channels import GetFullChannelRequest as getchat #line:25:from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon .tl .functions .phone import GetGroupCallRequest as getvc #line:26:from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from dotenv import load_dotenv #line:27:from dotenv import load_dotenv
from requests import get #line:28:from requests import get
from telethon .tl .functions .channels import JoinChannelRequest ,LeaveChannelRequest #line:29:from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon .sync import TelegramClient ,custom #line:30:from telethon.sync import TelegramClient, custom
from telethon .sessions import StringSession #line:31:from telethon.sessions import StringSession
from telethon .events import callbackquery ,InlineQuery ,NewMessage #line:32:from telethon.events import callbackquery, InlineQuery, NewMessage
from telethon .tl .functions .users import GetFullUserRequest #line:33:from telethon.tl.functions.users import GetFullUserRequest
from math import ceil #line:34:from math import ceil
from telethon .tl .functions .channels import EditPhotoRequest ,CreateChannelRequest #line:35:from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
from telethon import TelegramClient ,events #line:36:from telethon import TelegramClient, events
from telethon .errors import SessionPasswordNeededError ,PhoneCodeInvalidError ,PasswordHashInvalidError ,PhoneNumberInvalidError #line:37:from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
from telethon .network import ConnectionTcpAbridged #line:38:from telethon.network import ConnectionTcpAbridged
from telethon .utils import get_display_name #line:39:from telethon.utils import get_display_name
from telethon .sessions import StringSession #line:40:from telethon.sessions import StringSession
load_dotenv ("config.env")#line:42:load_dotenv("config.env")
KURULUM =os .environ .get ("KURULUM",None )#line:44:KURULUM = os.environ.get("KURULUM", None)
STRING_SESSION =os .environ .get ("STRING_SESSION",None )#line:46:STRING_SESSION = os.environ.get("STRING_SESSION", None)
if (STRING_SESSION ==None ):#line:47:if (STRING_SESSION == None):
 if KURULUM ==None :#line:49:if KURULUM == None:
  os .system ("python GenerateStringSession.py")#line:50:os.system("python GenerateStringSession.py")
  print ("İlk Kurulum tamamlandı STRING_SESSION İsimli Secret oluşturduktan sonra Lütfen yeniden başlatın!!")#line:53:)
  exit ()#line:54:exit()
else :#line:55:else:
  pass #line:56:pass
StartTime =time .time ()#line:58:StartTime = time.time()
CONSOLE_LOGGER_VERBOSE =sb (os .environ .get ("CONSOLE_LOGGER_VERBOSE","False"))#line:61:CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
ASYNC_POOL =[]#line:63:ASYNC_POOL = []
if CONSOLE_LOGGER_VERBOSE :#line:65:if CONSOLE_LOGGER_VERBOSE:
  basicConfig (level =DEBUG ,format ="[%(asctime)s - %(levelname)s] - @TeloidUserBot : %(message)s",datefmt ='%d-%b-%y %H:%M:%S')#line:69:datefmt='%d-%b-%y %H:%M:%S')
else :#line:70:else:
  basicConfig (level =INFO ,format ="[%(asctime)s - %(levelname)s] - @TeloidUserBot : %(message)s",datefmt ='%d-%b-%y %H:%M:%S')#line:74:datefmt='%d-%b-%y %H:%M:%S')
LOGS =getLogger (__name__ )#line:75:LOGS = getLogger(__name__)
if version_info [0 ]<3 or version_info [1 ]<6 :#line:77:if version_info[0] < 3 or version_info[1] < 6:
  LOGS .info ("En az python 3.6 sürümüne sahip olmanız gerekir." "Birden fazla özellik buna bağlıdır. Bot kapatılıyor.")#line:79:"Birden fazla özellik buna bağlıdır. Bot kapatılıyor.")
  quit (1 )#line:80:quit(1)
branch ="master"#line:81:branch = "master"
CONFIG_CHECK =os .environ .get ("___________LUTFEN_______BU_____SATIRI_____SILIN__________",None )#line:85:"___________LUTFEN_______BU_____SATIRI_____SILIN__________", None)
if CONFIG_CHECK :#line:87:if CONFIG_CHECK:
  LOGS .info ("Lütfen ilk hashtag'de belirtilen satırı config.env dosyasından kaldırın")#line:89:"Lütfen ilk hashtag'de belirtilen satırı config.env dosyasından kaldırın")
  quit (1 )#line:90:quit(1)
LANGUAGE =os .environ .get ("LANGUAGE","DEFAULT").upper ()#line:93:LANGUAGE = os.environ.get("LANGUAGE", "DEFAULT").upper()
if not LANGUAGE in ["EN","TR","AZ","UZ","DEFAULT"]:#line:95:if not LANGUAGE in ["EN", "TR", "AZ", "UZ", "DEFAULT"]:
  LOGS .info ("Bilinmeyen bir dil yazdınız. Bundan dolayı DEFAULT kullanılıyor.")#line:96:LOGS.info("Bilinmeyen bir dil yazdınız. Bundan dolayı DEFAULT kullanılıyor.")
  LANGUAGE ="DEFAULT"#line:97:LANGUAGE = "DEFAULT"
TELOID_VERSION ="v0.2"#line:100:TELOID_VERSION = "v0.2"
MAX_MESSAGE_SIZE_LIMIT =4095 #line:102:MAX_MESSAGE_SIZE_LIMIT = 4095
API_KEY =os .environ .get ("API_KEY",None )#line:104:API_KEY = os.environ.get("API_KEY", None)
API_HASH =os .environ .get ("API_HASH",None )#line:105:API_HASH = os.environ.get("API_HASH", None)
SEVGILI =os .environ .get ("SEVGILI",None )#line:107:SEVGILI = os.environ.get("SEVGILI", None)
async def get_call (OO00OOO00O000OO0O ):#line:111:async def get_call(event):
  OOO0O00O0O0O00000 =await OO00OOO00O000OO0O .client (getchat (OO00OOO00O000OO0O .chat_id ))#line:112:mm = await event.client(getchat(event.chat_id))
  OO00OOO0O0OOOOOOO =await OO00OOO00O000OO0O .client (getvc (OOO0O00O0O0O00000 .full_chat .call ))#line:113:xx = await event.client(getvc(mm.full_chat.call))
  return OO00OOO0O0OOOOOOO .call #line:114:return xx.call
SUDO_HANDLER =os .environ .get ("SUDO_HANDLER",r".")#line:118:SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r".")
try :#line:119:try:
  SUDO_USERS =set (int (O00OO000O0OOO00OO )for O00OO000O0OOO00OO in os .environ .get ("SUDO_USERS","").split ())#line:120:SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
except ValueError :#line:121:except ValueError:
  raise Exception ("Bir Kullanıcı İd si Belirtmek zorundasın.")#line:122:raise Exception("Bir Kullanıcı İd si Belirtmek zorundasın.")
SILINEN_PLUGIN ={}#line:124:SILINEN_PLUGIN = {}
BOTLOG_CHATID =int (os .environ .get ("BOTLOG_CHATID",0 ))#line:128:BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID",0))
BOTLOG =sb (os .environ .get ("BOTLOG","False"))#line:131:BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER =sb (os .environ .get ("LOGSPAMMER","False"))#line:133:LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
PM_AUTO_BAN =sb (os .environ .get ("PM_AUTO_BAN","False"))#line:136:PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
HEROKU_MEMEZ =sb (os .environ .get ("HEROKU_MEMEZ","False"))#line:139:HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APPNAME =os .environ .get ("HEROKU_APPNAME",None )#line:140:HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY =os .environ .get ("HEROKU_APIKEY",None )#line:141:HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
EZZEC =False #line:143:EZZEC = False
Heroku =None #line:144:Heroku = None
app =None #line:145:app = None
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None :#line:147:if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
  if EZZEC ==True :#line:148:if EZZEC == True:
    pass #line:149:pass
  else :#line:150:else:
    EZZEC =True #line:151:EZZEC = True
    Heroku =heroku3 .from_key (HEROKU_APIKEY )#line:152:Heroku = heroku3.from_key(HEROKU_APIKEY)
    app =Heroku .app (HEROKU_APPNAME )#line:153:app = Heroku.app(HEROKU_APPNAME)
    heroku_var =app .config ()#line:154:heroku_var = app.config()
    heroku_var ["UPSTREAM_REPO_URL"]="https://github.com/Robotger/TeloidUserBot.git"#line:156:"UPSTREAM_REPO_URL"] = "https://github.com/Robotger/TeloidUserBot.git"
else :#line:157:else:
  app =None #line:158:app = None
try :#line:160:try:
  import randomstuff #line:161:import randomstuff
except ModuleNotFoundError :#line:162:except ModuleNotFoundError:
  install_pip ("randomstuff.py")#line:163:install_pip("randomstuff.py")
  import randomstuff #line:164:import randomstuff
RANDOM_STUFF_API_KEY =os .environ .get ("RANDOM_STUFF_API_KEY",None )#line:167:RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
if RANDOM_STUFF_API_KEY :#line:168:if RANDOM_STUFF_API_KEY:
  try :#line:169:try:
    rs_client =randomstuff .AsyncClient (api_key =RANDOM_STUFF_API_KEY ,version ="4")#line:171:version="4")
  except :#line:172:except:
    print ('Invalid RANDOM_STUFF_API_KEY')#line:173:print('Invalid RANDOM_STUFF_API_KEY')
    rs_client =None #line:174:rs_client = None
else :#line:175:else:
  rs_client =None #line:176:rs_client = None
AI_LANG =os .environ .get ("AI_LANG",'en')#line:177:AI_LANG = os.environ.get("AI_LANG", 'en')
STABILITY =sb (os .environ .get ("STABILITY","True"))#line:180:STABILITY = sb(os.environ.get("STABILITY", "True"))  #
UPSTREAM_REPO_URL ="https://github.com/Robotger/TeloidUserBot.git"#line:182:UPSTREAM_REPO_URL = "https://github.com/Robotger/TeloidUserBot.git"
EMERGENCY ="https://github.com/Robotger/TeloidUserBot.git"#line:183:EMERGENCY = "https://github.com/Robotger/TeloidUserBot.git"  # Acil durrum için
AFKILETME =sb (os .environ .get ("AFKILETME","True"))#line:185:AFKILETME = sb(os.environ.get("AFKILETME", "True"))
DB_URI =os .environ .get ("DATABASE_URL","sqlite:///teloid.db")#line:188:DB_URI = os.environ.get("DATABASE_URL", "sqlite:///teloid.db")
OCR_SPACE_API_KEY =os .environ .get ("OCR_SPACE_API_KEY",None )#line:191:OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
REM_BG_API_KEY =os .environ .get ("REM_BG_API_KEY",None )#line:194:REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
AUTO_PP =os .environ .get ("AUTO_PP",None )#line:197:AUTO_PP = os.environ.get("AUTO_PP", None)
SUDO_ID =set (int (O0OOOOO00O0O0000O )for O0OOOOO00O0O0000O in os .environ .get ("SUDO_ID","").split ())#line:199:SUDO_ID = set(int(x) for x in os.environ.get("SUDO_ID", "").split())
WARN_LIMIT =int (os .environ .get ("WARN_LIMIT",3 ))#line:203:WARN_LIMIT = int(os.environ.get("WARN_LIMIT", 3))
WARN_MODE =os .environ .get ("WARN_MODE","gmute")#line:204:WARN_MODE = os.environ.get("WARN_MODE", "gmute")
if not WARN_MODE in ["gmute","gban"]:#line:206:if not WARN_MODE in ["gmute", "gban"]:
  WARN_MODE ="gmute"#line:207:WARN_MODE = "gmute"
GALERI_SURE =int (os .environ .get ("GALERI_SURE",60 ))#line:210:GALERI_SURE = int(os.environ.get("GALERI_SURE", 60))
CHROME_DRIVER =os .environ .get ("CHROME_DRIVER",None )#line:213:CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
GOOGLE_CHROME_BIN =os .environ .get ("GOOGLE_CHROME_BIN",None )#line:214:GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
WORKTIME =time .time ()#line:217:WORKTIME = time.time()
PLUGINID =os .environ .get ("PLUGIN_CHANNEL_ID",None )#line:219:PLUGINID = os.environ.get("PLUGIN_CHANNEL_ID", None)
if not PLUGINID :#line:221:if not PLUGINID:
  PLUGIN_CHANNEL_ID ="me"#line:222:PLUGIN_CHANNEL_ID = "me"
else :#line:223:else:
  PLUGIN_CHANNEL_ID =int (PLUGINID )#line:224:PLUGIN_CHANNEL_ID = int(PLUGINID)
OPEN_WEATHER_MAP_APPID =os .environ .get ("OPEN_WEATHER_MAP_APPID",None )#line:227:OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY =os .environ .get ("WEATHER_DEFCITY",None )#line:228:WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)
ANTI_SPAMBOT =sb (os .environ .get ("ANTI_SPAMBOT","False"))#line:231:ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT =sb (os .environ .get ("ANTI_SPAMBOT_SHOUT","True"))#line:232:ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "True"))
YOUTUBE_API_KEY =os .environ .get ("YOUTUBE_API_KEY",None )#line:235:YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
COUNTRY =str (os .environ .get ("COUNTRY",""))#line:238:COUNTRY = str(os.environ.get("COUNTRY", ""))
TZ_NUMBER =int (os .environ .get ("TZ_NUMBER",1 ))#line:239:TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
CLEAN_WELCOME =sb (os .environ .get ("CLEAN_WELCOME","True"))#line:242:CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
BIO_PREFIX =os .environ .get ("BIO_PREFIX","@TeloidUserBot | ")#line:245:BIO_PREFIX = os.environ.get("BIO_PREFIX", "@TeloidUserBot | ")
LASTFM_API =os .environ .get ("LASTFM_API",None )#line:248:LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET =os .environ .get ("LASTFM_SECRET",None )#line:249:LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME =os .environ .get ("LASTFM_USERNAME",None )#line:250:LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN =os .environ .get ("LASTFM_PASSWORD",None )#line:251:LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS =md5 (LASTFM_PASSWORD_PLAIN )#line:252:LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS :#line:253:if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
  lastfm =LastFMNetwork (api_key =LASTFM_API ,api_secret =LASTFM_SECRET ,username =LASTFM_USERNAME ,password_hash =LASTFM_PASS )#line:257:password_hash=LASTFM_PASS)
else :#line:258:else:
  lastfm =None #line:259:lastfm = None
G_DRIVE_CLIENT_ID =os .environ .get ("G_DRIVE_CLIENT_ID",None )#line:262:G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET =os .environ .get ("G_DRIVE_CLIENT_SECRET",None )#line:263:G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA =os .environ .get ("G_DRIVE_AUTH_TOKEN_DATA",None )#line:264:G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
GDRIVE_FOLDER_ID =os .environ .get ("GDRIVE_FOLDER_ID",None )#line:265:GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY =os .environ .get ("TMP_DOWNLOAD_DIRECTORY","./downloads")#line:267:"./downloads")
DEFAULT_BIO =os .environ .get ("DEFAULT_BIO",None )#line:270:DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
USERBOT_ =True #line:273:USERBOT_ = True
BOT_TOKEN =os .environ .get ("BOT_TOKEN",None )#line:276:BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME =os .environ .get ("BOT_USERNAME",None )#line:277:BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
GENIUS =os .environ .get ("GENIUS",None )#line:280:GENIUS = os.environ.get("GENIUS", None)
CMD_HELP ={}#line:282:CMD_HELP = {}
CMD_HELP_BOT ={}#line:283:CMD_HELP_BOT = {}
PM_AUTO_BAN_LIMIT =int (os .environ .get ("PM_AUTO_BAN_LIMIT",4 ))#line:285:PM_AUTO_BAN_LIMIT = int(os.environ.get("PM_AUTO_BAN_LIMIT", 4))
SPOTIFY_DC =os .environ .get ("SPOTIFY_DC",None )#line:287:SPOTIFY_DC = os.environ.get("SPOTIFY_DC", None)
SPOTIFY_KEY =os .environ .get ("SPOTIFY_KEY",None )#line:288:SPOTIFY_KEY = os.environ.get("SPOTIFY_KEY", None)
PAKET_ISMI =os .environ .get ("PAKET_ISMI","| 🌃 @TeloidUserBot Paketi |")#line:290:PAKET_ISMI = os.environ.get("PAKET_ISMI", "| 🌃 @TeloidUserBot Paketi |")
BLACKLIST_CHAT =[1698661722 ]#line:294:BLACKLIST_CHAT = [1698661722]
OTOMATIK_KATILMA =sb (os .environ .get ("OTOMATIK_KATILMA","True"))#line:297:OTOMATIK_KATILMA = sb(os.environ.get("OTOMATIK_KATILMA", "True"))
AUTO_UPDATE =sb (os .environ .get ("AUTO_UPDATE","True"))#line:298:AUTO_UPDATE = sb(os.environ.get("AUTO_UPDATE", "True"))
PATTERNS =os .environ .get ("PATTERNS",".;!,")#line:301:PATTERNS = os.environ.get("PATTERNS", ".;!,")
WHITELIST =get ('https://raw.githubusercontent.com/Robotger/Teloidubdata/master/whitelist.json').json ()#line:304:).json()
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None :#line:306:if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
  Heroku =heroku3 .from_key (HEROKU_APIKEY )#line:307:Heroku = heroku3.from_key(HEROKU_APIKEY)
  app =Heroku .app (HEROKU_APPNAME )#line:308:app = Heroku.app(HEROKU_APPNAME)
  heroku_var =app .config ()#line:309:heroku_var = app.config()
forceVer =[]#line:312:forceVer = []
if os .path .exists ("force-surum.check"):#line:313:if os.path.exists("force-surum.check"):
  os .remove ("force-surum.check")#line:314:os.remove("force-surum.check")
else :#line:315:else:
  LOGS .info ("Force Sürüm Kontrol dosyası yok, getiriliyor...")#line:316:LOGS.info("Force Sürüm Kontrol dosyası yok, getiriliyor...")
URL ='https://raw.githubusercontent.com/Robotger/TeloidUbdata/master/force-surum.check'#line:318:URL = 'https://raw.githubusercontent.com/Robotger/TeloidUbdata/master/force-surum.check'
with open ('force-surum.check','wb')as load :#line:319:with open('force-surum.check', 'wb') as load:
  load .write (get (URL ).content )#line:320:load.write(get(URL).content)
DB =connect ("force-surum.check")#line:322:DB = connect("force-surum.check")
CURSOR =DB .cursor ()#line:323:CURSOR = DB.cursor()
CURSOR .execute ("""SELECT * FROM SURUM1""")#line:324:CURSOR.execute("""SELECT * FROM SURUM1""")
ALL_ROWS =CURSOR .fetchall ()#line:325:ALL_ROWS = CURSOR.fetchall()
for i in ALL_ROWS :#line:327:for i in ALL_ROWS:
  forceVer .append (i [0 ])#line:328:forceVer.append(i[0])
  forceVer .append (i [1 ])#line:329:forceVer.append(i[1])
import sys #line:332:import sys
def algo (OO0OO0OOO0O0000OO ):#line:334:def algo(S):
    OO00OO0OOO000O00O =0 #line:335:i = 0
    OO0OO0OO0OOO00OO0 =0 #line:336:j = 0
    while True :#line:337:while True:
        OO00OO0OOO000O00O =(OO00OO0OOO000O00O +1 )%256 #line:338:i = (i + 1) % 256
        OO0OO0OO0OOO00OO0 =(OO0OO0OO0OOO00OO0 +OO0OO0OOO0O0000OO [OO00OO0OOO000O00O ])%256 #line:339:j = (j + S[i]) % 256
        OO0OO0OOO0O0000OO [OO00OO0OOO000O00O ],OO0OO0OOO0O0000OO [OO0OO0OO0OOO00OO0 ]=OO0OO0OOO0O0000OO [OO0OO0OO0OOO00OO0 ],OO0OO0OOO0O0000OO [OO00OO0OOO000O00O ]#line:340:S[i], S[j] = S[j], S[i]
        yield OO0OO0OOO0O0000OO [(OO0OO0OOO0O0000OO [OO00OO0OOO000O00O ]+OO0OO0OOO0O0000OO [OO0OO0OO0OOO00OO0 ])%256 ]#line:342:yield S[(S[i] + S[j]) % 256]
def teloider (OOOOOOOO00OOOO00O ,O0OO0O0OO0OOO0000 ,OOO0OO0OO00OO0OO0 =False ):#line:345:def teloider(yazi, key, hexformat=False):
    O0OO0O0OO0OOO0000 ,OOOOOOOO00OOOO00O =bytearray (O0OO0O0OO0OOO0000 ),bytearray (OOOOOOOO00OOOO00O )#line:346:key, yazi = bytearray(key), bytearray(yazi)
    OO000O000O00O000O =list (range (256 ))#line:347:S = list(range(256))
    OO00O0OOO0000O00O =0 #line:348:j = 0
    for OOO00OOO0000OOOOO in range (256 ):#line:349:for i in range(256):
        OO00O0OOO0000O00O =(OO00O0OOO0000O00O +OO000O000O00O000O [OOO00OOO0000OOOOO ]+O0OO0O0OO0OOO0000 [OOO00OOO0000OOOOO %len (O0OO0O0OO0OOO0000 )])%256 #line:350:j = (j + S[i] + key[i % len(key)]) % 256
        OO000O000O00O000O [OOO00OOO0000OOOOO ],OO000O000O00O000O [OO00O0OOO0000O00O ]=OO000O000O00O000O [OO00O0OOO0000O00O ],OO000O000O00O000O [OOO00OOO0000OOOOO ]#line:351:S[i], S[j] = S[j], S[i]
    OOOOOO0O00OO00OOO =algo (OO000O000O00O000O )#line:352:keystream = algo(S)
    return b''.join (b"%02X"%(O0OO00O0OO0OO0O0O ^next (OOOOOO0O00OO00OOO ))for O0OO00O0OO0OO0O0O in OOOOOOOO00OOOO00O )if OOO0OO0OO00OO0OO0 else bytearray (O0O0OO0OO000O0O0O ^next (OOOOOO0O00OO00OOO )for O0O0OO0OO000O0O0O in OOOOOOOO00OOOO00O )#line:353:return b''.join(b"%02X" % (c ^ next(keystream)) for c in yazi) if hexformat else bytearray(c ^ next(keystream) for c in yazi)
teloidver =teloider (b"\xd0\x95\xf3)\xf8\xddY\xd61P\xfbE\xf3#\x01\x1d\x8b\x845\xea\xe5\x15L\x1eL\x85\x86s\x90\xee\xf1\x8c\xef\xa9\xd6#\xe1\xc0`:\xcfQ\xbe1\x9a\xe7-\xe8\x1dd\xf3j\x0bW!\xf7Q\x0b,\x88\x06\xfe\xa3\xfa",b"@TeloidUserBot").decode ("utf-8")#line:358:teloidver = teloider(b"\xd0\x95\xf3)\xf8\xddY\xd61P\xfbE\xf3#\x01\x1d\x8b\x845\xea\xe5\x15L\x1eL\x85\x86s\x90\xee\xf1\x8c\xef\xa9\xd6#\xe1\xc0`:\xcfQ\xbe1\x9a\xe7-\xe8\x1dd\xf3j\x0bW!\xf7Q\x0b,\x88\x06\xfe\xa3\xfa",b"@TeloidUserBot").decode("utf-8")
if teloidver [1 :10 ]==sys .argv [0 ]:#line:360:if teloidver[1:10] == sys.argv[0]:
    pass #line:361:pass
else :#line:362:else:
    print (teloidver [13 :60 ])#line:363:print(teloidver[13:60])
    exit ()#line:364:exit()
connect ("force-surum.check").close ()#line:369:connect("force-surum.check").close()
DEVS =[5159148002 ]#line:371:DEVS = [5159148002]  #Developer için ayrıcalıklar
upVer =[]#line:373:upVer = []
if os .path .exists ("force-update.check"):#line:374:if os.path.exists("force-update.check"):
  os .remove ("force-update.check")#line:375:os.remove("force-update.check")
else :#line:376:else:
  LOGS .info ("Force Update Kontrol dosyası yok, getiriliyor...")#line:377:LOGS.info("Force Update Kontrol dosyası yok, getiriliyor...")
URL ='https://raw.githubusercontent.com/Robotger/TeloidUBdata/master/force-update.check'#line:379:URL = 'https://raw.githubusercontent.com/Robotger/TeloidUBdata/master/force-update.check'
with open ('force-update.check','wb')as load :#line:380:with open('force-update.check', 'wb') as load:
  load .write (get (URL ).content )#line:381:load.write(get(URL).content)
WORKTIME =time .time ()#line:383:WORKTIME = time.time()
DB =connect ("force-update.check")#line:385:DB = connect("force-update.check")
CURSOR =DB .cursor ()#line:386:CURSOR = DB.cursor()
CURSOR .execute ("""SELECT * FROM SURUM1""")#line:387:CURSOR.execute("""SELECT * FROM SURUM1""")
ALL_ROWS =CURSOR .fetchall ()#line:388:ALL_ROWS = CURSOR.fetchall()
for i in ALL_ROWS :#line:390:for i in ALL_ROWS:
  upVer .append (i [0 ])#line:391:upVer.append(i[0])
connect ("force-update.check").close ()#line:392:connect("force-update.check").close()
if not os .path .exists ('bin'):#line:395:if not os.path.exists('bin'):
  os .mkdir ('bin')#line:396:os.mkdir('bin')
else :#line:398:else:
  app =None #line:399:app = None
binaries ={"https://raw.githubusercontent.com/yshalsager/megadown/master/megadown":"bin/megadown","https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":"bin/cmrudl"}#line:405:}
for binary ,path in binaries .items ():#line:407:for binary, path in binaries.items():
  downloader =SmartDL (binary ,path ,progress_bar =False )#line:408:downloader = SmartDL(binary, path, progress_bar=False)
  downloader .start ()#line:409:downloader.start()
  os .chmod (path ,0o755 )#line:410:os.chmod(path, 0o755)
from telethon .network .connection .tcpabridged import ConnectionTcpAbridged #line:412:from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
loop =None #line:414:loop = None
import sys #line:415:import sys
if STRING_SESSION :#line:417:if STRING_SESSION:
  session =StringSession (str (STRING_SESSION ))#line:418:session = StringSession(str(STRING_SESSION))
else :#line:419:else:
  session ="TeloidUserBot"#line:420:session = "TeloidUserBot"
try :#line:421:try:
  bot =TelegramClient (session =session ,api_id =API_KEY ,api_hash =API_HASH ,connection =ConnectionTcpAbridged ,auto_reconnect =True ,connection_retries =None ,)#line:429:)
except Exception as e :#line:431:except Exception as e:
  print (f"STRING_SESSION - {e}")#line:432:print(f"STRING_SESSION - {e}")
  sys .exit ()#line:433:sys.exit()
ASISTAN =5319669482 #line:435:ASISTAN = 5319669482  # Bot yardımcısı
if os .path .exists ("learning-data-root.check"):#line:437:if os.path.exists("learning-data-root.check"):
  os .remove ("learning-data-root.check")#line:438:os.remove("learning-data-root.check")
else :#line:439:else:
  LOGS .info ("Braincheck dosyası yok, getiriliyor...")#line:440:LOGS.info("Braincheck dosyası yok, getiriliyor...")
URL ='https://raw.githubusercontent.com/Robotger/Teloidubdata/master/learning-data-root.check'#line:442:URL = 'https://raw.githubusercontent.com/Robotger/Teloidubdata/master/learning-data-root.check'
with open ('learning-data-root.check','wb')as load :#line:443:with open('learning-data-root.check', 'wb') as load:
  load .write (get (URL ).content )#line:444:load.write(get(URL).content)
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
        quit(1)"""#line:466:quit(1)"""
from random import randint #line:468:from random import randint
import heroku3 #line:469:import heroku3
import asyncio #line:470:import asyncio
from telethon .tl .functions .contacts import UnblockRequest #line:471:from telethon.tl.functions.contacts import UnblockRequest
if not BOT_TOKEN ==None :#line:473:if not BOT_TOKEN == None:
  tgbot =TelegramClient ("TG_BOT_TOKEN",api_id =API_KEY ,api_hash =API_HASH ).start (bot_token =BOT_TOKEN )#line:475:api_hash=API_HASH).start(bot_token=BOT_TOKEN)
else :#line:476:else:
  tgbot =None #line:477:tgbot = None
def butonlastir (O000O0OO00O0O000O ,OO00OOO000O00000O ):#line:480:def butonlastir(sayfa, moduller):
  O000OO000O0000O0O =5 #line:481:Satir = 5
  OO00OO0O0OOOO00OO =2 #line:482:Kolon = 2
  OO00OOO000O00000O =sorted ([OOOO0O00O0O00OOOO for OOOO0O00O0O00OOOO in OO00OOO000O00000O if not OOOO0O00O0O00OOOO .startswith ("_")])#line:484:moduller = sorted([modul for modul in moduller if not modul.startswith("_")])
  O00O0OO0OO0O00O0O =list (map (list ,zip (OO00OOO000O00000O [::2 ],OO00OOO000O00000O [1 ::2 ])))#line:485:pairs = list(map(list, zip(moduller[::2], moduller[1::2])))
  if len (OO00OOO000O00000O )%2 ==1 :#line:486:if len(moduller) % 2 == 1:
    O00O0OO0OO0O00O0O .append ([OO00OOO000O00000O [-1 ]])#line:487:pairs.append([moduller[-1]])
  OO00OOO0OO0O0OOO0 =ceil (len (O00O0OO0OO0O00O0O )/O000OO000O0000O0O )#line:488:max_pages = ceil(len(pairs) / Satir)
  O00O0OO0OO0O00O0O =[O00O0OO0OO0O00O0O [OOOOOOOO0O000OOOO :OOOOOOOO0O000OOOO +O000OO000O0000O0O ]for OOOOOOOO0O000OOOO in range (0 ,len (O00O0OO0OO0O00O0O ),O000OO000O0000O0O )]#line:489:pairs = [pairs[i:i + Satir] for i in range(0, len(pairs), Satir)]
  O000O00000O00OO00 =[]#line:490:butonlar = []
  for O00O0OO0OO0O00O0O in O00O0OO0OO0O00O0O [O000O0OO00O0O000O ]:#line:491:for pairs in pairs[sayfa]:
    O000O00000O00OO00 .append ([custom .Button .inline ("🔸 "+OO00O0OO000OOO000 ,data =f"bilgi[{O000O0OO00O0O000O}]({OO00O0OO000OOO000})")for OO00O0OO000OOO000 in O00O0OO0OO0O00O0O ])#line:495:])
  O000O00000O00OO00 .append ([custom .Button .inline ("◀️ Geri",data =f"sayfa({(OO00OOO0OO0O0OOO0 - 1) if O000O0OO00O0O000O == 0 else (O000O0OO00O0O000O - 1)})"),custom .Button .inline ("İleri ▶️",data =f"sayfa({0 if O000O0OO00O0O000O == (OO00OOO0OO0O0OOO0 - 1) else O000O0OO00O0O000O + 1})")])#line:504:])
  return [OO00OOO0OO0O0OOO0 ,O000O00000O00OO00 ]#line:505:return [max_pages, butonlar]
with bot :#line:508:with bot:
  try :#line:510:try:
    bot (JoinChannelRequest ("@TeloidUserBot"))#line:511:bot(JoinChannelRequest("@TeloidUserBot"))
    bot (JoinChannelRequest ("@Robotger"))#line:512:bot(JoinChannelRequest("@Robotger"))
    bot (JoinChannelRequest ("@RobotgerStore"))#line:513:bot(JoinChannelRequest("@RobotgerStore"))
    bot (JoinChannelRequest ("@Lavanstax"))#line:514:bot(JoinChannelRequest("@Lavanstax"))
    bot (JoinChannelRequest ("@DisOwen"))#line:515:bot(JoinChannelRequest("@DisOwen"))
  except :#line:517:except:
    pass #line:518:pass
  moduller =CMD_HELP #line:520:moduller = CMD_HELP
  me =bot .get_me ()#line:522:me = bot.get_me()
  uid =me .id #line:523:uid = me.id
  usnm =me .username #line:524:usnm = me.username
  name =me .first_name #line:525:name = me.first_name
  lname =me .last_name #line:526:lname = me.last_name
  OWNER_ID =me .id #line:527:OWNER_ID = me.id
  DEFAULT_NAME =name #line:528:DEFAULT_NAME = name
  try :#line:529:try:
    @tgbot .on (NewMessage (pattern ='/start'))#line:531:@tgbot.on(NewMessage(pattern='/start'))
    async def start_bot_handler (O0OO000O0000OOO00 ):#line:532:async def start_bot_handler(event):
      if not O0OO000O0000OOO00 .message .from_id ==uid :#line:533:if not event.message.from_id == uid:
        await O0OO000O0000OOO00 .reply (f'`Merhaba ben` @TeloidUserBot`! Ben sahibime (`@{me.username}`) yardımcı olmak için varım, yaani sana yardımcı olamam :/ Ama sen de bir Teloid açabilirsin; Kanala bak` @TeloidUserBot')#line:536:)
      else :#line:537:else:
        await O0OO000O0000OOO00 .reply (f'`Tengri save Turks! Teloid working... `')#line:538:await event.reply(f'`Tengri save Turks! Teloid working... `')
    @tgbot .on (InlineQuery )#line:540:@tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler (O0OO000O0O00000OO ):#line:541:async def inline_handler(event):
      OO0O0000000OO00OO =O0OO000O0O00000OO .builder #line:542:builder = event.builder
      OOOOO0O00O0O0OO00 =None #line:543:result = None
      OOO0O00O0OO000000 =O0OO000O0O00000OO .text #line:544:query = event.text
      if O0OO000O0O00000OO .query .user_id ==uid and OOO0O00O0OO000000 =="@TeloidUserBot":#line:545:if event.query.user_id == uid and query == "@TeloidUserBot":
        O0000OO0000OOO00O =OOO0O00O0OO000000 [::-1 ]#line:546:rev_text = query[::-1]
        OOOOO00OO00O00OO0 =(butonlastir (0 ,sorted (CMD_HELP )))#line:547:veriler = (butonlastir(0, sorted(CMD_HELP)))
        OOOOO0O00O0O0OO00 =await OO0O0000000OO00OO .article (f"Lütfen Sadece .yardım Komutu İle Kullanın",text =f"**En Gelişmiş UserBot!** [Teloid](https://t.me/TeloidUserBot) __Çalışıyor...__\n\n**Yüklenen Modül Sayısı:** `{len(CMD_HELP)}`\n**Sayfa:** 1/{OOOOO00OO00O00OO0[0]}",buttons =OOOOO00OO00O00OO0 [1 ],link_preview =False )#line:553:link_preview=False)
      elif OOO0O00O0OO000000 .startswith ("http"):#line:554:elif query.startswith("http"):
        O0OO0O0OOO0OOO0O0 =OOO0O00O0OO000000 .split (" ")#line:555:parca = query.split(" ")
        OOOOO0O00O0O0OO00 =OO0O0000000OO00OO .article ("Dosya Yüklendi",text =f"**Dosya başarılı bir şekilde {O0OO0O0OOO0OOO0O0[2]} sitesine yüklendi!**\n\nYükleme zamanı: {O0OO0O0OOO0OOO0O0[1][:3]} saniye\n[‏‏‎ ‎]({O0OO0O0OOO0OOO0O0[0]})",buttons =[[custom .Button .url ('URL',O0OO0O0OOO0OOO0O0 [0 ])]],link_preview =True )#line:561:link_preview=True)
      else :#line:562:else:
        OOOOO0O00O0O0OO00 =OO0O0000000OO00OO .article ("@TeloidUserBot",text ="""@TeloidUserBot'u kullanmayı deneyin!
Hesabınızı bot'a çevirebilirsiniz ve bunları kullanabilirsiniz. Unutmayın, siz başkasının botunu yönetemezsiniz! Alttaki GitHub adresinden tüm kurulum detayları anlatılmıştır.""",buttons =[[custom .Button .url ("Kanala Katıl","https://t.me/TeloidUserBot"),custom .Button .url ("Gruba Katıl","https://t.me/RobotgerSupport")],[custom .Button .url ("GitHub","https://github.com/Robotger/TeloidUserBot")]],link_preview =False )#line:575:link_preview=False)
      await O0OO000O0O00000OO .answer ([OOOOO0O00O0O0OO00 ]if OOOOO0O00O0O0OO00 else None )#line:576:await event.answer([result] if result else None)
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"sayfa\((.+?)\)")))#line:578:@tgbot.on(callbackquery.CallbackQuery(data=compile(b"sayfa\((.+?)\)")))
    async def sayfa (OO0O00O0OO000OO0O ):#line:579:async def sayfa(event):
      if not OO0O00O0OO000OO0O .query .user_id ==uid :#line:580:if not event.query.user_id == uid:
        return await OO0O00O0OO000OO0O .answer ("❌ Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:584:alert=True)
      OO00OOOO00O0OO0O0 =int (OO0O00O0OO000OO0O .data_match .group (1 ).decode ("UTF-8"))#line:585:sayfa = int(event.data_match.group(1).decode("UTF-8"))
      OOOO000OOOO00OOOO =butonlastir (OO00OOOO00O0OO0O0 ,CMD_HELP )#line:586:veriler = butonlastir(sayfa, CMD_HELP)
      await OO0O00O0OO000OO0O .edit (f"** En Gelişmiş UserBot!** [Teloid](https://t.me/TeloidUserBot) __Çalışıyor...__\n\n**Yüklenen Modül Sayısı:** `{len(CMD_HELP)}`\n**Sayfa:** {OO00OOOO00O0OO0O0 + 1}/{OOOO000OOOO00OOOO[0]}",buttons =OOOO000OOOO00OOOO [1 ],link_preview =False )#line:590:link_preview=False)
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"bilgi\[(\d*)\]\((.*)\)")))#line:593:callbackquery.CallbackQuery(data=compile(b"bilgi\[(\d*)\]\((.*)\)")))
    async def bilgi (O0O00O00OO00000OO ):#line:594:async def bilgi(event):
      if not O0O00O00OO00000OO .query .user_id ==uid :#line:595:if not event.query.user_id == uid:
        return await O0O00O00OO00000OO .answer ("❌  Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:599:alert=True)
      OO000000OO00O000O =int (O0O00O00OO00000OO .data_match .group (1 ).decode ("UTF-8"))#line:601:sayfa = int(event.data_match.group(1).decode("UTF-8"))
      O00O000OO000000O0 =O0O00O00OO00000OO .data_match .group (2 ).decode ("UTF-8")#line:602:komut = event.data_match.group(2).decode("UTF-8")
      try :#line:603:try:
        O00O00O000O00OOOO =[custom .Button .inline ("🔹 "+O0OOOO0OO00O0O000 [0 ],data =f"komut[{O00O000OO000000O0}[{OO000000OO00O000O}]]({O0OOOO0OO00O0O000[0]})")for O0OOOO0OO00O0O000 in CMD_HELP_BOT [O00O000OO000000O0 ]['commands'].items ()]#line:608:]
      except KeyError :#line:609:except KeyError:
        return await O0O00O00OO00000OO .answer ("❌ Bu modüle açıklama yazılmamış.",cache_time =0 ,alert =True )#line:612:alert=True)
      O00O00O000O00OOOO =[O00O00O000O00OOOO [OO0O00OOOOOO000O0 :OO0O00OOOOOO000O0 +2 ]for OO0O00OOOOOO000O0 in range (0 ,len (O00O00O000O00OOOO ),2 )]#line:614:butonlar = [butonlar[i:i + 2] for i in range(0, len(butonlar), 2)]
      O00O00O000O00OOOO .append ([custom .Button .inline ("◀️ Geri",data =f"sayfa({OO000000OO00O000O})")])#line:616:[custom.Button.inline("◀️ Geri", data=f"sayfa({sayfa})")])
      await O0O00O00OO00000OO .edit (f"**📗 Dosya:** `{O00O000OO000000O0}`\n**🔢 Komut Sayısı:** `{len(CMD_HELP_BOT[O00O000OO000000O0]['commands'])}`",buttons =O00O00O000O00OOOO ,link_preview =False )#line:620:link_preview=False)
    @tgbot .on (callbackquery .CallbackQuery (data =compile (b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))#line:624:data=compile(b"komut\[(.*)\[(\d*)\]\]\((.*)\)")))
    async def komut (OO00000000O000O00 ):#line:625:async def komut(event):
      if not OO00000000O000O00 .query .user_id ==uid :#line:626:if not event.query.user_id == uid:
        return await OO00000000O000O00 .answer ("❌ Hey! Benim mesajlarımı düzenlemeye kalkma! Kendine bir @TeloidUserBot kur.",cache_time =0 ,alert =True )#line:630:alert=True)
      O000OO0OOO0000O00 =OO00000000O000O00 .data_match .group (1 ).decode ("UTF-8")#line:632:cmd = event.data_match.group(1).decode("UTF-8")
      OOO0OO0O0O0000000 =int (OO00000000O000O00 .data_match .group (2 ).decode ("UTF-8"))#line:633:sayfa = int(event.data_match.group(2).decode("UTF-8"))
      O0OOOO00OOO00OO0O =OO00000000O000O00 .data_match .group (3 ).decode ("UTF-8")#line:634:komut = event.data_match.group(3).decode("UTF-8")
      OO00O0O0OO00OO0OO =f"**📗 Dosya:** `{O000OO0OOO0000O00}`\n"#line:636:result = f"**📗 Dosya:** `{cmd}`\n"
      if CMD_HELP_BOT [O000OO0OOO0000O00 ]['info']['info']=='':#line:637:if CMD_HELP_BOT[cmd]['info']['info'] == '':
        if not CMD_HELP_BOT [O000OO0OOO0000O00 ]['info']['warning']=='':#line:638:if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
          OO00O0O0OO00OO0OO +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[O000OO0OOO0000O00]['info']['official'] else '❌'}\n"#line:639:result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
          OO00O0O0OO00OO0OO +=f"**⚠️ Uyarı:** {CMD_HELP_BOT[O000OO0OOO0000O00]['info']['warning']}\n\n"#line:640:result += f"**⚠️ Uyarı:** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
        else :#line:641:else:
          OO00O0O0OO00OO0OO +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[O000OO0OOO0000O00]['info']['official'] else '❌'}\n\n"#line:642:result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
      else :#line:643:else:
        OO00O0O0OO00OO0OO +=f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[O000OO0OOO0000O00]['info']['official'] else '❌'}\n"#line:644:result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
        if not CMD_HELP_BOT [O000OO0OOO0000O00 ]['info']['warning']=='':#line:645:if not CMD_HELP_BOT[cmd]['info']['warning'] == '':
          OO00O0O0OO00OO0OO +=f"**⚠️ Uyarı:** {CMD_HELP_BOT[O000OO0OOO0000O00]['info']['warning']}\n"#line:646:result += f"**⚠️ Uyarı:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
        OO00O0O0OO00OO0OO +=f"**ℹ️ Info:** {CMD_HELP_BOT[O000OO0OOO0000O00]['info']['info']}\n\n"#line:647:result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"
      O00O0O00O0OOO00OO =CMD_HELP_BOT [O000OO0OOO0000O00 ]['commands'][O0OOOO00OOO00OO0O ]#line:649:command = CMD_HELP_BOT[cmd]['commands'][komut]
      if O00O0O00O0OOO00OO ['params']is None :#line:650:if command['params'] is None:
        OO00O0O0OO00OO0OO +=f"**🛠 Komut:** `{PATTERNS[:1]}{O00O0O00O0OOO00OO['command']}`\n"#line:651:result += f"**🛠 Komut:** `{PATTERNS[:1]}{command['command']}`\n"
      else :#line:652:else:
        OO00O0O0OO00OO0OO +=f"**🛠 Komut:** `{PATTERNS[:1]}{O00O0O00O0OOO00OO['command']} {O00O0O00O0OOO00OO['params']}`\n"#line:653:result += f"**🛠 Komut:** `{PATTERNS[:1]}{command['command']} {command['params']}`\n"
      if O00O0O00O0OOO00OO ['example']is None :#line:655:if command['example'] is None:
        OO00O0O0OO00OO0OO +=f"**💬 Açıklama:** `{O00O0O00O0OOO00OO['usage']}`\n\n"#line:656:result += f"**💬 Açıklama:** `{command['usage']}`\n\n"
      else :#line:657:else:
        OO00O0O0OO00OO0OO +=f"**💬 Açıklama:** `{O00O0O00O0OOO00OO['usage']}`\n"#line:658:result += f"**💬 Açıklama:** `{command['usage']}`\n"
        OO00O0O0OO00OO0OO +=f"**⌨️ Örnek:** `{PATTERNS[:1]}{O00O0O00O0OOO00OO['example']}`\n\n"#line:659:result += f"**⌨️ Örnek:** `{PATTERNS[:1]}{command['example']}`\n\n"
      await OO00000000O000O00 .edit (OO00O0O0OO00OO0OO ,buttons =[custom .Button .inline ("◀️ Geri",data =f"bilgi[{OOO0OO0O0O0000000}]({O000OO0OOO0000O00})")],link_preview =False )#line:666:link_preview=False)
  except Exception as e :#line:667:except Exception as e:
    pass #line:668:pass
"""try:
        bot.loop.run_until_complete(check_botlog_chatid())
except:
        LOGS.info(
            "BOTLOG_CHATID ortam değişkeni geçerli bir varlık değildir. "
            "Ortam değişkenlerinizi / config.env dosyanızı kontrol edin."
        )
        quit(1)"""#line:676:quit(1)"""
SON_GORULME =0 #line:681:SON_GORULME = 0
COUNT_MSG =0 #line:682:COUNT_MSG = 0
USERS ={}#line:683:USERS = {}
MYID =uid #line:684:MYID = uid
ForceVer =forceVer #line:685:ForceVer = forceVer
upVer =int (upVer [0 ])#line:686:upVer = int(upVer[0])
BRAIN_CHECKER =[]#line:687:BRAIN_CHECKER = []
COUNT_PM ={}#line:688:COUNT_PM = {}
LASTMSG ={}#line:689:LASTMSG = {}
CMD_LIST ={}#line:690:CMD_LIST = {}
FUP =True #line:691:FUP = True
ENABLE_KILLME =True #line:692:ENABLE_KILLME = True
ISAFK =False #line:693:ISAFK = False
AFKREASON =None #line:694:AFKREASON = None
ZALG_LIST =[["̖"," ̗"," ̘"," ̙"," ̜"," ̝"," ̞"," ̟"," ̠"," ̤"," ̥"," ̦"," ̩"," ̪"," ̫"," ̬"," ̭"," ̮"," ̯"," ̰"," ̱"," ̲"," ̳"," ̹"," ̺"," ̻"," ̼"," ͅ"," ͇"," ͈"," ͉"," ͍"," ͎"," ͓"," ͔"," ͕"," ͖"," ͙"," ͚"," ",],[" ̍"," ̎"," ̄"," ̅"," ̿"," ̑"," ̆"," ̐"," ͒"," ͗"," ͑"," ̇"," ̈"," ̊"," ͂"," ̓"," ̈́"," ͊"," ͋"," ͌"," ̃"," ̂"," ̌"," ͐"," ́"," ̋"," ̏"," ̽"," ̉"," ͣ"," ͤ"," ͥ"," ͦ"," ͧ"," ͨ"," ͩ"," ͪ"," ͫ"," ͬ"," ͭ"," ͮ"," ͯ"," ̾"," ͛"," ͆"," ̚"],[" ̕"," ̛"," ̀"," ́"," ͘"," ̡"," ̢"," ̧"," ̨"," ̴"," ̵"," ̶"," ͜"," ͝"," ͞"," ͟"," ͠"," ͢"," ̸"," ̷"," ͡",]]#line:766:]]
