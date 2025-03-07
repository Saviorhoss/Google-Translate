import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.types import CallbackQuery
from googletrans import Translator
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN", "5466053464:AAHp-mFAeO1qRNS85i6oAC4zMfDf04uoFqA")

APP_ID = int(os.environ.get("APP_ID", 14699743))

API_HASH = os.environ.get("API_HASH", "0cef89ed2c8025c16d2b4d42a1b8d792")

OWNER = os.environ.get("OWNER", "Savior_128")

Deccan = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
START_TEXT = """
Hello {}, 
I am Google Translater bot.

Send me a text and I will translate it.

This is a clone of @GTranslateDCBot.You can create a your own bot by watching a small tutorial 📺
"""
HELP_TEXT = """
Follow these steps..

☛ Just send me a Word/Sentence/Paragraph.

☛ Select the Language and I will translate it you!

<b><u>Languages :-</u></b>
English, Tamil, Telugu, Hindi, Kannada, Malayalam, Korean, Japanese, Chinese, Greek, French, Russian, Arabic, Spanish, Italian, Uzbek, Latin, Polish, Mongolian, Marathi, Khazak, Myanmar, Indonesian, German
"""
ABOUT_TEXT = """
➠ **Bot : Google Translater Bot**

➠ **Language :** Python3

➠ **Server :** Heroku

➠ **Library :** Pyrogram
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Arteshenoor')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Arteshenoor')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Owner 👨‍💻', url=f"https://telegram.me/{OWNER}")
        ],[
        InlineKeyboardButton('Tutorial 📺', url='https://telegram.me/Arteshenoor')
        ]]
    )

@Deccan.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True
    )
@Deccan.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
	
@Deccan.on_message(filters.text & filters.private )
def echo(client, message):

 keybord = InlineKeyboardMarkup( [
        [
        InlineKeyboardButton("English", callback_data='en'),
        InlineKeyboardButton("persian", callback_data='fa'),
        InlineKeyboardButton("Telugu",callback_data='te')
        ],
        [
        InlineKeyboardButton("Hindi", callback_data='hi'),
        InlineKeyboardButton("Kannada", callback_data='kn'),
        InlineKeyboardButton("Malayalam",callback_data= 'ml')
        ],
        [
        InlineKeyboardButton("Korean", callback_data='ko'),
        InlineKeyboardButton("Japanese", callback_data='ja'),
        InlineKeyboardButton("Chinese", callback_data='zn-cn')
        ],
        [
        InlineKeyboardButton("Greek", callback_data='el'),
        InlineKeyboardButton("French", callback_data='fr'),
        InlineKeyboardButton("Russian", callback_data='ru')
        ],
        [InlineKeyboardButton("Arabic", callback_data='ar'),
         InlineKeyboardButton("Spanish", callback_data='es'),
         InlineKeyboardButton("Italian", callback_data='it')
        ],
        [InlineKeyboardButton("Uzbek", callback_data='uz'),
         InlineKeyboardButton("Latin", callback_data='la'),
         InlineKeyboardButton("Polish", callback_data='po')
        ],
        [InlineKeyboardButton("Mongolian", callback_data='mn'),
         InlineKeyboardButton("Marathi", callback_data='mr'),
         InlineKeyboardButton("Kazakh", callback_data='kk')
        ],
        [InlineKeyboardButton("Myanmar", callback_data='my'),
         InlineKeyboardButton("Indonesian", callback_data='id'),
         InlineKeyboardButton("German", callback_data='de')
        ]
        
    ]
 
 )

 
 message.reply_text("**Please Select language** 👇",reply_to_message_id = message, reply_markup = keybord)
    
    

@Deccan.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = Translator()  
  translation = translator.translate(tr_text,dest=cb_data) 
  await update.message.edit(translation.text)
  	

Deccan.run()
