# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 

""" Filtre komutlarını içeren UserBot modülüdür. """

from asyncio import sleep
import re
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, BLACKLIST_CHAT
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("filter")

# ████████████████████████████████ #

SMART_OPEN = '"'
SMART_CLOSE = '"'
START_CHAR = ('\'', '"', SMART_OPEN)

def remove_escapes(text: str):
    counter = 0
    res = ""
    is_escaped = False
    while counter < len(text):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
        counter += 1
    return res

def split_quotes(text: str):
    if any(text.startswith(char) for char in START_CHAR):
        counter = 1  # ignore first char -> is some kind of quote
        while counter < len(text):
            if text[counter] == "\\":
                counter += 1
            elif text[counter] == text[0] or (text[0] == SMART_OPEN and text[counter] == SMART_CLOSE):
                break
            counter += 1
        else:
            return text.split(None, 1)

        # 1 to avoid starting quote, and counter is exclusive so avoids ending
        key = remove_escapes(text[1:counter].strip())
        # index will be in range, or `else` would have been executed and returned
        rest = text[counter + 1:].strip()
        if not key:
            key = text[0] + text[0]
        return list(filter(None, [key, rest]))
    else:
        return text.split(None, 1)


@register(incoming=True, disable_edited=True, disable_errors=True)
async def filter_incoming_handler(handler):
    """ Gelen mesajın filtre tetikleyicisi içerip içermediğini kontrol eder """
    try:
        if not (await handler.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.filter_sql import get_filters
            except AttributeError:
                await handler.edit("`Bot Non-SQL modunda çalışıyor!!`")
                return
            name = handler.raw_text
            if handler.chat_id == -1001197341555 or handler.chat_id == -1001431607309:
                return
            elif handler.chat_id in BLACKLIST_CHAT:
                return

            filters = get_filters(handler.chat_id)
            if not filters:
                filters = get_filters("GENEL")
                if not filters:
                    return

            for trigger in filters:
                pro = re.fullmatch(trigger.keyword, name, flags=re.IGNORECASE)
                if pro and trigger.f_mesg_id:
                    msg_o = await handler.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id))
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger.reply:
                    await handler.reply(trigger.reply)
    except AttributeError:
        pass

@register(outgoing=True, pattern="^.genelfilter (.*)")
async def genelfilter(event):
    try:
        from userbot.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await event.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    mesj = split_quotes(event.pattern_match.group(1))
    if event.chat_id == -1001197341555 or event.chat_id == -1001431607309:
        await event.edit("`Kusura Bakma Ama Resmi Robotger Grubunda Genel Filtre Eklenemez!`")
        return
    else:
        
        if len(mesj) != 0:
            keyword = mesj[0]
            try:
                string = mesj[1]
            except IndexError:
                string = ""
        else:
            await event.edit(LANG['GENEL_USAGE'])
            return

        msg = await event.get_reply_message()
        msg_id = None
        if msg and msg.media and not string:
            if BOTLOG_CHATID:
                await event.client.send_message(
                    BOTLOG_CHATID, f"#GENELFILTER\
                \nGrup ID: {event.chat_id}\
                \nFiltre: {keyword}\
                \n\nBu mesaj filtrenin cevaplanması için kaydedildi, lütfen bu mesajı silmeyin!"
                )
                msg_o = await event.client.forward_messages(
                    entity=BOTLOG_CHATID,
                    messages=msg,
                    from_peer=event.chat_id,
                    silent=True)
                msg_id = msg_o.id
            else:
                await event.edit(
                    LANG['NEED_BOTLOG']
                )
                return
        elif event.reply_to_msg_id and not string:
            rep_msg = await event.get_reply_message()
            string = rep_msg.text
        success = " **{}** `{} {}`"
        if add_filter("GENEL", keyword, string, msg_id) is True:
            await event.edit(success.format(keyword, LANG['GENEL_FILTER'], LANG['ADDED']))
        else:
            await event.edit(success.format(keyword, LANG['GENEL_FILTER'], LANG['UPDATED']))


@register(outgoing=True, pattern="^.filter (.*)")
async def add_new_filter(new_handler):
    """ .filter komutu bir sohbete yeni filtreler eklemeye izin verir """
    try:
        from userbot.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await new_handler.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    mesj = split_quotes(new_handler.pattern_match.group(1))
    if new_handler.chat_id == -1001197341555 or new_handler.chat_id == -1001431607309:
        await new_handler.edit("`Kusura Bakma Ama Resmi Robotger Grubunda Filtre Eklenemez!`")
        return
    else:

        if len(mesj) != 0:
            keyword = mesj[0]
            try:
                string = mesj[1]
            except IndexError:
                string = ""
        else:
            await new_handler.edit(LANG['FILTER_USAGE'])
            return

        msg = await new_handler.get_reply_message()
        msg_id = None
        if msg and msg.media and not string:
            if BOTLOG_CHATID:
                await new_handler.client.send_message(
                    BOTLOG_CHATID, f"#FILTER\
                \nGrup ID: {new_handler.chat_id}\
                \nFiltre: {keyword}\
                \n\nBu mesaj filtrenin cevaplanması için kaydedildi, lütfen bu mesajı silmeyin!"
                )
                msg_o = await new_handler.client.forward_messages(
                    entity=BOTLOG_CHATID,
                    messages=msg,
                    from_peer=new_handler.chat_id,
                    silent=True)
                msg_id = msg_o.id
            else:
                await new_handler.edit(
                    LANG['NEED_BOTLOG']
                )
                return
        elif new_handler.reply_to_msg_id and not string:
            rep_msg = await new_handler.get_reply_message()
            string = rep_msg.text
        success = " **{}** `{} {}`"
        if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
            await new_handler.edit(success.format(keyword, LANG['GENEL_FILTER'], LANG['ADDED']))
        else:
            await new_handler.edit(success.format(keyword, LANG['GENEL_FILTER'], LANG['UPDATED']))

@register(outgoing=True, pattern="^.genelstop (\w*)")
async def remove_a_genel(r_handler):
    """ .stop komutu bir filtreyi durdurmanızı sağlar. """
    try:
        from userbot.modules.sql_helper.filter_sql import remove_filter
    except AttributeError:
        await r_handler.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    mesj = r_handler.text
    if '"' in mesj:
        filt = re.findall(r"\"(.*)\"", mesj)[0]
    else:
        filt = r_handler.pattern_match.group(1)

    if not remove_filter("GENEL", filt):
        await r_handler.edit(" **{}** `{}`".format(filt, LANG['NOT_FOUND']))
    else:
        await r_handler.edit(
            "**{}** `{}`".format(filt, LANG['DELETED']))

@register(outgoing=True, pattern="^.stop (\w*)")
async def remove_a_filter(r_handler):
    """ .stop komutu bir filtreyi durdurmanızı sağlar. """
    try:
        from userbot.modules.sql_helper.filter_sql import remove_filter
    except AttributeError:
        await r_handler.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    mesj = r_handler.text
    if '"' in mesj:
        filt = re.findall(r"\"(.*)\"", mesj)[0]
    else:
        filt = r_handler.pattern_match.group(1)

    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit(" **{}** `{}`".format(filt, LANG['NOT_FOUND']))
    else:
        await r_handler.edit(
            "**{}** `{}`".format(filt, LANG['DELETED']))

@register(outgoing=True, pattern="^.genelfilters$")
async def genelfilters_active(event):
    """ .genelfilters komutu bir sohbetteki tüm aktif filtreleri gösterir. """
    try:
        from userbot.modules.sql_helper.filter_sql import get_filters
    except AttributeError:
        await event.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    transact = LANG['GENELFILTERS']
    filters = get_filters("GENEL")
    for filt in filters:
        if transact == LANG['GENELFILTERS']:
            transact = f"{LANG['GENEL_FILTERS']}\n"
            transact += "`{}`\n".format(filt.keyword)
        else:
            transact += "`{}`\n".format(filt.keyword)

    await event.edit(transact)

@register(outgoing=True, pattern="^.filters$")
async def filters_active(event):
    """ .filters komutu bir sohbetteki tüm aktif filtreleri gösterir. """
    try:
        from userbot.modules.sql_helper.filter_sql import get_filters
    except AttributeError:
        await event.edit("`Bot Non-SQL modunda çalışıyor!!`")
        return
    transact = LANG['FILTERS']
    filters = get_filters(event.chat_id)
    for filt in filters:
        if transact == LANG['FILTERS']:
            transact = f"{LANG['_FILTERS']}\n"
            transact += "`{}`\n".format(filt.keyword)
        else:
            transact += "`{}`\n".format(filt.keyword)

    await event.edit(transact)

CmdHelp('filter').add_command(
    'filters', None, LANG['FLTR1']
).add_command(
    'filter', LANG['FLTR2'], LANG['FLTR3'], LANG['FLTR4']
).add_command(
    'stop', LANG['FLTR5'], LANG['FLTR6']
).add_command(
    'genelfilter', LANG['FLTR7'], LANG['FLTR8']
).add_command(
    '.genelstop', LANG['FLTR9'], LANG['FLTR0']
).add()
