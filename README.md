# Open-GCI

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/Open-GCI/master/Resources/Images/OPEN-GCI-Logo.png" width="50%" height="50%" alt="Open-GCI Logo"/>
</p>

An open-source accessible gaming interface that enables those with limited or no hand movement to play their favourite console based game using more accessible input methods.
Adaptive switches and USB keyboards are currently the two input methods that can be used to play console based games.


# Downloads 

These are all the files and documentation associated with the Open-GCI project.

 <table style="width:100%">
  <tr>
    <th>Resource</th>
    <th>Version</th>
    <th>Format</th>
    <th>Link</th>
  </tr>
    <tr>
    <td>Open-GCI All</td>
    <td>1.0</td>
    <td>ZIP</td>
    <td><a href="https://github.com/milador/Open-GCI/archive/master.zip">Open-GCI-master.zip</a></td>
  </tr>
  <tr>
    <td>Open-GCI Manual</td>
    <td></td>
    <td>PDF</td>
    <td><a href=""> </a></td>
  </tr>
  <tr>
    <td>Open-GCI BOM (XLSX)</td>
    <td>October 6, 2018</td>
    <td>XLSX</td>
    <td><a href="https://github.com/milador/Open-GCI/raw/master/Open-GCI_BOM.xlsx">Open-GCI_BOM.xlsx</a></td>
  </tr>
  <tr>
    <td>Open-GCI Keyboard code</td>
    <td>1.0</td>
    <td>Py</td>
    <td><a href="https://github.com/milador/Open-GCI/raw/master/Software/gci_keyboard.py">gci_keyboard.py</a></td>
  </tr>
  <tr>
    <td>Open-GCI Board Layout</td>
    <td>1.0</td>
    <td>BRD</td>
    <td><a href="https://raw.githubusercontent.com/milador/Open-GCI/master/Hardware/PCB_design/Open-GCI.brd">Open-GCI.brd</a></td>
  </tr>
  <tr>
    <td>Open-GCI Board Schematic</td>
    <td>1.0</td>
    <td>SCH</td>
    <td><a href="https://raw.githubusercontent.com/milador/Open-GCI/master/Hardware/PCB_design/Open-GCI.sch">Open-GCI.sch</a></td>
  </tr>
</table> 

# Diagram

The following diagram represents the hardware of the Open-GCI interface.

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/Open-GCI/master/Resources/Images/opengci-diagram.png" width="50%" height="50%" alt="Open-GCI Diagram"/>
</p>

# Installation 

## Hardware Setup Instructions

Coming soon..

## Software Setup Instructions

  1. Install Raspbian on an SD card according to the official documents 

https://www.raspberrypi.org/documentation/installation/installing-images/

2.	Download Dependencies

  2.1. Startup the raspberrypi zero W
  
  2.2. Open the command line
  
  2.3. Install the necessary packages
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip git scons swig
sudo pip install RPi.GPIO
```

3.	Compile & Install rpi_ws281x Library
  
  3.1. Download the library source and compile it using following command : 
``` 
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
``` 
  3.2. Install the Python library by executing following command : 
``` 
cd python
sudo python setup.py install
``` 
  
4.	Download gci_keyboard.py
  
  4.1. Open the command line
  
  4.2. Enter the pi directory
  
  4.3. Create a new python file using nano and name it gci_keyboard.py using following command: ```sudo nano gci_keyboar.py``` 
  
  4.4. Copy and paste the keyboard code from Software/gci_keyboard.py 
  
  4.5. Save the file and exit nano
  
5. Run code on bootup

  5.1. Open /etc/rc.local using nano by running following command: ```sudo nano /etc/rc.local```
  
  5.2. Add the following line on its own line right before exit 0: ```sudo python /home/pi/gci_keyboard.py  &```
  
  5.3. Save and exit /etc/rc.local
  
  5.4. Reboot the raspberrypi zero W by running following command: ```sudo shutdown -r now```
  
6.	Varify software is running 
  
   6.1. The Led will change color from Blue to Green when the software is ready to use

# PS4 to keyboard button mapping 

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/Open-GCI/master/Resources/Images/ps4-keyboard-mapping.png" width="50%" height="50%" alt="Open-GCI PS4 to keyboard button mapping"/>
</p>

# Picture 

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/milador/Open-GCI/master/Resources/Images/opengci1.png" width="50%" height="50%" alt="Open-GCI Interface"/>
</p>
  
  
