# -*- coding: utf-8 -*-

@bot.message_handler(commands=['date', 'time', 'Date', 'Time'])
def time_message(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, language[userlang]["TIME_NEA_MSG"], parse_mode="Markdown")
    return
  city = message.text.split()[1]
  try:
    tzd = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={}".format(city)))
    if str(tzd["status"]) == "OK":
      latlng = tzd["results"][0]["geometry"]["location"]
      lat = str(latlng["lat"])
      lng = str(latlng["lng"])
      tzl = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/timezone/json?location={}&timestamp=1331161200".format(lat + "," + lng)))
      timezone = tzl["timeZoneId"]
    else:
      bot.reply_to(message, "Timezone not found.")
      return
  except:
    print("[Time] Exception occured")
    return
#  bot.send_chat_action(message.chat.id, "typing")
#  tm.sleep(1)
  time = json.load(urllib.urlopen("https://script.google.com/macros/s/AKfycbyd5AcbAnWi2Yn0xhFRbyzS4qMq1VucMVgVvhul5XqS9HkAyJY/exec?tz={}".format(timezone)))
  bot.send_message(message.chat.id, "Current time in *" + timezone + "*: \n" + time["fulldate"], parse_mode="Markdown")
