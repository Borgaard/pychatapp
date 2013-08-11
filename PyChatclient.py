import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], 1025)
print "connecting to %s port %s" % server_address
sock.connect(server_address)
running = 1
data = sock.recv(30)
print "waiting welcome message..."
print "received '%s'" % data

while running:
 message = raw_input("Type something: ")
 print >>sys.stderr, 'sending "%s"' % message
 sock.sendall(message)
 print "waiting message..."
 amount_received = 0
 amount_expected = len(message)
 while amount_received < amount_expected:
  data = sock.recv(999)
  amount_received += len(data)
  print >>sys.stderr, 'received "%s"' % data
  amount_expected = 0
  if data =="killcon":
   print "Kicked from server"
   running = 0
  if message =="exit":
   print "Disconnecting..."
   sock.sendall("discon")
   running = 0
sock.close()
