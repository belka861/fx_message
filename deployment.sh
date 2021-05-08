#!/bin/sh
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install wget -y
sudo apt-get install mc -y
sudo apt-get install screen -y
sudo apt-get install python3-pip -y
#sudo apt-get install xvf
wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
pip3 install selenium
