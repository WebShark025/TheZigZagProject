# -*- coding: utf-8 -*-

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.message:
    if call.data == "help":
      bot.send_message(call.message.chat.id, START_MSG, parse_mode="Markdown")
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Here you are!")
    if call.data == "settingsmain":
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("Language - زبان", callback_data='settingslang')
      markupic = types.InlineKeyboardButton("More coming soon!", callback_data='soon')
      markup.add(markupib,markupic)
      msgid = call.inline_message_id
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=SETTINGS_WLC_MSG, parse_mode="Markdown", reply_markup=markup)
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
    if call.data == "settings":
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("Language - زبان", callback_data='settingslang')
      markupic = types.InlineKeyboardButton("More coming soon!", callback_data='soon')
      markup.add(markupib,markupic)
      bot.send_message(call.message.chat.id, SETTINGS_WLC_MSG, parse_mode="Markdown", reply_markup=markup)
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False)
    if call.data == "settingslang":
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markupib = types.InlineKeyboardButton("🇱🇷 English", callback_data='settingslangen')
      markupic = types.InlineKeyboardButton("🇮🇷 Persian", callback_data='settingslangfa')
      markup.add(markupib,markupic)
      markupif = types.InlineKeyboardButton("Back بازگشت", callback_data='settingsmain')
      markup.add(markupif)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text="Please choose a language. \nلطفا یک زبان انتخاب کنید. \n〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰", parse_mode="Markdown", reply_markup=markup)
    if call.data == "settingslangen":
      redisserver.set("settings:user:language:" + str(call.message.from_user.id), "en")
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markupif = types.InlineKeyboardButton("Back to main", callback_data='settingsmain')
      markup.add(markupif)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=SETTINGS_LANGUAGE_CHANGED_MSG, parse_mode="Markdown", reply_markup=markup)
    if call.data == "settingslangfa":
      redisserver.set("settings:user:language:" + str(call.message.from_user.id), "fa")
      msgid = call.inline_message_id
      markup = types.InlineKeyboardMarkup()
      markupif = types.InlineKeyboardButton("بازگشت به منو اصلی", callback_data='settingsmain')
      markup.add(markupif)
      bot.edit_message_text(inline_message_id=msgid, chat_id=call.message.chat.id, message_id=call.message.message_id, text=SETTINGS_LANGUAGE_CHANGED_MSG, parse_mode="Markdown", reply_markup=markup)
    if call.data == "inlinehelp":
      bot.send_message(call.message.chat.id, INLINE_HELP_MSG, parse_mode="Markdown")
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Here you are!")
    if call.data == "showit":
      markup = types.ReplyKeyboardMarkup()
      numbers = list(range(3, 3000, 3))
      numbers = [0] + numbers
      cline = 0
      linelength = len(START_BUTTONS)
      try:
        while (cline < linelength):
          itembtn = []
          cfrom = numbers[cline]
          cto = numbers[cline + 1]
          cline = cline + 1
          while (cfrom < cto):
            itembtn.append(START_BUTTONS[cfrom])
            cfrom = cfrom + 1
            if len(itembtn) == 3:
              markup.row(*itembtn)
      except:
        lolalola = 0
      bot.send_message(call.message.chat.id, SHOWED_BUTTONS_MSG, reply_markup=markup, parse_mode="Markdown")
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Here you are!")
    if call.data.split("-")[0] == "sil":
      print("OMG")
      markup = types.ReplyKeyboardMarkup()
      inlineid = call.data.split("-")[1][-5:]
      if inlineid in querymessages:
        inline_text = querymessages(inlineid)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=inline_text)
        print("OMG1")
      else:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Timeout exceeded.")
        print("OMG2")
  try:
    if call.data.split("|")[0] == "sil":
      markup = types.ReplyKeyboardMarkup()
      inlineid = call.data.split("|")[1]
      if inlineid in querymessages:
        inline_text = querymessages[inlineid]
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text=inline_text)
      else:
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Timeout exceeded.")
        print("OMG2")
  except:
    print("EXC")
    pass
