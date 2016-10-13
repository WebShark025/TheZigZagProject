# -*- coding: utf-8 -*-

@bot.message_handler(commands=['setlang' , 'Setlang'])
def setlang_message(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, "Please choose a language! En/Fa \nلطفا زبان مورد نظر خود را وارد کنید! فارسی/انگلیسی", parse_mode="Markdown")
    return
  if True:
    langz = message.text.replace("/setlang ","",1).replace("/Setlang ","",1)
    if langz == "en":
      redisserver.set("settings:user:language:" + str(message.from_user.id), "en")
      bot.send_message(message.chat.id, "Success!")
    elif langz == "fa":
      redisserver.set("settings:user:language:" + str(message.from_user.id), "fa")
      bot.send_message(message.chat.id, "انجام شد!")
    else:
      bot.reply_to(message, "Language not found \n زبان یافت نشد")
