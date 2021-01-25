# Install Ubuntu 20.10 on a SD card

follow this instructions (https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#1-overview) to: 
- wirte an Ubuntu Desktop 20.10 image on a 256GB micro sd card with Raspberry Pi Imager
- Boot your Raspberry Pi4 with Ubuntu Desktop

# Install Spyder

sudo apt install spyder

# Install some extra libraries for python 3 (run installation file tbc)

- update and upgrade your ubuntu installation (make take a few minutes)

sudo apt update

sudo apt -y upgrade

- python should already be installed, but some of the following packages may be missing

sudo apt install -y python3-pip build-essential libssl-dev libffi-dev python3-setuptools git-core

- check pip and pip3 versions to see if pip points to pip3, if it does, you can use pip instead of pip3

pip --version

pip3 --version

- install gpiozero and blinkstick libraries

sudo pip install gpiozero blinkstick


# Install kivy by running the following commands

sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

sudo apt update

sudo pip install kivy[base] kivy_examples


sudo apt autoremove

sudo reboot


# Change Permissions to access GPIO pins

Last but not least, to be able to access gpio pins without using sudo you need to change permissions for sys/class/gpio folder and all enclosed files

open file manager from terminal with 
sudo nautilus
navigate to sys/class and on the gpio folger change permission for others

# Download repository and start GUI 

