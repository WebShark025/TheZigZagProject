echo "Installing..."
git pull
sudo pip install pyTelegramBotAPI
sudo pip install redis
chmod +x launch.sh

echo "Installed successfully!"
echo "Be sure to edit the config for your requirements!"
echo "Exiting."
