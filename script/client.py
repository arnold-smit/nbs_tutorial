import socket
import pickle
import struct

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 8080

# connection to hostname on the port.
clientsocket.connect((host, port))

# send an object
my_obj = {'one':[1], 'two':[1,2], 'three':[1,2,3], 'four':[1,2,3,4]}
packet = pickle.dumps(my_obj) ## note dumps converts the object to a binary string, so no need to encode
length = struct.pack('!I', len(packet))
packet = length + packet
clientsocket.send(packet)

# receive a short reply & print it
msg = clientsocket.recv(1024).decode('utf-8')
print(msg)

# close the clientsocket and 
clientsocket.close()
