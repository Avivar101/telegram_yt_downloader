import os
import re

import telebot
from telebot import types

from decouple import config
from yt_script import resolution_picker, create_yt, download_video

API_TOKEN = config('SECRET_KEY')

bot = telebot.TeleBot(API_TOKEN)

video_data = {}


# handle /start and /help
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """
    Welcome
    """)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """
    Need Help?
    """)


# get resolutions of video link
@bot.message_handler(func=lambda message:True, content_types=['text'])
def handle_message(message):
    message_text = message.text

    # verify if message is a link
    if is_link(message_text):
        print('getting resolutions...')

        yt = create_yt(message_text)

        # store the link in dictionary
        video_data[message.chat.id] = {'url': message_text, 'yt': yt}

        # return resolutions
        resolutions = resolution_picker(yt)

        # generates the inline keyboard
        keyboard = inline_keyboard(resolutions)

        bot.send_message(message.chat.id, 'Select resolution:', reply_markup=keyboard)
        print(message.chat.id)  
    else:
        bot.send_message(message.chat.id, "Please send a link")



# handler for resolution button clicks
@bot.callback_query_handler(func=lambda call:True)
def button_click(call):

    chat_id = call.message.chat.id

    stored_data = video_data.get(chat_id)
    # get the selected resolution
    resolution = call.data
    yt = stored_data['yt']

    bot.edit_message_text(text="Selected resolution: " + str(resolution), chat_id=call.message.chat.id, message_id=call.message.message_id)
    print("selected resolution: " + str(resolution))

    bot.edit_message_text(text="download starting...", chat_id=call.message.chat.id, message_id=call.message.message_id)
    print("downloading video...")
    download_video(resolution, yt)
    # respond

    bot.edit_message_text(text="uploading video to telegram...", chat_id=call.message.chat.id, message_id=call.message.message_id)
    print("uploading video")
    # Send the downloaded video to the user
    with open(yt.title + ".mp4", "rb") as video_file:
        bot.send_video(call.message.chat.id, video_file)
    print("video uploaded successfully")

    # Clean up: Remove the downloaded video file
    os.remove(yt.title + ".mp4")





# create inlinekeyboard message
def inline_keyboard(resolutions):
    # Create an InlineKeyboardMarkup
    keyboard = types.InlineKeyboardMarkup(row_width=1)
        
    # Create InlineKeyboardButtons for each food option
    buttons = [types.InlineKeyboardButton(str(resolution), callback_data=str(resolution)) for resolution in resolutions]
    
    # Add the buttons to the keyboard
    keyboard.add(*buttons)
    return keyboard


# check if text is a link
def is_link(text):
    # Regular expression pattern to check for URLs
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return bool(re.match(pattern, text))

bot.infinity_polling()
