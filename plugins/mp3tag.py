import requests

awaiting_audio = {"981": "hi"}

@bot.message_handler(commands=['mp3tag'])
def mp3tag(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split("||")) < 2:
    bot.send_message(message.chat.id, "Please use correct syntax: \n`/mp3tag Artist||Title`\nAnd then, send the audio file.", parse_mode="Markdown")
    return
  if awaiting_audio.has_key(str(userid)):
    bot.send_message(message.chat.id, "Please send the audio now!")
    return
  args = message.text.replace("/mp3tag","")
  dictargs = {str(userid): args}
  awaiting_audio.update(dictargs)
  bot.send_message(message.chat.id, "Please send the audio now!")
@bot.message_handler(content_types=['audio'])
def handle_docs_audio(message):
  if awaiting_audio.has_key(str(message.from_user.id)):
    fileid = message.audio.file_id
    fileargs = awaiting_audio[str(message.from_user.id)].split("||")
    file_info = bot.get_file(fileid)
    file = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path), 'music.mp3')
    bot.send_audio(message.chat.id, open('music.mp3', 'rb'), duration=message.audio.duration, performer=fileargs[0], title=fileargs[1])
    del awaiting_audio[str(message.from_user.id)]
#

