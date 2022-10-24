from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def back_from_selecting_goal_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✏️ Изменить', callback_data='edit_goal'),
                InlineKeyboardButton(text='❌ Удалить', callback_data='delete_goal')
            ],
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data='my_goals')
            ]
        ]
    )
    return markup


async def back_from_selecting_habit_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✏️ Изменить', callback_data='edit_habit'),
                InlineKeyboardButton(text='❌ Удалить', callback_data='delete_habit')
            ],
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data='my_habits')
            ]
        ]
    )
    return markup


async def back_from_selecting_task_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✏️ Изменить', callback_data='edit_task'),
                InlineKeyboardButton(text='❌ Удалить', callback_data='delete_task')
            ],
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data='my_tasks')
            ]
        ]
    )
    return markup
