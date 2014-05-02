import socket
import sys
global welmsg
welmsg = "mikroskeem pychat"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 1025))
print 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)
while True:
 print 'waiting for a connection'
 global connection
 connection, client_address = sock.accept()

 print 'client connected:', client_address
 connection.send(welmsg)
 while True:
   print "waiting message..."
   data = connection.recv(2048)
   print 'received: %s' % data
   msg = raw_input("Send response: ")
   if msg == "exit":
     connection.sendall("Server killed")
     connection.close()
     break
   elif msg == "kick":
     connection.sendall("killcon")
     connection.close()
     break
   else:
     connection.sendall(msg)
     print 'sended "%s"' % msg
