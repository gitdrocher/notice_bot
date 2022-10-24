if __name__ == '__main__':
    import logging

    logging.basicConfig(
        level=logging.INFO
    )
    from aiogram import executor
    from handlers import dp
    from data.functions.connect_base import on_startup

    executor.start_polling(dp, on_startup=on_startup())
