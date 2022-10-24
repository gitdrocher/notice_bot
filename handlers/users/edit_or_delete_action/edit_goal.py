from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import ViewedAction, EditAction
from keyboards.inline.backs_kb.back_from_creating_actions_kb import \
    skip_adding_description_keyboard_goal
from keyboards.inline.backs_kb.back_from_editing_actions_kb import \
    back_from_editing_goal_keyboard
from loader import dp
from states.user import EditGoal


@dp.callback_query_handler(text='edit_goal')
async def edit_goal(call: types.CallbackQuery):
    await call.message.edit_text(f'Отправьте название цели:',
                                 reply_markup=await back_from_editing_goal_keyboard()
                                 )
    await EditGoal.name.set()


@dp.message_handler(state=EditGoal.name)
async def goal_name_state(message: types.message, state: FSMContext):
    count = len(message.text)
    if count <= 30:
        await state.update_data(name=message.text)
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('Отправьте описание цели:',
                             reply_markup=await skip_adding_description_keyboard_goal()
                             )
        await EditGoal.description.set()
    else:
        await dp.bot.delete_message(message.chat.id, message.message_id)
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('❌ Цель не может быть установлена, т.к. вы ввели более 30 символов!',
                             reply_markup=await back_from_editing_goal_keyboard()
                             )


@dp.message_handler(state=EditGoal.description)
async def goal_description_state(message: types.message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    var = ViewedAction().select_viewed_goal(message.from_user.id)
    EditAction().edit_goal(f'{data["name"]}', f'{data["description"]}', var[0])
    await message.delete()
    await dp.bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer(f'✅ Цель изменена!',
                         reply_markup=await back_from_editing_goal_keyboard())
    await state.finish()
