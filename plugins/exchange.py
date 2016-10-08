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
  aud = exresult['AUD']
  bgn = exresult['BGN']
  brl = exresult['BRL']
  cad = exresult['CAD']
  chf = exresult['CHF']
  cny = exresult['CNY']
  czk = exresult['CZK']
  dkk = exresult['DKK']
  gbp = exresult['GBP']
  hdk = exresult['HKD']
#  hrk = exresult['HRK'] FLAG NOT FOUND
#  huf = exresult['HUF'] SAME AS ABOVE
  idr = exresult['IDR']
#  ils = exresult['ILS'] NOT FOUND? WTF?
  inr = exresult['INR']
  jpy = exresult['JPY']
#  kry = exresult['KRY'] KOREA? NOT FOUND.
  mxn = exresult['MXN']
  myr = exresult['MYR']
  nok = exresult['NOK']
  nzd = exresult['NZD']
  php = exresult['PHP']
#  pln = exresult['PLN'] NOT FLAGGED CORRECTLY. MORE THAN 6 FLAGS FOUND
#  ron = exresult['RON'] WTF?
  rub = exresult['RUB']
  sek = exresult['SEK']
  sgd = exresult['SGD']
  thb = exresult['THB']
#  tryy = exresult['TRY'] not found.
#  zar = exresult['ZAR'] NOT SURE WHICH FLAG
  eur = exresult['EUR']
