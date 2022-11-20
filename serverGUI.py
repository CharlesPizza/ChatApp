from tkinter import *
from tkinter import ttk 
from server import *
import socket


def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

def launch_server():
    server((ip_addr.get(), int(iport.get())), 16)
    root.destroy()


root = Tk()
root.title('Server')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#==================================== Row 1 ====================================
# IP Address /
# ----------/
ttk.Label(mainframe, text='IP Address:').grid(column=0, row=0, sticky=W)
ip_addr=ttk.Entry(mainframe,)
ip_addr.grid(column=1, row=0, padx=10, pady=5, sticky=(W))
ip_addr.insert(0, get_ip())

#==================================== Row 2 ==================================== 
# External Port /
# -------------/
ttk.Label(mainframe,text='External Port:').grid(column=0, row=1, sticky=W)
eport=ttk.Entry(mainframe,)
eport.grid(column=1, row=1,padx=10, pady=0,sticky=(W))
eport.insert(0, 9000)

#==================================== Row 3 ====================================
# Internal Port /
# -------------/
ttk.Label(mainframe,text='Internal Port:').grid(column=0, row=2, sticky=W)
iport=ttk.Entry(mainframe)
iport.grid(column=1, row=2,padx=10, pady=5,sticky=(W))
iport.insert(0, 9000)

#==================================== Row 4 ====================================
# Launch Server /
# -------------/
launch_btn = ttk.Button(mainframe,text="Launch Server", command=launch_server)
launch_btn.grid(column=0, row=3, columnspan=2,padx=5, pady=5, sticky=(W,E))


root.mainloop()