from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname
from threading import Thread 
from queue import Queue 
from tkinter import *
import keyboard
hostname = gethostname()
host = gethostbyname(hostname)
port = 9000
def read_msg(c, chatlog):
    while True:
        msg = c.recv(1024)
        # print(msg.decode())
        # print('>')
        chatlog.insert(END, f'{msg.decode()}\n')
    c.close()

def write_msg(c,input_box):
    while True:
        msg = input()
        if msg == '!quit':
            c.close()
        c.send(msg.encode())
        input_box.delete(END)

def connect(chatlog, input_box):
    with socket(AF_INET, SOCK_STREAM) as c:
        c.connect((host, port))
        q = Queue()
        read_thread = Thread(target=read_msg, name='read', args=(c,chatlog))
        write_thread = Thread(target=write_msg, name='write',args=(c,input_box))
        read_thread.start()
        write_thread.start()
        while True:
            pass
