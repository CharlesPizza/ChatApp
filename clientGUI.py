from tkinter import *
from tkinter import ttk 
import socket
import client

def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

width = 250
height = 125
root = Tk()
root.title('Client Launch')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry(f'{width}x{height}')
launch_frame = ttk.Frame(root)
launch_frame.grid(column=0, row=0)
#==================================== Row 1 ====================================
# IP Address /
# ----------/
ttk.Label(launch_frame, text='IP Address:').grid(column=0, row=0, sticky=W)
ip_addr=ttk.Entry(launch_frame,)
ip_addr.grid(column=1, row=0, padx=10, pady=(5,0), sticky=(W,S))
ip_addr.insert(0, get_ip())

#==================================== Row 2 ==================================== 
# Port /
# ----/
ttk.Label(launch_frame,text='External Port:').grid(column=0, row=1, sticky=W)
eport=ttk.Entry(launch_frame,)
eport.grid(column=1, row=1,padx=10, pady=5,sticky=(W))
eport.insert(0, 9000)

#==================================== Row 3 ====================================
# Get Username  /
# -------------/
ttk.Label(launch_frame,text='Username:').grid(column=0, row=2, sticky=W)
username=ttk.Entry(launch_frame,)
username.grid(column=1, row=2,padx=10, pady=0,sticky=(W))
username.insert(0,str(socket.gethostname()))

#==================================== Row 4 ====================================
# Launch Server /
# -------------/
launch_btn = ttk.Button(launch_frame,text="Launch Server", command=client.connect)
launch_btn.grid(column=0, row=3, columnspan=2,padx=5, pady=5, sticky=(W,E))



if not launch_frame:
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0)
    input_frame = ttk.Frame(root)
    input_frame.grid(column=0, row=1)
    #====================================ChatBox====================================
    scrollbar = Scrollbar(mainframe)
    scrollbar.pack(side=RIGHT, fill=Y)

    #====================================SendMSG====================================
    input_box = ttk.Entry(input_frame, width=100)
    input_box.grid(column=0, row=1, padx=10,pady=10)


root.mainloop()