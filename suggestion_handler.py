import database_api as dbi
import telebot
import util

def create_suggestion(bot, message):
    arg = util.get_arg(message.text)
    if (arg == None or len(arg) == 0) :
        bot.reply_to(message, "Insira a sugestão junto com o comando")
    else :
        dbi.create_suggestion(message.from_user.username, arg)
        bot.reply_to(message, "Sugestão salva!")
