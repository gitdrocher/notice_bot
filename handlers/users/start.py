from aiogram import types
from loader import dp
from keyboards.inline.start_kb import menu_keyboard
from data.functions import Base


@dp.message_handler(commands='start')
async def start(message: types.message):
    await message.answer(f'Добро пожаловать, <b>{message.from_user.first_name}</b>!\n'
                         f'Выберите действие:',
                         reply_markup=await menu_keyboard()
                         )
    Base().add_user(
        message.from_user.id,
    )
