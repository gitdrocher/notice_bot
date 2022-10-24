from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import Base
from keyboards.inline.backs_kb.back_from_creating_actions_kb import \
    back_from_creating_actions_keyboard, \
    back_from_creating_actions_keyboard_end_state, \
    skip_adding_description_keyboard_task
from loader import dp
from states.user import Task


@dp.callback_query_handler(text='task')
async def create_task(call: types.CallbackQuery):
    await call.message.edit_text(f'Отправьте название задачи:',
                                 reply_markup=await back_from_creating_actions_keyboard()
                                 )
    await Task.name.set()


@dp.message_handler(state=Task.name)
async def task_name_state(message: types.message, state: FSMContext):
    count = len(message.text)
    if count <= 30:
        await state.update_data(name=message.text)
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('Отправьте описание задачи:',
                             reply_markup=await skip_adding_description_keyboard_task()
                             )
        await Task.description.set()
    else:
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('❌ Задача не может быть установлена, т.к. вы ввели более 30 символов!',
                             reply_markup=await back_from_creating_actions_keyboard()
                             )


@dp.message_handler(state=Task.description)
async def task_description_state(message: types.message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    Base().add_task(message.from_user.id, f'{data["name"]}', f'{data["description"]}')
    await message.delete()
    await dp.bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer(f'✅ Задача "<code>{data["name"]}</code>" установлена!',
                         reply_markup=await back_from_creating_actions_keyboard_end_state()
                         )
    await state.finish()
    