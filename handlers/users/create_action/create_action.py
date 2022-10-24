from aiogram import types

from keyboards.inline import create_action_kb
from loader import dp


@dp.callback_query_handler(text='create')
async def create_action(call: types.CallbackQuery):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )