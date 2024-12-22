from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Help", callback_data='help'),
                 InlineKeyboardButton("About", callback_data='about')],
                [InlineKeyboardButton('Backup Channel', url='https://t.me/AIO_Backup'),
                 InlineKeyboardButton('Developer', url='https://t.me/Soutick_09')],
                [InlineKeyboardButton("Close", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"✨ Exclusive Premium Membership ✨\n<i>Unlock a World of Benefits Just for You!</i>\n\n🔥 Premium Perks:\n<i>✔️ Direct Channel Links – No Ads, No Distractions!</i>\n<i>✔️ Special Access to Exclusive Events & Content</i>\n<i>✔️ Faster Support & Priority Assistance</i>\n\n💭 Plus: You'll get direct access to these channels with any of these plans!\n[<a href=https://graph.org/AIO-Backup-12-22-2>List of Channels</a>]\n\n💰 Affordable Pricing:\n              ○ 1 Day: <code>INR 10</code>\n              ○ 7 Days: <code>INR 40</code>\n              ○ 1 Month: <code>INR 100</code>\n              ○ 3 Months: <code>INR 200</code>\n\nReady to Upgrade?💓\n» Message @Soutick_09 to get UPI or QR Code for payment.\n» Send a screenshot of your payment to @Soutick_09 <i>(for Auto Verification)</i>.\n\n⚡ Seats are LIMITED for Premium Members – Grab Yours Now!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Owner", url="https://t.me/Soutick_09"),
                        InlineKeyboardButton("Main Channel", url="https://t.me/AIO_Backup")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
