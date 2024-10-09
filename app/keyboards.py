from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Клик')],
    [KeyboardButton(text='Стоп')],
    [KeyboardButton(text='Обнулить')]],
    resize_keyboard=True, 
    input_field_placeholder='Выберите пункт меню'
)
