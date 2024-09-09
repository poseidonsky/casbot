from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram.ext.filters import Filters
import config

# Состояния для диалога
CHOOSING, TYPING_REPLY = range(2)

# Кнопки
BALANCE, ADD_BALANCE, RESET = range(3)
BALANCE_BUTTONS = [
    KeyboardButton("/balance"),
    KeyboardButton("/addbalance"),
    KeyboardButton("/reset")
]

def admin_start(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    if user_id == config.ADMIN_ID:
        reply_keyboard = ReplyKeyboardMarkup([BALANCE_BUTTONS], resize_keyboard=True)
        update.message.reply_text(
            "Добро пожаловать в админ-панель! Что вы хотите сделать?",
            reply_markup=reply_keyboard
        )
        return CHOOSING
    else:
        update.message.reply_text("У вас нет доступа к админ-панели.")
        return ConversationHandler.END

def admin_balance(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    if user_id == config.ADMIN_ID:
        # Получить баланс всех пользователей (из базы данных)
        # ...
        balances = "Балансы пользователей:\n"
        # ... 
        update.message.reply_text(balances)
    else:
        update.message.reply_text("У вас нет доступа к админ-панели.")
    return CHOOSING

def admin_addbalance(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    if user_id == config.ADMIN_ID:
        update.message.reply_text("Введите ID пользователя и сумму:")
        return TYPING_REPLY
    else:
        update.message.reply_text("У вас нет доступа к админ-панели.")
        return ConversationHandler.END

def admin_addbalance_reply(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    if user_id == config.ADMIN_ID:
        text = update.message.text
        try:
            user_to_add, amount = map(int, text.split())
            # Добавить баланс пользователю (в базу данных)
            # ...
            update.message.reply_text(f"Баланс пользователя {user_to_add} увеличен на {amount} монет.")
        except ValueError:
            update.message.reply_text("Неверный формат данных! Введите ID пользователя и сумму через пробел.")
        return CHOOSING
    else:
        update.message.reply_text("У вас нет доступа к админ-панели.")
        return ConversationHandler.END

def admin_reset(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    if user_id == config.ADMIN_ID:
        # Сбросить балансы всех пользователей (в базе данных)
        # ...
        update.message.reply_text("Балансы всех пользователей сброшены.")
    else:
        update.message.reply_text("У вас нет доступа к админ-панели.")
    return CHOOSING

# Обработчики команд для админ-панели
admin_handler = ConversationHandler(
    entry_points=[CommandHandler('admin', admin_start)],
    states={
        CHOOSING: [
            CommandHandler('balance', admin_balance),
            CommandHandler('addbalance', admin_addbalance),
            CommandHandler('reset', admin_reset),
        ],
        TYPING_REPLY: [MessageHandler(Filters.text & ~Filters.command, admin_addbalance_reply)],
    },
    fallbacks=[CommandHandler('cancel', ConversationHandler.END)],
)
