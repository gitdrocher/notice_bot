from aiogram import types

from keyboards.inline.watch_action_kb.my_habits_kb import my_habits_keyboard
from loader import dp


@dp.callback_query_handler(text='my_habits')
async def my_habits(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>Список привычек:</b>\n',
                                 reply_markup=await my_habits_keyboard(call.from_user.id)
                                 )
