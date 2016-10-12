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
    userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
    if len(message.text.split()) < 2:
        bot.reply_to(message, language[userlang]["CHATTER_NEA_MSG"], parse_mode="Markdown")
        return
    cid = message.chat.id
    text = message.text.replace("/addreply ","",1)
    try:
        i = text.rindex(separator)
    except:
        bot.send_message(cid, language[userlang]["CHATTER_INCORRECT_MSG"])
        return
    tr = text.split(separator)[0]
    if len(tr) < 3:
        bot.reply_to(message, str(tr) + " Is too short!")
        return
    re = text.split(separator)[1]
    if triggers.has_key(tr):
        bot.reply_to(message, language[userlang]["CHATTER_ALREADYDEFINED_MSG"])
        return
    newTrigger(tr,re)
    bot.send_message(cid, language[userlang]["CHATTER_DONE_MSG"].format(tr, re), parse_mode="Markdown")
