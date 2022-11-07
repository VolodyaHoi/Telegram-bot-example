import telebot # lib 

print ("Bot started!..") # log

bot = telebot.TeleBot("your bot`s token") # token

@bot.message_handler(commands=["start"]) # start
def start(m, res=False):
    bot.send_message(m.chat.id, "Hello, Im B0t, if you need help, send /help")
    
@bot.message_handler(commands=["help"]) # user command
def start(m, res=False):
    bot.send_message(m.chat.id, "Help: ")

@bot.message_handler(content_types=["text"]) # get user message
def handle_text(message):
    bot.send_message(message.chat.id, "Your text: " + message.text)

bot.polling(none_stop=True, interval=0) # start
