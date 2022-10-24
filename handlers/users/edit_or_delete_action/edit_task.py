from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import ViewedAction, EditAction
from keyboards.inline.backs_kb.back_from_creating_actions_kb import \
    skip_adding_description_keyboard_task
from keyboards.inline.backs_kb.back_from_editing_actions_kb import \
    back_from_editing_task_keyboard
from loader import dp
from states.user import EditTask


@dp.callback_query_handler(text='edit_task')
async def edit_task(call: types.CallbackQuery):
    await call.message.edit_text(f'Отправьте название задачи:',
                                 reply_markup=await back_from_editing_task_keyboard()
                                 )
    await EditTask.name.set()


@dp.message_handler(state=EditTask.name)
async def task_name_state(message: types.message, state: FSMContext):
    count = len(message.text)
    if count <= 30:
        await state.update_data(name=message.text)
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('Отправьте описание задачи:',
                             reply_markup=await skip_adding_description_keyboard_task()
                             )
        await EditTask.description.set()
    else:
        await message.delete()
        await dp.bot.delete_message(message.chat.id, message.message_id - 1)
        await message.answer('❌ Задача не может быть установлена, т.к. вы ввели более 30 символов!',
                             reply_markup=await back_from_editing_task_keyboard()
                             )


@dp.message_handler(state=EditTask.description)
async def task_description_state(message: types.message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    var = ViewedAction().select_viewed_task(message.from_user.id)
    EditAction().edit_task(f'{data["name"]}', f'{data["description"]}', var[0])
    await message.delete()
    await dp.bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer(f'✅ Задача изменена!',
                         reply_markup=await back_from_editing_task_keyboard())
    await state.finish()
