read -p "(SO DANGEROUS) Do you want to use auto launch? (to kill it=HOLD Ctrl+C) " -n 1 -r
echo " "
if [[ $REPLY =~ ^[Yy]$ ]]
then
  while true
  do
    python bot.py
    echo "Bot has crashed! Launching it again."
  done
else
  python bot.py
  echo "Bot stopped. exiting"
fi
