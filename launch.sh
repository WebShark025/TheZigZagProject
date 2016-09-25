read -p "Do you want to use auto launch? (to kill it=Ctrl+C) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
  while true
    python bot.py
    echo "Bot has crashed! Launching it again."
  done
else
  python bot.py
fi
