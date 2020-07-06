# Program: Python Package Assignment
# Author: Skyler Brown
# Date: 06/27/2020
import tkinter
m = tkinter.Tk() # where m is the name of the main window object

m.mainloop()  # infinite loop that waits for events to happen
m.title('Favorite Meal')
button = tkinter.Button(m, text='Stop', width=25, command=m.destroy)
button.pack()
m.title('Major Decision')
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2).grid(row=1)
button = tkinter.Button(m, text='Choose', width=25, command=m.destroy)
button.grid(row=3)


def on_button_click():
    label.config(text="Nice choice")

m = tkinter.Tk() # where m is the name of the main window object
m.title('Major Decision')
label = tkinter.Label(m, text="No Selection Made")
label.grid(row=4)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="CIS", variable=var1).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="BIS", variable=var2).grid(row=1)
button = tkinter.Button(m, text='Choose', width=25, command=on_button_click)
button.grid(row=3)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)
m.mainloop()  # infinite loop that waits for events to happen

def pick_cis():
    label.config(text="Nice choice")

def pick_bis():
    label.config(text="Are you sure?")

m = tkinter.Tk() # where m is the name of the main window object
m.title('Major Decision')
label = tkinter.Label(m, text="No Selection Made")
label.grid(row=4)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="CIS", variable=var1, command=pick_cis).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="BIS", variable=var2, command=pick_bis).grid(row=1)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)
m.mainloop()  # infinite loop that waits for events to happen

