# The ZigZag project!

WARNING: ZigZag v1 is completely abandoned and will receive no further updates!

If you wish to use the ZigZag project for easier and faster interaction with Telegram API, use https://github.com/WebShark025/ZigZag-v2-Base

-----------

The official ZigZag project!

This page will get updated after the first stable release.

# Installation

To install the bot, execute these commands one by one:

```
git clone https://github.com/WebShark025/TheZigZagProject
cd TheZigZagProject
chmod +x install.sh
sudo ./install.sh
```

Launch the bot once: `./launch.sh` then stop it (`Ctrl + C`)

A Copy of `locale.py.new` & `config.py.new` will be made => `locale.py` & `config.py`. 

Edit those as you need.

Then launch the bot normaly. To do so, simply execute `./launch.sh` 

If you have problems, visit [Manual installation](https://github.com/WebShark025/MySimpleFirstPythonBot/wiki/Manual-installation)

# Commands 

| Command | Description | Permission |
|:--------|:------------|:-----------|
| /help & /start | Returns the start message | Members |
| /test & /toast | (BetaVersionsOnly) Just replies a message | Members |
| /echo text | Echoes the text | Members |
| /feedback | Sends users feedback | Members |
| /sendcontact | Sends user contact to bot admin | Members |
| /id | Sends user ID & name (if in group, groups ID too) | Members |
| /calc | Maths! :D | Members |
| /time | Returns time (in IRST) | Members |
| /support | Joines the support chat. | Members |
| /leave | Leaves the support chat. | Members |
| /meme | Meme! :O... | Members |
| /short | URL Shortner | Members |
| /tocontact | String to contact converter! | Members |
| /mp3tag | Changes MP3 file tags | Members |
| /addreply | Adds a reply to chatwith system! | Members |
| /weather <city> | Weather! | Members |
| /qrcode <text> | QR Code creator | Members |
| /adminhelp | Admin commands help | Admins |
| /members | List of members & banned users | Admins |
| /bc | Broadcast message to all members | Admins |
| /ban userid | Bans a user | Admins |
| /unban userid | Unbans a user | Admins |
| /force_user_leave userid | Forces a user to leave support chat | Admins |

More commands comming soon!

# Use ZigZag's base for your bot!

If you are interested in how ZigZag works and you want to write a Python bot using ZigZag's base, you can do this:

Copy `install.sh`, `bot.py`, `locale.new.py`, `config.new.py`, `plugins/start.py`, `plugins/callback_handler.py`, `plugins/message_handler.py` and `launch.sh`, Clean those three plugins up, and use it for yourself :) 

Note: v2 is comming soon, and it will be a FULL RECODE of the project, BUT, I'm writing it in the best way I can, so the only small thing you need to do to the plugins you wrote for ZigZag, is to change its patterns (I mean @bot.handlemessage...). Just wanted you guys to know :) Full instructions will be published when the new update arrives.

# Contact me

[![https://telegram.me/WebShark25](https://img.shields.io/badge/💬_Telegram-WebShark25-blue.svg)](https://telegram.me/WebShark25)

The ZigZag official channel in Telegram: [@TheZigZagProject](https://telegram.me/TheZigZagProject)

The ZigZag official bot in Telegram: [@TheZigZagBot](https://telegram.me/TheZigZagBot)

# Credits

Special thanks to [Iman Daneshi](https://github.com/imandaneshi) for the idea.

Thanks to [ThisIsAmir](https://github.com/ThisIsAmir) for some part of his codes.

Thanks to [flo](https://github.com/aRandomStranger) for its awesome chat-with code.

And thanks to [eternnoir](https://github.com/eternnoir/) for his awesome API!
