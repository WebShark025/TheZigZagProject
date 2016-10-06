# -*- coding: utf-8 -*-

import telebot
import json
from os.path import exists

triggers = {}
tfile = "chatter_data.json"
separator = '||'

if(exists(tfile)):
    with open(tfile) as f:
        f = open(tfile)
        triggers = json.load(f)
        print("[Chatter] Loaded data.json file.")
else:
    print("[Chatter] Creating data.json file.")
    f = open(tfile, 'a')
    f.write("{}")
    f.close()

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

def newTrigger(trigger, response):
    trigger = trim(trigger)
    triggers[trigger.lower()] = trim(response)
    with open(tfile, "w") as f:
        json.dump(triggers, f)

@bot.message_handler(commands=['addreply'])
def add_reply_t(message):
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Hey! 😱 \n \nI think you don't know how to work with this. \n \nYou can actually learn me how to respond to some messages 😏 \n \nSimply do: /addreply <Text>||<Response> \n \nFor example, if you want to enter 'hi' and then you want me to say 'hello', you need to execute this: \n /addreply Hi||Hello \n \nIts simple 😌 And also fun 😍", parse_mode="Markdown")
        return
    cid = message.chat.id
    text = message.text.replace("/addreply ","",1)
    try:
        i = text.rindex(separator)
    except:
        bot.send_message(cid, "String recieved in an incorrect format..")
        return
    tr = text.split(separator)[0]
    if len(tr) < 3:
        bot.reply_to(message, str(tr) + " Is too short!")
        return
    re = text.split(separator)[1]
    if triggers.has_key(tr):
        bot.reply_to(message, "Im sorry, this message had already been defined!")
        return
    newTrigger(tr,re)
    bot.send_message(cid, "Ooo yeah! Now I know if you say `"+tr+"`, I Should Answer `"+re+"` :) \nCan you teach me *more*? 😁😁", parse_mode="Markdown")
