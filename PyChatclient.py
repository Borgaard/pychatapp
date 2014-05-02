import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (sys.argv[1], 1025)
print "connecting to %s port %s" % server_address
sock.connect(server_address)
print "waiting welcome message..."
data = sock.recv(30)
print "Welcome message: '%s'" % data
while True:
 message = raw_input("Send text: ")
 print 'sending "%s"' % message
 sock.send(message)
 print "waiting message..."
 amount_expected = len(message)
 while amount_received < 0:
  data = sock.recv(2048)
  amount_received += len(data)
  print 'received "%s"' % data
  if data =="killcon":
   print "Kicked from server"
   break
  if message =="exit":
   print "Disconnecting..."
   sock.sendall("discon")
   break
sock.close()
