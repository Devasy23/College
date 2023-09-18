# # first of all import the socket library
# import socket			

# # next create a socket object
# s = socket.socket()		
# print ("Socket successfully created")

# # reserve a port on your computer in our
# # case it is 12345 but it can be anything
# port = 50000			

# # Next bind to the port
# # we have not typed any ip in the ip field
# # instead we have inputted an empty string
# # this makes the server listen to requests
# # coming from other computers on the network
# s.bind(('', port))		
# print ("socket binded to %s" %(port))

# # put the socket into listening mode
# s.listen(5)	
# print ("socket is listening")		

# # a forever loop until we interrupt it or
# # an error occurs
# while True:

#     # Establish connection with client.
#     c, addr = s.accept()	
#     print ('Got connection from', addr )

#     # send a thank you message to the client. encoding to send byte type.
#     c.send('Thank you for connecting'.encode())

#     # Close the connection with the client
#     c.close()

#     # Breaking once connection closed
#     break



# Now multi threaded client 
import socket
import sys
cs= socket.socket()
host = '127.0.0.1'
port = 50000
try: 
    cs.connect((host, port))
    print("Connected to server")
except:
    print("Connection to server failed")
    sys.exit()
response = cs.recv(1024).decode()
print(response)
while True:
    print("Enter message to send to server")
    message = input()
    cs.send(message.encode())
    data = cs.recv(1024).decode()
    print("Server says: ", data)
    if data == "bye":
        break
cs.close()


	
