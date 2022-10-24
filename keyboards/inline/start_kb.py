from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def menu_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='➕ Добавить', callback_data='create')
            ],
            [
                InlineKeyboardButton(
                    text='♻️ Привычки', callback_data='my_habits'
                ),

                InlineKeyboardButton(
                    text='🎯 Цели', callback_data='my_goals'
                ),
                InlineKeyboardButton(
                    text='❗️ Задачи', callback_data='my_tasks'
                )
            ]
        ]
    )
    return markup