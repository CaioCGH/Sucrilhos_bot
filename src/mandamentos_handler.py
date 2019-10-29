import database_api as dbi
import telebot
import util

def set_mandamento(bot, message):
    arg = util.get_arg(message.text)
    if (arg == None or len(arg) == 0) :
        bot.reply_to(message, "Oh seu animal, tem q mandar alguma coisa né?!")
    else :
        dbi.insert_commandment(message.from_user.username, arg)
        bot.reply_to(message, "Mandamento salvo!")
    
def list_mandamentos(bot, message):
    commandments = dbi.find_all_commandments()
    s = ""
    for row in commandments:
        s += str( row[0] )  + ": \"" + str(row[3]) + "\"\n"
        
    bot.send_message(message.chat.id, s)

def find_mandamento(bot, message):
    arg = util.get_arg(message.text)
    if  not arg.isdigit():
        bot.reply_to(message, "Que tal experimentar um número?")
        return
    commandment = dbi.find_commandment(int(arg))
    if commandment == None:
        bot.reply_to(message, "Ainda não há um mandamento com este número")
        return
    s = str( commandment[0] )  + ": \"" + str(commandment[3]) + "\"\n"
    bot.send_message(message.chat.id, s)