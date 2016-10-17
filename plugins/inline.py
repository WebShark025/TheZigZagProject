# -*- coding: utf-8 -*-

querymessages = {}


@bot.inline_handler(lambda query: len(query.query) is 0)
def default_query(inline_query):
  try:
    r = types.InlineQueryResultArticle('1', 'default', types.InputTextMessageContent('default'))
    bot.answer_inline_query(inline_query.id, [None], switch_pm_text="Inline mode help", switch_pm_parameter="inlinem")
  except Exception as e:
    print(e)
@bot.inline_handler(lambda query: query.query.split()[0] == 'echo')
def query_text(inline_query):
  userlang = redisserver.get("settings:user:language:" + str(inline_query.from_user.id))
  try:
    if inline_query.query == "echo":
      r = types.InlineQueryResultArticle('1', language[userlang]["INLINE_ENTERTEXT_MSG"], types.InputTextMessageContent('I Love empty texts.'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      try:
        r3 = types.InlineQueryResultArticle('3', language[userlang]["INLINE_SUCCESSECHO_MSG"], types.InputTextMessageContent(inline_query.query.replace("echo ", "", 1), parse_mode="HTML"))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', language[userlang]["INLINE_ERRORECHO_MSG"], types.InputTextMessageContent("I forgot to close a tag."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)


@bot.inline_handler(lambda query: query.query.split()[0] == 'calc')
def query_text(inline_query):
  userlang = redisserver.get("settings:user:language:" + str(inline_query.from_user.id))
  try:
    if inline_query.query == "calc":
      r = types.InlineQueryResultArticle('1', language[userlang]["INLINE_CALC_MSG"], types.InputTextMessageContent('0! :D'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      text = inline_query.query.replace("calc ", "",1)
      res = urllib.urlopen("http://api.mathjs.org/v1/?expr={}".format(text).replace("+","%2B")).read()
      try:
        r3 = types.InlineQueryResultArticle('3', "_{}_ = `{}`".format(text,res), types.InputTextMessageContent("_{}_ = `{}`".format(text,res), parse_mode="Markdown"))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("I forgot to close a tag."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)

@bot.inline_handler(lambda query: query.query.split()[0] == 'hideit')
def hideit_text(inline_query):
  userlang = redisserver.get("settings:user:language:" + str(inline_query.from_user.id))
  try:
    if inline_query.query == "hideit":
      r = types.InlineQueryResultArticle('1', language[userlang]["INLINE_HIDEIT_MSG"], types.InputTextMessageContent('I Love empty texts.'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      try:
        markupz = types.InlineKeyboardMarkup()
        markupid = types.InlineKeyboardButton("Show hidden message!", callback_data='sil|' + inline_query.id)
        markupz.add(markupid)
        query_text = {inline_query.id: inline_query.query.replace("hideit ", "", 1)}
        querymessages.update(query_text)
        r3 = types.InlineQueryResultArticle('3', 'Send!', types.InputTextMessageContent("❓❓❓"), reply_markup=markupz)
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("Unexpected error occured."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)


@bot.inline_handler(lambda query: query.query.split()[0] == 'weather')
def query_text(inline_query):
  userlang = redisserver.get("settings:user:language:" + str(inline_query.from_user.id))
  try:
    if inline_query.query == "weather":
      r = types.InlineQueryResultArticle('1', language[userlang]["INLINE_WEATHER_MSG"], types.InputTextMessageContent('Wait, what?'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      city = inline_query.query.replace("weather ","").replace(" ", "%20")
      try:
        url = json.load(urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d2def4a0a0455314526b0f455f98ec0f&units=metric".format(city)))
      except:
        print("[WeatherInline] Exception occured")
        return
      try:
        r3 = types.InlineQueryResultArticle('3', language[userlang]["INLINE_SENDWEATHER_MSG"] + str(url["name"]), types.InputTextMessageContent("💢 Current status of *" + str(url["name"]) + "*: \n\n🌍 Country: `" + str(url["sys"]["country"]) + "` \n☀️ Temperature: `" + str(url["main"]["temp"]) + "°C` \n" + "🌤 Weather: `" + str(url["weather"][0]["main"]) + "` \n💨 Wind: `" + str(url["wind"]["speed"]) + "m/s` \n💧 Humidity: `" + str(url["main"]["humidity"]) + "%`", parse_mode="Markdown"))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("Unexpected error occured."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)


@bot.inline_handler(lambda query: query.query.split()[0] == 'time')
def query_text(inline_query):
  userlang = redisserver.get("settings:user:language:" + str(inline_query.from_user.id))
  try:
    if inline_query.query == "time":
      r = types.InlineQueryResultArticle('1', language[userlang]["INLINE_SENDTIME_MSG"], types.InputTextMessageContent('Time in nowhere: 00:00:00'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      city = inline_query.query.split()[1]
      try:
        tzd = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={}".format(city)))
        if str(tzd["status"]) == "OK":
          latlng = tzd["results"][0]["geometry"]["location"]
          lat = str(latlng["lat"])
          lng = str(latlng["lng"])
          tzl = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/timezone/json?location={}&timestamp=1331161200".format(lat + "," + lng)))
          timezone = tzl["timeZoneId"]
        else:
          rz = types.InlineQueryResultArticle('3', 'Timezone not found', types.InputTextMessageContent("Time in nowhere: 00:00:00"))
          bot.answer_inline_query(inline_query.id, [rz], cache_time=1, is_personal=True)
          return
      except:
        print("[TimeInline] Exception occured")
        return
      time = json.load(urllib.urlopen("https://script.google.com/macros/s/AKfycbyd5AcbAnWi2Yn0xhFRbyzS4qMq1VucMVgVvhul5XqS9HkAyJY/exec?tz={}".format(timezone)))
      try:
        r3 = types.InlineQueryResultArticle('3', language[userlang]["INLINE_TIMETIME_MSG"] + str(timezone), types.InputTextMessageContent("Current time in *" + timezone + "*: \n" + time["fulldate"], parse_mode="Markdown"))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("Unexpected error occured."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)


@bot.inline_handler(lambda query: query.query.split()[0] == 'lmgtfy')
def query_text(inline_query):
  userlang = redisserver.get("settings:user:language:" + str(inline_query.from_user.id))
  try:
    if inline_query.query == "lmgtfy":
      r = types.InlineQueryResultArticle('1', language[userlang]["INLINE_LMGTFY_MSG"], types.InputTextMessageContent('http://google.com'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      query = inline_query.query.replace("lmgtfy ", "", 1)
      lmgtfyurl = urllib.urlopen("http://r1z.ir/api.php?long=http://lmgtfy.com/?q={}".format(query.replace(" ", "+"))).read()
      try:
        r3 = types.InlineQueryResultArticle('3', language[userlang]["INLINE_LMGTFYSEND_MSG"], types.InputTextMessageContent("Direct link: `{}`\n\nOr click on [this :D]({})".format(lmgtfyurl, lmgtfyurl), parse_mode="Markdown", disable_web_page_preview=True))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("Unexpected error occured."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)
