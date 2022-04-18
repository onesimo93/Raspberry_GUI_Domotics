from cgitb import text
from tkinter import *
from tkinter import ttk
import time
##from w1thermsensor import W1ThermSensor

root = Tk()
Variable_Test = "Mira"
Null = "Null"

content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)
frame_2 = ttk.Frame(content, borderwidth=5, relief="ridge", width=275, height=300)
frame_3 = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)
frame_4 = ttk.Frame(content, borderwidth=5, relief="ridge", width=150, height=300)

## Labels ## Add Variables as text = "BLABLA" + var
Realtime_Label = ttk.Label(content, text ="Realtime Temp Sensors")
Temp1_Label = ttk.Label(content, text="Temp 1: " + Null)
Temp2_Label = ttk.Label(content, text= "Temp 2 : " + Null)
Temp3_Label = ttk.Label(content, text = "Temp 3: " + Null)
Override_Label = ttk.Label(content, text="Override Target Values")
OV_Avg_Temp_Label = ttk.Label(content, text= "New Target Avg. Temp: ")
OV_Humidity_Label = ttk.Label(content, text= "New Target Humidity: ")
RT_Label = ttk.Label(content, text="Realtime Values")
RT_Avg_Temp_Label = ttk.Label(content, text= "Avg. Temp: " + Null)
RT_Humidity_Label = ttk.Label(content, text= "Humidity: " + Null)
TV_Label = ttk.Label(content,  text="Target Values")
TV_Avg_Temp_Label = ttk.Label(content, text="Target Avg Temp: " + Null)
TV_Humidity_Label = ttk.Label(content, text="Target Humidity: " + Null)

## Text Entry ##
OV_Avg_Temp = ttk.Entry(content)
OV_Humidity = ttk.Entry(content)
## Button
Submit_Button = ttk.Button(content, text="Override")

## Mainloop
#root.geometry("1000x400")
root.title("House Garden Automation")
content.grid(column=0, row=0)
frame.grid(column=1, row=1, columnspan=1, rowspan=5)
Realtime_Label.grid(column=1,row=1, padx=10, pady=10)
Temp1_Label.grid(column=1,row=2, padx=10, pady=10)
Temp2_Label.grid(column=1,row=3, padx=10, pady=10)
Temp3_Label.grid(column=1,row=4, padx=10, pady=10)
Override_Label.grid(column=2,row=1,columnspan=2,padx=10,pady=10)
OV_Avg_Temp_Label.grid(column=2,row=2,padx=5,pady=10)
OV_Avg_Temp.grid(column=3,row=2,padx=5,pady=10)
OV_Humidity_Label.grid(column=2,row=3,padx=5,pady=10)
OV_Humidity.grid(column=3,row=3,padx=5,pady=10)
Submit_Button.grid(column=2,row=4,padx=10,pady=10,columnspan=2)
frame_2.grid(column=2, row=1, columnspan=2, rowspan=5)
RT_Label.grid(column=4,row=1,padx=10,pady=10)
RT_Avg_Temp_Label.grid(column=4,row=2,padx=10,pady=10)
RT_Humidity_Label.grid(column=4,row=3,padx=10,pady=10)
frame_3.grid(column=4,row=1,rowspan=5)
TV_Label.grid(column=5,row=1,padx=10,pady=10)
TV_Avg_Temp_Label.grid(column=5,row=2,padx=10,pady=10)
TV_Humidity_Label.grid(column=5,row=3,padx=10,pady=10)
frame_4.grid(column=5,row=1,rowspan=5)
root.mainloop()