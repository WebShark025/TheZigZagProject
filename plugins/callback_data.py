@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.message:
    if call.data == "help":
      bot.send_message(call.from_user.id, START_MSG.encode("utf-8"), parse_mode="Markdown")
