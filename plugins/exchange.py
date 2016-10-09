# -*- coding: utf-8 -*-

@bot.message_handler(commands=['rate'])
def ex_message(message):
  userid = message.from_user.id
  banlist = redisserver.sismember('zigzag_banlist', '{}'.format(userid))
  if banlist:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, "Enter a base currency! \n\nExample: `/rate USD`", parse_mode="Markdown")
    return
  currency = message.text.upper().split()[1]
  rlex = re.compile(r'^\b\w{3}\b')
  if rlex.search(currency[0]):
    pass
  else:
    bot.reply_to(message, "Error: \n\n`Invalid currency code!`", parse_mode="Markdown")
    return
  exresult = requests.get('http://api.fixer.io/latest?base={}'.format(currency)).json()
# check for .. chichi bood? aha Check for errors.... rah behtari naresid be zehnam XD IM NOOB IN PYTHON
  try:
    asd = exresult['error']
    return
  except:
    pass
  base = str(exresult['base'])
  datet = str(exresult['date'])
  aud = "🇦🇮 `AUD`: *" + str(exresult['AUD']) + "*"
  bgn = "🇧🇬 `BGN`: *" + str(exresult['BGN']) + "*"
  brl = "🇧🇷 `BRL`: *" + str(exresult['BRL']) + "*"
  cad = "🇨🇦 `CAD`: *" + str(exresult['CAD']) + "*"
  chf = "🇨🇭 `CHF`: *" + str(exresult['CHF']) + "*"
  cny = "🇨🇳 `CNY`: *" + str(exresult['CNY']) + "*"
  czk = "🇨🇿 `CZK`: *" + str(exresult['CZK']) + "*"
  dkk = "🇩🇰 `DKK`: *" + str(exresult['DKK']) + "*"
  gbp = "🇬🇧 `GBP`: *" + str(exresult['GBP']) + "*"
  hdk = "🇭🇰 `HKD`: *" + str(exresult['HKD']) + "*"
#  hrk = exresult['HRK'] FLAG NOT FOUND
#  huf = exresult['HUF'] SAME AS ABOVE
  idr = "🇮🇩 `IDR`: *" + str(exresult['IDR']) + "*"
#  ils = exresult['ILS'] NOT FOUND? WTF?
  inr = "🇮🇳 `INR`: *" + str(exresult['INR']) + "*"
  jpy = "🇯🇵 `JPY`: *" + str(exresult['JPY']) + "*"
#  kry = exresult['KRY'] KOREA? NOT FOUND.
  mxn = "🇮🇹 `MXN`: *" + str(exresult['MXN']) + "*"
  myr = "🇲🇾 `MYR`: *" + str(exresult['MYR']) + "*"
  nok = "🇳🇴 `NOK`: *" + str(exresult['NOK']) + "*"
  nzd = "🇬🇸 `NZD`: *" + str(exresult['NZD']) + "*"
  php = "🇵🇭 `PHP`: *" + str(exresult['PHP']) + "*"
#  pln = exresult['PLN'] NOT FLAGGED CORRECTLY. MORE THAN 6 FLAGS FOUND
#  ron = exresult['RON'] WTF?
  rub = "🇷🇺 `RUB`: *" + str(exresult['RUB']) + "*"
  sek = "🇸🇪 `SEK`: *" + str(exresult['SEK']) + "*"
  sgd = "🇸🇬 `SGD`: *" + str(exresult['SGD']) + "*"
  thb = "🇹🇭 `THB`: *" + str(exresult['THB']) + "*"
#  tryy = exresult['TRY'] not found.
#  zar = exresult['ZAR'] NOT SURE WHICH FLAG
  eur = "🇪🇺 `EUR`: *" + str(exresult['EUR']) + "*"
  bot.send_message(message.chat.id, "Exchange date rata as `{}`: \nBase currency: `{}`\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(datet, base, aud, bgn, brl, cad, chf, cny, czk, dkk, gbp, hkd, idr, inr, jpy, mxn, myr, nok, nzd, php, rub, sek, sgd, ehb, eur), parse_mode="Markdown")
