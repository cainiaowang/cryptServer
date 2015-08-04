## Crypto Client Server

### Aim
To create a basic chat server using python, such that on this server we can practice the implementation of basic crypto functions.

### 1-BasicSC: Basic Server Client
My First attempt at using TCP Sockets in python to send and recieve messages

### 2-ChatSC: Chat Server Client
A working (but simple) Chat Client

The Server accepts connections from clients, who provide a nickname, the server
then relays all messages sent from clients to other members of the chatroom.

Extensions beyond the base tutorial code:
- Fix problems associated with clients leaving and rejoining
- Add a nickname system of identification
- minor modifications to the Client to minimise problems still existing in the UI

Posibile future work:
- Authentication, and the adding of an admin account with kick privilages
- better client UI, currently if a message is recieved while typing the half 
  completed message is lost.
- crypt work
