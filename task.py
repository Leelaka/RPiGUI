from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#define variables 
red = LED(18)
yellow = LED(22)
green = LED(27)

#gui box design
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event functions

def redToggle():
    if red.is_lit:
        red.off()
        RedButton["text"] = "Turn Red LED on"
    else:
        red.on()
        RedButton["text"] = "Turn Red LED off"
        
def yellowToggle():
    if yellow.is_lit:
        yellow.off()
        YellowButton["text"] = "Turn Yellow LED on"
    else:
        yellow.on()
        YellowButton["text"] = "Turn Yellow LED off"
        
def greenToggle():
    if green.is_lit:
        green.off()
        GreenButton["text"] = "Turn Green LED on"
    else:
        green.on()
        GreenButton["text"] = "Turn Green LED off"
        
#widgets
RedButton = Button(win, text = 'Turn Red LED on', font = myFont, command = redToggle, bg = 'bisque2', height = 1, width = 20)
RedButton.grid(row=0,column=1)

YellowButton = Button(win, text = 'Turn Yellow LED on', font = myFont, command = yellowToggle, bg = 'bisque2', height = 1, width = 20)
YellowButton.grid(row=1,column=1)

GreenButton = Button(win, text = 'Turn Green LED on', font = myFont, command = greenToggle, bg = 'bisque2', height = 1, width = 20)
GreenButton.grid(row=2,column=1)
