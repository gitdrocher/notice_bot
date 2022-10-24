from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def creating_action_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text='♻️ Привычка', callback_data='habit'),
                InlineKeyboardButton(
                    text='🎯 Цель', callback_data='goal'),
                InlineKeyboardButton(
                    text='❗️ Задача', callback_data='task')
            ],
            [InlineKeyboardButton(
                text='🔙 Назад', callback_data='back_to_menu')
            ]
        ]
    )
    return markup
