read -p "Are you sure? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
  while true
  python bot.py
  echo "Bot has crashed! Launching it again."
else
  python bot.py
fi
