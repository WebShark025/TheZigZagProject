# -*- coding: utf-8 -*-

@bot.message_handler(commands=['ip', 'Ip'])
def ip_message(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.replace("📡 IP Geolocation", "", 1).split()) < 2:
    bot.reply_to(message, language[userlang]["IP_NEA_MSG"], parse_mode="Markdown")
    return
  ip = message.text.split()[1]
  rlip = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')
  rlhn = re.compile(r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])')
  if rlip.search(ip[0]):
    pass
  elif rlhn.search(ip[0]):
    pass
  else:
    bot.reply_to(message, language[userlang]["IP_ERROR_MSG"], parse_mode="Markdown")
    return
  ipresult = requests.get('http://ip-api.com/json/{}?fields=262143'.format(ip)).json()
  if str(ipresult["status"]) == "success":
    country = ipresult['country']
    cityn = ipresult['city']
    isp = ipresult['isp']
    timezone = ipresult['timezone']
    long = ipresult['lon']
    lati = ipresult['lat']
    bot.send_location(message.chat.id, lati, long)
    bot.send_message(message.chat.id, language[userlang]["IP_DONE_MSG"].format(ip, country, cityn, isp, timezone), parse_mode="Markdown")
  else:
    bot.reply_to(message, "Error: \n\n`{}`".format(ipresult['message']), parse_mode="Markdown")
    return
