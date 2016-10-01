import subprocess

@bot.message_handler(commands=['status'])
def bc_msg(message):
  if message.from_user.id in ADMINS_IDS:
    proc = subprocess.check_output("top -b |head -2 && free && df -l", shell=True)
    bot.reply_to(message, proc)
  else:
    bot.send_message(message.chat.id, "You dont have permission.")



