def e_(fayl_adi, name, slep, siyahi):
	f = open(f"./TeloidUserBot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(misaki):
	for i in a:
		await misaki.edit(' '+str(i))
		sleep({slep})
Help = CmdHelp("TeloidUserBot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @TeloidUserBot tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def a_(fayl_adi, name, siyahi, slep):
	f = open(f"./TeloidUserBot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep
from telethon import events
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(misaki):
	text= " "
	for i in a:
		text+=i+"\\n"
		await misaki.edit(text)
		sleep({slep})
Help = CmdHelp("TeloidUserBot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @TeloidUserBot tarafından hazırlanmıştır.")
Help.add()
								""")
	return f.close()

def r_(fayl_adi, name, siyahi):
	f = open(f"./TeloidUserBot{fayl_adi}.py", "x")
	f.write(f"""from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from random import choice
a={siyahi}
@register(outgoing=True, pattern="^.{name}$")
async def _(misaki):
	random_ = choice(a)
	await misaki.client.send_file(misaki.chat_id, random_)
	await misaki.delete()
Help = CmdHelp("TeloidUserBot{fayl_adi}")
Help.add_command("{name}", None, "Bu plugin @TeloidUserBot tarafından hazırlanmıştır.")
Help.add()
		""")

def m_(fayl_adi, name, siyahi):
	f = open(f"./TeloidUserBot{fayl_adi}.py", "x")
	f.write("""from telethon import events
import asyncio
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import random
import os
IFACI = [{siyahi}]
@register(outgoing=True, pattern="^.{name}$")
async def misakimusic(misaki):
    
    
    await misaki.edit("`Sizin için  "+IFACI+"müziğini aktarıyorum`")
    try:
        results = await misaki.client.inline_query('deezermusicbot', '+IFACI+')
    except:
            await misaki.edit("`Bottan cevap alamadım`")
            return
    netice = False
    while netice is False:
            rast = random.choice(results)
            if rast.description == IFACI:
                await misaki.edit("`Müzik Yükleniyor!")
                yukle = await rast.download_media()
                await misaki.edit("`Yükleme tamamlandı!`")
                await misaki.client.send_file(misaki.chat_id, yukle, caption="@TeloidUserBot sizin için `"+rast.description+" - "+rast.title+"` müziğini seçti iyi dinlemeler. :)")
                await event.delete()
                os.remove(yukle)
                netice = True
Help = CmdHelp("TeloidUserBot{fayl_adi}")
Help.add_command("{name}", None, "Bu Plugin @TeloidUserBot Tərəfindən Hazırlanmışdır..")
Help.add()
		""".format(
siyahi=siyahi,
name=name,
fayl_adi=fayl_adi
			))
