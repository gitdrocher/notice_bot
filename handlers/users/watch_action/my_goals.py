from aiogram import types

from keyboards.inline.watch_action_kb.my_goals_kb import my_goals_keyboard
from loader import dp


@dp.callback_query_handler(text='my_goals')
async def my_goals(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>Список целей:</b>\n',
                                 reply_markup=await my_goals_keyboard(call.from_user.id)
                                 )
