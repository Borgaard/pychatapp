#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

from twisted.python import log
from twisted.internet.protocol import Factory
from twisted.protocols.basic import NetstringReceiver
from twisted.internet import reactor
from uuid import uuid4 as get_uuid
import sys
print("Started up on port 1025 at 127.0.0.1")
class BrokerServer(NetstringReceiver):

    def __init__(self, cons):
        self.cons = cons #connections from facotry
        self.uuid = str(get_uuid()) #connection uuid

    def connectionMade(self):
        self.cons[self.uuid] = self
        print("New client:", self.uuid[24:])

    def connectionLost(self, reason):
        print("Client disconnect:", self.uuid[24:])
        if self.uuid in self.cons:
            del self.cons[self.uuid]

    def stringReceived(self, line):
        for uuid, conn in self.cons.iteritems():
              print(self.uuid[24:], ": ",  line)
              #if uuid != self.uuid: #don't send packet back to the originating clien
                #conn.sendString(line)

class BrokerFactory(Factory):

    def __init__(self):
        self.cons = {} # holds connections

    def buildProtocol(self, addr):
        return BrokerServer(self.cons)


#log.startLogging(sys.stdout)
reactor.listenTCP(1025, BrokerFactory())
reactor.run()
