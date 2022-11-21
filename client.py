from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname
from threading import Thread 
from queue import Queue 

hostname = gethostname()
host = gethostbyname(hostname)
port = 9000
def read_msg(c):
    while True:
        msg = c.recv(1024)
        print(msg.decode())
        print('>')
    c.close()

def write_msg(c):
    while True:
        msg = input('>')
        if msg == '!quit':
            c.close()
        c.send(msg.encode())

def connect():
    with socket(AF_INET, SOCK_STREAM) as c:
        c.connect((host, port))
        q = Queue()
        read_thread = Thread(target=read_msg, name='read', args=(c,))
        write_thread = Thread(target=write_msg, name='write',args=(c,))
        read_thread.start()
        write_thread.start()
        while True:
            pass