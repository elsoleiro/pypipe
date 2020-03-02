#!/usr/bin/env python
# coding: utf-8



# imports
from tkinter import *
import math
from datetime import datetime

# validate input keystrokes
def validate_input(new_value):
    valid = (new_value .isdigit() and len(new_value) <= 3) or new_value == ''
    return valid

# conversion function formulas
def convert():

    Diameter = EntryDiameter.get()
    Length = EntryLength.get() 
    Radius = Diameter / 2
    
    VolumeResult.set(round(3.14 * pow(Radius, 2) * Length / 1000)) 
    VolumeResult2.set(round(3.14 * pow(Radius, 2) * Length / 1000 * 2))
    
    Area = round(pow(Radius, 2) * 3.14)
    
# try and except for dividing by zero
    try:
        SoftFlush.set(round(Area / 1000 * 0.5 * 60))
        SoftFlushTime.set(round(VolumeResult2.get() / SoftFlush.get()))
        FullFlush.set(round(Area / 1000 * 0.8 * 60))
        FullFlushTime.set(round(VolumeResult2.get() / FullFlush.get()))
        
    except ZeroDivisionError:
        VolumeResult.set('0') 
        VolumeResult2.set('0')
        SoftFlush.set('0')
        SoftFlushTime.set('0')
        FullFlush.set('0')
        FullFlushTime.set('0')
        Area = '0'
        Radius = '0'

# date time
now = datetime.now()
date_time = now.strftime("[%d/%m/%Y - %H:%M]")

#create & append textfiles - soft flush & full flush
def writefile_Soft():
    
    with open ('FlushingDiary.txt', 'a') as af:
        af.write(f"{date_time} {VolumeResult2.get()} litres flushed at {SoftFlush.get()} L/PM, for a total of {SoftFlushTime.get()} minutes\n")
           
def writefile_Full():
    
    with open ('FlushingDiary.txt', 'a') as af:
            af.write(f"{date_time} {VolumeResult2.get()} litres flushed at {FullFlush.get()} L/PM, for a total of {FullFlushTime.get()} minutes\n")

# tkinter setup
root = Tk()
root.geometry("350x280")
root.configure(background='gray99')
root.title("PyPipe")
root.resizable(0, 0)
validate = root.register(validate_input)

# defining variable types and assigning default labels
VolumeResult = IntVar()
VolumeResult.set('0')

# twice capacity
VolumeResult2 = IntVar()
VolumeResult2.set('0')

# 0.5m/s flush
SoftFlush = IntVar()
SoftFlush.set('0')

# time to flush at 0.5m/s
SoftFlushTime = IntVar()
SoftFlushTime.set('0')

# 0.8m/s flush
FullFlush = IntVar()
FullFlush.set('0')

# time to flush at 0.8m/s
FullFlushTime = IntVar()
FullFlushTime.set('0')

# inputs fields
EntryLength = IntVar()
EntryDiameter = IntVar()

# entry boxes
EnterDiameter = Entry(root, relief='sunken', validate="key", validatecommand=(validate, "%P"), width=4, borderwidth=1, textvariable = EntryDiameter, font=('lucida 9 bold'), bg='grey95', fg="firebrick3").place(x=160, y=10)
EnterLength = Entry(root, relief='sunken', validate="key", validatecommand=(validate, "%P"), width=4, borderwidth=1, textvariable = EntryLength, font=('lucida 9 bold'), bg='grey95', fg="firebrick3").place(x=160, y=35)

# buttons, conversion and saves
Button1 = Button(root, relief='groove', width=22, text = "Convert", bg="deepskyblue", font=('lucida 9 bold'), fg="black", command=convert).place(x=95, y=70)
Button2 = Button(root, relief='groove', width=22, text = "Save Soft Flush", bg="deepskyblue", font=('lucida 9 bold'), fg="black", command=writefile_Soft).place(x=10, y=210)
Button3 = Button(root, relief='groove', width=22, text = "Save Full Flush", bg="deepskyblue", font=('lucida 9 bold'), fg="black", command=writefile_Full).place(x=180, y=210)

# labels for results
ResultVolume = Label(root, textvariable=VolumeResult, font=('lucida 9 bold'), bg='gray99', fg="firebrick3").place(x=105, y=110)
ResultVolume2 = Label(root, textvariable=VolumeResult2, font=('lucida 9 bold'), bg='gray99', fg="firebrick3").place(x=105, y=130)
ResultSoftFlush = Label(root, textvariable=SoftFlush, font=('lucida 9 bold'), bg='gray99', fg="firebrick3").place(x=105, y=150)
ResultSoftFlushTime = Label(root,  textvariable=SoftFlushTime, font=('lucida 9 bold'), bg='gray99', fg="firebrick3").place(x=265, y=150)
ResultFullFlush = Label(root, textvariable = FullFlush, font=('lucida 9 bold'), bg='gray99', fg="firebrick3").place(x=105, y=170)
ResultFullFlushTime = Label(root, textvariable = FullFlushTime, font=('lucida 9 bold'), bg='gray99', fg="firebrick3").place(x=265, y=170)

# labels for inputs
DiameterLabel =  Label(root, text="Outer Diameter:", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=60, y=10)
MillimetersLabel = Label(root, text="mm", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=198, y=10)
LengthLabel= Label(root, text="Length:", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=105, y=35)
MetersLabel = Label(root, text="meters", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=198, y=35)

# labels for outputs
VolumeLabel = Label(root, text="Volume:", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=48, y=110)
VolumeLitres = Label(root, text="litres", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=150,y=110)
TwiceCapacity = Label(root, text="Twice Capacity:", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=10, y=130)
TwiceCapacityLitres = Label(root, text="litres", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=150,y=130)
SoftFlushLabel = Label(root, text="Soft Flush:", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=38, y=150)
SoftFlushLPM = Label(root, text="litres per minute, for", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=145, y=150)
SoftFlushMinutes = Label(root, text="minutes", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=282,y=150)
FullFlushLabel = Label(root, text="Full Flush:", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=38, y=170)
FullFlushLPM = Label(root, text="litres per minute, for", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=145, y=170)
FullFlushMinutes = Label(root, text="minutes", font=('lucida 9 bold'), bg='gray99', fg="black").place(x=282, y=170)

# footer
myLabel = Label(root, text="Developed for the use of Network Service Technicians at Thames Water Utilities", font=('lucida 9 bold', 7), bg='gray99', fg="gray60").place(x=1, y=260)

# eof
root.mainloop()




