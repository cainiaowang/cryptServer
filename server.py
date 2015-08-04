# This program acts as a simple server, which in its first iteration accepts up to X
# connections and allows these users to broadcast to all

# Hopefully we will upgrade this later to include
# - Usernames
# - Private Messaging

# Note: I have used the following tutorial/code as the basis of my code:
# Python socket - chat server and client with code example
# published on Binary Tides by Silver Moon (March 31 2013)

import socket, select
 
#Function to broadcast chat messages to all connected clients
def broadcast_data (author,message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != author :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                peername = names[str(socket)]
                CONNECTION_LIST.remove(socket)
                print peername+" is offline"
                broadcast_data(server_socket,"<Server> "+ peername+ " is offline\n")
                names.pop(str(socket))
                socket.close()
                
 
# List to keep track of socket descriptors
CONNECTION_LIST = []
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 5000
     
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)
 
# Add server socket to the list of readable connections
CONNECTION_LIST.append(server_socket)
names={} 
print "Chat server started on port " + str(PORT)

# Keep Track of Usernames
while 1:
    # Get the list sockets which are ready to be read through select
    read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
    for sock in read_sockets:
        #New connection
        if sock == server_socket:
            # Handle the case in which there is a new connection recieved through server_socket
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            print "Client (%s, %s) connected" % addr
            #broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
             
        #Some incoming message from a client
        else:
            # Data recieved from client, process it
            data = sock.recv(RECV_BUFFER)
            if data:
                
                # CASE: NEW USER WELCOME MESSAGE / CHANGE NAME
                words = data.split(":")
                if len(words) ==2 and words[0]=="HELLO":
                    newname = words[1].strip()
                    if newname in names.values():
                        print "Duplicate name ("+newname+") rejected for user " + str(sock.getpeername())
                        sock.send("Username already taken")
                        print("Username already taken")
                        CONNECTION_LIST.remove(sock)
                        sock.close()
                    else:
                        sock.send("<Server> Welcome " +newname+"\n")
                        if len(names) == 0:
                            sock.send("<Server> you are the first user to join the chat room\n")
                        elif len(names) == 1:
                            sock.send("<Server> " + " ".join(names.values()) + " is presently in the chat room\n")
                        else:
                            sock.send("<Server> " + " ".join(names.values()) + " are presently in the chat room\n")
                        names[str(sock)]=newname
                        broadcast_data(sock,"<Server> " + newname + ' has joined the chatroom\n')
                        print newname +" is " + str(sock.getpeername())
                
                # CASE: NORMAL MESSAGE RECIEVED FROM KNOWN PERSON
                elif str(sock) in names.keys():
                    broadcast_data(sock, '<' + names[str(sock)] + '> ' + data)
                
                # CASE NORMAL MESSAGE RECIEVED FROM UNKNOWN PERSON
                else:
                    print "Unknown user detected: " + str(sock.getpeername())
                    print "Message: " + data

