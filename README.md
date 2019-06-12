# Setup

## Pin Connections

| RF522 Modul |      Raspberry Pi      |
| :---------: | :--------------------: |
|     SDA     |  Pin 24 / GPIO8 (CE0)  |
|     SCK     | Pin 23 / GPIO11 (SCKL) |
|    MOSI     | Pin 19 / GPIO10 (MOSI) |
|    MISO     | Pin 21 / GPIO9 (MISO)  |
|     IRQ     |           —            |
|     GND     |       Pin6 (GN)        |
|     RST     |     Pin22 / GPIO25     |
|    3.3V     |      Pin 1 (3V3)       |

## Activate SPI Interface

1. Open raspi-config `sudo raspi-config`
1. Go to `5 Interfacing Options`
1. Enable `P4 SPI`
1. Reboot `sudo reboot now`
1. Check if working. `lsmod | grep spi` should result in something similiar to: 
```
spidev                 16384  0
spi_bcm2835            16384  0
```

## Install additional packages

```
sudo apt install python3-dev python3-pip
```

## Install python requirements

```
pip3 install -r requirements.txt
```

# Use

## Start read test

```
python3 read.py
```
