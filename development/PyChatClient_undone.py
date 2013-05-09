#!/usr/bin/env python2
# -*- coding: utf-8 -*-
 
from __future__ import print_function
 
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import NetstringReceiver
from twisted.python import log
import msgpack
import sys
print("Due to connection bug, run me twice :)")
global no_err
no_err = 0
class BrokerClient(NetstringReceiver):
    def connectionMade(self):
        print("Connected")
        no_err = 1
        msg = msgpack.dumps(raw_input("Send text: "))
        self.sendString(msg)

    def connectionLost(self, reason):
        print("Connection Lost")
        no_err = 0

    def stringReceived(self, line):
        print("Recived:", msgpack.loads(line))

class BrokerFactory(ReconnectingClientFactory):
    protocol = BrokerClient
 
if __name__ == '__main__':
    #log.startLogging(sys.stdout)
    reactor.connectTCP("localhost", 1025, BrokerFactory())
    reactor.run()
