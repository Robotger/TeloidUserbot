""#line:10
import re #line:11
from requests import get #line:12
import sys #line:13
from asyncio import create_subprocess_shell as asyncsubshell #line:14
from asyncio import subprocess as asyncsub #line:15
from os import remove #line:16
from time import gmtime ,strftime #line:17
from traceback import format_exc #line:18
from telethon import events #line:19
import base64 #line:20
from userbot import bot ,BOTLOG_CHATID ,LOGSPAMMER ,PATTERNS ,TELOID_VERSION ,ForceVer #line:21
from telethon .tl .functions .channels import JoinChannelRequest #line:22
from userbot import PATTERNS ,DEVS ,bot #line:23
import inspect #line:24
from pathlib import Path #line:25
CMD_LIST ={}#line:28
def teloid_cmd (pattern =None ,command =None ,**O0O00000O00O0O00O ):#line:30
    O0O00000O00O0O00O ["func"]=lambda OO0O0O0O00O00O00O :OO0O0O0O00O00O00O .via_bot_id is None #line:31
    O0OO00000O0O00OOO =inspect .stack ()#line:32
    O0O00O0OO00O0O000 =O0OO00000O0O00OOO [1 ]#line:33
    O0O00000OOO00OOO0 =Path (O0O00O0OO00O0O000 .filename )#line:34
    O0O00000OOO00OOO0 =O0O00000OOO00OOO0 .stem .replace (".py","")#line:35
    O0O00000O00O0O00O .get ("allow_sudo",False )#line:36
    if pattern is not None :#line:37
        if pattern .startswith (r"\#"):#line:38
            O0O00000O00O0O00O ["pattern"]=re .compile (pattern )#line:39
        elif pattern .startswith (r"^"):#line:40
            O0O00000O00O0O00O ["pattern"]=re .compile (pattern )#line:41
            O0O000OO0O0000000 =pattern .replace ("$","").replace ("^","").replace ("\\","")#line:42
            try :#line:43
                CMD_LIST [O0O00000OOO00OOO0 ].append (O0O000OO0O0000000 )#line:44
            except BaseException :#line:45
                CMD_LIST .update ({O0O00000OOO00OOO0 :[O0O000OO0O0000000 ]})#line:46
        else :#line:47
            if len (PATTERNS )==2 :#line:48
                O0OOO0OOO0OO00OOO ="^"+PATTERNS #line:49
                OOO00O0OOOOO00OOO =PATTERNS [1 ]#line:50
            elif len (PATTERNS )==1 :#line:51
                O0OOO0OOO0OO00OOO ="^\\"+PATTERNS #line:52
                OOO00O0OOOOO00OOO =PATTERNS #line:53
            O0O00000O00O0O00O ["pattern"]=re .compile (O0OOO0OOO0OO00OOO +pattern )#line:54
            if command is not None :#line:55
                O0O000OO0O0000000 =OOO00O0OOOOO00OOO +command #line:56
            else :#line:57
                O0O000OO0O0000000 =((OOO00O0OOOOO00OOO +pattern ).replace ("$","").replace ("\\","").replace ("^",""))#line:60
            try :#line:61
                CMD_LIST [O0O00000OOO00OOO0 ].append (O0O000OO0O0000000 )#line:62
            except BaseException :#line:63
                CMD_LIST .update ({O0O00000OOO00OOO0 :[O0O000OO0O0000000 ]})#line:64
    if "allow_edited_updates"in O0O00000O00O0O00O and O0O00000O00O0O00O ["allow_edited_updates"]:#line:66
        del O0O00000O00O0O00O ["allow_edited_updates"]#line:67
    return events .NewMessage (**O0O00000O00O0O00O )#line:69
def command (**O00O0OOOOOO000OO0 ):#line:72
    O00O0OOOOOO000OO0 ["func"]=lambda OOO00O00OOO0O0O00 :OOO00O00OOO0O0O00 .via_bot_id is None #line:73
    OO00O00OO000O0O0O =inspect .stack ()#line:75
    OO0O0OOO0O0OOOOOO =OO00O00OO000O0O0O [1 ]#line:76
    O0O000OOO00O0000O =Path (OO0O0OOO0O0OOOOOO .filename )#line:77
    O0O000OOO00O0000O =O0O000OOO00O0000O .stem .replace (".py","")#line:78
    O00O000O0OO0OO00O =O00O0OOOOOO000OO0 .get ("pattern")#line:80
    O0OO0OOOOO0000OOO =O00O0OOOOOO000OO0 .get ("allow_edited_updates",False )#line:81
    O00O0OOOOOO000OO0 ["incoming"]=O00O0OOOOOO000OO0 .get ("incoming",False )#line:82
    O00O0OOOOOO000OO0 ["outgoing"]=True #line:83
    if bool (O00O0OOOOOO000OO0 ["incoming"]):#line:84
        O00O0OOOOOO000OO0 ["outgoing"]=False #line:85
    try :#line:87
        if O00O000O0OO0OO00O is not None and not O00O000O0OO0OO00O .startswith ("(?i)"):#line:88
            O00O0OOOOOO000OO0 ["pattern"]="(?i)"+O00O000O0OO0OO00O #line:89
    except BaseException :#line:90
        pass #line:91
    O0O00O0O0O000OO0O =re .compile ("(.*)")#line:93
    if O00O000O0OO0OO00O is not None :#line:94
        try :#line:95
            O000OOOO0OO000O00 =re .search (O0O00O0O0O000OO0O ,O00O000O0OO0OO00O )#line:96
            try :#line:97
                O000OOOO0OO000O00 =O000OOOO0OO000O00 .group (1 ).replace ("$","").replace ("\\","").replace ("^","")#line:98
            except BaseException :#line:99
                pass #line:100
            try :#line:101
                CMD_LIST [O0O000OOO00O0000O ].append (O000OOOO0OO000O00 )#line:102
            except BaseException :#line:103
                CMD_LIST .update ({O0O000OOO00O0000O :[O000OOOO0OO000O00 ]})#line:104
        except BaseException :#line:105
            pass #line:106
def register (**O0OOO0OO0OOOO0O00 ):#line:109
    ""#line:110
    O0OO0O0000O0O00OO =O0OOO0OO0OOOO0O00 .get ('pattern',None )#line:111
    O0O0OO00OO00OOO00 =O0OOO0OO0OOOO0O00 .get ('disable_edited',False )#line:112
    OOO000O000000000O =O0OOO0OO0OOOO0O00 .get ('groups_only',False )#line:113
    OO000000OO0O000O0 =O0OOO0OO0OOOO0O00 .get ('trigger_on_fwd',False )#line:114
    OO0O0OO0O0O0000O0 =O0OOO0OO0OOOO0O00 .get ('trigger_on_inline',False )#line:115
    OOOO00OO000000O0O =O0OOO0OO0OOOO0O00 .get ('disable_errors',False )#line:116
    if O0OO0O0000O0O00OO :#line:118
        O0OOO0OO0OOOO0O00 ["pattern"]=O0OO0O0000O0O00OO .replace ("^.","^["+PATTERNS +"]")#line:119
    if "disable_edited"in O0OOO0OO0OOOO0O00 :#line:120
        del O0OOO0OO0OOOO0O00 ['disable_edited']#line:121
    if "ignore_unsafe"in O0OOO0OO0OOOO0O00 :#line:123
        del O0OOO0OO0OOOO0O00 ['ignore_unsafe']#line:124
    if "groups_only"in O0OOO0OO0OOOO0O00 :#line:126
        del O0OOO0OO0OOOO0O00 ['groups_only']#line:127
    if "disable_errors"in O0OOO0OO0OOOO0O00 :#line:129
        del O0OOO0OO0OOOO0O00 ['disable_errors']#line:130
    if "trigger_on_fwd"in O0OOO0OO0OOOO0O00 :#line:132
        del O0OOO0OO0OOOO0O00 ['trigger_on_fwd']#line:133
    if "trigger_on_inline"in O0OOO0OO0OOOO0O00 :#line:135
        del O0OOO0OO0OOOO0O00 ['trigger_on_inline']#line:136
    def OOOOO0OO00O00O000 (OOOO00000OOO00O00 ):#line:138
        async def OOO0OO0O0O0O0OO0O (OO00OO0OOOO0O0000 ):#line:139
            if OO00OO0OOOO0O0000 .out ==True :#line:142
              if ForceVer [1 ]!=sys .argv [0 ]:#line:143
                await OO00OO0OOOO0O0000 .edit ("**KOPYALANMIŞ USERBOT KULLANIMINA İZİN VERMİYORUZ‼️**\n\n**Lütfen Güvenliğiniz için orjinal [Teloid](https://t.me/teloiduserbot) botunu kullanın**\n\n**Powered By [Robotger](https://t.me/robotger)**")#line:144
                return #line:145
            else :#line:146
                pass #line:147
            if not LOGSPAMMER :#line:149
                O00OO00OO0O0O0O00 =OO00OO0OOOO0O0000 .chat_id #line:150
            else :#line:151
                O00OO00OO0O0O0O00 =BOTLOG_CHATID #line:152
            if not OO000000OO0O000O0 and OO00OO0OOOO0O0000 .fwd_from :#line:154
                return #line:155
            if OO00OO0OOOO0O0000 .via_bot_id and not OO0O0OO0O0O0000O0 :#line:157
                return #line:158
            if OOO000O000000000O and not OO00OO0OOOO0O0000 .is_group :#line:160
                await OO00OO0OOOO0O0000 .respond ("`⛔ Bunun bir grup olduğunu sanmıyorum. Bu plugini bir grupta dene! `")#line:161
                return #line:162
            try :#line:164
                await OOOO00000OOO00O00 (OO00OO0OOOO0O0000 )#line:165
            except events .StopPropagation :#line:168
                raise events .StopPropagation #line:169
            except KeyboardInterrupt :#line:170
                pass #line:171
            except AttributeError :#line:172
                pass #line:173
            except BaseException :#line:174
                if not OOOO00OO000000O0O :#line:175
                    O00OOO000OOO0OOOO =strftime ("%Y-%m-%d %H:%M:%S",gmtime ())#line:176
                    O0OO0O0O0O00O000O =str (OO00OO0OOOO0O0000 .text )#line:178
                    OO0O0OO0O00OO00O0 ="**🛑USERBOT HATA RAPORU🛑**\n"#line:179
                    O0OO0O0000OO0O000 ="[Teloid Destek Grubuna](https://t.me/RobotgerSupport)"#line:180
                    if len (O0OO0O0O0O00O000O )<10 :#line:181
                        OO0O0OO0O00OO00O0 +=f"\n**🗒️ Şu yüzden:** {O0OO0O0O0O00O000O}\n"#line:182
                    OO0O0OO0O00OO00O0 +="\nℹ️ İsterseniz, bunu bildirebilirsiniz."#line:183
                    OO0O0OO0O00OO00O0 +=f"- sadece bu mesajı {O0OO0O0000OO0O000} gönderin.\n"#line:184
                    OO0O0OO0O00OO00O0 +="Hata ve tarih haricinde hiçbir şey kayıt edilmez.\n"#line:185
                    OO0O0OO0000000OOO ="========== UYARI =========="#line:187
                    OO0O0OO0000000OOO +="\nBu dosya sadece burada yüklendi,"#line:188
                    OO0O0OO0000000OOO +="\nSadece hata ve tarih kısmını kaydettik,"#line:189
                    OO0O0OO0000000OOO +="\nGizliliğinize saygı duyuyoruz,"#line:190
                    OO0O0OO0000000OOO +="\nBurada herhangi bir gizli veri varsa"#line:191
                    OO0O0OO0000000OOO +="\nBu hata raporu olmayabilir, kimse verilerinize ulaşamaz.\n"#line:192
                    OO0O0OO0000000OOO +="--------USERBOT HATA GUNLUGU--------\n"#line:193
                    OO0O0OO0000000OOO +="\nTarih: "+O00OOO000OOO0OOOO #line:194
                    OO0O0OO0000000OOO +="\nGrup ID: "+str (OO00OO0OOOO0O0000 .chat_id )#line:195
                    OO0O0OO0000000OOO +="\nGönderen kişinin ID: "+str (OO00OO0OOOO0O0000 .sender_id )#line:196
                    OO0O0OO0000000OOO +="\n\nOlay Tetikleyici:\n"#line:197
                    OO0O0OO0000000OOO +=str (OO00OO0OOOO0O0000 .text )#line:198
                    OO0O0OO0000000OOO +="\n\nHata metni:\n"#line:199
                    OO0O0OO0000000OOO +=str (sys .exc_info ()[1 ])#line:200
                    OO0O0OO0000000OOO +="\n\n\nGeri izleme bilgisi:\n"#line:201
                    OO0O0OO0000000OOO +=str (format_exc ())#line:202
                    OO0O0OO0000000OOO +="\n\n--------USERBOT HATA GUNLUGU BITIS--------"#line:203
                    OO0O0OO0000000OOO +="\n\n================================\n"#line:204
                    OO0O0OO0000000OOO +=f"====== BOTVER : {TELOID_VERSION} ======\n"#line:205
                    OO0O0OO0000000OOO +="======  Powered by RobotgerDev   ======"#line:206
                    OO0O0OO0000000OOO +="================================"#line:207
                    O0OO00O0O0O0O0O00 ="git log --pretty=format:\"%an: %s\" -7"#line:209
                    OO0O0OO0000000OOO +="\n\n\nSon 7 commit:\n"#line:211
                    O0OO0000OOO00O000 =await asyncsubshell (O0OO00O0O0O0O0O00 ,stdout =asyncsub .PIPE ,stderr =asyncsub .PIPE )#line:215
                    O0OO00OO0O00O0OO0 ,O00OOOOOOO0OOO0O0 =await O0OO0000OOO00O000 .communicate ()#line:216
                    O0OOO0O000OO0O000 =str (O0OO00OO0O00O0OO0 .decode ().strip ())+str (O00OOOOOOO0OOO0O0 .decode ().strip ())#line:218
                    OO0O0OO0000000OOO +=O0OOO0O000OO0O000 #line:220
                    OO00O000OO0O0OOO0 =open ("error.log","w+")#line:222
                    OO00O000OO0O0OOO0 .write (OO0O0OO0000000OOO )#line:223
                    OO00O000OO0O0OOO0 .close ()#line:224
                    if LOGSPAMMER :#line:226
                        try :#line:227
                            await OO00OO0OOOO0O0000 .edit ("`❕ Üzgünüm, UserBot bir hatayla karşılaştı.\n ℹ️ Hata günlükleri UserBot günlük grubunda saklanır.`")#line:228
                        except :#line:229
                            pass #line:230
                    await OO00OO0OOOO0O0000 .client .send_file (O00OO00OO0O0O0O00 ,"error.log",caption =OO0O0OO0O00OO00O0 )#line:233
                    remove ("error.log")#line:235
            else :#line:236
                pass #line:237
        if bot :#line:238
            if not O0O0OO00OO00OOO00 :#line:239
                bot .add_event_handler (OOO0OO0O0O0O0OO0O ,events .MessageEdited (**O0OOO0OO0OOOO0O00 ))#line:240
            bot .add_event_handler (OOO0OO0O0O0O0OO0O ,events .NewMessage (**O0OOO0OO0OOOO0O00 ))#line:241
        return OOO0OO0O0O0O0OO0O #line:243
    return OOOOO0OO00O00O000 #line:245
