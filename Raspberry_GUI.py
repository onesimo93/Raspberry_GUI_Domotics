from cgitb import text
from tkinter import *
from tkinter import ttk
import tkinter
import time
import os
import glob
import datetime
from board import SCL,SDA
import busio
from adafruit_seesaw.seesaw import Seesaw
from gpiozero import LED




from w1thermsensor import W1ThermSensor, SensorNotReadyError, NoSensorFoundError

root = Tk()
Variable_Test = "Mira"
Null = "Null"
Array_ID = [0,0,0]
Array_T = ["Null","Null","Null"]
Temp1 = None
Temp2 = None
Temp3 = None
Humidity = None
TV_Temp_Max = 30
TV_Temp_Min = 25
TV_Humidity = 0
AV_Temp = None
#i2c_bus = busio.I2C(SCL,SDA)
#ss = Seesaw(i2c_bus, addr = 0x36)
RL_Channel_Temp = LED(26)
RL_Channel_Humidity = LED(20)
RL_Channel_Timer = LED(21)



content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=175, height=300)
frame_2 = ttk.Frame(content, borderwidth=5, relief="ridge", width=375, height=300)
frame_3 = ttk.Frame(content, borderwidth=5, relief="ridge", width=175, height=300)
frame_4 = ttk.Frame(content, borderwidth=5, relief="ridge", width=175, height=300)

#### Functions
    
 
def count():
    global counter
    counter.set(counter.get() + 1)

def Humidity():
    Check = i2c_bus.scan()
    if not bool(Check):
        Humidity_Tk_Var.set("Null")
    else:
        
        touch = ss.moisture_read()
        Humidity_Tk_Var.set(touch)
        
    root.after(2000,Humidity)
    
def Update_Temperature_TV():
    Check=1
    test = OV_Temp_Max.get()
    print(OV_Temp_Max.get())
    


def poll():
    global counter
    Counter = 0
    for sensor in W1ThermSensor.get_available_sensors():
        try:
            Array_ID[Counter] = sensor.id
        except SensorNotReadyError:
            Array_ID[Counter] = 8000
        try:
            Array_T[Counter] = sensor.get_temperature()
        except IndexError:
            Array_T[Counter] = "Null"
        
        Counter = Counter +1

            
            
      
    Temp1.set(Array_T[0])
    Temp2.set(Array_T[1])
    Temp3.set(Array_T[2])
    root.after(500,poll)

def Average_temperature():
    Contador = 0
    Tot_Temp = 0
    IsANumber = 0
    Average = 0.0
    while Contador < 3:
        if Array_T[Contador] != "Null":
            Tot_Temp = Tot_Temp + Array_T[Contador]
            IsANumber = IsANumber + 1
            
        Contador = Contador + 1
       
    Average = Tot_Temp/IsANumber
    strAverage = '{:.2f}'.format(Average)
    AV_Temp.set(strAverage)
    root.after(500,Average_temperature)

        
    


##   DS18B20 Example code ###






####




##### /////tk variables

counter = tkinter.DoubleVar()
Temp1 = tkinter.DoubleVar()
Temp2 = tkinter.DoubleVar()
Temp3 = tkinter.DoubleVar()
AV_Temp = tkinter.StringVar()
Humidity_Tk_Var= tkinter.StringVar()
AV_Temp.set("0.0")
TV_Max_Temp = tkinter.DoubleVar()
TV_Min_Temp = tkinter.DoubleVar()
TV_Max_Temp.set(TV_Temp_Max)
TV_Min_Temp.set(TV_Temp_Min)


## Labels ## Add Variables as text = "BLABLA" + var
Realtime_Label = ttk.Label(content, text ="Realtime Temp Sensors")
Temp1_Label = ttk.Label(content, text="Temp 1: ")
Temp1_Label_Dynamic = ttk.Label(content, textvariable= Temp1)
Temp2_Label = ttk.Label(content, text= "Temp 2 : " )
Temp2_Label_Dynamic = ttk.Label(content, textvariable= Temp2)
Temp3_Label = ttk.Label(content, text = "Temp 3: ")
Temp3_Label_Dynamic = ttk.Label(content, textvariable= Temp3)
Override_Label = ttk.Label(content, text="Override Target Values")
OV_Avg_Temp_Label = ttk.Label(content, text= "New Target Max Temp: ")
OV_Humidity_Label = ttk.Label(content, text= "New Target Min Temp: ")
RT_Label = ttk.Label(content, text="Realtime Values")
RT_Avg_Temp_Label = ttk.Label(content, text= "Avg. Temp: ")
RT_Avg_Label_Dynamic = ttk.Label(content, textvariable = AV_Temp)
RT_Humidity_Label = ttk.Label(content, text= "Humidity: ")
RT_Humidity_Label_Dynamic = ttk.Label(content, textvariable = Humidity_Tk_Var)
TV_Label = ttk.Label(content,  text="Target Values")
TV_Avg_Temp_Label = ttk.Label(content, text="Target Max Temp: ")
TV_Max_Temp_Dynamic_Label = ttk.Label(content, textvariable = TV_Max_Temp)
TV_Humidity_Label = ttk.Label(content, text="Target Min Temp: ")
TV_Min_Temp_Dynamic_Label = ttk.Label(content, textvariable = TV_Min_Temp)

## Text Entry ##
OV_Temp_Max = ttk.Entry(content)
OV_Temp_Min = ttk.Entry(content)
## Button
Submit_Button = ttk.Button(content, text="Override", command=Update_Temperature_TV)

## Mainloop
#root.geometry("1000x400")
root.title("House Garden Automation")
content.grid(column=0, row=0)
frame.grid(column=1, row=1, columnspan=2, rowspan=5)
Realtime_Label.grid(column=1,row=1, padx=10, pady=10, columnspan=2)
Temp1_Label.grid(column=1,row=2, pady=10)
Temp1_Label_Dynamic.grid(column= 2, row =2, padx=5, pady=10)
Temp2_Label.grid(column=1,row=3, padx=10, pady=10)
Temp2_Label_Dynamic.grid(column= 2, row =3,  pady=10)
Temp3_Label.grid(column=1,row=4, padx=10, pady=10)
Temp3_Label_Dynamic.grid(column= 2, row =4, pady=10)
Override_Label.grid(column=3,row=1,columnspan=2,padx=10,pady=10)
OV_Avg_Temp_Label.grid(column=3,row=2,padx=5,pady=10)
OV_Temp_Max.grid(column=4,row=2,padx=5,pady=10)
OV_Humidity_Label.grid(column=3,row=3,padx=5,pady=10)
OV_Temp_Min.grid(column=4,row=3,padx=5,pady=10)
Submit_Button.grid(column=3,row=4,padx=10,pady=10,columnspan=2)
frame_2.grid(column=3, row=1, columnspan=2, rowspan=5)
RT_Label.grid(column=5,row=1,padx=10,pady=10)
RT_Avg_Temp_Label.grid(column=5,row=2,padx=10,pady=10)
RT_Avg_Label_Dynamic.grid(column=6,row=2,padx=10,pady=10)
RT_Humidity_Label.grid(column=5,row=3,padx=10,pady=10,)
RT_Humidity_Label_Dynamic.grid(column=6,row=3,padx=10,pady=10)
frame_3.grid(column=5,row=1,rowspan=5, columnspan=2)
TV_Label.grid(column=7,row=1,padx=10,pady=10)
TV_Avg_Temp_Label.grid(column=7,row=2,padx=10,pady=10)
TV_Max_Temp_Dynamic_Label.grid(column = 8, row = 2, padx = 10, pady=10)
TV_Humidity_Label.grid(column=7,row=3,padx=10,pady=10)
TV_Min_Temp_Dynamic_Label.grid(column=8, row=3, padx=10, pady=10)
frame_4.grid(column=7,row=1,rowspan=5, columnspan= 2)
poll()
#Average_temperature()
#Humidity()

root.mainloop()
