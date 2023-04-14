# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 

""" Internet ile alakalı bilgileri edinmek için kullanılan UserBot modülüdür. """

from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP, ASISTAN, MYID
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("www")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ .speed komutu sunucu hızını tespit etmek için SpeedTest kullanır. """
    await spd.edit(LANG['SPEED'])
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    result = test.results.dict()

    await spd.edit("`"
                   f"{LANG['STARTED_TIME']}"
                   f"{result['timestamp']} \n\n"
                   f"{LANG['DOWNLOAD_SPEED']}"
                   f"{speed_convert(result['download'])} \n"
                   f"{LANG['UPLOAD_SPEED']}"
                   f"{speed_convert(result['upload'])} \n"
                   "Ping: "
                   f"{result['ping']} \n"
                   f"{LANG['ISP']}"
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Merhaba Owen, baytları okuyamıyor musun?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.dc$")
async def neardc(event):
    """ .dc komutu en yakın datacenter bilgisini verir. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Şehir : `{result.country}`\n"
                     f"En yakın datacenter : `{result.nearest_dc}`\n"
                     f"Şu anki datacenter : `{result.this_dc}`")


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ .ping komutu userbotun ping değerini herhangi bir sohbette gösterebilir.  """
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))

@register(incoming=True, from_users=ASISTAN, pattern="^.ping$")
async def asistanping(ups):
    if ups.is_reply:
        reply = await ups.get_reply_message()
        reply_user = await ups.client.get_entity(reply.from_id)
        ren = reply_user.id
        if ren == MYID:
            "Asistan pinge bakıyor"
            start = datetime.now()
            usp = await ups.reply("`Pong!`")
            end = datetime.now()
            duration = (end - start).microseconds / 1000
            await usp.edit("`Pong!\n%sms`" % (duration))
        else:
            return
    else:
         return

CmdHelp('www').add_command(
    'speed', None, LANG['W1']
).add_command(
    'dc', None, LANG['W2']
).add_command(
    'ping', None, LANG['W3']
).add()