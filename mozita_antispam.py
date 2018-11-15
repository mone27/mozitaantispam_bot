﻿import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

TOKEN="---NASCOSTO---"

#COPIARE E INCOLLARE DA QUI - IL TOKEN E' GIA' INSERITO

versione="0.0.5 preview"
ultimoAggiornamento="16-11-2018"

VUtenti=[240188083,75870906]#295348075
VUtenti_name=["mone27"]
TUtenti=[]
SUtenti=[]
#V = Verified - T = Temporary - S = Spam

def risposte(msg):
    localtime=datetime.now()
    localtime=localtime.strftime("%d/%m/%y %H:%M:%S")
    '''file=open("log.txt","a") #apre il file in scrittura "append" per inserire orario e data -> log di utilizzo del bot (ANONIMO)
    file.write(localtime+"\n") #ricordare che l'orario è in fuso orario UTC pari a 0 (Greenwich, Londra) - mentre l'Italia è a +1 (CET) o +2 (CEST - estate)
    file.close()'''
    try:
        chat_id=msg['chat']['id']
        text=msg['text']
        user_id=msg['from']['id']
        user_name=msg['from']['username']
        message_id=msg['message_id']
    except:
        print("Exception:001 - "+localtime)
        ##entra in questa eccezione se NON è avviato come comando diretto (digitato come comando e inviato)
    try:
        query_id, chat_id, text = telepot.glance(msg, flavor='callback_query')
    except:
        print("Exception:002 - "+localtime)
        ##entra in questa eccezione se NON è stato premendo su un pulsante delle inlineKeyboard
    ##I try-except precedenti servono per assegnare, in qualunque circostanza, chat_id e text corettamente (in base al caso)
    print("Testo: "+str(text)+" - Chat: "+str(chat_id)+" - Utente: "+str(user_name)+" - Id Utente: "+str(user_id)+" - Id Messaggio: "+str(message_id))

    new = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Leggi il Regolamento', url='https://github.com/Sav22999/Guide/blob/master/Mozilla%20Italia/Telegram/regolamento.md')],
                ])

    #response = bot.getUpdates()
    #print(response)

    if user_id in VUtenti or str(user_name) in VUtenti_name:
        print ("Utente verificato!")
        #bot.sendMessage(chat_id, "@"+str(user_name)+" è un utente verificato !")
    elif user_id in TUtenti:
        print ("Utente non verificato!")
        bot.deleteMessage(telepot.message_identifier(msg))
        bot.sendMessage(chat_id, "@"+str(user_name)+" non è stato verificato: Messaggio eliminato.")
    elif user_id in SUtenti:
        print ("Utente spam")
        bot.kickChatMember(chat_id, user_id, until_date=None)
        bot.sendMessage(chat_id, "@"+str(user_name)+" è stato bannato !")
    else:
        bot.sendMessage(chat_id, "@"+user_name+", benvenuto nel gruppo ufficiale di Mozilla Italia!", reply_markup=new)
        TUtenti.append(int(user_id))
        #utente da inserire nella lista momentanea -> nuovo utente

bot=telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': risposte, 'callback_query': risposte}).run_as_thread()

while 1:
    time.sleep(10)