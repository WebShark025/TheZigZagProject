# -*- coding: utf-8 -*-

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    bot.reply_to(message, "You are banned!")
    return
  if len(message.text.split()) > 1:
    if message.text.replace("/start ","",1) == "inlinem":
      bot.send_message(message.chat.id, language[userlang]["INLINE_HELP_MSG"], parse_mode="Markdown")
      return
  markup = types.InlineKeyboardMarkup()
  markupib = types.InlineKeyboardButton(language[userlang]["HELP"],callback_data='help')
  markupic = types.InlineKeyboardButton(language[userlang]["CHANNEL"], url=CHANNEL_LINK)
  markup.add(markupib,markupic)
  markupif = types.InlineKeyboardButton(language[userlang]["SETTINGS"], callback_data='settings')
  markup.add(markupif)
  markupid = types.InlineKeyboardButton(language[userlang]["SHOW_ALL"], callback_data='showit')
  markup.add(markupid)
  markupie = types.InlineKeyboardButton(language[userlang]["INLINE_HELP"], callback_data='inlinehelp')
  markup.add(markupie)
  
  if message.chat.type == "private":
    bot.reply_to(message, language[userlang]["START_MSG"], reply_markup=markup, parse_mode="Markdown")
    redisserver.sadd('zigzag_members',message.from_user.id)
  else:
    bot.reply_to(message, language[userlang]["START_MSG"], parse_mode="Markdown")
