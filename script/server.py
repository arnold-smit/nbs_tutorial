import socket
import pickle
import struct ## used in handling binary data stored in files or from network connections

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 8080

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    socket4client, addr = serversocket.accept()
    # create an empty binary string
    buf = b''
    # start reading from the clientbuffer until we have 4 bytes, the first 4 bytes will contain the message length
    while len(buf) < 4:
        buf += socket4client.recv(4 - len(buf))
    # get the message length by unpacking 
    length = struct.unpack('!I', buf)[0] ## ! stands for network & # stands for unsigned int (standard size is 4 bytes)
    # now that we know the length, receive length bytes into msg
    msg = socket4client.recv(length)
    # pickle this binary string into the original object
    obj = pickle.loads(msg, encoding='utf-8')
    # proceed - here simply print the object
    print(obj)
    # send a short response back to the clinet
    socket4client.send('Thanks for sending something!'.encode('utf-8'))
    # close this connection, and jump to beginning of the loop
    socket4client.close()
