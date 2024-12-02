#(©)Codexbotz

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats', 'add_premium', 'remove_premium', 'list_premium']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ", url=f'https://telegram.me/share/url?text=%2A%2A%F0%9F%94%97%20Here%20is%20Your%20Link%20%F0%9F%91%87%2A%2A%0A%0A{link}%0A%0A%2A%2AProvided%20by%20%40AIO_Backup%2A%2A')]])

    await reply_text.edit(f"<b>🔗 Here is Your Link 👇</b>\n\n{link}\n\n<b>Provided by @AIO_Backup</b>", reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 ʏᴏᴜʀ ᴜʀʟ​", url=f'https://telegram.me/share/url?text=%2A%2A%F0%9F%94%97%20Here%20is%20Your%20Link%20%F0%9F%91%87%2A%2A%0A%0A{link}%0A%0A%2A%2AProvided%20by%20%40AIO_Backup%2A%2A')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass