import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="5005602397:AAGnxBKUNRfpVeFwsLUMMWVFuOFCIo20X58")
bot = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

button_helpp = KeyboardButton('/help')
button1 = KeyboardButton('/spams')
button2 = KeyboardButton('/spamv')
button3 = KeyboardButton('/shifr')
button4 = KeyboardButton('/dos')

helpp = ReplyKeyboardMarkup()
helpp.add(button_helpp)

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3).add(button4)

@bot.message_handler(commands="start")
async def welcome (message: types.Message):
    await message.reply("Привет!", reply_markup=helpp)
    
@bot.message_handler(commands="help")
async def help (message: types.Message):
    await message.reply("Все команды:\n/spams - приложение для спама смс\n/spamv - приложение для спама WhatsApp\n/shifr - приложение для шифрования текста\n/dos - приложение для dos атаки\n\nПо всем вопросам обращаться к @Programming_hacking_1.", reply_markup=markup3)
    
@bot.message_handler(commands = 'spams')
async def send_file_1(message: types.Document):
    await message.answer("Подождите, бот загружает файл для отправки...")
    await message.reply_document(open('Bomber(1.8.1).apk', 'rb'))
	
@bot.message_handler(commands = 'spamv')
async def send_file_2(message: types.Document):
    await message.answer("Подождите, бот загружает файл для отправки...")
    await message.reply_document(open('Clicker(1.0).apk', 'rb'))
	
@bot.message_handler(commands = 'shifr')
async def send_file_3(message: types.Document):
    await message.answer("Подождите, бот загружает файл для отправки...")
    await message.reply_document(open('Enigma(1.1).apk', 'rb'))

@bot.message_handler(commands = 'dos')
async def send_file_4(message: types.Document):
    await message.answer("Подождите, бот загружает файл для отправки...")
    await message.reply_document(open('Dos(1.3).apk', 'rb'))
    await message.answer("Советую запускать на WIFI, либо моб. интернет(безлимит), т.к. трафик огромный")
    await message.answer_photo(open('photo.jpg', 'rb'))
	
if __name__ == "__main__":
    executor.start_polling(bot, skip_updates=True)
