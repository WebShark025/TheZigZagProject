# -*- coding: utf-8 -*-

@bot.message_handler(commands=['settings', 'Settings'])
def send_settings(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  markup = types.InlineKeyboardMarkup()
  markupib = types.InlineKeyboardButton("Show settings!", callback_data='settings')
  markup.add(markupib)
  bot.send_message(message.chat.id, "Please, press on the button below :)", parse_mode="Markdown", reply_markup=markup)
