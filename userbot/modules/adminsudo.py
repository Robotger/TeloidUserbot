# Copyright (C) 2023 RobotgerDev
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TeloidUserBot 


from asyncio import sleep
from os import remove

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest, InviteToChannelRequest)
from telethon.tl.functions.messages import (UpdatePinnedMessageRequest, AddChatUserRequest)
from telethon.tl.types import (PeerChannel, ChannelParticipantsAdmins,
                               ChatAdminRights, ChatBannedRights,
                               MessageEntityMentionName, MessageMediaPhoto,
                               ChannelParticipantsBots, User, InputPeerChat)
from telethon.events import ChatAction
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, WARN_MODE, WARN_LIMIT, WHITELIST, SUDO_ID, WHITELIST
from userbot.events import register
from userbot.main import PLUGIN_MESAJLAR
from userbot.cmdhelp import CmdHelp
import datetime

# =================== CONSTANT ===================
# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("admin")

# ████████████████████████████████ #

PP_TOO_SMOL = LANG['PP_TOO_SMOL']
PP_ERROR = LANG['PP_ERROR']
NO_ADMIN = LANG['NO_ADMIN']
NO_PERM = LANG['NO_PERM']
NO_SQL = LANG['NO_SQL']

CHAT_PP_CHANGED = LANG['CHAT_PP_CHANGED']
CHAT_PP_ERROR = LANG['CHAT_PP_ERROR']
INVALID_MEDIA = LANG['INVALID_MEDIA']

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================


@register(incoming=True, from_users=SUDO_ID, pattern="^.sgban(?: |$)(.*)")
async def gbanspider(gspdr):
    """ .gban komutu belirlenen kişiyi küresel olarak yasaklar """
    # Yetki kontrolü
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        await gspdr.edit(NO_ADMIN)
        return

    # Fonksiyonun SQL modu altında çalışıp çalışmadığını kontrol et
    try:
        from userbot.modules.sql_helper.gban_sql import gban
    except:
        await gspdr.edit(NO_SQL)
        return

    user, reason = await get_user_from_event(gspdr)
    if user:
        pass
    else:
        return

    

    # Başarı olursa bilgi ver
    await gspdr.edit(LANG['BANNING'])
    if gban(user.id) == False:
        await gspdr.edit(
            LANG['ALREADY_GBANNED'])
    else:
        if reason:
            await gspdr.edit(f"{LANG['GBANNED_REASON']} {reason}")
        else:
            await gspdr.edit(LANG['GBANNED'])

        if BOTLOG:
            await gspdr.client.send_message(
                BOTLOG_CHATID, "#GBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {gspdr.chat.title}(`{gspdr.chat_id}`)")


@register(incoming=True)
async def gbanmsg(moot):
    """ Küresel banlanan kullanıcı mesaj gelirse """
    try:
        from userbot.modules.sql_helper.gban_sql import is_gbanned
    except:
        return

    gbanned = is_gbanned(str(moot.sender_id))
    if gbanned == str(moot.sender_id):
        try:
            chat = await moot.get_chat()
        except:
            return
            
        if (type(chat) == User):
            return 

        admin = chat.admin_rights
        creator = chat.creator

        if not admin and not creator:
            return

        try:
            await moot.client(EditBannedRequest(moot.chat_id, moot.sender_id,
                                            BANNED_RIGHTS))
            await moot.reply(LANG['GBAN_TEXT'])
        except:
            return


@register(incoming=True, from_users=SUDO_ID, pattern="^.sunban(?: |$)(.*)")
async def ungban(un_gban):
    """ .ungban komutu belirlenen kişinin küresel susturulmasını kaldırır """
    # Yetki kontrolü
    chat = await un_gban.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        await un_gban.edit(NO_ADMIN)
        return

    # Fonksiyonun SQL modu altında çalışıp çalışmadığını kontrol et
    try:
        from userbot.modules.sql_helper.gban_sql import ungban
    except:
        await un_gban.edit(NO_SQL)
        return

    user = await get_user_from_event(un_gban)
    user = user[0]
    if user:
        pass
    else:
        return

    await un_gban.edit(LANG['UNGBANNING'])

    if ungban(user.id) is False:
        await un_gban.edit(LANG['NO_BANNED'])
    else:
        # Başarı olursa bilgi ver
        await un_gban.edit(LANG['UNGBANNED'])

        if BOTLOG:
            await un_gban.client.send_message(
                BOTLOG_CHATID, "#UNGBAN\n"
                f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {un_gban.chat.title}(`{un_gban.chat_id}`)")




@register(incoming=True, from_users=WHITELIST, pattern="^.apromote(?: |$)(.*)")
@register(incoming=True, from_users=SUDO_ID, pattern="^.spromote(?: |$)(.*)")
async def promote(promt):
    """ .promote komutu ile belirlenen kişiyi yönetici yapar """
    # Hedef sohbeti almak
    chat = await promt.get_chat()
    # Yetkiyi sorgula
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değilse geri dön
    if not admin and not creator:
        await promt.edit(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=True,
                                 invite_users=True,
                                 change_info=True,
                                 ban_users=True,
                                 manage_call=True,
                                 delete_messages=True,
                                 pin_messages=True)

    
    await promt.client.send_message(promt.chat_id, LANG['PROMOTING'])
    user, rank = await get_user_from_event(promt)
    if not rank:
        rank = "Yönetici"  # Her ihtimale karşı.
    if user:
        pass
    else:
        return

    # Geçerli kullanıcı yönetici veya sahip ise tanıtmaya çalışalım
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
       
        await promt.client.send_message(promt.chat_id, LANG['SUCCESS_PROMOTE'])

    # Telethon BadRequestError hatası verirse
    # yönetici yapma yetkimiz yoktur
    except:
        
        await promt.client.send_message(promt.chat_id, NO_PERM)
        return

    # Yetkilendirme işi başarılı olursa günlüğe belirtelim
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID, "#YETKI\n"
            f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {promt.chat.title}(`{promt.chat_id}`)")



@register(incoming=True, from_users=SUDO_ID, pattern="^.sdemote(?: |$)(.*)")
async def demote(dmod):
    """ .demote komutu belirlenen kişiyi yöneticilikten çıkarır """
    # Yetki kontrolü
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        
        await dmod.client.send_message(dmod.chat_id, NO_ADMIN)
        return

    # Eğer başarılı olursa, yetki düşürüleceğini beyan edelim
    
    await dmod.client.send_message(dmod.chat_id, LANG['UNPROMOTING'])
    rank = "admeme"  # Burayı öylesine yazdım
    user = await get_user_from_event(dmod)
    user = user[0]
    if user:
        pass
    else:
        return

    # Yetki düşürme sonrası yeni izinler
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                manage_call=None,
                                delete_messages=None,
                                pin_messages=None)
    # Yönetici iznini düzenle
    try:
        await dmod.client(
            EditAdminRequest(dmod.chat_id, user.id, newrights, rank))

    # Telethon BadRequestError hatası verirse
    # gerekli yetkimiz yoktur
    except:
        
        await dmod.client.send_message(dmod.chat_id, NO_PERM)
        return
    
    await dmod.client.send_message(dmod.chat_id, LANG['UNPROMOTE'])

    # Yetki düşürme işi başarılı olursa günlüğe belirtelim
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID, "#YETKIDUSURME\n"
            f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {dmod.chat.title}(`{dmod.chat_id}`)")



@register(incoming=True, from_users=SUDO_ID, pattern="^.sban(?: |$)(.*)")
async def ban(bon):
    """ .ban komutu belirlenen kişiyi gruptan yasaklar """
    # Yetki kontrolü
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        
        await bon.client.send_message(bon.chat_id, NO_ADMIN)
        return

    user, reason = await get_user_from_event(bon)
    if user:
        pass
    else:
        return

   
    # Hedefi yasaklayacağınızı duyurun
    
    await bon.client.send_message(bon.chat_id, LANG['BANNING'])

    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id,
                                           BANNED_RIGHTS))
    except:
        
        await bon.client.send_message(bon.chat_id, NO_PERM)
        return
    # Spamcılar için
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except:
        
        await bon.client.send_message(bon.chat_id, LANG['NO_PERM_BUT_BANNED'])
        return
    # Mesajı silin ve ardından komutun
    # incelikle yapıldığını söyleyin
    SONMESAJ = PLUGIN_MESAJLAR['ban'].format(
        id = user.id,
        username = '@' + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})",
        first_name = user.first_name,
        last_name = '' if not user.last_name else user.last_name,
        mention = f"[{user.first_name}](tg://user?id={user.id})",
        date = datetime.datetime.strftime(datetime.datetime.now(), '%c'),
        count = (chat.participants_count - 1) if chat.participants_count else 'Bilinmiyor'
    )
    
    if reason:
        
        await bon.client.send_message(bon.chat_id, f"{SONMESAJ}\n{LANG['REASON']}: {reason}")
    else:
        await bon.edit(SONMESAJ)
        await bon.client.send_message(bon.chat_id, SONMESAJ)
    # Yasaklama işlemini günlüğe belirtelim
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID, "#BAN\n"
            f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {bon.chat.title}(`{bon.chat_id}`)")



@register(incoming=True, from_users=SUDO_ID, pattern="^.sunban(?: |$)(.*)")
async def nothanos(unbon):
    """ .unban komutu belirlenen kişinin yasağını kaldırır """
    # Yetki kontrolü
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
       
        await unbon.client.send_message(unbon.chat_id, NO_ADMIN)
        return

    # Her şey yolunda giderse...
   
    await unbon.client.send_message(unbon.chat_id, LANG['UNBANNING'])

    user = await get_user_from_event(unbon)
    user = user[0]
    if user:
        pass
    else:
        return

    try:
        
        await unbon.client.send_message(unbon.chat_id, LANG['UNBANNED'].format(
            id = user.id,
            username = '@' + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})",
            first_name = user.first_name,
            last_name = '' if not user.last_name else user.last_name,
            mention = f"[{user.first_name}](tg://user?id={user.id})",
            date = datetime.datetime.strftime(datetime.datetime.now(), '%c'),
            count = (chat.participants_count) if chat.participants_count else 'Bilinmiyor'
        ))

        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID, "#UNBAN\n"
                f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {unbon.chat.title}(`{unbon.chat_id}`)")
    except:
        
        await unbon.client.send_message(unbon.chat_id, LANG['EXCUSE_ME_WTF'])



@register(incoming=True, from_users=SUDO_ID, pattern="^.smute(?: |$)(.*)")
async def spider(spdr):
    """
    Bu fonksiyon temelde susturmaya yarar
    """
    # Fonksiyonun SQL modu altında çalışıp çalışmadığını kontrol et
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except:
       
        await spdr.client.send_message(spdr.chat_id, NO_SQL)
        return

    # Yetki kontrolü
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        
        await spdr.client.send_message(spdr.chat_id, NO_ADMIN)
        return

    user, reason = await get_user_from_event(spdr)
    if user:
        pass
    else:
        return

    # Eğer kullanıcı sudo ise
    if user.id in WHITELIST:
        await spdr.edit(
            LANG['BRAIN']
        )
        await spdr.client.send_message(spdr.chat_id, LANG['BRAIN'])
        return

    self_user = await spdr.client.get_me()

    if user.id == self_user.id:
       
        await spdr.client.send_message(spdr.chat_id, LANG['NO_MUTE_ME'])
        return

    # Hedefi sustaracağınızı duyurun
    
    await spdr.client.send_message(spdr.chat_id, LANG['MUTING'])
    if mute(spdr.chat_id, user.id) is False:
        await spdr.client.send_message(spdr.chat_id, LANG['ALREADY_MUTED'])
        
    else:
        try:
            await spdr.client(
                EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))

            await mutmsg(spdr, user, reason, chat)
        except UserAdminInvalidError:
            await mutmsg(spdr, user, reason, chat)
        except:
            
            await spdr.client.send_message(spdr.chat_id, LANG['WTF_MUTE'])


async def mutmsg(spdr, user, reason, chat):
    # Fonksiyonun yapıldığını duyurun
    SONMESAJ = PLUGIN_MESAJLAR['mute'].format(
            id = user.id,
            username = '@' + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})",
            first_name = user.first_name,
            last_name = '' if not user.last_name else user.last_name,
            mention = f"[{user.first_name}](tg://user?id={user.id})",
            date = datetime.datetime.strftime(datetime.datetime.now(), '%c'),
            count = (chat.participants_count) if chat.participants_count else 'Bilinmiyor'
        )

    if reason:
        await spdr.edit(f"{SONMESAJ}\n{LANG['REASON']}: {reason}")
    else:
        await spdr.edit(f"{SONMESAJ}")

    # Susturma işlemini günlüğe belirtelim
    if BOTLOG:
        await spdr.client.send_message(
            BOTLOG_CHATID, "#MUTE\n"
            f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {spdr.chat.title}(`{spdr.chat_id}`)")



@register(incoming=True, from_users=SUDO_ID, pattern="^.sunmute(?: |$)(.*)")
async def unmoot(unmot):
    """ .unmute komutu belirlenin kişinin sesini açar (yani grupta tekrardan konuşabilir) """
    # Yetki kontrolü
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
       
        await unmot.client.send_message(unmot.chat_id, NO_ADMIN)
        return

    # Fonksiyonun SQL modu altında çalışıp çalışmadığını kontrol et
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except:
        
        await unmot.client.send_message(unmot.chat_id, NO_SQL)
        return

    
    await unmot.client.send_message(unmot.chat_id, LANG['UNMUTING'])
    user = await get_user_from_event(unmot)
    user = user[0]
    if user:
        pass
    else:
        return

    if unmute(unmot.chat_id, user.id) is False:
        await unmot.client.send_message(unmot.chat_id, LANG['ALREADY_UNMUTED'])
       
    else:

        try:
            await unmot.client.send_message(unmot.chat_id, LANG['UNMUTED'].format(
            id = user.id,
            username = '@' + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})",
            first_name = user.first_name,
            last_name = '' if not user.last_name else user.last_name,
            mention = f"[{user.first_name}](tg://user?id={user.id})",
            date = datetime.datetime.strftime(datetime.datetime.now(), '%c'),
            count = (chat.participants_count) if chat.participants_count else 'Bilinmiyor'
        ))

        except UserAdminInvalidError:
            await unmot.client.send_message(LANG['UNMUTED'].format(
            id = user.id,
            username = '@' + user.username if user.username else f"[{user.first_name}](tg://user?id={user.id})",
            first_name = user.first_name,
            last_name = '' if not user.last_name else user.last_name,
            mention = f"[{user.first_name}](tg://user?id={user.id})",
            date = datetime.datetime.strftime(datetime.datetime.now(), '%c'),
            count = (chat.participants_count) if chat.participants_count else 'Bilinmiyor'
        ))
        except:
            
            await unmot.client.send_message(unmot.chat_id, LANG['WTF_MUTE'])
            return

        if BOTLOG:
            await unmot.client.send_message(
                BOTLOG_CHATID, "#UNMUTE\n"
                f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {unmot.chat.title}(`{unmot.chat_id}`)")


@register(incoming=True)
async def muter(moot):
    """ Sessize alınan kullanıcıların mesajlarını silmek için kullanılır """
    try:
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if muted:
        for i in muted:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
                try:
                    await moot.client(
                        EditBannedRequest(moot.chat_id, moot.sender_id, rights))
                except:
                    pass
    if gmuted:
        for i in gmuted:
            if i.sender == str(moot.sender_id):
                await moot.delete()


@register(incoming=True, from_users=SUDO_ID, pattern="^.sungmute(?: |$)(.*)")
async def ungmoot(un_gmute):
    """ .ungmute komutu belirlenen kişinin küresel susturulmasını kaldırır """
    # Yetki kontrolü
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        
        await un_gmute.client.send_message(un_gmute.chat_id, NO_ADMIN)
        return

    # Fonksiyonun SQL modu altında çalışıp çalışmadığını kontrol et
    try:
        from userbot.modules.sql_helper.gmute_sql import ungmute
    except:
        
        await un_gmute.client.send_message(un_gmute.chat_id, NO_SQL)
        return

    user = await get_user_from_event(un_gmute)
    user = user[0]
    if user:
        pass
    else:
        return

    
    await un_gmute.client.send_message(un_gmute.chat_id, LANG['GUNMUTING'])

    if ungmute(user.id) is False:
        
        await un_gmute.client.send_message(un_gmute.chat_id, LANG['NO_GMUTE'])
    else:
        # Başarı olursa bilgi ver
        
        await un_gmute.client.send_message(un_gmute.chat_id, LANG['UNMUTED'])

        if BOTLOG:
            await un_gmute.client.send_message(
                BOTLOG_CHATID, "#UNGMUTE\n"
                f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
                f"GRUP: {un_gmute.chat.title}(`{un_gmute.chat_id}`)")



@register(incoming=True, from_users=SUDO_ID, pattern="^.sgmute(?: |$)(.*)")
async def gspider(gspdr):
    """ .gmute komutu belirlenen kişiyi küresel olarak susturur """
    # Yetki kontrolü
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        
        await gspdr.client.send_message(gspdr.chat_id, NO_ADMIN)
        return

    # Fonksiyonun SQL modu altında çalışıp çalışmadığını kontrol et
    try:
        from userbot.modules.sql_helper.gmute_sql import gmute
    except:
        
        await gspdr.client.send_message(gspdr.chat_id, NO_SQL)
        return

    user, reason = await get_user_from_event(gspdr)
    if user:
        pass
    else:
        return

    # Eğer kullanıcı sudo ise
    if user.id in WHITELIST:
        
        await gspdr.client.send_message(gspdr.chat_id, LANG['BRAIN'])
        return

    # Başarı olursa bilgi ver
    
    await gspdr.client.send_message(gspdr.chat_id, LANG['GMUTING'])
    if gmute(user.id) == False:
        
        await gspdr.client.send_message(gspdr.chat_id, LANG['ALREADY_GMUTED'])
    else:
        if reason:
            
            await gspdr.client.send_message(gspdr.chat_id, f"{LANG['GMUTED']} {LANG['REASON']}: {reason}")
        else:
          
            await gspdr.client.send_message(gspdr.chat_id, LANG['GMUTED'])

        if BOTLOG:
            await gspdr.client.send_message(
                BOTLOG_CHATID, "#GMUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {gspdr.chat.title}(`{gspdr.chat_id}`)")






@register(incoming=True, from_users=SUDO_ID, pattern="^.spin(?: |$)(.*)")
async def pin(msg):
    """ .pin komutu verildiği grupta ki yazıyı & medyayı sabitler """
    # Yönetici kontrolü
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        
        await msg.client.send_message(msg.chat_id, NO_ADMIN)
        return

    to_pin = msg.reply_to_msg_id

    if not to_pin:
        
        await msg.client.send_message(msg.chat_id, LANG['NEED_MSG'])
        return

    options = msg.pattern_match.group(1)

    is_silent = True

    if options.lower() == "loud":
        is_silent = False

    try:
        await msg.client(
            UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except:
        
        await msg.client.send_message(msg.chat_id, NO_PERM)
        return

    
    await msg.client.send_message(msg.chat_id, LANG['PINNED'])

    user = await get_user_from_id(msg.from_id, msg)

    if BOTLOG:
        await msg.client.send_message(
            BOTLOG_CHATID, "#PIN\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {msg.chat.title}(`{msg.chat_id}`)\n"
            f"LOUD: {not is_silent}")



@register(incoming=True, from_users=SUDO_ID, pattern="^.skick(?: |$)(.*)")
async def kick(usr):
    """ .kick komutu belirlenen kişiyi gruptan çıkartır """
    # Yetki kontrolü
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değil ise geri dön
    if not admin and not creator:
        
        await usr.client.send_message(usr.chat_id, NO_ADMIN)
        return

    user, reason = await get_user_from_event(usr)
    if not user:
        
        await usr.client.send_message(usr.chat_id, LANG['NOT_FOUND'])
        return

    # Eğer kullanıcı sudo ise
    if user.id in WHITELIST:
        await usr.client.send_message(usr.chat_id, LANG['BRAIN'])
        return

    
    await usr.client.send_message(usr.chat_id, LANG['KICKING'])

    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(.5)
    except Exception as e:
       
        await usr.client.send_message(usr.chat_id, NO_PERM + f"\n{str(e)}")

        return

    if reason:
        await usr.client.send_message(usr.chat_id, f"[{user.first_name}](tg://user?id={user.id}) `{LANG['KICKED']}`\n{LANG['REASON']}: {reason}")
    else:
        await usr.client.send_message(usr.chat_id, f"[{user.first_name}](tg://user?id={user.id}) `{LANG['KICKED']}`")

    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID, "#KICK\n"
            f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {usr.chat.title}(`{usr.chat_id}`)\n")



@register(incoming=True, from_users=SUDO_ID, pattern="^.stagver(?: |$)(.*)")
async def tagver(promt):
    """ .tagver komutu ile belirlenen kişiyi kısıtlı yönetici yapar """
    # Hedef sohbeti almak
    chat = await promt.get_chat()
    # Yetkiyi sorgula
    admin = chat.admin_rights
    creator = chat.creator

    # Yönetici değilse geri dön
    if not admin and not creator:
        await promt.client.send_message(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=False,
                                 invite_users=True,
                                 change_info=False,
                                 ban_users=False,
                                 delete_messages=True,
                                 pin_messages=True)

    try:
        await promt.client.send_message(LANG['PROMOTING'])
    except:
        await promt.client.send_message(LANG['PROMOTING'])
    user, rank = await get_user_from_event(promt)
    if not rank:
        rank = "ᴛᴀɢ"  # Her ihtimale karşı.
    if user:
        pass
    else:
        return

    # Geçerli kullanıcı yönetici veya sahip ise tanıtmaya çalışalım
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await promt.client.send_message(LANG['SUCCESS_PROMOTE'])

    # Telethon BadRequestError hatası verirse
    # yönetici yapma yetkimiz yoktur
    except:
        await promt.client.send_message(NO_PERM)
        return

    # Yetkilendirme işi başarılı olursa günlüğe belirtelim
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID, "#TAG_VERME\n"
            f"KULLANICI: [{user.first_name}](tg://user?id={user.id})\n"
            f"GRUP: {promt.chat.title}(`{promt.chat_id}`)")






CmdHelp('sadmin').add_command(
        'spromote', (LANG['SPROMOTE1']), (LANG['SPROMOTE2'])
    ).add_command(
        'stagver', (LANG['STAGVER1']), (LANG['STAGVER2'])
    ).add_command(
        'sdemote', (LANG['SDEMOTE1']), (LANG['SDEMOTE2'])
    ).add_command(
        'sban', (LANG['SBAN1']), (LANG['SBAN2'])
    ).add_command(
        'smute', (LANG['SMUTE1']), (LANG['SMUTE2'])
    ).add_command(
        'sunmute', (LANG['SUNMUTE1']), (LANG['SUNMUTE2'])
    ).add_command(
        'sunban', (LANG['SUNBAN1']), (LANG['SUNBAN2'])
    ).add_command(
        'skick', (LANG['SKİCK1']), (LANG['SKİCK2'])
    ).add_command(
        'sgmute', (LANG['SGMUTE1']), (LANG['SGMUTE2'])
    ).add_command(
        'sungmute', (LANG['SUNGMUTE1']), (LANG['SUNGMUTE2'])
    ).add_command(
        'sgban', (LANG['SGBAN1']), (LANG['SGBAN2'])
    ).add_command(
        'sungban', (LANG['SUNGBAN1']), (LANG['SUNGBAN2'])
    ).add()
