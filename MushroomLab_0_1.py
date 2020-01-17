import tkinter as tk
import Adafruit_DHT
import threading
from tkinter import StringVar
from w1thermsensor import W1ThermSensor
import time
import RPi.GPIO as GPIO

"***Pins init***"
cooler0Pin = 3
cooler1Pin = 5
lamp0Pin = 7
lamp1Pin = 11
heater0Pin = 13
heater1Pin = 15
hum0Pin = 19
hum1Pin = 21
fan0Pin = 23
fan1Pin = 29
"***"

"***Hum Sensor***"
dhtSensor0 = Adafruit_DHT.DHT11
DHT11_pin0 = 2
"***"

"***GPIO init***"
GPIO.setmode(GPIO.BOARD)
GPIO.setup(cooler0Pin,GPIO.OUT)
GPIO.setup(cooler1Pin,GPIO.OUT)
GPIO.setup(lamp0Pin,GPIO.OUT)
GPIO.setup(lamp1Pin,GPIO.OUT)
GPIO.setup(heater0Pin,GPIO.OUT)
GPIO.setup(heater1Pin,GPIO.OUT)
GPIO.setup(hum0Pin,GPIO.OUT)
GPIO.setup(hum1Pin,GPIO.OUT)
GPIO.setup(fan0Pin,GPIO.OUT)
GPIO.setup(fan1Pin,GPIO.OUT)
"***"

root = tk.Tk()
root.title("Mushroom Lab")

"***AVG***"
TempAvgLabel = tk.Label(root,text="AVG Temp").grid(row = 0,column = 0)
HumAvgLabel = tk.Label(root,text="AVG HUM").grid(row = 1,column = 0)
TempAvgValue = tk.Label(root,text="NONE")
TempAvgValue.grid(row = 0,column = 1)
HumAvgValue = tk.Label(root,text="NONE")
HumAvgValue.grid(row = 1,column = 1)
"***"

"***Temp & Hum***"
Temp0Label = tk.Label(root,text="Temp0").grid(row = 2,column = 0)
Temp0Value = tk.Label(root,text="NONE")
Temp0Value.grid(row = 2,column = 1)

Temp1Label = tk.Label(root,text="Temp1").grid(row = 3,column = 0)
Temp1Value = tk.Label(root,text = "NONE")
Temp1Value.grid(row = 3,column = 1)

Temp2Label = tk.Label(root,text="Temp2").grid(row = 4,column = 0)
Temp2Value = tk.Label(root,text="NONE")
Temp2Value.grid(row = 4,column = 1)

Temp3Label = tk.Label(root,text="Temp3").grid(row = 5,column = 0)
Temp3Value = tk.Label(root,text="NONE")
Temp3Value.grid(row = 5,column = 1)

hum0Label = tk.Label(root,text="Hum").grid(row = 6,column = 0)
hum0Value = tk.Label(root,text="NONE")
hum0Value.grid(row = 6,column = 1)
"***"

"***Cooler0***"
cooler0Manual = True
GPIO.output(cooler0Pin,GPIO.HIGH)
autoCooler0Status = tk.Label(root,text="Manual Mode")
autoCooler0Status.grid(row = 1,column = 6)
cooler0State = tk.Label(root,text="OFF")
cooler0State.grid(row = 0,column = 3)

def ButtonCooler0OnPressed():
    cooler0Manual = True
    GPIO.output(cooler0Pin,GPIO.LOW)
    cooler0State.configure(text = "ON")
    autoCooler0Status.configure(text = "Manual Mode")

def ButtonCooler0OffPressed():
    cooler0Manual = True
    GPIO.output(cooler0Pin,GPIO.HIGH)
    cooler0State.configure(text = "OFF")
    autoCooler0Status.configure(text = "Manual Mode")

cooler0Label = tk.Label(root,text="Cooler0").grid(row = 0,column = 2)
cooler0On = tk.Button(root,text="ON",bg = "green",command = ButtonCooler0OnPressed)
cooler0On.grid(row = 0,column = 4)
cooler0Off = tk.Button(root,text="OFF",bg = "red",command = ButtonCooler0OffPressed)
cooler0Off.grid(row = 0,column = 5)
"***"

"***Cooler1***"
cooler1Manual = True
GPIO.output(cooler1Pin,GPIO.HIGH)
autoCooler1Status = tk.Label(root,text="Manual Mode")
autoCooler1Status.grid(row = 3,column = 6)
cooler1State = tk.Label(root,text="OFF")
cooler1State.grid(row = 1,column = 3)

def ButtonCooler1OnPressed():
    cooler1Manual = True
    GPIO.output(cooler1Pin,GPIO.LOW)
    cooler1State.configure(text = "ON")
    autoCooler1Status.configure(text = "Manual Mode")

def ButtonCooler1OffPressed():
    cooler1Manual = True
    GPIO.output(cooler1Pin,GPIO.HIGH)
    cooler1State.configure(text = "OFF")
    autoCooler1Status.configure(text = "Manual Mode")

cooler1Label = tk.Label(root,text="Cooler1").grid(row = 1,column = 2)
cooler1On = tk.Button(root,text="ON",bg = "green",command = ButtonCooler1OnPressed)
cooler1On.grid(row = 1,column = 4)
cooler1Off = tk.Button(root,text="OFF",bg = "red",command = ButtonCooler1OffPressed)
cooler1Off.grid(row = 1,column = 5)
"***"

"***Lamp0***"
GPIO.output(lamp0Pin,GPIO.HIGH)
lamp0State = tk.Label(root,text="OFF")
lamp0State.grid(row = 2,column = 3)

def ButtonLamp0OnPressed():
    GPIO.output(lamp0Pin,GPIO.LOW)
    lamp0State.configure(text = "ON")

def ButtonLamp0OffPressed():
    GPIO.output(lamp0Pin,GPIO.HIGH)
    lamp0State.configure(text = "OFF")

lamp0Label = tk.Label(root,text="Lamp0").grid(row = 2,column = 2)
lamp0On = tk.Button(root,text="ON",bg = "green",command = ButtonLamp0OnPressed)
lamp0On.grid(row = 2,column = 4)
lamp0Off = tk.Button(root,text="OFF",bg = "red",command = ButtonLamp0OffPressed)
lamp0Off.grid(row = 2,column = 5)
"***"

"***Lamp1***"
GPIO.output(lamp1Pin,GPIO.HIGH)
lamp1State = tk.Label(root,text="OFF")
lamp1State.grid(row = 3,column = 3)

def ButtonLamp1OnPressed():
    GPIO.output(lamp1Pin,GPIO.LOW)
    lamp1State.configure(text = "ON")

def ButtonLamp1OffPressed():
    GPIO.output(lamp1Pin,GPIO.HIGH)
    lamp1State.configure(text = "OFF")

lamp1Label = tk.Label(root,text="Lamp1").grid(row = 3,column = 2)
lamp1On = tk.Button(root,text="ON",bg = "green",command = ButtonLamp1OnPressed)
lamp1On.grid(row = 3,column = 4)
lamp1Off = tk.Button(root,text="OFF",bg = "red",command = ButtonLamp1OffPressed)
lamp1Off.grid(row = 3,column = 5)
"***"

"***Heater0***"
heater0Manual = True
GPIO.output(heater0Pin,GPIO.HIGH)
autoHeater0Status = tk.Label(root,text="Manual Mode")
autoHeater0Status.grid(row = 5,column = 6)
heater0State = tk.Label(root,text="OFF")
heater0State.grid(row = 4,column = 3)

def ButtonHeater0OnPressed():
    heater0Manual = True
    GPIO.output(heater0Pin,GPIO.LOW)
    heater0State.configure(text = "ON")
    heater0Status.configure(text = "Manual Mode")

def ButtonHeater0OffPressed():
    heater0Manual = True
    GPIO.output(heater0Pin,GPIO.HIGH)
    heater0State.configure(text = "OFF")
    heater0Status.configure(text = "Manual Mode")

heater0Label = tk.Label(root,text="heater0").grid(row = 4,column = 2)
heater0On = tk.Button(root,text="ON",bg = "green",command = ButtonHeater0OnPressed)
heater0On.grid(row = 4,column = 4)
heater0Off = tk.Button(root,text="OFF",bg = "red",command = ButtonHeater0OffPressed)
heater0Off.grid(row = 4,column = 5)
"***"

"***Heater1***"

heater1Manual = True
GPIO.output(heater1Pin,GPIO.HIGH)
autoHeater1Status = tk.Label(root,text="Manual Mode")
autoHeater1Status.grid(row = 7,column = 6)
heater1State = tk.Label(root,text="OFF")
heater1State.grid(row = 5,column = 3)

def ButtonHeater1OnPressed():
    heater1Manual = True
    GPIO.output(heater1Pin,GPIO.LOW)
    heater1State.configure(text = "ON")
    autoHeater1Status.configure(text = "Manual Mode")

def ButtonHeater1OffPressed():
    heater1Manual = True
    GPIO.output(heater1Pin,GPIO.HIGH)
    heater1State.configure(text = "OFF")
    autoHeater1Status.configure(text = "Manual Mode")

heater1Label = tk.Label(root,text="heater1").grid(row = 5,column = 2)
heater1On = tk.Button(root,text="ON",bg = "green",command = ButtonHeater1OnPressed)
heater1On.grid(row = 5,column = 4)
heater1Off = tk.Button(root,text="OFF",bg = "red",command = ButtonHeater1OffPressed)
heater1Off.grid(row = 5,column = 5)
"***"

"***Hum0***"
hum0Manual = True
GPIO.output(hum0Pin,GPIO.HIGH)
autoHum0Status = tk.Label(root,text="Manual Mode")
autoHum0Status.grid(row = 9,column = 6)
hum0State = tk.Label(root,text="OFF")
hum0State.grid(row = 6,column = 3)

def ButtonHum0OnPressed():
    hum0Manual = True
    GPIO.output(hum0Pin,GPIO.LOW)
    hum0State.configure(text = "ON")
    autoHum0Status.configure(text = "Manual Mode")

def ButtonHum0OffPressed():
    hum0Manual = True
    GPIO.output(hum0Pin,GPIO.HIGH)
    hum0State.configure(text = "OFF")
    autoHum0Status.configure(text = "Manual Mode")

hum0Label = tk.Label(root,text="hum0").grid(row = 6,column = 2)
hum0On = tk.Button(root,text="ON",bg = "green",command = ButtonHum0OnPressed)
hum0On.grid(row = 6,column = 4)
hum0Off = tk.Button(root,text="OFF",bg = "red",command = ButtonHum0OffPressed)
hum0Off.grid(row = 6,column = 5)
"***"

"***Hum1***"

hum1Manual = True
GPIO.output(hum1Pin,GPIO.HIGH)
autoHum1Status = tk.Label(root,text="Manual Mode")
autoHum1Status.grid(row = 11,column = 6)
hum1State = tk.Label(root,text="OFF")
hum1State.grid(row = 7,column = 3)

def ButtonHum1OnPressed():
    hum1Manual = True
    GPIO.output(hum1Pin,GPIO.LOW)
    hum1State.configure(text = "ON")
    autoHum1Status.configure(text = "OFF")

def ButtonHum1OffPressed():
    hum1Manual = True
    GPIO.output(hum1Pin,GPIO.HIGH)
    hum1State.configure(text = "OFF")
    autoHum1Status.configure(text = "Manual Mode")

hum1Label = tk.Label(root,text="hum1").grid(row = 7,column = 2)
hum1On = tk.Button(root,text="ON",bg = "green",command = ButtonHum1OnPressed)
hum1On.grid(row = 7,column = 4)
hum1Off = tk.Button(root,text="OFF",bg = "red",command = ButtonHum1OffPressed)
hum1Off.grid(row = 7,column = 5)
"***"

"***Fan0***"

GPIO.output(fan0Pin,GPIO.HIGH)
fan0State = tk.Label(root,text="Off")
fan0State.grid(row = 8,column = 3)

def ButtonFan0OnPressed():
    GPIO.output(fan0Pin,GPIO.LOW)
    fan0State.configure(text = "ON")

def ButtonFan0OffPressed():
    GPIO.output(fan0Pin,GPIO.HIGH)
    fan0State.configure(text = "OFF")

fan0Label = tk.Label(root,text="fan0").grid(row = 8,column = 2)
fan0On = tk.Button(root,text="ON",bg = "green",command = ButtonFan0OnPressed)
fan0On.grid(row = 8,column = 4)
fan0Off = tk.Button(root,text="OFF",bg = "red",command = ButtonFan0OffPressed)
fan0Off.grid(row = 8,column = 5)
"***"

"***Fan1***"

GPIO.output(fan1Pin,GPIO.HIGH)
fan1State = tk.Label(root,text="Off")
fan1State.grid(row = 9,column = 3)

def ButtonFan1OnPressed():
    GPIO.output(fan1Pin,GPIO.LOW)
    fan1State.configure(text = "ON")

def ButtonFan1OffPressed():
    GPIO.output(fan1Pin,GPIO.HIGH)
    fan1State.configure(text = "OFF")

fan1Label = tk.Label(root,text="fan1").grid(row = 9,column = 2)
fan1On = tk.Button(root,text="ON",bg = "green",command = ButtonFan1OnPressed)
fan1On.grid(row = 9,column = 4)
fan1Off = tk.Button(root,text="OFF",bg = "red",command = ButtonFan1OffPressed)
fan1Off.grid(row = 9,column = 5)
"***"

"***Auto***"

autoCooler0LowVal = 20
autoCooler0HighVal = 25
autoCooler0Label = tk.Label(root,text="cooler0").grid(row = 0,column = 6)
autoCooler0LowLabel = tk.Label(root,text="low").grid(row = 0,column = 7)
autoCooler0LowSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoCooler0LowSpinBox.grid(row = 0,column = 8)
autoCooler0HighLabel = tk.Label(root,text="high").grid(row = 0,column = 9)
autoCooler0HighSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoCooler0HighSpinBox.grid(row = 0,column = 10)

def AutoCooler0Ok():
    global cooler0Manual
    cooler0Manual = False
    autoCooler0Status.configure(text = "Auto Mode")
    global autoCooler0LowVal
    global autoCooler0HighVal
    autoCooler0LowVal = float(autoCooler0LowSpinBox.get())
    autoCooler0HighVal = float(autoCooler0HighSpinBox.get())

def AutoCooler0Clear():
    global cooler0Manual
    cooler0Manual = True
    autoCooler0Status.configure(text = "Manual Mode")

autoCooler0Ok = tk.Button(root,text="Apply",bg = "green",command = AutoCooler0Ok)
autoCooler0Ok.grid(row = 0,column = 11)
autoCooler0Clear = tk.Button(root,text="Clear",bg = "red",command = AutoCooler0Clear)
autoCooler0Clear.grid(row = 0,column = 12)

autoCooler1LowVal = 20
autoCooler1HighVal = 25
autoCooler1Label = tk.Label(root,text="cooler1").grid(row = 2,column = 6)
autoCooler1LowLabel = tk.Label(root,text="low").grid(row = 2,column = 7)
autoCooler1LowSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoCooler1LowSpinBox.grid(row = 2,column = 8)
autoCooler1HighLabel = tk.Label(root,text="high").grid(row = 2,column = 9)
autoCooler1HighSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoCooler1HighSpinBox.grid(row = 2,column = 10)

def AutoCooler1Ok():
    global cooler1Manual
    cooler1Manual = False
    autoCooler1Status.configure(text = "Auto Mode")
    global autoCooler1LowVal
    global autoCooler1HighVal
    autoCooler1LowVal = autoCooler1LowSpinBox.get()
    autoCooler1HighVal = autoCooler1HighSpinBox.get()

def AutoCooler1Clear():
    global cooler1Manual
    cooler1Manual = True
    autoCooler1Status.configure(text = "Manual mode")

autoCooler1Ok = tk.Button(root,text="Apply",bg = "green",command = AutoCooler1Ok)
autoCooler1Ok.grid(row = 2,column = 11)
autoCooler1Clear = tk.Button(root,text="Clear",bg = "red",command = AutoCooler1Clear)
autoCooler1Clear.grid(row = 2,column = 12)

autoHeater0LowVal = 20
autoHeater0HighVal = 25
autoHeater0Label = tk.Label(root,text="heater0").grid(row = 4,column = 6)
autoHeater0LowLabel = tk.Label(root,text="low").grid(row = 4,column = 7)
autoHeater0LowSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHeater0LowSpinBox.grid(row = 4,column = 8)
autoHeater0HighLabel = tk.Label(root,text="high").grid(row = 4,column = 9)
autoHeater0HighSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHeater0HighSpinBox.grid(row = 4,column = 10)

def AutoHeater0Ok():
    global heater0Manual
    heater0Manual = False
    autoHeater0Status.configure(text = "Auto Mode")
    global autoHeater0LowVal
    global autoHeater0HighVal
    autoHeater0LowVal = autoHeater0LowSpinBox.get()
    autoHeater0HighVal = autoHeater0HighSpinBox.get()

def AutoHeater0Clear():
    global heater0Manual
    heater0Manual = True
    autoHeater0Status.configure(text = "Manual Mode")

autoHeater0Ok = tk.Button(root,text="Apply",bg = "green",command = AutoHeater0Ok)
autoHeater0Ok.grid(row = 4,column = 11)
autoHeater0Clear = tk.Button(root,text="Clear",bg = "red",command = AutoHeater0Clear)
autoHeater0Clear.grid(row = 4,column = 12)

autoHeater1LowVal = 20
autoHeater1HighVal = 25
autoHeater1Label = tk.Label(root,text="heater1").grid(row = 6,column = 6)
autoHeater1LowLabel = tk.Label(root,text="low").grid(row = 6,column = 7)
autoHeater1LowSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHeater1LowSpinBox.grid(row = 6,column = 8)
autoHeater1HighLabel = tk.Label(root,text="high").grid(row = 6,column = 9)
autoHeater1HighSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHeater1HighSpinBox.grid(row = 6,column = 10)

def AutoHeater1Ok():
    global heater1Manual
    heater1Manual = False
    autoHeater1Status.configure(text = "Manual Mode")
    global autoHeater1LowVal
    global autoHeater1HighVal
    autoHeater1LowVal = autoHeater1LowSpinBox.get()
    autoHeater1HighVal = autoHeater1HighSpinBox.get()

def AutoHeater1Clear():
    global heaterManual
    heaterManual = True
    autoHeater1Status.configure(text = "Manual Mode")

autoHeater1Ok = tk.Button(root,text="Apply",bg = "green",command = AutoHeater1Ok)
autoHeater1Ok.grid(row = 6,column = 11)
autoHeater1Clear = tk.Button(root,text="Clear",bg = "red",command = AutoHeater1Clear)
autoHeater1Clear.grid(row = 6,column = 12)

autoHum0LowVal = 50
autoHum0HighVal = 70
autoHum0Label = tk.Label(root,text="hum0").grid(row = 8,column = 6)
autoHum0LowLabel = tk.Label(root,text="low").grid(row = 8,column = 7)
autoHum0LowSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHum0LowSpinBox.grid(row = 8,column = 8)
autoHum0HighLabel = tk.Label(root,text="high").grid(row = 8,column = 9)
autoHum0HighSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHum0HighSpinBox.grid(row = 8,column = 10)

def AutoHum0Ok():
    global hum0Manual
    hum0Manual = False
    autoHum0Status.configure(text = "Auto Mode")
    global autoHum0LowVal
    global autoHum0HighVal
    autoHum0LowVal = autoHum0LowSpinBox.get()
    autoHum0HighVal = autoHum0HighSpinBox.get()
    print(autoHum0LowVal)

def AutoHum0Clear():
    global hum0Manual
    hum0Manual = True
    autoHum0Status.configure(text = "Manual Mode")

autoHum0Ok = tk.Button(root,text="Apply",bg = "green",command = AutoHum0Ok)
autoHum0Ok.grid(row = 8,column = 11)
autoHum0Clear = tk.Button(root,text="Clear",bg = "red",command = AutoHum0Clear)
autoHum0Clear.grid(row = 8,column = 12)

autoHum1LowVal = 50
autoHum1HighVal = 70
autoHum1Label = tk.Label(root,text="hum1").grid(row = 10,column = 6)
autoHum1LowLabel = tk.Label(root,text="low").grid(row = 10,column = 7)
autoHum1LowSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHum1LowSpinBox.grid(row = 10,column = 8)
autoHum1HighLabel = tk.Label(root,text="high").grid(row = 10,column = 9)
autoHum1HighSpinBox = tk.Spinbox(root,from_ = 0,to = 100,width = 3)
autoHum1HighSpinBox.grid(row = 10,column = 10)

def AutoHum1Ok():
    global hum1Manual
    hum1Manual = False
    autoHum1Status.configure(text = "Auto Mode")
    global autoHum1LowVal
    global autoHum1HighVal
    autoHum1LowVal = autoHum1LowSpinBox.get()
    autoHum1HighVal = autoHum1HighSpinBox.get()

def AutoHum1Clear():
    global hum1Manual
    hum1Manual = True
    autoHum1Status.configure(text = "Manual Mode")

autoHum1Ok = tk.Button(root,text="Apply",bg = "green",command = AutoHum1Ok)
autoHum1Ok.grid(row = 10,column = 11)
autoHum1Clear = tk.Button(root,text="Clear",bg = "red",command = AutoHum1Clear)
autoHum1Clear.grid(row = 10,column = 12)

def MainLoop():
    avgTemp = 0.0
    i = 0
    sensor = W1ThermSensor()
    for sensor in W1ThermSensor.get_available_sensors():
        tmp = sensor.get_temperature()
        avgTemp = avgTemp + tmp
        if i == 0:
            Temp0Value.configure(text = str(tmp))
            if cooler0Manual is False:
                if tmp > autoCooler0HighVal:
                    GPIO.output(cooler0Pin,GPIO.LOW)
                    cooler0State.configure(text = "ON")
                if tmp < autoCooler0LowVal:
                    GPIO.output(cooler0Pin,GPIO.HIGH)
                    cooler0State.configure(text = "OFF")
            if heater0Manual == False:
                if tmp < autoHeater0LowVal:
                    GPIO.output(heater0Pin,GPIO.LOW)
                    heater0State.configure(text = "ON")
                if tmp > autoHeater0HighVal:
                    GPIO.output(heater0Pin,GPIO.HIGH)
                    heater0State.configure(text = "OFF")
        if i == 1:
            Temp1Value.configure(text = str(tmp))
            if cooler0Manual == False:
                if tmp > autoCooler0HighVal:
                    GPIO.output(cooler0Pin,GPIO.LOW)
                    cooler0State.configure(text = "ON")
                if tmp < autoCooler0LowVal:
                    GPIO.output(cooler0Pin,GPIO.HIGH)
                    cooler0State.configure(text = "OFF")
            if heater0Manual == False:
                if tmp < autoHeater0LowVal:
                    GPIO.output(heater0Pin,GPIO.LOW)
                    heater0State.configure(text = "ON")
                if tmp > autoHeater0HighVal:
                    GPIO.output(heater0Pin,GPIO.HIGH)
                    heater0State.configure(text = "OFF")
        if i == 2:
            Temp2Value.configure(text = str(tmp))
            if cooler1Manual == False:
                if tmp > autoCooler1HighVal:
                    GPIO.output(cooler1Pin,GPIO.LOW)
                    cooler1State.configure(text = "ON")
                if tmp < autoCooler1LowVal:
                    GPIO.output(cooler1Pin,GPIO.HIGH)
                    cooler1State.configure(text = "OFF")
            if heater1Manual == False:
                if tmp < autoHeater1LowVal:
                    GPIO.output(heater1Pin,GPIO.LOW)
                    heater1State.configure(text = "ON")
                if tmp > autoHeater1HighVal:
                    GPIO.output(heater1Pin,GPIO.HIGH)
                    heater1State.configure(text = "OFF")
        if i == 3:
            Temp3Value.configure(text = str(tmp))
            if cooler1Manual == False:
                if tmp > autoCooler1HighVal:
                    GPIO.output(cooler1Pin,GPIO.LOW)
                    cooler1State.configure(text = "ON")
                if tmp < autoCooler1LowVal:
                    GPIO.output(cooler1Pin,GPIO.HIGH)
                    cooler1State.configure(text = "OFF")
            if heater1Manual == False:
                if tmp < autoHeater1LowVal:
                    GPIO.output(heater1Pin,GPIO.LOW)
                    heater1State.configure(text = "ON")
                if tmp > autoHeater1HighVal:
                    GPIO.output(heater1Pin,GPIO.HIGH)
                    heater1State.configure(text = "OFF")
        i = i + 1
    avgTemp = avgTemp / i
    TempAvgValue.configure(text = str(avgTemp))

    humidity0, temperature0 = Adafruit_DHT.read_retry(dhtSensor0,DHT11_pin0)
    if humidity0 is not None and temperature0 is not None:
        hum0Value.configure(text = str(humidity0))
        if hum0Manual == False:
            if humidity0 < autoHum0LowVal:
                GPIO.output(hum0Pin,GPIO.LOW)
                hum0State.configure(text = "ON")
            if humidity0 > autoHum0HighVal:
                GPIO.output(hum0Pin,GPIO.HIGH)
                hum0State.configure(text = "OFF")

    avgHum = humidity0
    HumAvgValue.configure(text = str(avgHum))

    root.update_idletasks()
    root.update()
    timer = threading.Timer(1,MainLoop)
    timer.start()

timer = threading.Timer(1,MainLoop)
timer.start()

root.mainloop()

