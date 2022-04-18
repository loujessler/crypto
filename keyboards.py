from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Пополнение')
        ], [
            KeyboardButton(text='Мой кошелек'),
            KeyboardButton(text='Мои виртуальные карты'),
        ], [
            KeyboardButton(text='Как пользоваться ботом'),
            KeyboardButton(text='Связаться с нами')
        ]
    ],
    resize_keyboard=True
)


call_back = CallbackData('buy', 'id', 'name')

keyboard_charge = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пополнение внутреннего Bitcoin кошелька (BTC)'),
        ],[
            KeyboardButton(text='Пополнение внутреннего Ethereum кошелька (ETH)'),
        ],[
            KeyboardButton(text='Пополнение внутреннего Tron кошелька (TRX)'),
        ],[
            KeyboardButton(text='Пополнение внутреннего USDT кошелька (USDT)'),
        ],[
            KeyboardButton(text='Назад'),
        ]
    ],
    resize_keyboard=True
)