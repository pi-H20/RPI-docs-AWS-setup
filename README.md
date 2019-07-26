# Pi- H20 - Raspberry Pi with Python

This repo contains the Raspberry Pi setup and python scripts.

## Authors 

Liz Mahoney, Jen Shin, Greg Chidrome, Jorie Fernandez


# Getting Started
1. On local machine, create a directory: `mkdir python-h20`
2. Go into the directory: `cd python-h20`, then clone this repo `git clone https://github.com/pi-H20/pi-python.git`
3. Voila! You should see all the files in this repo on your machine.

## Raspberry Pi Setup

Steps 1...4 [TBD]

## Write some code to turn the pump on from the command line
***Note*** Before these next steps, the laptop can be able to ssh into Raspberry Pi to write any code!

1. Make a directory called water and go into the water directory.

2. To ensure the library is installed on the Raspberry pi, run: 

`sudo python3 -m pip install RPi.GPI` 

If successful, it shows the following: 

```
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Requirement already satisfied: RPi.GPIO in /usr/lib/python3/dist-packages (0.6.5

```

3. Open and create a new file `vim water.py`
4. After the file is done, it needs execute permissions, therefore run `chmod 777 water.py`
5. To run the file: `python3 water.py`

The pump should successfully run from the raspberry pi.

6. To edit the file: `vim water.py`

## Resources

Water Plant Tutorial - http://www.cyber-omelette.com/2017/09/automated-plant-watering.html
