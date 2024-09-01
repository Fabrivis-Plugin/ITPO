# Refresh.py
import socket

def connectionLabel(connection, label):
    if connection:
        label.configure(text_color="green")
    else:
        label.configure(text_color="red")


def refreshConnection(HOSTS, labels):
    print("Refreshing connection...")
    
    for i, (host, port) in enumerate(HOSTS):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((host, port))
            s.close()

            connectionLabel(True, labels[i])
        
        except:
            connectionLabel(False, labels[i])
