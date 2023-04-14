# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 
#
# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("chat")

# ████████████████████████████████ #

""" Userid, chatid ve log komutlarını içeren UserBot modülü """

from asyncio import sleep
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, bot, BLACKLIST_CHAT
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from userbot.main import PLUGIN_MESAJLAR
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.id$")
async def useridgetter(target):
    """ .userid komutu belirlenen kullanıcının ID numarasını verir """
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit("**{}** {} \n**{}** `{}`".format(
            LANG['USERNAME'], name, LANG['ID'], user_id))


@register(outgoing=True, pattern="^.link(?: |$)(.*)")
async def permalink(mention):
    """ .link komutu belirlenen kullanıcının profil bağlantısını metin ile ulaşılabilir hale getirir """
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await mention.edit(f"[{custom}](tg://user?id={user.id})")
    else:
        tag = user.first_name.replace("\u2060",
                                      "") if user.first_name else user.username
        await mention.edit(f"[{tag}](tg://user?id={user.id})")


@register(outgoing=True, pattern="^.chatid$")
async def chatidgetter(chat):
    """ .chatid komutu belirlenen grubun ID numarasını verir """
    await chat.edit(f"{LANG['GROUP']} `" + str(chat.chat_id) + "`")


@register(outgoing=True, pattern=r"^.log(?: |$)([\s\S]*)")
async def log(log_text):
    """ .log komutu seçilen mesajı günlük grubuna gönderir """
    if BOTLOG:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"#LOG / Grup ID: {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await bot.send_message(BOTLOG_CHATID, textx)
        else:
            await log_text.edit("`Bununla ne yapmam gerekiyor ?`")
            return
        await log_text.edit("`Günlüğe Kaydedildi`")
    else:
        await log_text.edit(LANG['NEED_LOG'])
    await sleep(2)
    await log_text.delete()


@register(outgoing=True, pattern="^.kickme ?(.*)")
async def kickme(leave):
    if leave.chat_id in BLACKLIST_CHAT:
        return await leave.edit("**Sahibim kusura bakma ama burdan çıkamam resmi Robotger grubu burası**,\n\n**Bana gelen yeniliklerden haberdar olman için burada kalmam lazım.**")
    """ .kickme komutu gruptan çıkmaya yarar """
    sebep = leave.pattern_match.group(1)
    chat = await leave.get_chat()
    if sebep:
        await leave.edit(f"{PLUGIN_MESAJLAR['kickme']}\n **Reason:** `{sebep}`".format(
            id=chat.id,
            title=chat.title,
            member_count="Bilinmiyor" if chat.participants_count == None else (chat.participants_count - 1)
        ))
    else:
        await leave.edit(f"{PLUGIN_MESAJLAR['kickme']}".format(
            id=chat.id,
            title=chat.title,
            member_count="Bilinmiyor" if chat.participants_count == None else (chat.participants_count - 1)
        ))
    await leave.client.kick_participant(leave.chat_id, 'me')


@register(outgoing=True, pattern="^.unmutechat$")
async def unmute_chat(unm_e):
    """ .unmutechat komutu susturulmuş grubun sesini açar """
    try:
        from userbot.modules.sql_helper.keep_read_sql import unkread
    except AttributeError:
        await unm_e.edit('`SQL dışı modda çalışıyor!`')
        return
    unkread(str(unm_e.chat_id))
    await unm_e.edit(LANG['UNMUTED'])
    await sleep(2)
    await unm_e.delete()


@register(outgoing=True, pattern="^.mutechat$")
async def mute_chat(mute_e):
    """ .mutechat komutu grubu susturur """
    try:
        from userbot.modules.sql_helper.keep_read_sql import kread
    except AttributeError:
        await mute_e.edit("`SQL dışı modda çalışıyor!`")
        return
    await mute_e.edit(str(mute_e.chat_id))
    kread(str(mute_e.chat_id))
    await mute_e.edit(LANG['MUTED'])
    await sleep(2)
    await mute_e.delete()
    if BOTLOG:
        await mute_e.client.send_message(
            BOTLOG_CHATID,
            str(mute_e.chat_id) + " susturuldu.")


@register(incoming=True, disable_errors=True)
async def keep_read(message):
    """ Mute mantığı. """
    try:
        from userbot.modules.sql_helper.keep_read_sql import is_kread
    except AttributeError:
        return
    kread = is_kread()
    if kread:
        for i in kread:
            if i.groupid == str(message.chat_id):
                await message.client.send_read_acknowledge(message.chat_id)


# Regex-Ninja modülü için teşekkürler @Kandnub
regexNinja = False


@register(outgoing=True, pattern="^s/")
async def sedNinja(event):
    """Regex-ninja modülü için, s/ ile başlayan otomatik silme komutu"""
    if regexNinja:
        await sleep(.5)
        await event.delete()


@register(outgoing=True, pattern="^.regexninja (on|off)$")
async def sedNinjaToggle(event):
    """ Regex ninja modülünü etkinleştirir veya devre dışı bırakır. """
    global regexNinja
    if event.pattern_match.group(1) == "on":
        regexNinja = True
        await event.edit("`Regexbot için ninja modu etkinleştirdi.`")
        await sleep(1)
        await event.delete()
    elif event.pattern_match.group(1) == "off":
        regexNinja = False
        await event.edit("`Regexbot için ninja modu devre dışı bırakıldı.`")
        await sleep(1)
        await event.delete()

CmdHelp('chat').add_command(
    'chatid', LANG['CHAT1']
).add_command(
    'id', LANG['CHAT2']
).add_command(
    'kickme', LANG['CHAT4']
).add_command(
    'log', LANG['CHAT3']
).add_command(
    'unmutechat', LANG['CHAT5']
).add_command(
    'mutechat', LANG['CHAT6']
).add_command(
    'link', LANG['CHAT7'], LANG['CHAT8']
).add()
