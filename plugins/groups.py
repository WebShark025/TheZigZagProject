
@bot.message_handler(func=lambda message: True, content_types=['new_chat_member'])
def user_greet(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  if userlang == None:
    userlang = "en"
  if GP_GREETING:
    if message.new_chat_member.id != bot.get_me().id:
      name = message.new_chat_member.first_name
      title = message.chat.title
      bot.send_message(message.chat.id, language[userlang]["GP_GREETING_MSG"].format(name,title), parse_mode='Markdown')
  
  if message.new_chat_member.id == bot.get_me().id:
    inviter = message.from_user.id
#    if inviter not in ADMINS_IDS:
#      bot.send_message(message.chat.id, language[userlang]["NON_ADMIN_ADDED_BOT_MSG"])
#      bot.leave_chat(message.chat.id)
#    else:
     if True:
      bot.send_message(message.chat.id, language[userlang]["BOT_JOINED_MSG"])
#      groupargs = 0
#      redisserver.sadd(message.chat.id, groupargs)
#      redisserver.sadd("zigzag_groups", message.chat.id)
  
@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def user_greet(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  if userlang == None:
    userlang = "en"
  if GP_FAREWELL:
    name = message.left_chat_member.first_name
    title = message.chat.title
    bot.send_message(message.chat.id, language[userlang]["GP_FAREWELL_MSG"].format(name,title), parse_mode='Markdown')
  
@bot.message_handler(func=lambda m: True, content_types=['contact'])
def contact_forwarder(contact):
  userid = contact.from_user.id
  if userid in contacter_list:
    bot.send_message("-" + str(SUPPORT_GP), language[userlang]["CONTACT_RECIEVED_MSG"])
    bot.forward_message("-" + str(SUPPORT_GP), contact.chat.id, contact.message_id)
    bot.reply_to(contact, language[userlang]["CONTACT_FORWARDED_MSG"])

@bot.message_handler(commands=['stats', 'Status'])
def send_gpstats(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  groupid = message.chat.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.chat.type == "supergroup" or message.chat.type == "group":
    gpmsgs = redisserver.get("stats:group:messages:" + str(groupid))
    gpphotos = redisserver.get("stats:group:messages:photos:" + str(groupid))
    gpaudios = redisserver.get("stats:group:messages:audios:" + str(groupid))
    gpvideos = redisserver.get("stats:group:messages:videos:" + str(groupid))
    gpdocs = redisserver.get("stats:group:messages:docs:" + str(groupid))
    gpvoices = redisserver.get("stats:group:messages:voices:" + str(groupid))
    bot.send_message(message.chat.id, language[userlang]["GP_STATS_MSG"].format(gpmsgs, gpvoices, gpaudios, gpphotos, gpdocs, gpvideos), parse_mode="Markdown")
  else:
    bot.reply_to(message, language[userlang]["GP_NOTINGP_MSG"])

@bot.message_handler(commands=['setrules', 'Setrules'])
def send_gpstats(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  groupid = message.chat.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.chat.type == "supergroup" or message.chat.type == "group":
    if len(message.text.split()) < 2:
      bot.reply_to(message, language[userlang]["GP_RULES_NEA_MSG"], parse_mode="Markdown")
      return
    try:
      rrules = message.text.replace("/setrules ","",1).replace("/Setrules ", "", 1)
      redisserver.set("settings:group:rules:" + str(groupid), rrules)
      bot.reply_to(message, language[userlang]["GP_RULESSET_MSG"], parse_mode="HTML")
    except:
      bot.send_message(message.chat.id, language[userlang]["ERROR_MSG"])
  else:
    bot.reply_to(message, language[userlang]["GP_NOTINGP_MSG"])

@bot.message_handler(commands=['rules', 'Rules'])
def send_gpstats(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  userid = message.from_user.id
  groupid = message.chat.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if message.chat.type == "supergroup" or message.chat.type == "group":
    rules = redisserver.get("settings:group:rules:" + str(groupid))
    if not rules:
      bot.send_message(message.chat.id, "No rules defined!")
    bot.send_message(message.chat.id, rules, parse_mode="Markdown")
  else:
    bot.reply_to(message, language[userlang]["GP_NOTINGP_MSG"])
