echo "Installing..."
sudo apt-get install python-qt4
git pull
git clone https://github.com/eternnoir/pyTelegramBotAPI.git
mv pyTelegramBotAPI .pyTelegramBotAPI
cd .pyTelegramBotAPI
python setup.py install
cd ../
sudo pip install redis
chmod +x launch.sh

echo "Installed successfully!"
echo "Be sure to edit the config for your requirements!"
echo "Exiting."
