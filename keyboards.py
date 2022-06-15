from aiogram.types import InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton



button_hi = KeyboardButton('Сделайте мне красиво! 👋')
button_h2 = KeyboardButton('Dali')
button_h3 = KeyboardButton('VanGog')
button_h4 = KeyboardButton('Simpsons')
button_h5 = KeyboardButton('Да')
button_h6 = KeyboardButton('Нет')
greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi,button_h2)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_h2,button_h3,button_h4 )
greet_kb11 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_h5,button_h6)
greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

greet_kb9 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_h2,button_h3)



button1 = KeyboardButton('Сделайте мне красиво')
button2 = KeyboardButton('Саня питерский')
button3 = KeyboardButton('3апросить пива у Ds9')

markup3 = ReplyKeyboardMarkup().add(
    button1)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)