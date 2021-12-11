from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot():
    global plot_frame
    plot_frame.pack_forget()
    plot_frame.destroy()
    plot_frame = Frame(window)
    plot_frame.pack()
    fig = Figure(figsize=(5, 5), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    s2 = "x=np.linspace(" + minvalue.get() + "," + maxvalue.get() + ", 100)\n"
    s3 = "y=" + function.get().replace("^", "**")
    s4 = '''
plot1 = fig.add_subplot(111)
plot1.plot(x,y, 'g')
canvas.draw()
canvas.get_tk_widget().pack()
'''
    try:
        exec(s2 + s3 + s4)
    except:
        tkinter.messagebox.showwarning("error", "invalid input")


window = Tk()
window.title('Function Plotter')
window.geometry("500x500")
function = StringVar()
minvalue = StringVar()
maxvalue = StringVar()
function_frame = Frame(window)
function_frame.pack()
function_label = Label(function_frame, text="write a function of x (supported operators are + - / * ^)           ")
function_label.pack(side=LEFT)
function_entry = Entry(function_frame, textvariable=function)
function_entry.pack()
min_frame = Frame(window)
min_frame.pack()
min_label = Label(min_frame,
                  text="write a min value of x                                                                      ")
min_label.pack(side=LEFT)
min_entry = Entry(min_frame, textvariable=minvalue)
min_entry.pack()
max_frame = Frame(window)
max_frame.pack()
max_label = Label(max_frame,
                  text="write a max value of x                                                                      ")
max_label.pack(side=LEFT)
max_entry = Entry(max_frame, textvariable=maxvalue)
max_entry.pack()
plot_button = Button(master=window, command=plot, height=2, width=10, text="Plot")
plot_button.pack()
plot_frame = Frame(window)
plot_frame.pack()
window.mainloop()
