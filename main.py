from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from os import environ

bot = Client(
            "Proxy",
            api_id=int(environ["API_ID"]),
            api_hash= environ["API_HASH"],
            bot_token= "5305093897:AAG4EDZ_Nlz_foDltAfn-8nA_DmUHU5N8Dw"
)

FORCE_CHL = "FIREEYEX"
FROM_CHL = "H9Z2X4"

FORCE_BUT = [[InlineKeyboardButton("CHANNEL", url="https://t.me/" + FORCE_CHL)]]
START_BUT = [[("HTTPS"), ("SOCKS4"), ("SOCKS5")], [("HELP")], [("PREMIUM")]]


@bot.on_message(filters.command("start") & filters.private)
async def start(bot, msg):
    if FORCE_CHL:
        try:
            FORCE_CHK = await bot.get_chat_member(FORCE_CHL, msg.from_user.id)
            if FORCE_CHK:
                sss = await bot.get_messages(FROM_CHL, 5)
                START_MSG = "<b>" + sss.text + "</b>"
                reply_markup = ReplyKeyboardMarkup(START_BUT, one_time_keyboard=False, resize_keyboard=True)
                await msg.reply_text(text=START_MSG, reply_markup=reply_markup)
        except UserNotParticipant:
            rrr = await bot.get_messages(FROM_CHL, 3)
            FORCE_MSG = "<b>" + rrr.text + "</b>"
            text = FORCE_MSG
            reply_markup2 = InlineKeyboardMarkup(FORCE_BUT)
            await msg.reply_text(text=text, reply_markup=reply_markup2)


@bot.on_message(filters.regex("HTTPS") & filters.private)
async def https(bot, msg):
    if FORCE_CHL:
        try:
            FORCE_CHK = await bot.get_chat_member(FORCE_CHL, msg.from_user.id)
            if FORCE_CHK:
                await bot.copy_message(chat_id=msg.chat.id, from_chat_id=FROM_CHL, message_id=7)

        except UserNotParticipant:
            rrr = await bot.get_messages(FROM_CHL, 3)
            FORCE_MSG = "<b>" + rrr.text + "</b>"
            text = FORCE_MSG
            reply_markup2 = InlineKeyboardMarkup(FORCE_BUT)
            await msg.reply_text(text=text, reply_markup=reply_markup2)


@bot.on_message(filters.regex("SOCKS4") & filters.private)
async def socks4(bot, msg):
    if FORCE_CHL:
        try:
            FORCE_CHK = await bot.get_chat_member(FORCE_CHL, msg.from_user.id)
            if FORCE_CHK:
                await bot.copy_message(chat_id=msg.chat.id, from_chat_id=FROM_CHL, message_id=9)

        except UserNotParticipant:
            rrr = await bot.get_messages(FROM_CHL, 3)
            FORCE_MSG = "<b>" + rrr.text + "</b>"
            text = FORCE_MSG
            reply_markup2 = InlineKeyboardMarkup(FORCE_BUT)
            await msg.reply_text(text=text, reply_markup=reply_markup2)


@bot.on_message(filters.regex("SOCKS5") & filters.private)
async def socks5(bot, msg):
    if FORCE_CHL:
        try:
            FORCE_CHK = await bot.get_chat_member(FORCE_CHL, msg.from_user.id)
            if FORCE_CHK:
                await bot.copy_message(chat_id=msg.chat.id, from_chat_id=FROM_CHL, message_id=11)

        except UserNotParticipant:
            rrr = await bot.get_messages(FROM_CHL, 3)
            FORCE_MSG = "<b>" + rrr.text + "</b>"
            text = FORCE_MSG
            reply_markup2 = InlineKeyboardMarkup(FORCE_BUT)
            await msg.reply_text(text=text, reply_markup=reply_markup2)


@bot.on_message(filters.regex("HELP") & filters.private)
async def HELP(bot, msg):
    if FORCE_CHL:
        try:
            FORCE_CHK = await bot.get_chat_member(FORCE_CHL, msg.from_user.id)
            if FORCE_CHK:
                await bot.copy_message(chat_id=msg.chat.id, from_chat_id=FROM_CHL, message_id=13)

        except UserNotParticipant:
            rrr = await bot.get_messages(FROM_CHL, 3)
            FORCE_MSG = "<b>" + rrr.text + "</b>"
            text = FORCE_MSG
            reply_markup2 = InlineKeyboardMarkup(FORCE_BUT)
            await msg.reply_text(text=text, reply_markup=reply_markup2)


@bot.on_message(filters.regex("PREMIUM") & filters.private)
async def PREMIUM(bot, msg):
    if FORCE_CHL:
        try:
            FORCE_CHK = await bot.get_chat_member(FORCE_CHL, msg.from_user.id)
            if FORCE_CHK:
                await bot.copy_message(chat_id=msg.chat.id, from_chat_id=FROM_CHL, message_id=15)

        except UserNotParticipant:
            rrr = await bot.get_messages(FROM_CHL, 3)
            FORCE_MSG = "<b>" + rrr.text + "</b>"
            text = FORCE_MSG
            reply_markup2 = InlineKeyboardMarkup(FORCE_BUT)
            await msg.reply_text(text=text, reply_markup=reply_markup2)


print("iam alive")
bot.run()
