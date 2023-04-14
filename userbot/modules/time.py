# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 


""" Bir konumun ya da UserBot sunucusunun tarih/saatini gösterebilecek modüldür. """

from datetime import datetime as dt

from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from userbot import CMD_HELP, COUNTRY, TZ_NUMBER
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("time")

# ████████████████████████████████ #

async def get_tz(con):
    """ Seçilen bölgenin saat dilimini elde etmek içindir. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


@register(outgoing=True, pattern="^.time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def time_func(tdata):
    """ .time komutu şu şekilde kullanılabilir
        1- Bölge belirtilerek.
        2. Varsayılan userbot bölgesi (.settime komutuyla ayarlanabilir)
        3. UserBot'un barındığı sunucunun tarihi.
    """
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)

    t_form = "%H:%M"
    c_name = None

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await tdata.edit(f"{LANG['CLOCK']}  **{dt.now().strftime(t_form)}** ")
        return

    if not timezones:
        await tdata.edit(LANG['INVALID_COUNTRY'])
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} {LANG['TOO_TIMEZONE']}:`\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += f"\n`{LANG['CHOICE_TIMEZONE']}."
            return_str += f"`{LANG['EXAMPLE']}: .time {c_name} 2`"

            await tdata.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(t_form)

    if c_name != COUNTRY:
        await tdata.edit(
            f"{c_name} {LANG['IS_CLOCK']}  **{dtnow}**  ({time_zone} {LANG['IS_TZ']}).")
        return

    elif COUNTRY:
        await tdata.edit(f"{COUNTRY} {LANG['IS_CLOCK']} **{dtnow}**  "
                         f"({time_zone} {LANG['IS_TZ']}).")
        return


@register(outgoing=True, pattern="^.date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def date_func(dat):
    """ .date komutu şu şekilde kullanılabilir
        1- Bölge belirtilerek.
        2. Varsayılan userbot bölgesi (.settime komutuyla ayarlanabilir)
        3. UserBot'un barındığı sunucunun tarihi.
    """
    con = dat.pattern_match.group(1).title()
    tz_num = dat.pattern_match.group(2)

    d_form = "%d/%m/%y - %A"
    c_name = ''

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await dat.edit(f"{LANG['DATE']}: **{dt.now().strftime(d_form)}** ")
        return

    if not timezones:
        await dat.edit(LANG['INVALID_COUNTRY'])
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} {LANG['TOO_TIMEZONE']}:`\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += f"\n`{LANG['CHOICE_TIMEZONE']}"
            return_str += f"{LANG['EXAMPLE']}: .date {c_name} 2"

            await dat.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(d_form)

    if c_name != COUNTRY:
        await dat.edit(
            f"{c_name} {LANG['IS_DATE']}  **{dtnow}**  ({time_zone} {LANG['IS_TZ']}).`")
        return

    elif COUNTRY:
        await dat.edit(f"{COUNTRY} {LANG['IS_DATE']} **{dtnow}**"
                       f"({time_zone} {LANG['IS_TZ']}).")
        return

CmdHelp('time').add_command(
    'time', LANG['T1'], LANG['T2']
).add_command(
    'date', LANG['T3'], LANG['T4']
).add()
