import telebot
import json
from os.path import exists

triggers = {}
tfile = "data.json"
tokenf = "token.txt"

separator = '/'

if(exists(tfile)):
    with open(tfile) as f:
        #If exists, but is empty, don't load.
        if(f.readline() == ''):
            print("> The File for Data is empty!")
            f.close
        else:
            f = open(tfile)
            triggers = json.load(f)
else:
    print("Creating new file.")
    f = open(tfile, 'w')
    f.close()

#Check if Token file exists, if not, create.
if(exists(tokenf)):
    with open(tokenf) as g:
        token = g.readline()
        #Here we cut the last char in token because is a newline char.
        token = token[:len(token) -1]
        print("Token = [" + token + "]")
else:
    print("Token File not found, creating.")
    g = open(tokenf, 'w')
    g.write("YOUR TOKEN HERE")
    f.close()

#Delete whitespaces at start & end
def trim(s):
    i = 0
    while(s[i] == ' '):
        i += 1
    s = s[i:]
    i = len(s)-1
    while(s[i] == ' '):
        i-= 1
    s = s[:i+1]
    return s

#Function to add new Trigger - Response
def newTrigger(trigger, response):
    trigger = trim(trigger)
    triggers[trigger.lower()] = trim(response)
    with open(tfile, "w") as f:
        json.dump(triggers, f)
    print("triggers file saved")

#Create Bot.
bot = telebot.TeleBot("YOUR TOKEN HERE!")

#Adds another trigger-response. ex: "/add Hi / Hi!! :DD"
@bot.message_handler(commands=['add'])
def add(m):
    cid = m.chat.id
    text = m.text[4:]
    print("Try :" + text)
    try:
        i = text.rindex(separator)
    except:
        bot.send_message(cid, "Error :|")
    print("I value = " + str(i))
    tr = text[:i]
    re = text[i+1:]
    print("TR = " + tr + " - RE = " + re)
    newTrigger(tr,re)
    bot.send_message(cid, "ALASKA! \nCommand:"+tr+"] \n Answer: ["+re+"]")




#Sets separator character.
@bot.message_handler(commands=['separator'])
def separat(m):
    v = "#$=*-|@~+^ยบ"
    h = "Usage: /separator <char>\nset separator character for <Trigger> <Response>, valid chars: "+v
    cid = m.chat.id
    try:
        m.text.rindex(' ')
    except:
        bot.send_message(cid, h)
    sep = m.text[11:]
    if(sep in v):
        separator = sep
        bot.send_message(cid, "Separator character set to ["+separator+"]")
    else:
        bot.send_message(cid, "Character ["+sep+"] not allowed.")


@bot.message_handler(commands=['cmds'])
def all(m):
    cid = m.chat.id
    build = ''
    for t in triggers:
        build = build + t +"\n"
    bot.reply_to(m, build)

#Catch every message, for triggers :D
@bot.message_handler(func=lambda m: True)
def response(m):
    print("Checking for triggers in Message [" + m.text + "]")
    for t in triggers:
        if(t in m.text):
            bot.reply_to(m, triggers[t])
