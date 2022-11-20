from tkinter import *
from tkinter import ttk 
import socket


root = Tk()
root.title('Client Launch')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
input_frame = ttk.Frame(root)
input_frame.grid(column=0, row=1)
#====================================ChatBox====================================
scrollbar = Scrollbar(mainframe)
scrollbar.pack(side=RIGHT, fill=Y)

#====================================SendMSG====================================
input_box = ttk.Entry(input_frame, width=100)
input_box.grid(column=0, row=1, padx=10,pady=10)

root.mainloop()