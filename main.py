import socket
import impacket.smb3
from impacket.smbconnection import SMBConnection

def HostQuery():
    // Any Multicast host
    MCAST_HOST = "WPAD"
    // Default port 
    MCAST_PORT = 445
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 0))

    while True:
        try:   
            sock.connect((MCAST_HOST, MCAST_PORT))     
            return sock.getpeername()
        except (socket.error, socket.gaierror):
            return


def SambaConnect(user, password, password):
    response = HostQuery()
    
    if not response:
        return

    while True:
        try:
            cliend = SMBConnection(response[0], response[0], sess_port=response[1])
            cliend.login(user, password, password)
        except (impacket.smb3.SessionError, impacket.smbconnection.SessionError):
            return response

def main():
    print(SambaConnect())

main()
