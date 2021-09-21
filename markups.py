from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

games = InlineKeyboardMarkup(row_width=2)
game_bones = InlineKeyboardButton(text="Игральные Кости", callback_data="bones")
game_kmb = InlineKeyboardButton(text="Камень, Ножницы, Бумага", callback_data="kmb")

games.insert(game_bones)
games.insert(game_kmb)

kam_noj_bum = InlineKeyboardMarkup(row_width=3)
kamen = InlineKeyboardButton(text='✊🏻', callback_data='kamen')
nojnicy = InlineKeyboardButton(text='✌🏻', callback_data='nojnicy')
bumaga = InlineKeyboardButton(text='✋🏻', callback_data='bumaga')

kam_noj_bum.insert(kamen)
kam_noj_bum.insert(nojnicy)
kam_noj_bum.insert(bumaga)