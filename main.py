import telebot
import The_smart_part

bot = telebot.TeleBot('7224983182:AAHeT5I3WIhUIqnYOs6fUwhZXINi6wtpAIo');


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton(text="Начать анализ")
    button1 = telebot.types.KeyboardButton(text="поддержать автора")
    keyboard.add(button_support, button1)

    bot.send_message(chat_id,
                     'Добро пожаловать в бота который подскажет Вам стоит ли покупать акцию',
                     reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Начать анализ':
        bot.send_message(message.from_user.id, text='@' + message.from_user.first_name)
        question = 'давай начнем торговлю нужно ' + The_smart_part.main(The_smart_part.dt_now)
        bot.send_message(message.from_user.id, text=question)
    if message.text == 'поддержать автора':
        question = '+79914010490'
        bot.send_message(message.from_user.id, text=question)


bot.polling(none_stop=True, interval=0)
