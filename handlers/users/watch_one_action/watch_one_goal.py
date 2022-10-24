from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import WatchAction, ViewedAction
from keyboards.inline.edit_or_delete_action_kb import back_from_selecting_goal_keyboard
from keyboards.inline.watch_action_kb.my_goals_kb import my_goals_keyboard
from loader import dp
from states import EditGoal


@dp.callback_query_handler(lambda call: call.data.startswith(f'goal|{call.from_user.id}_'))
async def watch_one_goal(call: types.CallbackQuery):
    row_id = call.data.split('_')[-1]
    ViewedAction().insert_viewed_goal(row_id, call.from_user.id)
    var = WatchAction().select_goal_text(row_id)
    await call.message.edit_text(f'<b>🏷 Название:</b> <code>{var[0]}</code>\n'
                                 f'<b>💭 Описание:</b> <code>{var[1]}</code>',
                                 reply_markup=await back_from_selecting_goal_keyboard()
                                 )


@dp.callback_query_handler(text='back_edit_goal')
async def back_from_edit_goal(call: types.CallbackQuery):
    await call.message.edit_text(f'<b>Список целей:</b>\n',
                                 reply_markup=await my_goals_keyboard(call.from_user.id)
                                 )


@dp.callback_query_handler(text='back_edit_goal', state=EditGoal.name)
async def back_from_edit_goal(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'<b>Список целей:</b>\n',
                                 reply_markup=await my_goals_keyboard(call.from_user.id)
                                 )
    await state.finish()
