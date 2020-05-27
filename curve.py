from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
	
temperature = []
volt = []
percentage = []
capacity = []
charge = []
time = []

window = Tk()
frame = Frame(window).pack()

text = StringVar()
text.set("")
label= Label(frame, textvariable=text,bg="white", fg="black").place(x = 200, y = 15)
def buttonCallBack():
	name = filedialog.askopenfilename(initialdir=os.getcwd())
	text.set(name)
	read_file(name)
	

    

def draw_main_window():
    window_width = 800
    window_height = 600 
    

    window.title('Plot App') #Title
    window.geometry('800x600') #Size
    window.configure(background='white') # bg color
    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


    text = Label(frame, text="Select file",bg="white", fg="black").place(x = 100, y = 15)

    button = Button(frame, text ="Loadfile", command = buttonCallBack).place(x = 400, y = 10)

    window.mainloop()


def read_file(filename):
	with open(filename,'r') as fp:
            all_lines = fp.readlines()

	for line in all_lines:
		t, v, p, c, ch = line.split(' ')
		temperature.append(float(t))
		volt.append(float(v))
		percentage.append(float(p))
		capacity.append(float(c))
		charge.append(int(ch))

	for i in range(0, len(volt)):
		time.append(i)
	
	fig = Figure(figsize=(6, 5), dpi=100)
	fig.add_subplot(111).plot(time, volt)

	canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
	canvas.draw()
	canvas.get_tk_widget().place(x = 80, y = 50)

	toolbar = NavigationToolbar2Tk(canvas, window)
	toolbar.update()
	canvas.get_tk_widget().place(x = 80, y = 50)

draw_main_window()
