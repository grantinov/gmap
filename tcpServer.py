"""
The objective for tcpServer is to ...

 Project Name: gmap
 Developed by grant.stokley
 Date:    12/01/2017
 Time:    09:14


Example usage()s):

"""

import socket
import threading

bindIp = "0.0.0.0"
bindTcpPort = 9999

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.bind((bindIp,bindTcpPort))

# set the number of connections
tcpServer.listen(5)
print("[*] Listening on %s:%d" % (bindIp, bindTcpPort))


# Start the client handling thread
def handleClient(clientSocket):
    # print out what the client sends
    request = clientSocket.recv(1024)
    print("[*] Received")