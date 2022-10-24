from aiogram import types

from data.functions.base import ViewedAction, DeleteAction
from keyboards.inline.watch_action_kb import my_goals_kb, my_habits_kb, my_tasks_kb
from loader import dp


@dp.callback_query_handler(text='delete_goal')
async def delete_goal(call: types.CallbackQuery):
    var = ViewedAction().select_viewed_goal(call.from_user.id)
    DeleteAction().delete_goal(row_id=var[0])
    await call.message.edit_text('❌ Цель удалена!')
    await call.answer('❌ Цель удалена!')
    await call.message.delete()
    await call.message.answer(f'<b>Список целей:</b>\n',
                              reply_markup=await my_goals_kb.my_goals_keyboard(call.from_user.id)
                              )


@dp.callback_query_handler(text='delete_habit')
async def delete_habit(call: types.CallbackQuery):
    var = ViewedAction().select_viewed_habit(call.from_user.id)
    DeleteAction().delete_habit(row_id=var[0])
    await call.message.edit_text('❌ Привычка удалена!')
    await call.answer('❌ Привычка удалена!')
    await call.message.delete()
    await call.message.answer(f'<b>Список привычек:</b>\n',
                              reply_markup=await my_habits_kb.my_habits_keyboard(call.from_user.id)
                              )


@dp.callback_query_handler(text='delete_task')
async def delete_task(call: types.CallbackQuery):
    var = ViewedAction().select_viewed_task(call.from_user.id)
    DeleteAction().delete_task(row_id=var[0])
    await call.message.edit_text('❌ Задача удалена!')
    await call.answer('❌ Задача удалена!')
    await call.message.delete()
    await call.message.answer(f'<b>Список задач:</b>\n',
                              reply_markup=await my_tasks_kb.my_tasks_keyboard(call.from_user.id)
                              )
