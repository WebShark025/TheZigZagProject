import requests

awaiting_audio = {"981": "hi"}

@bot.message_handler(commands=['mp3tag', 'Mp3tag'])
def mp3tag(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split("||")) < 2:
    bot.send_message(message.chat.id, language[userlang]["MP3TAG_NEA_MSG"], parse_mode="Markdown")
    return
  if awaiting_audio.has_key(str(userid)):
    bot.send_message(message.chat.id, language[userlang]["MP3TAG_SENDAUDIO_MSG"])
    return
  args = message.text.replace("/mp3tag","")
  dictargs = {str(userid): args}
  awaiting_audio.update(dictargs)
  bot.send_message(message.chat.id, language[userlang]["MP3TAG_SENDAUDIO_MSG"])
@bot.message_handler(content_types=['audio'])
def handle_docs_audio(message):
  if awaiting_audio.has_key(str(message.from_user.id)):
    bot.send_chat_action(message.chat.id, "upload_document")
    tm.sleep(2)
    fileid = message.audio.file_id
    fileargs = awaiting_audio[str(message.from_user.id)].split("||")
    file_info = bot.get_file(fileid)
    file = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path), 'music.mp3')
    bot.send_audio(message.chat.id, open('music.mp3', 'rb'), duration=message.audio.duration, performer=fileargs[0], title=fileargs[1])
    del awaiting_audio[str(message.from_user.id)]
#

