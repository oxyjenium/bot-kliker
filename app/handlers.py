from aiogram import F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router=Router()

class stat(StatesGroup):
    name=State()
    

@router.message(CommandStart())
async def cmd_start(message : Message, state : FSMContext):
    await message.reply(f'Привет. Это бот кликер. Чтобы начать игру нажми клик. После того как закончишь, напиши команду /reg, чтобы сохранить свой результат!',reply_markup=kb.main)
    k=0
    flag=True
    data = await state.get_data()
    flag=data.get("flag")
    await state.update_data(flag=True)


@router.message(F.text=='Клик')
async def klik(message : Message, state : FSMContext):
        data = await state.get_data()
        k=data.get("k") if data.get("k") else 0
        flag=data.get("flag")
        if flag:
            await state.update_data(k=k+1)
            await message.answer(f'Сейчас у вас {k+1} кликов', reply_markup=kb.main)
        else:
            await message.answer('Вы закончили кликать, теперь пропишите /reg')
    

@router.message(F.text=='Стоп')
async def stop(message : Message, state:FSMContext):
    data = await state.get_data()
    k=data.get("k") if data.get("k") else 0
    flag=data.get("flag")
    await message.answer(f'Окончательное количество кликов {k}')
    await state.update_data(flag=False)

@router.message(F.text=='Обнулить')
async def obn(message: Message, state : FSMContext):
    k=0
    await state.clear()
    await message.reply('Вы успешно обнулили количество кликов')
    data = await state.get_data()
    flag=data.get("flag")
    await state.update_data(flag=True)

@router.message(Command('reg'))
async def stat_one(message : Message, state : FSMContext):
    await state.set_state(stat.name)
    await message.answer('Введите ваше имя')

@router.message(stat.name)
async def stat_two(message : Message, state : FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    await message.answer(f'Регистрация завершена\n Имя: {data["name"]}\n Результат: {data["k"]}')
    await state.update_data(k=0)
    flag=data.get("flag")
    await state.update_data(flag=True)
    await state.clear()
    


