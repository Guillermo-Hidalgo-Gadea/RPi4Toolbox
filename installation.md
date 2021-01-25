# Install Ubuntu 20.10 on a SD card

follow the instructions in this link https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#1-overview
- wirte an Ubuntu Desktop 20.10 image on a 256GB micro sd card with Raspberry Pi Imager
- Boot your Raspberry Pi4 with Ubuntu Desktop

# Install python 3 and some extra libraries

sudo apt update
sudo apt -y upgrade

sudo apt install -y python3-pip build-essential libssl-dev libffi-dev python3-dev

check pip and pip3 versions to see if pip points to pip3 
pip --version
pip3 --version

sudo pip3 gpiozero blinkstick

# change permisson for sys/class/gpio folder and enclosed files

# install kivy

sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

sudo apt update

sudo apt install python3-setuptools git-core python3-dev

python3 -m pip install kivy[base] kivy_examples

