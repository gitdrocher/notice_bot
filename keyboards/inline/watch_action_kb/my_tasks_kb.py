from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.functions import WatchAction


async def my_tasks_keyboard(user_id):
    var = WatchAction().watch_tasks(user_id,)
    buttons_dict = {
        i: x
        for i, x in enumerate(var)
    }
    button_list = [
        InlineKeyboardButton(
            text=a[1], callback_data=f'task|{user_id}_{a[0]}')
        for a in buttons_dict.values()
    ]
    back_button = InlineKeyboardButton(
        text='🔙 Назад', callback_data='back_to_menu'
    )
    markup = InlineKeyboardMarkup(row_width=1).add(*button_list, back_button)
    return markup
