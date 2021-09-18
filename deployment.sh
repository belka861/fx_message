#!/bin/sh
#python3 -m pip install selenium phone_gen requests transliterate
echo 'sv ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install wget -y
sudo apt-get install mc -y
sudo apt-get install screen -y
sudo apt-get install python3-pip -y
sudo apt-get install xvfb -y

wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

wget https://raw.githubusercontent.com/belka861/fx_message/main/headless_test.py

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y

wget https://datahub.io/core/nyse-other-listings/r/nyse-listed.csv

wget https://raw.githubusercontent.com/belka861/fx_message/main/h2.py
wget https://raw.githubusercontent.com/belka861/fx_websocket/main/w5_edit.py

pip3 install requests transliterate random_username phone-gen selenium websocket-client pyvirtualdisplay
