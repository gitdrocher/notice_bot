from aiogram import types
from loader import dp
from keyboards.inline import start_kb


@dp.callback_query_handler(text='back_to_menu')
async def back_to_menu(call: types.CallbackQuery):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await start_kb.menu_keyboard()
                                 )