# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 
from userbot.cmdhelp import CmdHelp
from telethon.tl.types import *
from userbot.events import register

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("st")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.statis")
async def stats(e): 
   await e.edit("`Lütfen Bekleyin...`") 
   msg = str((await e.client.get_messages(e.chat_id, limit=0)).total) 
   img = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterPhotos())).total) 
   vid = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterVideo())).total) 
   msc = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterMusic())).total) 
   ses = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterVoice())).total) 
   rvid = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterRoundVideo())).total) 
   doc = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterDocument())).total) 
   url = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterUrl())).total) 
   gif = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterGif())).total) 
   geo = str((await e.client.get_messages(e.chat_id, limit=0, filter=InputMessagesFilterGeo())).total) 
   stat = f"✉️ **Mesajlar:** `{msg}`\n🖼️ **Fotoğraflar:** `{img}`\n📹 **Videolar:** `{vid}`\n🎵 **Muzikler:** `{msc}`\n🎤 **Sesli Mesajlar:** `{ses}`\n🎥 **Videolar:** `{rvid}`\n📂 **Dosyalar:** `{doc}`\n🔗 **Linkler:** `{url}`\n🎞️ **GIFler:** `{gif}`\n🗺 **Konumlar:** `{geo}`"
   await e.edit(stat)

CmdHelp('statistics').add_command('statis', None, LANG['ST1']).add()
