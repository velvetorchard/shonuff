#!/bin/bash
sudo apt-get update
sudo apt-get install tightvncserver -y
sudo apt-get install xfce4 xfce4-goodies -y
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt-get update
sudo apt-get install google-chrome-stable -y|
sudo apt install adobe-flashplugin -y
sudo apt install browser-plugin-freshplayer-pepperflash -y
nc localhost 5901
sudo kill-1
sudo passwd
su
Rocky12#
apt-get install fail2ban -y
service fail2ban start
chkconfig fail2ban on
systemctl enable fail2ban
systemctl start fail2ban
