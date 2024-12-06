from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import Regex

# Ваш токен бота
BOT_TOKEN = "7522613936:AAHCP56J038xerHw--G7NtjYyIzZ0JLnbqQ"

# Обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user

    # Исключаем пользователя из чата
    try:
        await context.bot.ban_chat_member(chat.id, user.id)
        # Разбаниваем сразу, чтобы его сообщения остались
        await context.bot.unban_chat_member(chat.id, user.id)
        # Уведомляем чат
        await update.message.reply_text(f"Пользователь {user.first_name} исключён за использование запрещённого слова!")
    except Exception as e:
        print(f"Ошибка при исключении пользователя: {e}")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот активен! Запрещено писать слово 'Сталинград'.")

# Основная функция
def main():
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Regex("(?i).*Сталинград.*"), handle_message))  # Регулярное выражение

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()