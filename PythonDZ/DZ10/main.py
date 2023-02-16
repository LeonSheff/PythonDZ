from controller import parseable_data, calculate
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from log import get_id_user, get_input_data, get_result, save_log

        
TOKEN = '5935535467:AAFgg_9HXqLyYadigUvRyshKEdYbO3BYSH4'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_calc = 0

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! Я бот-калькулятор\n\
    Напиши мне и я помогу тебе с решением')
    
    get_id_user(update.effective_chat.id)
    return start_calc
       

def receiving_data(update, context):
    data = update.message.text
    get_input_data(data)
    list_data = parseable_data(data)
    result = calculate(list_data)
    get_result(result)
    save_log()
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')
    
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Пакеда')
    return ConversationHandler.END

start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(Filters.text, receiving_data)
mes_data_handler = CommandHandler('end', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start_calc: [receiving_data_handler]},
                                   fallbacks=[mes_data_handler])

dispatcher.add_handler(conv_handler)

print('БОТ ЗАПУЩЕН)))')

updater.start_polling()
updater.idle()