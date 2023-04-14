
# Copyright (C) 2022 RobotgerDev.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# TeloidUserBot

from datetime import datetime
from telethon import events
from userbot import OWNER_ID
from userbot.asisstant.events import lavan
import asyncio

@lavan(incoming=True, from_users=OWNER_ID, pattern="^/ping")
async def evnt (e):
    start = datetime.now()
    msg = await e.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")
    
    

