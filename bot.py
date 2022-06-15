from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from io import BytesIO

from config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import keyboards as kb
import models

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет я бот,который накладывает определенный стиль на изображение!"
                        "Желаете попробовать?", reply_markup=kb.greet_kb11)






@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    await message.reply("В каком стиле, вы хотите обработать фото?", reply_markup=kb.greet_kb1)

    img_path = 'input.jpg'
    await message.photo[-1].download(img_path)


    img = models.load_img(img_path)
    models.magic_S(img)


@dp.message_handler()
async def echo_message(msg: types.Message):


    mes = msg.text
    user_id = msg.from_user.id

    if mes == 'VanGog':
        img_path = 'input.jpg'
        img = models.load_img(img_path)
        models.magic_V(img)
        photo = open('/home/alexandr/bot_risovach/result.png', 'rb')
        await bot.send_photo(msg.from_user.id, photo)
        await msg.reply("Пожалуйста!")
    if mes == 'Dali':
        img_path = 'input.jpg'
        img = models.load_img(img_path)
        models.magic_D(img)
        photo = open('/home/alexandr/bot_risovach/result.png', 'rb')
        await bot.send_photo(msg.from_user.id, photo)
        await msg.reply("Пожалуйста!")
    if mes == 'Simpsons':
        img_path = 'input.jpg'
        img = models.load_img(img_path)
        models.magic_S(img)
        photo = open('/home/alexandr/bot_risovach/result.png', 'rb')



        await bot.send_photo(msg.from_user.id, photo)
        await msg.reply("Пожалуйста!")
    if mes == 'Нет':
        await msg.reply("Тогда,всего доброго!")
    if mes == 'Да':
        await msg.reply("Тогда загрузите фото для обработки")






if __name__ == '__main__':
    executor.start_polling(dp)
