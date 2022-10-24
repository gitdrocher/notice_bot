from aiogram import types

from keyboards.inline.watch_action_kb.my_tasks_kb import my_tasks_keyboard
from loader import dp


@dp.callback_query_handler(text='my_tasks')
async def my_tasks(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>Список задач:</b>\n',
                                 reply_markup=await my_tasks_keyboard(call.from_user.id)
                                 )
