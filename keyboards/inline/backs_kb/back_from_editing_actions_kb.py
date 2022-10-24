from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# State
async def back_from_editing_goal_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data=f'back_edit_goal')
            ]
        ]
    )
    return markup


async def back_from_editing_habit_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data=f'back_edit_habit')
            ]
        ]
    )
    return markup


async def back_from_editing_task_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data=f'back_edit_task')
            ]
        ]
    )
    return markup
