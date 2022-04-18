from email import message
from subprocess import call
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text, Command
# from aiogram.types.input_media import InputMediaPhoto


from keyboards import keyboard,keyboard_charge

from main import bot, dp
from config import admin_users
from config import message_about_us, message_how_use, message_put, message_contact, message_my_vcard, message_my_wallet
from config import messages_of_wallets, wallets

async def send_hello(dp):
    await bot.send_message(chat_id=admin_users[0], text='Start crypto bot')


@dp.message_handler(Command('start'))
async def show_start(message: Message):
    await message.answer(f'Здравствуйте, {message.chat.first_name} {message.chat.last_name}!\nПожалуйста, выберите пункт из меню ниже.', reply_markup=keyboard)
    print(message.chat.id)
# @dp.message_handler(Text(equals=['Назад']))
# async def show_guide(message: Message):
#         await message.answer('Пожалуйста, выберите пункт из меню ниже.', reply_markup=keyboard)

@dp.message_handler(Command('guide'))
async def show_guide(message: Message):
    await message.answer(message_how_use, reply_markup=keyboard)

@dp.message_handler(Command('wallet'))
async def show_wallet(message: Message):
    await message.answer(message_my_wallet, reply_markup=keyboard)

@dp.message_handler(Command('mycards'))
async def show_mycards(message: Message):
    await message.answer_photo(open('card.jpeg', 'rb'),message_my_vcard, reply_markup=keyboard)

@dp.message_handler(Command('help'))
async def show_help(message: Message):
    await message.answer(message_contact, reply_markup=keyboard)

@dp.message_handler(Command('charge'))
async def _(message: Message):
    await show_charge(message)
# await message.answer(show_charge(), reply_markup=keyboard)
# await message.answer.s


@dp.message_handler(Text(equals=['Пополнение внутреннего Bitcoin кошелька (BTC)',\
    'Пополнение внутреннего Ethereum кошелька (ETH)',\
        'Пополнение внутреннего Tron кошелька (TRX)',\
        'Пополнение внутреннего USDT кошелька (USDT)',\
            'Назад']))
async def show_charge(message: Message):
    if message.text == 'Пополнение внутреннего Bitcoin кошелька (BTC)':
        await message.answer_photo(open('btc_qr.png','rb'),messages_of_wallets[0])
        await message.answer(wallets[0], reply_markup=keyboard)   
        for x in range(len(admin_users)):
            await bot.send_message(admin_users[x],'Кто-то пополняет BTC')
    elif message.text == 'Пополнение внутреннего Ethereum кошелька (ETH)':
        await message.answer_photo(open('eth_qr.png','rb'),messages_of_wallets[1])
        await message.answer(wallets[1], reply_markup=keyboard)
        for x in range(len(admin_users)):
            await bot.send_message(admin_users[x],'Кто-то пополняет ETH')
    elif message.text == 'Пополнение внутреннего Tron кошелька (TRX)':
        await message.answer_photo(open('trx_qr.png','rb'),messages_of_wallets[2])
        await message.answer(wallets[2], reply_markup=keyboard)
        for x in range(len(admin_users)):
            await bot.send_message(admin_users[x],'Кто-то пополняет TRX')
    elif message.text == 'Пополнение внутреннего USDT кошелька (USDT)':
        await message.answer_photo(open('usdt_qr.png','rb'),messages_of_wallets[3])
        await message.answer(wallets[3], reply_markup=keyboard)
        for x in range(len(admin_users)):
            await bot.send_message(admin_users[x],'Кто-то пополняет USDT')
    elif message.text == 'Назад':
        await message.answer('Пожалуйста, выберите пункт из меню ниже.', reply_markup=keyboard)
    else:
        await message.answer(message_put, reply_markup=keyboard_charge)
    # if message.text == 'Назад':
    #     await message.answer('Пожалуйста, выберите пункт из меню ниже.', reply_markup=keyboard)


@dp.message_handler(Text(equals=['О нас','Пополнение','Мой кошелек','Мои виртуальные карты','Как пользоваться ботом','Связаться с нами']))
async def get_menu(message: Message):
    photo_card = open('card.jpeg')
    if message.text == 'О нас':
        await message.answer(message_about_us, reply_markup=keyboard)
    elif message.text == 'Пополнение':
        await show_charge(message)
    elif message.text == 'Мой кошелек':
        await show_wallet(message)
    elif message.text == 'Мои виртуальные карты':
        await show_mycards(message)
    elif message.text == 'Как пользоваться ботом':
        await show_guide(message)
    elif message.text == 'Связаться с нами':
        await show_help(message)


# await message.answer(message.text, reply_markup=ReplyKeyboardRemove())