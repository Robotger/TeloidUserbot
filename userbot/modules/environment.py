

# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 
from userbot import (
    BOTLOG,
    BOTLOG_CHATID
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon.errors.rpcerrorlist import PeerIdInvalidError # Botlog grubundan çıktıysa
import os
import sys


# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("heroku")

# ████████████████████████████████ #
"""Config Vars değeri ilave edin veya silin..."""


def get_config_var(variable):
    with open('config.env', 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        if key == variable.strip():
            value.strip()
            return value
    return None


@register(outgoing=True,
          pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
   
    if exe == "get":
        await var.edit("`🔄 Kullanıcı Bilgileri Getiriliyor..`")
        variable = var.pattern_match.group(2)
        if variable != '':
            my_variable = get_config_var(variable)
            if my_variable is not None:
                
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#CONFIGVAR\n\n"
                        "**ConfigVar**:\n"
                        f"`{variable}` = `{my_variable}`\n"
                    )
                    await var.edit("`BOTLOG grubuna gönderdim!`")
                    return True
                else:
                    await var.edit("`Lütfen BOTLOG grubu ayarlayınız...`")
                    return False
            else:
                await var.edit("`Hata:` **NoInfo.**")
                return True
        
    """elif exe == "del":
        await var.edit("`Bilgileri siliyorum...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Silmek istediğiniz ConfigVars'ı seçin ve bana bildirin...`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#DELCONFIGVAR\n\n"
                    "**ConfigVar Silindi**:\n"
                    f"`{variable}`"
                )
            await var.edit("`Bilgiler silindi!`")
            del heroku_var[variable]
        else:
            await var.edit("`Bilgiler Yok!`")
            return True"""
    
def set_config_var(variable, value):
    with open('config.env', 'r') as f:
        lines = f.readlines()
        
    value_str = str(value)
    
    if value_str.lower() in ['true', 'false']:
        
        value_str = value_str.capitalize()
    else:
        
        value_str = f'"{value_str}"'

    found = False
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            continue
        key, val = line.split('=', 1)
        if key.strip() == variable.strip():
            lines[i] = f'{key}={value_str}\n'
            found = True
            break

    if not found:
        lines.append(f'{variable}={value_str}\n')

    with open('config.env', 'w') as f:
        f.writelines(lines)
    os.environ[variable] = value_str
    os.execl(sys.executable, sys.executable, *sys.argv)

@register(outgoing=True, pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`🔄 Verilenler Yazılıyor...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    fix = False
    my_variable = get_config_var(variable)
    
    if my_variable is not None:
        try:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#SETCONFIGVAR\n\n"
                    "**ConfigVar Değişikliği**:\n"
                    f"`{variable}` = `{value}`"
                )
            await var.edit("`Veriler Yazıldı!`")
        except PeerIdInvalidError:
             fix = True
             await var.edit("😒 Botlog grubundan çıkmışsın.. Senin için düzeltiyorum..")
    else:
        try:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#ADDCONFIGVAR\n\n"
                    "**Yeni ConfigVar Eklendi**:\n"
                    f"`{variable}` = `{value}`"
                )
            await var.edit("`Veriler Yazıldı!`")
        except PeerIdInvalidError:
            fix = True
            await var.edit("😒 Botlog grubundan çıkmışsın.. Senin için düzeltiyorum..")
    if fix:
        
       set_config_var('BOTLOG', 'False')
    else:
        
         set_config_var(variable, value)








CmdHelp('config').add_command(
'dyno', None, LANG['H1']
    ).add_command(
        'set var', None, LANG['H2']
    ).add_command(
        'get var', None, LANG['H3']
    ).add_command(
        'del var', None, LANG['H4']
    ).add_command(
        'log', None, LANG['H5']
    ).add_info(LANG['H6']).add()
