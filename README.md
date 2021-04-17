# Simple Raspberry Pi Music Player

Recently, I decided that I wanted a simple MP3 Player-like device. Unwilling to simply go out and buy one for relatively cheap, I decided to make my own using a Raspberry Pi and a handful of small electronics. While it may not look as flashy as something you might buy, money will never be able to buy the satisfaction of making something yourself!

> _Make it yours! Add your own creative touch! I've intentionally left this project at some buttons on a breadboard but I'm sure that it would look great in a custom 3D printed or laser-cut enclosure!_

## Materials

- Raspberry Pi Board (While this project was created and tested on a Model B V2, it should work on all boards)
- SD Card
- Ethernet Cable and Computer OR Monitor (with HDMI cable) and Keyboard
- Small Breadboard
- _(Optional)_ Raspberry Pi Breakout Board
- Handful of jumper wires
- 3 Momentary pushbuttons
- _(Optional)_ Enclosure to put it all in!
- Pair of headphones/speakers

## Instructions

### Preparing the Pi's Operating System

- Install Raspberry Pi OS Lite on an SD card using the tool of your choice (such as the Raspberry Pi Imager)

- _(Optional, follow this step if you do not wish to connect a keyboard and monitor to the Pi)_ In order to use a Raspberry Pi over the network, you will need to enable ssh. This can be done by creating a blank file with the name `ssh` (no extension) in the `BOOT` partition of the SD card. This can be done on Mac or Linux using the `touch` command.

```shell
$ cd /PATH/TO/BOOT
$ touch ssh
```

### Powering on and connecting to the Pi

- Now it's time time to plug your Pi into the network (or conenct a keyboard and monitor) and boot it up. If you have gone the route of connecting remotely, open up a terminal on another machine and run the following commands:

```shell
$ ssh pi@raspberrypi.local (Or the IP adress of your pi)
[INSERT YOUR PASSWORD, THE DEFUALT IS 'raspberry']
```

### Setting up the hardware

- Either directly to the Pi, or through a convenient breakout board, make the following connections. You can use different GPIO pins as shown in the table, however you will need to modify the code (not that hard).

  | Button                | Raspberry Pi Pin |
  | --------------------- | ---------------- |
  | Previous Track Button | Ground           |
  | Previous Track Button | GPIO 4           |
  | Play/Pause Button     | Ground           |
  | Play/Pause Button     | GPIO 3           |
  | Next Track Button     | Ground           |
  | Next Track Button     | GPIO 2           |

### Setting up the software

- Install the required libraries. This project uses [pip](https://pypi.org/project/pip/) to manage all of our python libraries, [OMXPlayer](https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md) to do the heavy lifting with audio, [omxplayer-wrapper](https://pypi.org/project/omxplayer-wrapper/) to allow us to control OMXPlayer through a python script, and [GPIO Zero](https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/) for interfacing with the physical controls! These can all be installed by running the following commands in sequence.

```shell
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ sudo apt-get install omxplayer
$ pip3 install omxplayer-wrapper
$ sudo apt-get install python3-gpiozero
```

- Download the `music_player.py` script from GitHub.

```shell
$ wget https://raw.githubusercontent.com/calebrodgers/RaspberryPiMusicPlayer/main/music_player.py
```

## Time for some tunes!

- Create a folder in the root directetory called `music`:

```shell
$ mkdir music
```

- Add some music files to this directory, either by mounting and copying from a USB, or through the network, possibly using `wget` to download from an HTTP server. Now connect some headphones/speakers and run the `music_player.py` script.

```shell
$ python3 music_player.py
```

- To run the script automatically on startup, add `python3 /home/pi/music_player.py` to `rc.local`.

```shell
$ sudo nano /etc/rc.local
[Right before the line that has 'exit 0', add the following]
python3 /home/pi/music_player.py &
```

### That's it!

_For more, visit [calebrodgers.com](https://calebrodgers.com)._
