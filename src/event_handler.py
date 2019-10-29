import database_api as dbi
import telebot
import util

def create_event(bot, message):
    arg = util.get_arg(message.text)
    print("["+arg+"]")
    if len(arg) == 0:
        bot.reply_to(message, "Que tal escrever o nome do evento?")
        return
    event_parts = arg.split("###")
    if len(event_parts) == 1:
        bot.reply_to(message, """Utilize \"###\" para separar o nome da descrição do evento\n
                    exemplo: /create-event festa da paula###paula dentro, paula fora""")
        return  
    dbi.create_event(message.from_user.username, event_parts[0], event_parts[1])
    bot.reply_to(message, "Evento criado!")
    
def delete_event(bot, message):
    arg = util.get_arg(message.text)
    if len(arg) == 0:
        bot.reply_to(message, "Que tal escrever o nome do evento?")
        return
    if not dbi.event_exists(arg):
        bot.reply_to(message, "Não existe evento com nome " + arg)
        return
    dbi.delete_event(arg)
    bot.reply_to(message, "Evento deletado!")
    
def find_all_events(bot, message):
    arg = util.get_arg(message.text)
    print("["+arg+"]")
    if  not arg.isdigit():
        arg = 5
    event_name_list = dbi.find_all_events(int(arg))
    s = ""
    for event_name in event_name_list:
        s += event_name[0] + "\n"
    bot.reply_to(message, "Últimos " + str(len(event_name_list)) + " eventos:\n" + s )
    
def find_event(bot, message):
    arg = util.get_arg(message.text)
    print("["+arg+"]")
    if len(arg) == 0:
        bot.reply_to(message, "Escreva o nome de um evento")
        return
    if not dbi.event_exists(arg):
        bot.reply_to(message, "Não existe evento com nome " + arg)
        return
    row = dbi.find_event_by_name(arg)
    bot.reply_to(message, "Nome: " + row[0] + "\nDescrição:\n" + row[1] )

def update_event(bot, message):
    arg = util.get_arg(message.text)
    print("["+arg+"]")
    if len(arg) == 0:
        bot.reply_to(message, "Escreva o nome de um evento")
        return
    event_parts = arg.split("###")
    if len(event_parts) == 1:
        bot.reply_to(message, "Utilize \"###\" para separar o nome da descrição do evento")
        return
    if not dbi.event_exists(event_parts[0]):
        bot.reply_to(message, "Não existe evento com nome " + arg)
        return
    dbi.update_event_description(message.from_user.username, event_parts[0], event_parts[1])
    bot.reply_to(message, "Evento atualizado!\n")
    
def last_event(bot, message):
    row = dbi.last_event()
    bot.reply_to(message, "Nome: " + row[0] + "\nDescrição:\n" + row[1] )