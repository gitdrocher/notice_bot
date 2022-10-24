from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# State
async def back_from_creating_actions_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data='back_from_creating_actions')
            ]
        ]
    )
    return markup


# Not State
async def back_from_creating_actions_keyboard_end_state():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔙 Назад', callback_data='back_from_creating_actions_end_state')
            ]
        ]
    )
    return markup


# Back From Description State
async def skip_adding_description_keyboard_goal():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✖️ Пропустить', callback_data='goal|skip_adding_description')
            ]
        ]
    )
    return markup


async def skip_adding_description_keyboard_habit():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✖️ Пропустить', callback_data='habit|skip_adding_description')
            ]
        ]
    )
    return markup


async def skip_adding_description_keyboard_task():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='✖️ Пропустить', callback_data='task|skip_adding_description')
            ]
        ]
    )
    return markup
