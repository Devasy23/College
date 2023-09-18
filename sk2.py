# # Import socket module
# import socket			

# # Create a socket object
# s = socket.socket()		

# # Define the port on which you want to connect
# port = 50000		

# # connect to the server on local computer
# s.connect(('127.0.0.1', port))
# s.send(bytes("hello ", 'utf-8'))
# # receive data from the server and decoding to get the string.
# print (s.recv(1024).decode())
# # close the connection
# s.close()	

# # now for udp client
# import socket
# import sys
# s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# message = "Hello, world I came via UDP".encode('utf-8')
# s.sendto(message, ('127.0.0.1', 50000))
# data, addr = s.recvfrom(4096)
# print(str(data))
# s.close()

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


	
