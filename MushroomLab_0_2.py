import tkinter as tk
import Adafruit_DHT
import threading
from tkinter import StringVar
from w1thermsensor import W1ThermSensor
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

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

#Graphs
hour = 3600
day = hour * 24
week = day * 7
month = week * 4
graphItter = 1

X1 = np.arange(hour)          #hourly
X2 = np.arange(day)           #daily
X3 = np.arange(week)          #weekly
X4 = np.arange(month)         #monthly

currentTimeH = datetime.now()
currentTimeD = datetime.now()
currentTimeW = datetime.now()
currentTimeM = datetime.now()

avgTempHourly = np.arange(hour)
avgTempHourly[:] = np.NaN
avgTempDaily = np.arange(day)
avgTempDaily[:] = np.NaN
avgTempWeekly = np.arange(week)
avgTempWeekly[:] = np.NaN
avgTempMonthly = np.arange(month)
avgTempMonthly[:] = np.NaN

avgHumHourly = np.arange(hour)
avgHumHourly[:] = np.NaN
avgHumDaily = np.arange(day)
avgHumDaily[:] = np.NaN
avgHumWeekly = np.arange(week)
avgHumWeekly[:] = np.NaN
avgHumMonthly = np.arange(month)
avgHumMonthly[:] = np.NaN

temp0Hourly = np.arange(hour)
temp0Hourly[:] = np.NaN
temp0Daily = np.arange(day)
temp0Daily[:] = np.NaN
temp0Weekly = np.arange(week)
temp0Weekly[:] = np.NaN
temp0Monthly = np.arange(month)
temp0Monthly[:] = np.NaN

temp1Hourly = np.arange(hour)
temp1Hourly[:] = np.NaN
temp1Daily = np.arange(day)
temp1Daily[:] = np.NaN
temp1Weekly = np.arange(week)
temp1Weekly[:] = np.NaN
temp1Monthly = np.arange(month)
temp1Monthly[:] = np.NaN

temp2Hourly = np.arange(hour)
temp2Hourly[:] = np.NaN
temp2Daily = np.arange(day)
temp2Daily[:] = np.NaN
temp2Weekly = np.arange(week)
temp2Weekly[:] = np.NaN
temp2Monthly = np.arange(month)
temp2Monthly[:] = np.NaN

temp3Hourly = np.arange(hour)
temp3Hourly[:] = np.NaN
temp3Daily = np.arange(day)
temp3Daily[:] = np.NaN
temp3Weekly = np.arange(week)
temp3Weekly[:] = np.NaN
temp3Monthly = np.arange(month)
temp3Monthly[:] = np.NaN

hum0Hourly = np.arange(hour)
hum0Hourly[:] = np.NaN
hum0Daily = np.arange(day)
hum0Daily[:] = np.NaN
hum0Weekly = np.arange(week)
hum0Weekly[:] = np.NaN
hum0Monthly = np.arange(month)
hum0Monthly[:] = np.NaN

hum1Hourly = np.arange(hour)
hum1Hourly[:] = np.NaN
hum1Daily = np.arange(day)
hum1Daily[:] = np.NaN
hum1Weekly = np.arange(week)
hum1Weekly[:] = np.NaN
hum1Monthly = np.arange(month)
hum1Monthly[:] = np.NaN

#Avg Temp
def ShowAvgTempHourly():
    global currentTimeH
    global avgTempHourly
    global X1
    fig = plt.figure()
    fig.suptitle("Avg Temp Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,avgTempHourly)
    plt.show()

def ShowAvgTempDaily():
    global currentTimeD
    global avgTempDaily
    global X2
    fig = plt.figure()
    fig.suptitle("Avg Temp Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,avgTempDaily)
    plt.show()

def ShowAvgTempWeekly():
    global currentTimeW
    global avgTempWeekly
    global X3
    fig = plt.figure()
    fig.suptitle("Avg Temp Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,avgTempWeekly)
    plt.show()

def ShowAvgTempMonthly():
    global currentTimeM
    global avgTempMonthly
    global X4
    fig = plt.figure()
    fig.suptitle("Avg Temp Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,avgTempMonthly)
    plt.show()

def SaveAvgTempHourly():
    global currentTimeH
    global X1
    global avgTempHourly
    fig = plt.figure()
    fig.suptitle("Avg Temp Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,avgTempHourly)
    fig.savefig("./AvgTemp/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveAvgTempDaily():
    global currentTimeD
    global X2
    global avgTempDaily
    fig = plt.figure()
    fig.suptitle("Avg Temp Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,avgTempDaily)
    fig.savefig("./AvgTemp/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveAvgTempWeekly():
    global currentTimeW
    global X3
    global avgTempWeekly
    fig = plt.figure()
    fig.suptitle("Avg Temp Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,avgTempWeekly)
    fig.savefig("./AvgTemp/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveAvgTempMonthly():
    global currentTimeM
    global X4
    global avgTempMonthly
    fig = plt.figure()
    fig.suptitle("Avg Temp Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,avgTempMonthly)
    fig.savefig("./AvgTemp/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitAvgTempHourly():
    global currentTimeH
    global avgTempHourly
    avgTempHourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitAvgTempDaily():
    global currentTimeD
    global avgTempDaily
    avgTempDaily[:] = np.NaN
    currentTimeD = datetime.now()

def InitAvgTempWeekly():
    global currentTimeW
    global avgTempWeekly
    avgTepmWeekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitAvgTempMonthly():
    global currentTimeM
    global avgTempMonthly
    avgTempMonthly[:] = np.NaN
    currentTimeM = datetime.now()

#Avg Hum
def ShowAvgHumHourly():
    global currentTimeH
    global avgHumHourly
    global X1
    fig = plt.figure()
    fig.suptitle("Avg Hum Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,avgHumHourly)
    plt.show()

def ShowAvgHumDaily():
    global currentTimeD
    global avgHumDaily
    global X2
    fig = plt.figure()
    fig.suptitle("Avg Hum Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,avgHumDaily)
    plt.show()

def ShowAvgHumWeekly():
    global currentTimeW
    global avgHumWeekly
    global X3
    fig = plt.figure()
    fig.suptitle("Avg Hum Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,avgHumWeekly)
    plt.show()

def ShowAvgHumMonthly():
    global currentTimeM
    global avgHumMonthly
    global X4
    fig = plt.figure()
    fig.suptitle("Avg Hum Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,avgHumMonthly)
    plt.show()

def SaveAvgHumHourly():
    global currentTimeH
    global X1
    global avgHumHourly
    fig = plt.figure()
    fig.suptitle("Avg Hum Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,avgHumHourly)
    fig.savefig("./AvgHum/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveAvgHumDaily():
    global currentTimeD
    global X2
    global avgHumDaily
    fig = plt.figure()
    fig.suptitle("Avg Hum Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,avgHumDaily)
    fig.savefig("./AvgHum/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveAvgHumWeekly():
    global currentTimeW
    global X3
    global avgHumWeekly
    fig = plt.figure()
    fig.suptitle("Avg Hum Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,avgHumWeekly)
    fig.savefig("./AvgHum/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveAvgHumMonthly():
    global currentTimeM
    global X4
    global avgHumMonthly
    fig = plt.figure()
    fig.suptitle("Avg Hum Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,avgHumMonthly)
    fig.savefig("./AvgHum/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitHumHourly():
    global currentTimeH
    global avgHumHourly
    avgHumHourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitHumTempDaily():
    global currentTimeD
    global avgHumDaily
    avgHumDaily[:] = np.NaN
    currentTimeD = datetime.now()

def InitAvgHumWeekly():
    global currentTimeW
    global avgHumWeekly
    avgHumWeekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitAvgHumMonthly():
    global currentTimeM
    global avgHumMonthly
    avgHumMonthly[:] = np.NaN
    currentTimeM = datetime.now()
#Temp0
def ShowTemp0Hourly():
    global currentTimeH
    global temp0Hourly
    global X1
    fig = plt.figure()
    fig.suptitle("Temperature0 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp0Hourly)
    plt.show()

def ShowTemp0Daily():
    global currentTimeD
    global temp0Daily
    global X2
    fig = plt.figure()
    fig.suptitle("Temperature0 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp0Daily)
    plt.show()

def ShowTemp0Weekly():
    global currentTimeW
    global temp0Weekly
    global X3
    fig = plt.figure()
    fig.suptitle("Temperature0 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp0Weekly)
    plt.show()

def ShowTemp0Monthly():
    global currentTimeM
    global temp0Monthly
    global X4
    fig = plt.figure()
    fig.suptitle("Temperature0 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp0Monthly)
    plt.show()

def SaveTemp0Hourly():
    global currentTimeH
    global X1
    global temp0Hourly
    fig = plt.figure()
    fig.suptitle("Temperature0 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp0Hourly)
    fig.savefig("./Temp0/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveTemp0Daily():
    global currentTimeD
    global X2
    global temp0Daily
    fig = plt.figure()
    fig.suptitle("Temperature0 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp0Daily)
    fig.savefig("./Temp0/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveTemp0Weekly():
    global currentTimeW
    global X3
    global temp0Weekly
    fig = plt.figure()
    fig.suptitle("Temperature0 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp0Weekly)
    fig.savefig("./Temp0/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveTemp0Monthly():
    global currentTimeM
    global X4
    global temp0Monthly
    fig = plt.figure()
    fig.suptitle("Temperature0 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp0Monthly)
    fig.savefig("./Temp0/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitTemp0Hourly():
    global currentTimeH
    global temp0Hourly
    temp0Hourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitTemp0Daily():
    global currentTimeD
    global temp0Daily
    temp0Daily[:] = np.NaN
    currentTimeD = datetime.now()

def InitTemp0Weekly():
    global currentTimeW
    global temp0Weekly
    temp0Weekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitTemp0Monthly():
    global currentTimeM
    global temp0Monthly
    temp0Monthly[:] = np.NaN
    currentTimeM = datetime.now()

#Temp1
def ShowTemp1Hourly():
    global currentTimeH
    global temp1Hourly
    global X1
    fig = plt.figure()
    fig.suptitle("Temperature1 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp1Hourly)
    plt.show()

def ShowTemp1Daily():
    global currentTimeD
    global temp1Daily
    global X2
    fig = plt.figure()
    fig.suptitle("Temperature1 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp1Daily)
    plt.show()

def ShowTemp1Weekly():
    global currentTimeW
    global temp0Weekly
    global X3
    fig = plt.figure()
    fig.suptitle("Temperature0 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp0Weekly)
    plt.show()

def ShowTemp1Monthly():
    global currentTimeM
    global temp1Monthly
    global X4
    fig = plt.figure()
    fig.suptitle("Temperature1 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp1Monthly)
    plt.show()

def SaveTemp1Hourly():
    global currentTimeH
    global X1
    global temp1Hourly
    fig = plt.figure()
    fig.suptitle("Temperature1 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp1Hourly)
    fig.savefig("./Temp1/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveTemp1Daily():
    global currentTimeD
    global X2
    global temp1Daily
    fig = plt.figure()
    fig.suptitle("Temperature1 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp1Daily)
    fig.savefig("./Temp1/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveTemp1Weekly():
    global currentTimeW
    global X3
    global temp1Weekly
    fig = plt.figure()
    fig.suptitle("Temperature1 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp1Weekly)
    fig.savefig("./Temp1/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveTemp1Monthly():
    global currentTimeM
    global X4
    global temp1Monthly
    fig = plt.figure()
    fig.suptitle("Temperature1 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp1Monthly)
    fig.savefig("./Temp1/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitTemp1Hourly():
    global currentTimeH
    global temp1Hourly
    temp1Hourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitTemp1Daily():
    global currentTimeD
    global temp1Daily
    temp1Daily[:] = np.NaN
    currentTimeD = datetime.now()

def InitTemp1Weekly():
    global currentTimeW
    global temp1Weekly
    temp1Weekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitTemp1Monthly():
    global currentTimeM
    global temp1Monthly
    temp1Monthly[:] = np.NaN
    currentTimeM = datetime.now()

#Temp2
def ShowTemp2Hourly():
    global currentTimeH
    global temp2Hourly
    global X1
    fig = plt.figure()
    fig.suptitle("Temperature2 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp2Hourly)
    plt.show()

def ShowTemp2Daily():
    global currentTimeD
    global temp2Daily
    global X2
    fig = plt.figure()
    fig.suptitle("Temperature2 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp2Daily)
    plt.show()

def ShowTemp2Weekly():
    global currentTimeW
    global temp2Weekly
    global X3
    fig = plt.figure()
    fig.suptitle("Temperature2 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp2Weekly)
    plt.show()

def ShowTemp2Monthly():
    global currentTimeM
    global temp2Monthly
    global X4
    fig = plt.figure()
    fig.suptitle("Temperature2 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp2Monthly)
    plt.show()

def SaveTemp2Hourly():
    global currentTimeH
    global X1
    global temp2Hourly
    fig = plt.figure()
    fig.suptitle("Temperature2 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp2Hourly)
    fig.savefig("./Temp2/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveTemp2Daily():
    global currentTimeD
    global X2
    global temp2Daily
    fig = plt.figure()
    fig.suptitle("Temperature2 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp2Daily)
    fig.savefig("./Temp2/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveTemp2Weekly():
    global currentTimeW
    global X3
    global temp2Weekly
    fig = plt.figure()
    fig.suptitle("Temperature2 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp2Weekly)
    fig.savefig("./Temp2/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveTemp2Monthly():
    global currentTimeM
    global X4
    global temp2Monthly
    fig = plt.figure()
    fig.suptitle("Temperature2 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp2Monthly)
    fig.savefig("./Temp2/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitTemp2Hourly():
    global currentTimeH
    global temp2Hourly
    temp2Hourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitTemp2Daily():
    global currentTimeD
    global temp2Daily
    temp2Daily[:] = np.NaN
    currentTimeD = datetime.now()

def InitTemp2Weekly():
    global currentTimeW
    global temp2Weekly
    temp2Weekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitTemp2Monthly():
    global currentTimeM
    global temp2Monthly
    temp2Monthly[:] = np.NaN
    currentTimeM = datetime.now()

#Temp3
def ShowTemp3Hourly():
    global currentTimeH
    global temp3Hourly
    global X1
    fig = plt.figure()
    fig.suptitle("Temperature3 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp3Hourly)
    plt.show()

def ShowTemp3Daily():
    global currentTimeD
    global temp3Daily
    global X2
    fig = plt.figure()
    fig.suptitle("Temperature3 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp3Daily)
    plt.show()

def ShowTemp3Weekly():
    global currentTimeW
    global temp3Weekly
    global X3
    fig = plt.figure()
    fig.suptitle("Temperature3 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp3Weekly)
    plt.show()

def ShowTemp3Monthly():
    global currentTimeM
    global temp3Monthly
    global X4
    fig = plt.figure()
    fig.suptitle("Temperature3 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp3Monthly)
    plt.show()

def SaveTemp3Hourly():
    global currentTimeH
    global X1
    global temp3Hourly
    fig = plt.figure()
    fig.suptitle("Temperature3 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,temp3Hourly)
    fig.savefig("./Temp3/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveTemp3Daily():
    global currentTimeD
    global X2
    global temp3Daily
    fig = plt.figure()
    fig.suptitle("Temperature3 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,temp3Daily)
    fig.savefig("./Temp3/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveTemp3Weekly():
    global currentTimeW
    global X3
    global temp3Weekly
    fig = plt.figure()
    fig.suptitle("Temperature3 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,temp3Weekly)
    fig.savefig("./Temp3/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveTemp3Monthly():
    global currentTimeM
    global X4
    global temp3Monthly
    fig = plt.figure()
    fig.suptitle("Temperature3 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,temp3Monthly)
    fig.savefig("./Temp3/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitTemp3Hourly():
    global currentTimeH
    global temp3Hourly
    temp3Hourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitTemp3Daily():
    global currentTimeD
    global temp3Daily
    temp3Daily[:] = np.NaN
    currentTimeD = datetime.now()

def InitTemp3Weekly():
    global currentTimeW
    global temp3Weekly
    temp3Weekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitTemp3Monthly():
    global currentTimeM
    global temp3Monthly
    temp3Monthly[:] = np.NaN
    currentTimeM = datetime.now()

#Hum0
def ShowHum0Hourly():
    global currentTimeH
    global hum0Hourly
    global X1
    fig = plt.figure()
    fig.suptitle("Hum0 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,hum0Hourly)
    plt.show()

def ShowHum0Daily():
    global currentTimeD
    global hum0Daily
    global X2
    fig = plt.figure()
    fig.suptitle("Hum0 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,hum0Daily)
    plt.show()

def Showhum0Weekly():
    global currentTimeW
    global hum0Weekly
    global X3
    fig = plt.figure()
    fig.suptitle("Hum0 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,hum0Weekly)
    plt.show()

def ShowHum0Monthly():
    global currentTimeM
    global hum0Monthly
    global X4
    fig = plt.figure()
    fig.suptitle("Hum0 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,hum0Monthly)
    plt.show()

def SaveHum0Hourly():
    global currentTimeH
    global X1
    global hum0Hourly
    fig = plt.figure()
    fig.suptitle("Hum0 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,hum0Hourly)
    fig.savefig("./Hum0/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveHum0Daily():
    global currentTimeD
    global X2
    global hum0Daily
    fig = plt.figure()
    fig.suptitle("Hum0 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,hum0Daily)
    fig.savefig("./Hum0/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveHum0Weekly():
    global currentTimeW
    global X3
    global hum0Weekly
    fig = plt.figure()
    fig.suptitle("Hum0 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,hum0Weekly)
    fig.savefig("./Hum0/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveHum0Monthly():
    global currentTimeM
    global X4
    global hum0Monthly
    fig = plt.figure()
    fig.suptitle("Hum0 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,hum0Monthly)
    fig.savefig("./Hum0/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitHum0Hourly():
    global currentTimeH
    global hum0Hourly
    hum0Hourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitHum0Daily():
    global currentTimeD
    global hum0Daily
    hum0Daily[:] = np.NaN
    currentTimeD = datetime.now()

def InitHum0Weekly():
    global currentTimeW
    global hum0Weekly
    hum0Weekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitHum0Monthly():
    global currentTimeM
    global hum0Monthly
    hum0Monthly[:] = np.NaN
    currentTimeM = datetime.now()

#Hum1
def ShowHum1Hourly():
    global currentTimeH
    global hum1Hourly
    global X1
    fig = plt.figure()
    fig.suptitle("Hum1 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,hum1Hourly)
    plt.show()

def ShowHum1Daily():
    global currentTimeD
    global hum1Daily
    global X2
    fig = plt.figure()
    fig.suptitle("Hum1 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,hum1Daily)
    plt.show()

def Showhum1Weekly():
    global currentTimeW
    global hum1Weekly
    global X3
    fig = plt.figure()
    fig.suptitle("Hum1 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,hum1Weekly)
    plt.show()

def ShowHum1Monthly():
    global currentTimeM
    global hum1Monthly
    global X4
    fig = plt.figure()
    fig.suptitle("Hum1 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,hum1Monthly)
    plt.show()

def SaveHum1Hourly():
    global currentTimeH
    global X1
    global hum1Hourly
    fig = plt.figure()
    fig.suptitle("Hum1 Hourly\n" + str(currentTimeH))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X1,hum1Hourly)
    fig.savefig("./Hum1/Hourly/" + str(currentTimeH) + ".png")
    plt.close(fig)

def SaveHum1Daily():
    global currentTimeD
    global X2
    global hum1Daily
    fig = plt.figure()
    fig.suptitle("Hum1 Daily\n" + str(currentTimeD))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X2,hum1Daily)
    fig.savefig("./Hum1/Daily/" + str(currentTimeD) + ".png")
    plt.close(fig)

def SaveHum1Weekly():
    global currentTimeW
    global X3
    global hum1Weekly
    fig = plt.figure()
    fig.suptitle("Hum1 Weekly\n" + str(currentTimeW))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X3,hum1Weekly)
    fig.savefig("./Hum1/Weekly/" + str(currentTimeW) + ".png")
    plt.close(fig)

def SaveHum1Monthly():
    global currentTimeM
    global X4
    global hum1Monthly
    fig = plt.figure()
    fig.suptitle("Hum1 Monthly\n" + str(currentTimeM))
    ax = fig.add_subplot(1,1,1)
    ax.plot(X4,hum1Monthly)
    fig.savefig("./Hum1/Monthly" + str(currentTimeM) + ".png")
    plt.close(fig)

def InitHum1Hourly():
    global currentTimeH
    global hum1Hourly
    hum1Hourly[:] = np.NaN
    currentTimeH = datetime.now()

def InitHum1Daily():
    global currentTimeD
    global hum0Daily
    hum1Daily[:] = np.NaN
    currentTimeD = datetime.now()

def InitHum1Weekly():
    global currentTimeW
    global hum0Weekly
    hum1Weekly[:] = np.NaN
    currentTimeW = datetime.now()

def InitHum1Monthly():
    global currentTimeM
    global hum0Monthly
    hum1Monthly[:] = np.NaN
    currentTimeM = datetime.now()

def InitHourly():
    InitAvgTempHourly()
    InitAvgHumHourly()
    InitTemp0Hourly()
    InitTemp1Hourly()
    InitTemp2Hourly()
    InitTemp3Hourly()
    InitHum0Hourly()
    InitHum1Hourly()

def InitDaily():
    InitAvgTempDaily()
    InitAvgHumDaily()
    InitTemp0Daily()
    InitTemp1Daily()
    InitTemp2Daily()
    InitTemp3Daily()
    InitHum0Daily()
    InitHum1Daily()

def InitWeekly():
    InitAvgTempWeekly()
    InitAvgHumWeekly()
    InitTemp0Weekly()
    InitTemp1Weekly()
    InitTemp2Weekly()
    InitTemp3Weekly()
    InitHum0Weekly()
    InitHum1Weekly()

def InitMonthly():
    InitAvgTempMonthly()
    InitAvgHumMonthly()
    InitTemp0Monthly()
    InitTemp1Monthly()
    InitTemp2Monthly()
    InitTemp3Monthly()
    InitHum0Monthly()
    InitHum1Monthly()

def SaveHourly():
    SaveAvgTempHourly()
    SaveAvgHumHourly()
    SaveTemp0Hourly()
    SaveTemp1Hourly()
    SaveTemp2Hourly()
    SaveTemp3Hourly()
    SaveHum0Hourly()
    SaveHum1Hourly()

def SaveDaily:
    SaveAvgTempDaily()
    SaveAvgHumDaily()
    SaveTemp0Daily()
    SaveTemp1Daily()
    SaveTemp2Daily()
    SaveTemp3Daily()
    SaveHum0Daily()
    SaveHum1Daily()

def SaveWeekly():
    SaveAvgTempWeekly()
    SaveAvgHumWeekly()
    SaveTemp0Weekly()
    SaveTemp1Weekly()
    SaveTemp2Weekly()
    SaveTemp3Weekly()
    SaveHum0Weekly()
    SaveHum1Weekly()

def SaveMonthly():
    SaveAvgTempMonthly()
    SaveAvgHumMonthly()
    SaveTemp0Monthly()
    SaveTemp1Monthly()
    SaveTemp2Monthly()
    SaveTemp3Monthly()
    SaveHum0Monthly()
    SaveHum1Monthly()

def Graphs():
    rt = tk.Tk()
    rt.title("Graphs")
    
    #Avg Temp
    gAvgTempHourly = tk.Button(rt,text = "AVG Temp\nHourly",command = ShowAvgTempHourly)
    gAvgTempHourly.grid(row = 0,column = 0)
    gAvgTempDaily = tk.Button(rt,text = "AVG Temp\nDaily",command = 
            ShowAvgTempDaily)
    gAvgTempDaily.grid(row = 1,column = 0)
    gAvgTempWeekly = tk.Button(rt,text = "AVG Temp\nWeekly",command = ShowAvgTempWeekly)
    gAvgTempWeekly.grid(row = 2,column = 0)
    gAvgMonthly = tk.Button(rt,text = "AVG Temp\nMonthly",command = ShowAvgTempMonthly)
    gAvgMonthly.grid(row = 3,column = 0)

    #gAvgHum
    gAvgHumHourly = tk.Button(rt,text = "AVG HUM\nHourly",command = 
            ShowAvgHumHourly)
    gAvgHumHourly.grid(row = 0,column = 1)
    gAvgHumDaily = tk.Button(rt,text = "AVG HUM\nDaily",command = 
            ShowAvgHumDaily)
    gAvgHumDaily.grid(row = 1,column = 1)
    gAvgHumWeekly = tk.Button(rt,text = "AVG HUM\nWeekly",command = 
            ShowAvgHumWeekly)
    gAvgHumWeekly.grid(row = 2,column = 1)
    gAvgHumMonthly = tk.Button(rt,text = "AVG HUM\nMonthly",command = 
            ShowAvgHumMonthly)
    gAvgHumMonthly.grid(row = 3,column = 1)

    #gTemp0
    gTemp0Hourly = tk.Button(rt,text = "Temp0\nHourly",command = 
            ShowTemp0Hourly)
    gTemp0Hourly.grid(row = 0,column = 2)
    gTemp0Daily = tk.Button(rt,text = "Temp0\nDaily",command = 
            ShowTemp0Daily)
    gTemp0Daily.grid(row = 1,column = 2)
    gTemp0Weekly = tk.Button(rt,text = "Temp0\nWeekly",command = 
            ShowTemp0Weekly)
    gTemp0Weekly.grid(row = 2,column = 2)
    gTemp0Monthly = tk.Button(rt,text = "Temp0\nMonthly",command = 
            ShowTemp0Monthly)
    gTemp0Monthly.grid(row = 3,column = 2)

    #gTemp1
    gTemp1Hourly = tk.Button(rt,text = "Temp1\nHourly",command = 
            ShowTemp1Hourly)
    gTemp1Hourly.grid(row = 0,column = 3)
    gTemp1Daily = tk.Button(rt,text = "Temp1\nDaily",command = 
            ShowTemp1Daily)
    gTemp1Daily.grid(row = 1,column = 3)
    gTemp1Weekly = tk.Button(rt,text = "Temp1\nWeekly",command = 
            ShowTemp1Weekly)
    gTemp1Weekly.grid(row = 2,column = 3)
    gTemp1Monthly = tk.Button(rt,text = "Temp1\nMonthly",command = 
            ShowTemp1Monthly)
    gTemp1Monthly.grid(row = 3,column = 3)

    #gTemp2
    gTemp2Hourly = tk.Button(rt,text = "Temp2\nHourly",command = 
            ShowTemp2Hourly)
    gTemp2Hourly.grid(row = 0,column = 4)
    gTemp2Daily = tk.Button(rt,text = "Temp2\nDaily",command = 
            ShowTemp2Daily)
    gTemp2Daily.grid(row = 1,column = 4)
    gTemp2Weekly = tk.Button(rt,text = "Temp2\nWeekly",command = 
            ShowTemp2Weekly)
    gTemp2Weekly.grid(row = 2,column = 4)
    gTemp2Monthly = tk.Button(rt,text = "Temp2\nMonthly",command = 
            ShowTemp2Monthly)
    gTemp2Monthly.grid(row = 3,column = 4)

    #gTemp3
    gTemp3Hourly = tk.Button(rt,text = "Temp3\nHourly",command = 
            ShowTemp3Hourly)
    gTemp3Hourly.grid(row = 0,column = 5)
    gTemp3Daily = tk.Button(rt,text = "Temp2\nDaily",command = 
            ShowTemp3Daily)
    gTemp3Daily.grid(row = 1,column = 5)
    gTemp3Weekly = tk.Button(rt,text = "Temp3\nWeekly",command = 
            ShowTemp3Weekly)
    gTemp3Weekly.grid(row = 2,column = 5)
    gTemp3Monthly = tk.Button(rt,text = "Temp3\nMonthly",command = 
            ShowTemp3Monthly)
    gTemp3Monthly.grid(row = 3,column = 5)

    #gHum0
    gHum0Hourly = tk.Button(rt,text = "Hum0\nHourly",command = 
            ShowHum0Hourly)
    gHum0Hourly.grid(row = 0,column = 6)
    gHum0Daily = tk.Button(rt,text = "Hum0\nDaily",command = 
            ShowHum0Daily)
    gHum0Daily.grid(row = 1,column = 6)
    gHum0Weekly = tk.Button(rt,text = "Hum0\nWeekly",command = 
            ShowHum0Weekly)
    gHum0Weekly.grid(row = 2,column = 6)
    gHum0Monthly = tk.Button(rt,text = "Hum0\nMonthly",command = 
            ShowHum0Monthly)
    gHum0Monthly.grid(row = 3,column = 6)

    #gHum1
    gHum1Hourly = tk.Button(rt,text = "Hum1\nHourly",command = 
            ShowHum1Hourly)
    gHum1Hourly.grid(row = 0,column = 7)
    gHum1Daily = tk.Button(rt,text = "Hum1\nDaily",command = 
            ShowHum1Daily)
    gHum1Daily.grid(row = 1,column = 7)
    gHum1Weekly = tk.Button(rt,text = "Hum1\nWeekly",command = 
            ShowHum1Weekly)
    gHum1Weekly.grid(row = 2,column = 7)
    gHum1Monthly = tk.Button(rt,text = "Hum1\nMonthly",command = 
            ShowHum1Monthly)
    gHum1Monthly.grid(row = 3,column = 7)

    rt.mainloop()

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
    global graphItter
    avgTemp = 0.0
    i = 0
    sensor = W1ThermSensor()
    if graphItter % month == 0:
        graphItter = 1
        SaveMonthly()
        InitMonthly()
    if graphItter % week == 0:
        SaveWeekly()
        InitWeekly()
    if graphItter % day == 0:
        SaveDaily()
        InitDaily()
    if graphItter % hour == 0:
        SaveHourly()
        InitHourly()
    for sensor in W1ThermSensor.get_available_sensors():
        tmp = sensor.get_temperature()
        avgTemp = avgTemp + tmp
        if i == 0:
            temp0Hourly[graphItter % hour] = tmp
            temp0Daily[graphItter % day] = tmp
            temp0Weekly[graphItter % week] = tmp
            temp0Monthly[graphItter % month] = tmp

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
            temp1Hourly[graphItter % hour] = tmp
            temp1Daily[graphItter % day] = tmp
            temp1Weekly[graphItter % week] = tmp
            temp1Monthly[graphItter % month] = tmp

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
            temp2Hourly[graphItter % hour] = tmp
            temp2Daily[graphItter % day] = tmp
            temp2Weekly[graphItter % week] = tmp
            temp2Monthly[graphItter % month] = tmp

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
            temp3Hourly[graphItter % hour] = tmp
            temp3Daily[graphItter % day] = tmp
            temp3Weekly[graphItter % week] = tmp
            temp3Monthly[graphItter % month] = tmp

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
    avgTempHourly[graphItter % hour] = avgTemp
    avgTempDaily[graphItter % day] = avgTemp
    avgTempWeekly[graphItter % week] = avgTemp
    avgTempMonthly[graphItter % month] = avgTemp

    TempAvgValue.configure(text = str(avgTemp))

    humidity0, temperature0 = Adafruit_DHT.read_retry(dhtSensor0,DHT11_pin0)
    if humidity0 is not None and temperature0 is not None:
        hum0Hourly[graphItter % hour] = humidity0
        hum0Daily[graphItter % day] = humidity0
        hum0Weekly[graphItter % week] = humidity0
        hum0Monthly[graphItter % month] = humidity0

        hum0Value.configure(text = str(humidity0))
        if hum0Manual == False:
            if humidity0 < autoHum0LowVal:
                GPIO.output(hum0Pin,GPIO.LOW)
                hum0State.configure(text = "ON")
            if humidity0 > autoHum0HighVal:
                GPIO.output(hum0Pin,GPIO.HIGH)
                hum0State.configure(text = "OFF")

    avgHum = humidity0
    avgHumHourly[graphItter % hour] = avgHum
    avgHumDaily[graphItter % day] = avgHum
    avgHumWeekly[graphItter % week] = avgHum
    avgHumMonthly[graphItter % month] = avgHum
    HumAvgValue.configure(text = str(avgHum))
    graphItter = graphItter + 1
    root.update_idletasks()
    root.update()
    timer = threading.Timer(1,MainLoop)
    timer.start()

timer = threading.Timer(1,MainLoop)
timer.start()

root.mainloop()

