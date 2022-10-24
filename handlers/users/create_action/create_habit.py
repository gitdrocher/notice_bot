from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import Base
from keyboards.inline.backs_kb.back_from_creating_actions_kb import \
    back_from_creating_actions_keyboard, \
    back_from_creating_actions_keyboard_end_state, \
    skip_adding_description_keyboard_habit
from loader import dp
from states.user import Habit


@dp.callback_query_handler(text='habit')
async def create_habit(call: types.CallbackQuery):
    await call.message.edit_text(f'Отправьте название привычки:',
                                 reply_markup=await back_from_creating_actions_keyboard()
                                 )
    await Habit.name.set()


@dp.message_handler(state=Habit.name)
async def habit_name_state(message: types.message, state: FSMContext):
    count = len(message.text)
    if count <= 30:
        await state.update_data(name=message.text)
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('Отправьте описание привычки:',
                             reply_markup=await skip_adding_description_keyboard_habit()
                             )
        await Habit.description.set()
    else:
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('❌ Привычка не может быть установлена, т.к. вы ввели более 30 символов!',
                             reply_markup=await back_from_creating_actions_keyboard()
                             )


@dp.message_handler(state=Habit.description)
async def habit_description_state(message: types.message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    Base().add_habit(message.from_user.id, f'{data["name"]}', f'{data["description"]}')
    await message.delete()
    await dp.bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer(f'✅ Привычка "<code>{data["name"]}</code>" установлена!',
                         reply_markup=await back_from_creating_actions_keyboard_end_state()
                         )
    await state.finish()
