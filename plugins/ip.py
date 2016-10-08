@bot.message_handler(commands=['ip', 'Ip'])
def ip_message(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, "Enter a time zone/city/region/etc. please! \n\nExample: `/time Tehran`", parse_mode="Markdown")
    return
  text = m.text.split()[1]
  r = requests.get('http://ip-api.com/json/{}?fields=262143'.format(text))
  json_data = r.json()
  country = json_data['country']
  city = json_data['city']
  isp = json_data['isp']
  timezone = json_data['timezone']
  lon = json_data['lon']
  lat = json_data['lat']
  bot.send_location(m.chat.id, lat, lon)
  bot.send_message(m.chat.id, "*Country* : ```{}``` \n *City* : ```{}``` \n *Isp* : ```{}``` \n *Timezone* : ```{}```".format(country,city,isp,timezone), parse_mode="Markdown")
