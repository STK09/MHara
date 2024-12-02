#(©)Codexbotz
#recoded by @Its_Tartaglia_Childe

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "🚀​Fᴏʀᴡᴀʀᴅ ꜰɪʀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ DB ᴄʜᴀɴɴᴇʟ...! (with Quotes)..\n\n​Oʀ ꜱᴇɴᴅ DB ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ​", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("🚫 ᴇʀʀᴏʀ\n\n​​​Iᴛ'ꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴅᴜᴅᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ​...!", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "🚀​Fᴏʀᴡᴀʀᴅ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ʏᴏᴜʀ DB ᴄʜᴀɴɴᴇʟ...! (with Quotes)..\nOʀ ꜱᴇɴᴅ DB ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ​​", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("🚫 ᴇʀʀᴏʀ\n\nIᴛ'ꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴅᴜᴅᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ...!", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ", url=f'https://telegram.me/share/url?text=%2A%2A%F0%9F%94%97%20Here%20is%20Your%20Link%20%F0%9F%91%87%2A%2A%0A%0A{link}%0A%0A%2A%2AProvided%20by%20%40AIO_Backup%2A%2A')]])
    await second_message.reply_text(f"<b>🔗 Here is Your Link 👇</b>\n\n{link}\n\n<b>Provided by @AIO_Backup</b>", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "🚀Fᴏʀᴡᴀʀᴅ ꜰɪʀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ DB ᴄʜᴀɴɴᴇʟ...! (with Quotes)..\n​Oʀ ꜱᴇɴᴅ DB ᴄʜᴀɴɴᴇʟ ᴘᴏꜱᴛ ʟɪɴᴋ​", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("🚫 ᴇʀʀᴏʀ\n\nɪᴛ'ꜱ ɴᴏᴛ ꜰʀᴏᴍ ᴅʙ ᴄʜᴀɴɴᴇʟ ᴅᴜᴅᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ​...!", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ", url=f'https://telegram.me/share/url?text=%2A%2A%F0%9F%94%97%20Here%20is%20Your%20Link%20%F0%9F%91%87%2A%2A%0A%0A{link}%0A%0A%2A%2AProvided%20by%20%40AIO_Backup%2A%2A')]])
    await channel_message.reply_text(f"<b>🔗 Here is Your Link 👇</b>\n\n{link}\n\n<b>Provided by @AIO_Backup</b>", quote=True, reply_markup=reply_markup)