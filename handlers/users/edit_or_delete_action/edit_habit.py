from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import ViewedAction, EditAction
from keyboards.inline.backs_kb.back_from_creating_actions_kb import \
    skip_adding_description_keyboard_habit
from keyboards.inline.backs_kb.back_from_editing_actions_kb import \
    back_from_editing_habit_keyboard
from loader import dp
from states.user import EditHabit


@dp.callback_query_handler(text='edit_habit')
async def edit_habit(call: types.CallbackQuery):
    await call.message.edit_text(f'Отправьте название привычки:',
                                 reply_markup=await back_from_editing_habit_keyboard()
                                 )
    await EditHabit.name.set()


@dp.message_handler(state=EditHabit.name)
async def habit_name_state(message: types.message, state: FSMContext):
    count = len(message.text)
    if count <= 30:
        await state.update_data(name=message.text)
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('Отправьте описание привычки:',
                             reply_markup=await skip_adding_description_keyboard_habit()
                             )
        await EditHabit.description.set()
    else:
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('❌ Привычка не может быть установлена, т.к. вы ввели более 30 символов!',
                             reply_markup=await back_from_editing_habit_keyboard()
                             )


@dp.message_handler(state=EditHabit.description)
async def habit_description_state(message: types.message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    var = ViewedAction().select_viewed_habit(message.from_user.id)
    EditAction().edit_habit(f'{data["name"]}', f'{data["description"]}', var[0])
    await message.delete()
    await dp.bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer(f'✅ Привычка изменена!',
                         reply_markup=await back_from_editing_habit_keyboard())
    await state.finish()
