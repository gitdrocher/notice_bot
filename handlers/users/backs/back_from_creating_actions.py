from aiogram import types
from aiogram.dispatcher import FSMContext

from data.functions import Base, ViewedAction, EditAction
from keyboards.inline import create_action_kb
from keyboards.inline.backs_kb.back_from_creating_actions_kb import \
    back_from_creating_actions_keyboard_end_state
from keyboards.inline.backs_kb.back_from_editing_actions_kb import \
    back_from_editing_goal_keyboard, back_from_editing_habit_keyboard, back_from_editing_task_keyboard
from loader import dp
from states.user import Goal, Habit, Task, EditGoal, EditHabit, EditTask


# State
# goal
@dp.callback_query_handler(text='back_from_creating_actions', state=Goal.name)
async def back_1(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )
    await state.finish()


# Edit Goal
@dp.callback_query_handler(text='back_from_creating_actions', state=EditGoal.name)
async def back_edit_1(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )
    await state.finish()


# habit
@dp.callback_query_handler(text='back_from_creating_actions', state=Habit.name)
async def back_2(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )
    await state.finish()


# Edit Habit
@dp.callback_query_handler(text='back_from_creating_actions', state=EditHabit.name)
async def back_edit_2(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )
    await state.finish()


# task
@dp.callback_query_handler(text='back_from_creating_actions', state=Task.name)
async def back_3(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )
    await state.finish()


# Edit Task
@dp.callback_query_handler(text='back_from_creating_actions', state=EditTask.name)
async def back_edit_3(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )
    await state.finish()


# Not State
@dp.callback_query_handler(text='back_from_creating_actions_end_state')
async def back_4(call: types.CallbackQuery):
    await call.message.edit_text(f'Добро пожаловать, <b>{call.from_user.first_name}</b>!\n'
                                 f'Выберите действие:',
                                 reply_markup=await create_action_kb.creating_action_keyboard()
                                 )


# Other
@dp.callback_query_handler(text='goal|skip_adding_description', state=Goal.description)
async def skip_1(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(description='')
    data = await state.get_data()
    Base().add_goal(call.from_user.id, f'{data["name"]}', '')
    await call.message.edit_text(f'✅ Цель "<code>{data["name"]}</code>" установлена!',
                                 reply_markup=await back_from_creating_actions_keyboard_end_state()
                                 )
    await state.finish()


@dp.callback_query_handler(text='habit|skip_adding_description', state=Habit.description)
async def skip_2(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(description='')
    data = await state.get_data()
    Base().add_habit(call.from_user.id, f'{data["name"]}', '')
    await call.message.edit_text(f'✅ Привычка "<code>{data["name"]}</code>" установлена!',
                                 reply_markup=await back_from_creating_actions_keyboard_end_state()
                                 )
    await state.finish()


@dp.callback_query_handler(text='task|skip_adding_description', state=Task.description)
async def skip_3(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(description='')
    data = await state.get_data()
    Base().add_task(call.from_user.id, f'{data["name"]}', '')
    await call.message.edit_text(f'✅ Задача "<code>{data["name"]}</code>" установлена!',
                                 reply_markup=await back_from_creating_actions_keyboard_end_state()
                                 )
    await state.finish()


@dp.callback_query_handler(text='goal|skip_adding_description', state=EditGoal.description)
async def skip_edit_1(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(description='')
    data = await state.get_data()
    var = ViewedAction().select_viewed_goal(call.from_user.id)
    EditAction().edit_goal(f'{data["name"]}', f'{data["description"]}', var[0])
    await call.message.edit_text(f'✅ Цель изменена!',
                                 reply_markup=await back_from_editing_goal_keyboard())
    await state.finish()


@dp.callback_query_handler(text='habit|skip_adding_description', state=EditHabit.description)
async def skip_edit_2(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(description='')
    data = await state.get_data()
    var = ViewedAction().select_viewed_habit(call.from_user.id)
    EditAction().edit_habit(f'{data["name"]}', f'{data["description"]}', var[0])
    await call.message.edit_text(f'✅ Привычка изменена!',
                                 reply_markup=await back_from_editing_habit_keyboard())
    await state.finish()


@dp.callback_query_handler(text='task|skip_adding_description', state=EditTask.description)
async def skip_edit_3(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(description='')
    data = await state.get_data()
    var = ViewedAction().select_viewed_task(call.from_user.id)
    EditAction().edit_task(f'{data["name"]}', f'{data["description"]}', var[0])
    await call.message.edit_text(f'✅ Задача изменена!',
                                 reply_markup=await back_from_editing_task_keyboard())
    await state.finish()
