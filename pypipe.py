# imports
import tkinter as tk
from tkinter import messagebox
from datetime import datetime



# home
class Win:
    def __init__(self, root):
        # home geometry
        self.root = root
        self.root.geometry("250x370")
        self.root.configure(background='gray99')
        self.root.resizable(0, 0)
# selection information label
        self.selectionLabel = tk.Label(
            self.root, bg='gray99', text='Select the material of the pipe:', padx=10, pady=15).pack()
# cast iron selection
        self.materialCastIron = tk.Button(self.root, overrelief="raised", relief="groove", width=22, padx=10, pady=25, text="Cast Iron",
                                          command=lambda: self.new_window(castIron)).pack(padx=10, pady=10)
# ductile iron selection
        self.materialDuctileIron = tk.Button(self.root, overrelief="raised", relief="groove", width=22, padx=10, pady=25, text="Ductile Iron",
                                             command=lambda: self.new_window(ductileIron)).pack(padx=10, pady=10)
# HDPPE selection
        self.materialHdpe = tk.Button(self.root, overrelief="raised", relief="groove", width=22, padx=10, pady=25, text="HDPE",
                                       command=lambda: self.new_window(Hdpe)).pack(padx=10, pady=10)

        self.infoLabel = tk.Label(self.root, bg='gray99', text="Developed for the use of Thames Water\nInformed by WN37", fg='gray65').pack()


# validation - only allow one window at a time
    def new_window(self, _class):
        try:
            if self.new.state() == "normal":
                self.new.focus()
        except:
            self.new = tk.Toplevel(self.root)
            _class(self.new)


### class for cast iron ###
class castIron:
    def __init__(self, root):
        # cast iron geometry
        self.root = root
        self.root.title("PyPipe - Cast Iron")
        self.root.geometry("300x570")
        self.root.configure(background='gray99')
        self.root.resizable(0, 0)
# message boxes for formulas
        def ShowVolume():
            tk.messagebox.showinfo('Formula', '3.14 * Radius ^ 2 * Length / 1000')
        def ShowTwiceCapacity():
            tk.messagebox.showinfo('Formula', 'Volume * 2')
        def ShowVelocity():
            tk.messagebox.showinfo('Formula','Area = Radius ^ 2 * 3.14\nFlow Rate = Area / 1000 * Velocity')
        def ShowTime():
            tk.messagebox.showinfo('Formula', 'Twice Capacity / Flow Rate')
# calculation button
        def convert():
            Diameter = diameterVariable.get()
            if Diameter == 3:
                Diameter = 80
            if Diameter == 4:
                Diameter = 106
            if Diameter == 5:
                Diameter = 133
            if Diameter == 6:
                Diameter = 158
            if Diameter == 7:
                Diameter = 185
            if Diameter == 8:
                Diameter = 210
            if Diameter == 9:
                Diameter = 236
            if Diameter == 10:
                Diameter = 262
            if Diameter == 12:
                Diameter = 319
            if Diameter == 14:
                Diameter = 371
            if Diameter == 15:
                Diameter = 397
            if Diameter == 16:
                Diameter = 423
            Radius = Diameter/2
            Length = lengthVariable.get()
            Velocity = velocityVariable.get()
            Velocity = float(Velocity)
            volumeResult.set(round(3.14 * pow(Radius, 2) * Length/1000))
            twiceResult.set(round(3.14 * pow(Radius, 2) * Length/1000 * 2))
            try:
                Area = round(pow(Radius, 2) * 3.14)
                velocityResult.set(round(Area / 1000 * Velocity))
                timeResult.set(round(twiceResult.get() // (velocityResult.get() * 60)))
            except ZeroDivisionError:
                volumeResult.set('0')
                twiceResult.set('0')
                Area = '0'
                velocityResult.set('0')

# validation for entry field
        def validate_input(new_value):
            valid = (new_value .isdigit() and len(
                new_value) <= 3) or new_value == ''
            return valid
# validate variable to call on in entry field
        validate = root.register(validate_input)

# write to notepad
        def writefile():
            if twiceResult.get() == 0:
                tk.messagebox.showinfo("Error", "There are no values to be saved.")
            else:
                now = datetime.now()
                date_time = now.strftime("[%d/%m/%Y - %H:%M]")
                with open ('FlushingDiary.txt', 'a') as af:
                    af.write(f"{date_time} {twiceResult.get()} litres flushed at {velocityResult.get()} L/S, for a total of {timeResult.get()} minutes\n")

# cast iron variables
# diameter
        diameterVariable = tk.IntVar(root)
        diameterVariable.set("0")
        diameterLabel = tk.Label(root, pady=15,
                                 text="Set the diameter (INCH)", bg='gray99')
        diameterDropdown = tk.OptionMenu(root, diameterVariable,
                                         3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16)
        diameterLabel.pack()
        diameterDropdown.pack()
# length
        lengthVariable = tk.IntVar(root)
        lengthLabel = tk.Label(root, pady=15,
                               text="Set the length of the isolated section (METRE):", bg='gray99')
        lengthEntry = tk.Entry(root, textvariable=lengthVariable,
                               validate='key', validatecommand=(validate, '%P'), width=6, relief="groove")
        lengthLabel.pack()
        lengthEntry.pack()
# velocity entry
        velocityVariable = tk.StringVar(root)
        velocityVariable.set("0")
        velocityLabel = tk.Label(root, pady=10,
                                 text="Set the velocity (METRES/SECOND)", bg='gray99')
        velocityDropdown = tk.OptionMenu(root, velocityVariable,
                                         0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3)
        spacer1 = tk.Label(root, pady=2, bg='gray99')
        velocityLabel.pack()
        velocityDropdown.pack()
        spacer1.pack()
# convert button
        button = tk.Button(root, command=convert, text='Calculate', pady=5, width=15, overrelief="raised", relief="groove")
        spacer2 = tk.Label(root, pady=5, bg='gray99')
        button.pack()
        spacer2.pack()
# volume
        volumeInfo = tk.Button(root, relief='flat', command=ShowVolume, text="Volume of section (LITRE):", bg='gray99', pady=5)
        volumeResult = tk.IntVar(root)
        volumeResult.set('0')
        volumeLabel = tk.Label(root, textvariable=volumeResult, bg='gray99', fg='darkred')
        volumeInfo.pack()
        volumeLabel.pack()
# twice capacity
        twiceInfo = tk.Button(root, relief='flat', command=ShowTwiceCapacity, text="Twice capacity of section (LITRE):", bg='gray99')
        twiceResult = tk.IntVar(root)
        twiceResult.set('0')
        twiceLabel = tk.Label(root, textvariable=twiceResult, bg='gray99', fg='darkred')
        twiceInfo.pack()
        twiceLabel.pack()
# velocity
        velocityInfo = tk.Button(root, relief='flat', command=ShowVelocity, text="Flow (LITRES/SECONDS)", bg='gray99')
        velocityResult = tk.IntVar(root)
        velocityResult.set('0')
        velocityResultlabel = tk.Label(root, textvariable=velocityResult, bg='gray99', fg='darkred')
        velocityInfo.pack()
        velocityResultlabel.pack()
# time
        timeInfo = tk.Button(root, relief='flat', command=ShowTime, text="Time to flush (MINUTES)", bg='gray99')
        timeResult = tk.IntVar(root)
        timeResult.set('0')
        timeResultlabel = tk.Label(root, textvariable=timeResult, bg='gray99', fg='darkred')
        spacer3 = tk.Label(root, pady=5, bg='gray99')
        timeInfo.pack()
        timeResultlabel.pack()
        spacer3.pack()
# save
        saveButton = tk.Button(root, text='Save Results', command=writefile, width=15, overrelief="raised", relief="groove")
        saveButton.pack()
### class for ductile iron ###
class ductileIron:
    def __init__(self, root):
        # ductile iron geometry
        self.root = root
        self.root.title("PyPipe - Ductile Iron")
        self.root.geometry("300x570")
        self.root.configure(background='gray99')
        self.root.resizable(0, 0)
        self.root.option_add("*font", "calibri 10")
# message boxes for formulas
        def ShowVolume():
            tk.messagebox.showinfo('Formula', '3.14 * Radius ^ 2 * Length / 1000')
        def ShowTwiceCapacity():
            tk.messagebox.showinfo('Formula', 'Volume * 2')
        def ShowVelocity():
            tk.messagebox.showinfo('Formula','Area = Radius ^ 2 * 3.14\nFlow Rate = Area / 1000 * Velocity')
        def ShowTime():
            tk.messagebox.showinfo('Formula', 'Twice Capacity / Flow Rate')
# calculation button
        def convert():
            Diameter = diameterVariable.get()
            if Diameter == 80:
                Diameter = 86
            if Diameter == 100:
                Diameter = 96
            if Diameter == 150:
                Diameter = 147
            if Diameter == 200:
                Diameter = 199
            if Diameter == 250:
                Diameter = 250
            if Diameter == 300:
                Diameter = 302
            if Diameter == 350:
                Diameter = 350
            if Diameter == 400:
                Diameter = 403
            if Diameter == 450:
                Diameter = 453

            Radius = Diameter/2
            Length = lengthVariable.get()
            Velocity = velocityVariable.get()
            Velocity = float(Velocity)
            volumeResult.set(round(3.14 * pow(Radius, 2) * Length/1000))
            twiceResult.set(round(3.14 * pow(Radius, 2) * Length/1000 * 2))
            try:
                Area = round(pow(Radius, 2) * 3.14)
                velocityResult.set(round(Area / 1000 * Velocity))
                timeResult.set(round(twiceResult.get() // (velocityResult.get() * 60)))

            except ZeroDivisionError:
                volumeResult.set('0')
                twiceResult.set('0')
                Area = '0'
                velocityResult.set('0')
# validation for entry field
        def validate_input(new_value):
            valid = (new_value .isdigit() and len(
                new_value) <= 3) or new_value == ''
            return valid
# validate variable to call on in entry field
        validate = root.register(validate_input)

# write to notepad
        def writefile():
            if twiceResult.get() == 0:
                tk.messagebox.showinfo("Error", "There are no values to be saved.")
            else:
                now = datetime.now()
                date_time = now.strftime("[%d/%m/%Y - %H:%M]")
                with open ('FlushingDiary.txt', 'a') as af:
                    af.write(f"{date_time} {twiceResult.get()} litres flushed at {velocityResult.get()} L/S, for a total of {timeResult.get()} minutes\n")

# ductile iron variables
# diameter
        diameterVariable = tk.IntVar(root)
        diameterVariable.set("0")
        diameterLabel = tk.Label(root, pady=15,
                                 text="Set the diameter (MM)", bg='gray99')
        diameterDropdown = tk.OptionMenu(root, diameterVariable,
                                         80, 100, 150, 200, 250, 300, 350, 400, 450)
        diameterLabel.pack()
        diameterDropdown.pack()
# length
        lengthVariable = tk.IntVar(root)
        lengthLabel = tk.Label(root, pady=15,
                               text="Set the length of the isolated section (METRE):", bg='gray99')
        lengthEntry = tk.Entry(root, textvariable=lengthVariable,
                               validate='key', validatecommand=(validate, '%P'), width=6, relief="groove")
        lengthLabel.pack()
        lengthEntry.pack()
# velocity entry
        velocityVariable = tk.StringVar(root)
        velocityVariable.set("0")
        velocityLabel = tk.Label(root, pady=10,
                                 text="Set the velocity required (METRES/SECOND)", bg='gray99')
        velocityDropdown = tk.OptionMenu(root, velocityVariable,
                                         0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3)
        spacer1 = tk.Label(root, pady=2, bg='gray99')
        velocityLabel.pack()
        velocityDropdown.pack()
        spacer1.pack()
# convert button
        button = tk.Button(root, command=convert, text='Calculate', pady=5, width=15, overrelief="raised", relief="groove")
        spacer2 = tk.Label(root, pady=5, bg='gray99')
        button.pack()
        spacer2.pack()
# volume
        volumeInfo = tk.Button(root, relief='flat', command=ShowVolume, text="Volume of section (LITRE):", bg='gray99', pady=5)
        volumeResult = tk.IntVar(root)
        volumeResult.set('0')
        volumeLabel = tk.Label(root, textvariable=volumeResult, bg='gray99', fg='darkred')
        volumeInfo.pack()
        volumeLabel.pack()
# twice capacity
        twiceInfo = tk.Button(root, relief='flat', command=ShowTwiceCapacity, text="Twice capacity of section (LITRE):", bg='gray99')
        twiceResult = tk.IntVar(root)
        twiceResult.set('0')
        twiceLabel = tk.Label(root, textvariable=twiceResult, bg='gray99', fg='darkred')
        twiceInfo.pack()
        twiceLabel.pack()
# velocity
        velocityInfo = tk.Button(root, relief='flat', command=ShowVelocity, text="Flow (LITRES/SECONDS)", bg='gray99')
        velocityResult = tk.IntVar(root)
        velocityResult.set('0')
        velocityResultlabel = tk.Label(root, textvariable=velocityResult, bg='gray99', fg='darkred')
        velocityInfo.pack()
        velocityResultlabel.pack()
# time
        timeInfo = tk.Button(root, relief='flat', command=ShowTime, text="Time to flush (MINUTES)", bg='gray99')
        timeResult = tk.IntVar(root)
        timeResult.set('0')
        timeResultlabel = tk.Label(root, textvariable=timeResult, bg='gray99', fg='darkred')
        spacer3 = tk.Label(root, pady=5, bg='gray99')
        timeInfo.pack()
        timeResultlabel.pack()
        spacer3.pack()
# save
        saveButton = tk.Button(root, text='Save Results', command=writefile, width=15, overrelief="raised", relief="groove")
        saveButton.pack()
### class for hdpe ##
class Hdpe:
    def __init__(self, root):
        # hdpe geometry
        self.root = root
        self.root.title("PyPipe - HDPE")
        self.root.geometry("300x570")
        self.root.configure(background='gray99')
        self.root.resizable(0, 0)
        self.root.option_add("*font", "calibri 10")
# message boxes for formulas
        def ShowVolume():
            tk.messagebox.showinfo('Formula', '3.14 * Radius ^ 2 * Length / 1000')
        def ShowTwiceCapacity():
            tk.messagebox.showinfo('Formula', 'Volume * 2')
        def ShowVelocity():
            tk.messagebox.showinfo('Formula','Area = Radius ^ 2 * 3.14\nFlow Rate = Area / 1000 * Velocity')
        def ShowTime():
            tk.messagebox.showinfo('Formula', 'Twice Capacity / Flow Rate')
# calculation button
        def convert():
            Diameter = diameterVariable.get()
            if Diameter == 90:
                Diameter = 73.6
            if Diameter == 125:
                Diameter = 102.2
            if Diameter == 180:
                Diameter = 147.2
            if Diameter == 250:
                Diameter = 204.4
            if Diameter == 315:
                Diameter = 257.8
            if Diameter == 355:
                Diameter = 290.4
            if Diameter == 400:
                Diameter = 327.2
            if Diameter == 450:
                Diameter = 368.2
            if Diameter == 500:
                Diameter = 409
            Radius = Diameter/2
            Length = lengthVariable.get()
            Velocity = velocityVariable.get()
            Velocity = float(Velocity)
            volumeResult.set(round(3.14 * pow(Radius, 2) * Length/1000))
            twiceResult.set(round(3.14 * pow(Radius, 2) * Length/1000 * 2))
            try:
                Area = round(pow(Radius, 2) * 3.14)
                velocityResult.set(round(Area / 1000 * Velocity))
                timeResult.set(round(twiceResult.get() // (velocityResult.get() * 60)))
            except ZeroDivisionError:
                volumeResult.set('0')
                twiceResult.set('0')
                Area = '0'
                velocityResult.set('0')
            #volumeResult =
# validation for entry field
        def validate_input(new_value):
            valid = (new_value .isdigit() and len(
                new_value) <= 3) or new_value == ''
            return valid
# validate variable to call on in entry field
        validate = root.register(validate_input)

# write to notepad
        def writefile():
            if twiceResult.get() == 0:
                tk.messagebox.showinfo("Error", "There are no values to be saved.")
            else:
                now = datetime.now()
                date_time = now.strftime("[%d/%m/%Y - %H:%M]")
                with open ('FlushingDiary.txt', 'a') as af:
                    af.write(f"{date_time} {twiceResult.get()} litres flushed at {velocityResult.get()} L/S, for a total of {timeResult.get()} minutes\n")
# hdpe variables
# diameter
        diameterVariable = tk.IntVar(root)
        diameterVariable.set("0")
        diameterLabel = tk.Label(root, pady=15,
                                 text="Set the diameter (MM)", bg='gray99')
        diameterDropdown = tk.OptionMenu(root, diameterVariable,
                                         90, 125, 180, 250, 315, 355, 400, 450, 500)
        diameterLabel.pack()
        diameterDropdown.pack()
# length
        lengthVariable = tk.IntVar(root)
        lengthLabel = tk.Label(root, pady=15,
                               text="Set the length (METRE):", bg='gray99')
        lengthEntry = tk.Entry(root, textvariable=lengthVariable,
                               validate='key', validatecommand=(validate, '%P'), width=6, relief="groove")
        lengthLabel.pack()
        lengthEntry.pack()
# velocity entry
        velocityVariable = tk.StringVar(root)
        velocityVariable.set("0")
        velocityLabel = tk.Label(root, pady=10,
                                 text="Set the velocity (METRE/SEC)", bg='gray99')
        velocityDropdown = tk.OptionMenu(root, velocityVariable,
                                         0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3)
        spacer1 = tk.Label(root, pady=2, bg='gray99')
        velocityLabel.pack()
        velocityDropdown.pack()
        spacer1.pack()
# convert button
        button = tk.Button(root, command=convert, text='Calculate', pady=5, width=15, overrelief="raised", relief="groove")
        spacer2 = tk.Label(root, pady=5, bg='gray99')
        button.pack()
        spacer2.pack()
# volume
        volumeInfo = tk.Button(root, relief='flat', command=ShowVolume, text="Volume of section (LITRE):", bg='gray99', pady=5)
        volumeResult = tk.IntVar(root)
        volumeResult.set('0')
        volumeLabel = tk.Label(root, textvariable=volumeResult, bg='gray99', fg='darkred')
        volumeInfo.pack()
        volumeLabel.pack()
# twice capacity
        twiceInfo = tk.Button(root, relief='flat', command=ShowTwiceCapacity, text="Twice capacity of section (LITRE):", bg='gray99')
        twiceResult = tk.IntVar(root)
        twiceResult.set('0')
        twiceLabel = tk.Label(root, textvariable=twiceResult, bg='gray99', fg='darkred')
        twiceInfo.pack()
        twiceLabel.pack()
# velocity
        velocityInfo = tk.Button(root, relief='flat', command=ShowVelocity, text="Flow (LITRES/SECONDS)", bg='gray99')
        velocityResult = tk.IntVar(root)
        velocityResult.set('0')
        velocityResultlabel = tk.Label(root, textvariable=velocityResult, bg='gray99', fg='darkred')
        velocityInfo.pack()
        velocityResultlabel.pack()
# time
        timeInfo = tk.Button(root, relief='flat', command=ShowTime, text="Time to flush (MINUTES)", bg='gray99')
        timeResult = tk.IntVar(root)
        timeResult.set('0')
        timeResultlabel = tk.Label(root, textvariable=timeResult, bg='gray99', fg='darkred')
        spacer3 = tk.Label(root, pady=5, bg='gray99')
        timeInfo.pack()
        timeResultlabel.pack()
        spacer3.pack()
# save
        saveButton = tk.Button(root, text='Save Results', command=writefile, width=15, overrelief="raised", relief="groove")
        saveButton.pack()

# close loop and execute from __main__
if __name__ == "__main__":
    root = tk.Tk()
    app = Win(root)
    app.root.title("PyPipe v1.3")
    root.mainloop()
