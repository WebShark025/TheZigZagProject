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
  try:
    if inline_query.query == "echo":
      r = types.InlineQueryResultArticle('1', 'Please enter a text!', types.InputTextMessageContent('I Love empty texts.'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      try:
        r3 = types.InlineQueryResultArticle('3', 'Echo your message using HTML parse mode ;)', types.InputTextMessageContent(inline_query.query.replace("echo ", "", 1), parse_mode="HTML"))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured. One of your tags arent closed!', types.InputTextMessageContent("I forgot to close a tag."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)


@bot.inline_handler(lambda query: query.query.split()[0] == 'calc')
def query_text(inline_query):
  try:
    if inline_query.query == "calc":
      r = types.InlineQueryResultArticle('1', 'Please enter what you need I calculate.', types.InputTextMessageContent('0! :D'))
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
  try:
    if inline_query.query == "hideit":
      r = types.InlineQueryResultArticle('1', 'Please enter a text so I can hide it!', types.InputTextMessageContent('I Love empty texts.'))
      bot.answer_inline_query(inline_query.id, [r])
    if len(inline_query.query.split()) > 1:
      try:
        markupz = types.InlineKeyboardMarkup()
        markupid = types.InlineKeyboardButton("Show hidden message!", callback_data='sil|' + inline_query.id)
        markupz.add(markupid)
        query_text = {inline_query.id: inline_query.query.replace("hideit ", "", 1)}
        querymessages.update(query_text)
        r3 = types.InlineQueryResultArticle('3', 'Send hidden text!', types.InputTextMessageContent("❓❓❓"), reply_markup=markupz)
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
      except:
        r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("Unexpected error occured."))
        bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except Exception as e:
    print(e)

