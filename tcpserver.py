import socket
import sys
global welmsg
welmsg = "mikroskeem chat 0.1 alpha :)))"
# Create a TCP/IP socket
global sock
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address given on the command line
server_address = ('', 1000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()

def boot():
 switchmode(1)
 
def head():
 sock.listen(1)
 print >>sys.stderr, 'waiting for a connection'
 global connection
 connection, client_address = sock.accept()

 print >>sys.stderr, 'client connected:', client_address
 connection.sendall(welmsg)
 switchmode(2)
def body():
 data = connection.recv(30)
 print >>sys.stderr, 'received "%s"' % data
 msg = raw_input("Send response: ")
 if msg =="exit":
  connection.sendall("Server killed")
  connection.close()
  switchmode(1)
 if msg =="kick":
  connection.sendall("killcon")
  connection.close()
  switchmode(1)
 if data:
  connection.sendall(msg)
  print >>sys.stderr, 'sended "%s"' % msg
  print "waiting message..."

funcmap = {1: head, 2: body}
def switchmode(a):
 funcmap[a]()
boot()