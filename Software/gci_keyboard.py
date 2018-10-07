# File name: gci_keyboard.py
# Author: Milad Hajihassan
# Date created: 8/10/2018
# Date last modified: 10/06/2018
# Python Version: 2.7

import os
import sys    
import termios
import fcntl
import RPi.GPIO as gpio
import time
from neopixel import *
import argparse
import random

# LED configuration:
LED_COUNT      = 1      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz
LED_DMA        = 10      # DMA channel to use for generating signal
LED_BRIGHTNESS = 33     # Set brightest
LED_INVERT     = False   # True to invert the signal
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# LED cleanup:
def colorWipe(strip, color, wait_ms=50):
     strip.setPixelColor(0, color)
     strip.show()
     time.sleep(wait_ms/1000.0)

# LED startup:
def colorStartup(strip, color=Color(255, 50, 0), wait_ms=400, iterations=3):
    for i in range(iterations):
        strip.setPixelColor(0, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        strip.setPixelColor(0, Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)

		
def getch():
  import sys, tty, termios
  init()
  sleep_time = 0.050
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON

  try:
    colorWipe(strip, Color(0,255,0), 10)
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
    if (ch == 'w'):
        action_up(sleep_time)
    elif ch == 's':
        action_down(sleep_time)
    elif ch == 'a':
        action_left(sleep_time)
    elif ch == 'd':
        action_right(sleep_time)
    elif ch == 'm':
        action_x(sleep_time)
    elif ch == 'i':
        action_triangle(sleep_time)
    elif ch == 'j':
        action_square(sleep_time)
    elif ch == 'k':
        action_o(sleep_time)
    elif ch == 'r':
        action_l1(sleep_time)
    elif ch == 'f':
        action_l2(sleep_time)
    elif ch == 'o':
        action_r1(sleep_time)
    elif ch == 'l':
        action_r2(sleep_time)
    elif ch == 'v':
        action_select(sleep_time)
    elif ch == 'b':
        action_home(sleep_time)
    elif ch == 'n':
        action_start(sleep_time)
    elif ch == 'q':
        clean_up() 
        sys.exit()
    else:
        clean_up()
        pass
    init()
      
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch

# Initialization 
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(19, gpio.OUT)
    gpio.setup(21, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(31, gpio.OUT)
    gpio.setup(32, gpio.OUT) 
    gpio.setup(33, gpio.OUT)
    gpio.setup(35, gpio.OUT)
    gpio.setup(36, gpio.OUT)
    gpio.setup(37, gpio.OUT)
    gpio.setup(38, gpio.OUT)
    gpio.setup(40, gpio.OUT)

def action_l2(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()

def action_o(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def action_r1(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def action_square(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def action_home(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, False)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def action_left(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, False)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def action_down(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, False)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()	
	
	
def action_r2(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, False)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()	
	
def action_x(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, False)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()	
	
def action_l1(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, False)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()	

def action_triangle(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, False)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()	

def action_start(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, False)
    time.sleep(tf)
    clean_up()	

def action_select(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, False)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()	

def action_right(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, False)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def action_up(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, False) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    time.sleep(tf)
    clean_up()
	
def clean_up():
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.output(19, True)
    gpio.output(21, True)
    gpio.output(23, True)
    gpio.output(31, True)
    gpio.output(32, True) 
    gpio.output(33, True)
    gpio.output(35, True)
    gpio.output(36, True)
    gpio.output(37, True)
    gpio.output(38, True)
    gpio.output(40, True)
    colorWipe(strip, Color(0,0,0), 10)
    gpio.cleanup()   


def main():
  
  while True:
        print("\nKey: '" + getch() + "'\n")
      



if __name__ == "__main__":
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library 
    strip.begin()
    colorStartup(strip)
    colorWipe(strip, Color(0,255,0), 10)
    main()


