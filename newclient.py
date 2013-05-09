#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
from __future__ import print_function
 
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import NetstringReceiver
from twisted.python import log
import msgpack
import sys
print("Due to bug, run me twice :)")
class BrokerClient(NetstringReceiver):
 
    def connectionMade(self):
        print("Connected")
        #msg = msgpack.dumps({"type":"test", "Hello":"World"})
        msg = raw_input("Send text: ")
        self.sendString(msg)
 
    def connectionLost(self, reason):
        print("Connection Lost")
 
    def stringReceived(self, line):
        print("recived:", msgpack.loads(line))
 
class BrokerFactory(ReconnectingClientFactory):
    protocol = BrokerClient
 
if __name__ == '__main__':
    #log.startLogging(sys.stdout)
    reactor.connectTCP("localhost", 1025, BrokerFactory())
    reactor.run()
