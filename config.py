import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API token (замените на свой токен)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# ID администратора 
ADMIN_ID = int(os.getenv('ADMIN_ID'))

# База данных (на данный момент используется словарь, в будущем - подключение к БД)
DATABASE = {}

# Список игр
GAMES = {
    "игра_1": {
        "name": "Игра 1",
        "balance": 100,
        "currency": "Золотые монеты",
        "description": "Описание игры 1"
    },
    "игра_2": {
        "name": "Игра 2",
        "balance": 50,
        "currency": "Серебряные монеты",
        "description": "Описание игры 2"
    },
    "игра_3": {
        "name": "Игра 3",
        "balance": 25,
        "currency": "Бронзовые монеты",
        "description": "Описание игры 3"
    },
}

# Словарь для хранения ставок
BETS = {}
