#!/usr/bin/env python
import telebot
import datetime
from datetime import datetime
import random
import database_api as dbi
import mandamentos_handler as mh
import event_handler as eh
import exchange as ex
import miscellaneous as misc
import suggestion_handler as sh
import requests
import json
import keys
import sys
# Bot configuration

#bot = telebot.TeleBot(keys.keys['path_test'])
bot = telebot.TeleBot(keys.keys[sys.argv[1]])
session = {}
session['greeting_message'] = "Bom dia, grupo!"
session['have_already_sent_greeting'] = True
session['help_terator'] = 0
    
def to_timestamp(millis):
    return str(datetime.fromtimestamp(millis))


################################################################################
##                              MESSAGE HANDLERS                              ##
################################################################################

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Bem-vindo ao bot do Sucrilhos")

   
@bot.message_handler(commands=['help'])
def send_help(message):
    misc.send_help(bot, message, session['help_terator'])
    session['help_terator'] += 1
 
   
################### - mandamentos - #############################
@bot.message_handler(commands=['set_mandamento'])
def handle_command(message):
    mh.set_mandamento(bot, message)
    
@bot.message_handler(commands=['mandamentos'])
def handle_command(message):
    mh.list_mandamentos(bot, message)

@bot.message_handler(commands=['mandamento'])
def handle_command(message):
    mh.find_mandamento(bot, message)

############ - events - #################
@bot.message_handler(commands=['create_event', 'set_event', 'new_event'])
def handle_command(message):
    eh.create_event(bot, message)

@bot.message_handler(commands=['list_events', 'events'])
def handle_command(message):
    eh.find_all_events(bot, message)

@bot.message_handler(commands=['event', 'find_event'])
def handle_command(message):
    eh.find_event(bot, message)
        
@bot.message_handler(commands=['update_event', 'edit_event'])
def handle_command(message):
    print(message.text)
    eh.update_event(bot, message)

@bot.message_handler(commands=['delete_event', 'destroy_event', 'obliterate_event'])
def handle_command(message):
    eh.delete_event(bot, message)

@bot.message_handler(commands=['last_event'])
def handle_command(message):
    eh.last_event(bot, message)


############### - miscellaneous - ##################
@bot.message_handler(commands=['roll_d6'])
def roll_d6( message):  
    bot.reply_to(message, random.randint(1,6))
    
@bot.message_handler(commands=['roll_d20', 'roll'])   
def roll_d20( message):  
    bot.reply_to(message, random.randint(1,20))
    

@bot.message_handler(commands=['dolar', 'dólar', 'dollar', 'Dollar', 'dollar'])
def dollar(message):
    ex.dollar(bot, message)
    
@bot.message_handler(commands=['ex_rate', 'ex', 'rate', 'exchange_rate', 'quanto_tá'])
def ex_rate(message):
    ex.ex_rate(bot, message)
    
@bot.message_handler(commands=['create_suggestion', 'new_suggestion', 'set_suggestion'])
def create_suggestion(message):
    sh.create_suggestion(bot, message)

@bot.message_handler(commands=['vtncp'])
def vtncp(message):
    misc.vtncp(bot,message)
    
@bot.message_handler(command=['remount_greeting'])
def remount_greeting(message):
   session['have_already_sent_greeting'] = False
   session['greeting_message'] = util.get_arg(message.text)
   bot.reply_to(message, "Remontado! " + session['greeting_message'])
    
################### - general messages - ##########################
@bot.message_handler(func=lambda message: True)
def handle_any_message( message):
    print(to_timestamp(message.date) + " " + message.from_user.username + ": " + message.text)
    
    if message.content_type == "text":
        f = open("log" + str(message.chat.id) + ".txt","a+")
        m = {"user": str(message.from_user.username), "date": to_timestamp(message.date), "text": message.text}
        f.write(str(m))
        f.write("\n")
        f.close()
    if session['have_already_sent_greeting'] == False and datetime.now().hour > 5 and datetime.now().hour < 12:
        bot.send_message(message.chat.id, session['greeting_message'])
        session['have_already_sent_greeting'] = True
    if message.text in {"Olá", "olá", "ola", "olá", "oi", "Oi", "Olá!"} :
        bot.send_message(message.chat.id, "Olá de volta!")
    if message.text.lower() in {"maconha", "makonha", "droga", "erva"} :
        bot.send_message(message.chat.id, "Quero.")
    if random.randint(0,1000) == 69:
        bot.send_message(message.chat.id, "EITA GARRADA DURA!")


print("Starting bot")
bot.polling()

