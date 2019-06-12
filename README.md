# Requirements

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

1. `pip3 -r requirements.txt`
