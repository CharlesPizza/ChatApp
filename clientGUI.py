from threading import Thread
from tkinter import *
from tkinter import ttk 
import socket
import client

def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip
def chatlog_frame():
    launch_frame.destroy()
    width=800
    height=600
    root.geometry(f'{width}x{height}')
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0)
    input_frame = ttk.Frame(root)
    input_frame.grid(column=0, row=1)
    #====================================ChatBox====================================
    # scrollbar = Scrollbar(mainframe)
    # scrollbar.pack(side=RIGHT, fill=Y)
    chatlog = Text(mainframe, bg='white')
    chatlog.grid(column=0, row=0, columnspan=5, rowspan=3)
    #====================================SendMSG====================================
    input_box = ttk.Entry(input_frame, width=100)
    input_box.grid(column=0, row=1, padx=10,pady=10)
    conn_thread = Thread(target=lambda:client.connect(chatlog, input_box), name='connection')
    conn_thread.start()


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
launch_btn = ttk.Button(launch_frame,text="Connect to Server",
    command=lambda:chatlog_frame())
launch_btn.grid(column=0, row=3, columnspan=2,padx=5, pady=5, sticky=(W,E))






root.mainloop()