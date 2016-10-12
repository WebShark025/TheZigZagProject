# -*- coding: utf-8 -*-

@bot.message_handler(commands=['weather', 'Weather'])
def weather_image(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.replace("🌤 Weather", "", 1).split()) < 2:
    bot.reply_to(message, WWEATHER_NEA_MSG, parse_mode="Markdown")
    return
  city = message.text.replace("/weather ","").replace(" ", "%20")
  try:
    url = json.load(urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d2def4a0a0455314526b0f455f98ec0f&units=metric".format(city)))
  except:
    print("[Weather] Exception occured")
    return
  bot.send_message(message.chat.id, "💢 Current status of *" + str(url["name"]) + "*: \n\n🌍 Country: `" + str(url["sys"]["country"]) + "` \n☀️ Temperature: `" + str(url["main"]["temp"]) + "°C` \n" + "🌤 Weather: `" + str(url["weather"][0]["main"]) + "` \n💨 Wind: `" + str(url["wind"]["speed"]) + "m/s` \n💧 Humidity: `" + str(url["main"]["humidity"]) + "%`", parse_mode="Markdown")
