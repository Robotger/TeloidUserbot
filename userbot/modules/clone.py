# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 
import html
import os
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from userbot.events import register
from telethon.tl import functions
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot, DEFAULT_BIO,DEFAULT_NAME, BRAIN_CHECKER, WHITELIST
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("klon")

# ████████████████████████████████ #


@register(outgoing=True, pattern="^.clone ?(.*)")
async def clone(event):
    if event.fwd_from:
        return
    if event.is_reply:
        reply = await event.get_reply_message()
        reply_user = await event.client.get_entity(reply.from_id)
        if reply_user.id in BRAIN_CHECKER or reply_user.id in WHITELIST:
            await event.edit(LANG["WLKLON"])
            return
    reply_message = await event.get_reply_message()
    replied_user, error_i_a = await get_full_user(event)
    if replied_user is None:
        await event.edit(str(error_i_a))
        return False
    user_id = replied_user.user.id
    profile_pic = await event.client.download_profile_photo(user_id, TEMP_DOWNLOAD_DIRECTORY)
    # some people have weird HTML in their names
    first_name = html.escape(replied_user.user.first_name)
    # https://stackoverflow.com/a/5072031/4723940
    # some Deleted Accounts do not have first_name
    if first_name is not None:
        # some weird people (like me) have more than 4096 characters in their names
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.user.last_name
    # last_name is not Manadatory in @Telegram
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
      last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    # inspired by https://telegram.dog/afsaI181
    user_bio = replied_user.about
    if user_bio is not None:
        user_bio = html.escape(replied_user.about)
    await event.client(functions.account.UpdateProfileRequest(
        first_name=first_name
    ))
    await event.client(functions.account.UpdateProfileRequest(
        last_name=last_name
    ))
    await event.client(functions.account.UpdateProfileRequest(
        about=user_bio
    ))
    n = 1
    pfile = await event.client.upload_file(profile_pic)
    await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
        pfile
    ))

    await event.delete()
    await event.client.send_message(
      event.chat_id,
      "`Hahahah, Teloid Sayesinde Seni Çaldım.`",
      reply_to=reply_message
      )


@register(outgoing=True, pattern="^.revert ?(.*)")
async def revert(event):
    if event.fwd_from:
        return

    if DEFAULT_NAME:
        name = f"{DEFAULT_NAME}"
    else:
        await event.edit("**Lütfen herhangi bi sohbete** `.set var DEFAULT_NAME isminiz` **yazıp gönderin. İsminiz yazan kısma kendi isminizi yazmayı unutmayın.**")
        return


    n = 1
    try:
        await bot(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=n)))
        await bot(functions.account.UpdateProfileRequest(first_name=DEFAULT_NAME))
        await bot(functions.account.UpdateProfileRequest(about=DEFAULT_BIO))
        await event.edit(f"`{DEFAULT_NAME}, hesabınız başarıyla eski haline döndürüldü!`")
    except AboutTooLongError:
        srt_bio = "🎆 @TeloidUserBot"
        await bot(functions.account.UpdateProfileRequest(about=srt_bio))
        await event.edit("`Hesabınız başarıyla eski haline döndürüldü! Fakat bio'nuz çok uzun olduğu için hazır bio kullandım.`")


async def get_full_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.forward.from_id or previous_message.forward.channel_id
                )
            )
            return replied_user, None
        else:
            replied_user = await event.client(
                GetFullUserRequest(
                    previous_message.from_id
                )
            )
            return replied_user, None
    else:
        input_str = None
        try:
            input_str = event.pattern_match.group(1)
        except IndexError as e:
            return None, e
        if event.message.entities is not None:
            mention_entity = event.message.entities
            probable_user_mention_entity = mention_entity[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            else:
                try:
                    user_object = await event.client.get_entity(input_str)
                    user_id = user_object.id
                    replied_user = await event.client(GetFullUserRequest(user_id))
                    return replied_user, None
                except Exception as e:
                    return None, e
        elif event.is_private:
            try:
                user_id = event.chat_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e
        else:
            try:
                user_object = await event.client.get_entity(int(input_str))
                user_id = user_object.id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user, None
            except Exception as e:
                return None, e

CmdHelp('klon').add_command('clone', LANG['K1'], LANG['K2']
).add_command('revert', None, LANG['K3']
).add_warning(LANG['K4']
).add_info('🎆 Thx to @Ber4tbey').add()
