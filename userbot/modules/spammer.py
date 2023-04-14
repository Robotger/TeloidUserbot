# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 


import asyncio
import threading

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, BLACKLIST_CHAT
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("spam")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.tspam")
async def tmeme(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.reply("`Sence Ben Kendi Grubuma Spam Yapılmasına İzin Verirmiyim` \n(@erdewbey & @ByLeviAckerman) `Ben Spam Yapmaya Çalıştım``")
    message = e.text
    messageSplit = message.split(" ", 1)
    tspam = str(messageSplit[1])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()
    if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#TSPAM \n\n"
                "TSpam başarıyla gerçekleştirildi"
                )

@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.reply("`Sence Ben Kendi Grubuma Spam Yapılmasına İzin Verirmiyim` \n(@erdewbey & @ByLeviAckerman) `Ben Spam Yapmaya Çalıştım``")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#SPAM \n\n"
                "Spam başarıyla gerçekleştirildi"
                )
                               
@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.reply("`Sence Ben Kendi Grubuma Spam Yapılmasına İzin Verirmiyim` \n(@erdewbey & @ByLeviAckerman) `Ben Spam Yapmaya Çalıştım``")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit = message.split(" ", 2)
        counter = int(messageSplit[1])
        spam_message = str(messageSplit[2])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#BIGSPAM \n\n"
                "Bigspam başarıyla gerçekleştirildi"
                )
        
        
@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.reply("`Sence Ben Kendi Grubuma Spam Yapılmasına İzin Verirmiyim` \n(@erdewbey & @ByLeviAckerman) `Ben Spam Yapmaya Çalıştım``")
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#PICSPAM \n\n"
                "PicSpam başarıyla gerçekleştirildi"
                )


@register(outgoing=True, pattern="^.delayspam")
async def delayspammer(e):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.reply("`Sence Ben Kendi Grubuma Spam Yapılmasına İzin Verirmiyim` \n(@erdewbey & @ByLeviAckerman) `Ben Spam Yapmaya Çalıştım``")
    # Teşekkürler @ReversedPosix
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        messageSplit= message.split(" ", 3)
        spam_delay = float(messageSplit[1])
        counter = int(messageSplit[2])
        spam_message = str(messageSplit[3])
        from userbot.events import register
        await e.delete()
        delaySpamEvent = threading.Event()
        for i in range(1, counter):
            await e.respond(spam_message)
            delaySpamEvent.wait(spam_delay)
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DelaySPAM \n\n"
                "DelaySpam başarıyla gerçekleştirildi"
                )

@register(outgoing=True, pattern="^.mspam(?: |$)(.*)")
async def media_spam(event):
    if e.chat_id in BLACKLIST_CHAT:
        return await e.reply("`Sence Ben Kendi Grubuma Spam Yapılmasına İzin Verirmiyim` \n(@erdewbey & @ByLeviAckerman) `Ben Spam Yapmaya Çalıştım``")
    if event.fwd_from:
        return
    
    cmd = event.pattern_match.group(1)
    if len(cmd) < 1:
        await event.edit("`Lütfen bir sayı belirtin! Örnek: .mspam 10`") 
        return
    elif not cmd.isdigit():
        await event.edit("`Lütfen sadece sayı belirtin! Örnek: .mspam 10`") 
        return
    replymsg = await event.get_reply_message()
    if not event.reply_to_msg_id or not replymsg.media:
        await event.edit("`Lütfen bir medyaya yanıt verin. Bu ses, müzik, fotoğraf, sticker, gif, video olabilir.`") 
        return
    
    i = 0
    await event.delete()
    while i < int(cmd):
        await event.respond(replymsg)
        await asyncio.sleep(0.1)
        i += 1
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#MedyaSPAM \n\n"
            "MedyaSpam başarıyla gerçekleştirildi"
            )

CmdHelp('spammer').add_command(
    'tspam', LANG['S1'], LANG['S2']
).add_command(
    'spam', LANG['S3'], LANG['S4']
).add_command(
    'bigspam', LANG['S5'], LANG['S6']
).add_command(
    'picspam', LANG['S7'], LANG['S8']
).add_command(
    'mspam', LANG['S9'], LANG['S10']
).add_command(
    'delayspam', LANG['S11'], LANG['S12']
).add_command(
    'kill spam', None, LANG['S13'], None
).add_warning( LANG['S14']).add()
