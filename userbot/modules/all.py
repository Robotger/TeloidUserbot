# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 


from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from asyncio import sleep

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("all")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.all(?: |$)(.*)",groups_only=True)
async def _(q):
	if q.fwd_from:
		return
	if q.chat_id == -1001726719696:
		return
	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat):
		if not i.id in [1339844465, 1724329185, 1193186807]:
			if a_ == 5000:
				break
			a_+=1
			await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(seasons, i.first_name, i.id))
			await sleep(2.5)


@register(outgoing=True, pattern="^.alladmin(?: |$)(.*)", groups_only=True)
async def _(q):
	if q.fwd_from:
		return
	

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if not i.id in [1339844465, 1193186807]:
			if a_ == 50:
				break
			a_+=1
			await q.client.send_message(q.chat_id, "**{}**\n[{}](tg://user?id={})".format(seasons, i.first_name, i.id))
			await sleep(1.74)


CmdHelp('all').add_command(
	'all', (LANG['ALL1']), (LANG['ALL2'])
	).add_command(
	"alladmin", (LANG['ALLADMİN1']), (LANG['ALLADMİN2'])
    ).add_command(
    "kill all", None, (LANG['KİLLALL1'])
).add()

