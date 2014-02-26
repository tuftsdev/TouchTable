import socket, OSC
from OSC import *
import provider
from provider import *
from collections import deque

class TuioMotionEventProvider(MotionEventProvider):

    DEFAULT_IP = '127.0.0.1'
    DEFAULT_PORT = 3333

    '''
        Args expected to be of form:
                'ip:port'
            ie) '127.0.0.1:3333'
    '''
    def __init__(self, device, args):
        super(TuioMotionEventProvider, self).__init__(device, args)

        if len(args.split(':')) != 2:
            # TODO Error message
            self.ip = self.DEFAULT_IP
            self.port = self.DEFAULT_PORT
            print('Improper TUIO configuration')
            print('Expected form \'ip:port\' but given \'' + args + '\'' )
            print('Using default IP: ' + self.DEFAULT_IP + ' Port: ' + str(self.DEFAULT_PORT))
        else:
            self.ip, self.port = args.split(':')
            self.port = int(self.port)
        self.oschandler = None
        self.tuio_event_q = deque()
        self.handlers = {}
        self.touches = {}

    def start(self):
        self.oschandler = osc.listen(self.ip, self.port)
    
    def update(self, dispatch):
        osc.readQueue(self.oscid)
        


    def getIP(self):
        return self.ip

    def getPort(self):
        return self.port




'''
    Testing framework for TuioMotionEventProvider
'''
if __name__ == '__main__':
    print('Entering test mode for TuioMotionEventProvider')
    tmep = TuioMotionEventProvider(None, '127.0.0.1:3333')
    #tmep_invalid = TuioMotionEventProvider(None, '10.0.0.1')
    print('IP: ' + tmep.getIP())
    print('Port: ' + str(tmep.getPort()))

