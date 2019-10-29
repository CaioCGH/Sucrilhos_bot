import database_api as dbi
import telebot
import util
import json

def dollar(bot, message):
    content = util.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=BRL")
    obj = json.loads(content)
    print(str(obj.keys()))
    bot.reply_to(message, "R$" + str(obj['rates']['BRL']) )

def ex_rate(bot, message):
    arg = util.get_arg(message.text)
    content = util.get("https://api.exchangeratesapi.io/latest?base=" + arg + "&symbols=BRL")
    obj = json.loads(content)
    print(str(obj))
    if 'error' in obj:
        bot.reply_to(message, str(obj['error']) )
        return
    bot.reply_to(message, "R$" + str(obj['rates']['BRL']) )