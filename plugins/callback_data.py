# -*- coding: utf-8 -*-

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.message:
    if call.data == "help":
      bot.send_message(call.message.chat.id, START_MSG.encode("utf-8"), parse_mode="Markdown")
      bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Here you are!")
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
