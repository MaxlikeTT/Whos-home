import tkinter as tk
from tkinter import ttk
from tkinter import *

def font_config(widget, fontslant, event):
    widget.configure(font=fontslant)

#create window
window = tk.Tk()    
window.configure(bg='pink')
window.attributes('-fullscreen',True)
window.title("Who's home?")

########
# Top Label
label = tk.Label(window, text="Current occupants", font=("swiss", 70), bg='pink', fg='white',relief = "sunken")
label2 = tk.Label(window, text="Kappa Kappa Alpha KKA", font=("swiss", 20, "italic"), bg='pink', fg='white')
label.pack()
label2.pack(pady=10, padx=100)

f = tkk.frame
f2 = tkk.frame
f.pack
f2.pack




#Canvas boxes for names
#create a canvas to put the pic on
Max=Canvas(tk, height=100, width=100, bg="white")
Max.pack(pady=20, ipady =10, ipadx = 10)
picture_file = PhotoImage(file = "C:\pics\gsdgif.gif") 
Max.create_image(100, 0, anchor=NE, image=picture_file)
Max.pack(side="left", fill="both", expand=True)


#Max.place(x=262, y=357)


# First, we create a canvas to put the picture on
Jet= Canvas(f, height=100, width=100)
picture_file = PhotoImage(file = '')
Jet.create_image(100, 0, anchor=NE, image=picture_file)
#jet.pack(side="center", fill="both", expand=True)
#Jet.place(x=265, y=118)


# First, we create a canvas to put the picture on
Bryce= Canvas(f, height=100, width=100)
picture_file = PhotoImage(file = '')
Bryce.create_image(100, 0, anchor=NE, image=picture_file)
#Bryce.pack(side="right", fill="both", expand=True)
#Bryce.place(x=435, y=118)


# First, we create a canvas to put the picture on
Tommy= Canvas(f2, height=100, width=100)
picture_file = PhotoImage(file = '') 
Tommy.create_image(100, 0, anchor=NE, image=picture_file)
#Tommy.pack(side="left", fill="both", expand=True)
#Tommy.place(x=75, y=268)


# First, we create a canvas to put the picture on
Andrew= Canvas(f2, height=100, width=100)
picture_file = PhotoImage(file = '')
#image
Andrew.create_image(100, 0, anchor=NE, image=picture_file)
#Andrew.pack(side="center", fill="both", expand=True)
#Andrew.place(x=265, y=268)


# First, we create a canvas to put the picture on
Aki= Canvas(f2, height=100, width=100)
picture_file = PhotoImage(file = '')  
Aki.create_image(100, 0, anchor=NE, image=picture_file)
#Aki.pack(side="right", fill="both", expand=True)
#Aki.place(x=435, y=268)













#####
#WRITE ABOVE THIS LINE
#####
#runs tkinter event loop, tracks button clicks, blocks any code that comes after it until the window is closed..
label.pack()
window.mainloop()
