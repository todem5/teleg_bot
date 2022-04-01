import logging
from aiogram import Bot
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from telegram import Update

from settings import TG_TOKEN
from telegram.ext import Filters

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot)


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привет! Тест...."
    )
    keyboard = types.InlineKeyboardMarkup()
    foods = ['Бургер', 'Картофель', 'Куринные ножки']
    for food in foods:
        inline_btns = types.InlineKeyboardButton(food, callback_data=food)
    keyboard.add(inline_btns)

    @dp.callback_query_handler(lambda c: c.data == food)
    async def process_callback(call: types.CallbackQuery):
        await bot.edit_message_text(text=f"Нажата кнопка {food}", chat_id=call.message.chat.id,
                                    message_id=call.message.message_id)
    message.answer("Выберите блюдо:", reply_markup=keyboard)


def do_echo(bot: Bot, update: Update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )

def main():


    start_handler = CommandHandler("start", do_start)
    #message_handler = MessageHandler(Filters.text, do_echo())
    updater.dispatcher.add_handler(start_handler)
    #updater.dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)