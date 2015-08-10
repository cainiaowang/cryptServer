# telnet program example
import socket, select, string, sys
import dracReader
import time

username = "Honest Drac"

if(len(sys.argv) < 3) :
    print 'Usage : python telnet.py hostname port'
    sys.exit()
     
host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
     
# Connect to remote host
try :
    s.connect((host, port))
    s.send("HELLO:"+username) 
except :
    print 'Unable to connect'
    sys.exit()

print "Connected to remote host, beginning to send dracula quotes in the clear"
while 1:
    time.sleep(5)
    try:
        s.send(dracReader.getDracText()+"\n")
    except:
        print "Disconnected from chat server"
        sys.exit()
