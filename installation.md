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

- install RPi.gpio, gpiozero and blinkstick libraries

sudo apt-get install rpi.gpio-common rpi.gpio

sudo pip install gpiozero blinkstick pyusb pandas

## UPDATE
RPi.GPIO library uses digital PWM signals that lack precision to control servos, causing different bugs in the servo code.

A solution is using the pigpio library instead, with higher pwm precision (https://github.com/joan2937/pigpio).
Follow the intallation instructions here http://abyz.me.uk/rpi/pigpio/download.html to download and install pigpio.

Then install the Node.js package 

sudo apt install npm

npm install pigpio

Note that the pigpio daemon has to be running as sudo/root before using the library, and killed at the end.

sudo pigpiod

sudo killall pigpiod

**NOTE1**: pigpiod can be set up to run automatically on boot (see https://gpiozero.readthedocs.io/en/stable/remote_gpio.html)
**NOTE2**: pigpiod allows for remote control of Raspberry Pi pins. Technically the toolbox could be run on a separate computer controlling the RPi4Toolbox (TODO)

# Install kivy by running the following commands

sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

sudo apt update

sudo pip install kivy[base] kivy_examples


sudo apt autoremove

sudo reboot



# Download repository and start GUI 

