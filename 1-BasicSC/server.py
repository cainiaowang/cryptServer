# This program acts as a simple server, which in its first iteration accepts up to X
# connections and allows these users to broadcast to all

# Hopefully we will upgrade this later to include
# - Usernames
# - Private Messaging

# Note: I have used the following tutorial/code as the basis of my code:
# Python socket - chat server and client with code example
# published on Binary Tides by Silver Moon (March 31 2013)

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Server: Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection
