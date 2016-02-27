#!/usr/bin/python
'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.util import irange,dumpNodeConnections


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
        self.fanout = fanout
        switchCount = 1
        hostCount = 1
	core = self.addSwitch('s%s' % switchCount)
        switchCount += 1
	for i in irange(1, fanout):
            aggregation = self.addSwitch('s%s' % switchCount)
	    switchCount += 1
            self.addLink(core, aggregation, **linkopts1)
            #   linkopts1 = {'bw':50, 'delay':'5ms'}
            for j in irange(1, fanout):
                edge = self.addSwitch('s%s' % switchCount)
                switchCount += 1
                self.addLink(aggregation, edge, **linkopts2)
                for k in irange(1, fanout):
                    host = self.addHost('h%s' % hostCount)                
                    self.addLink(edge, host, **linkopts3)
                    hostCount += 1

def perfTest():
    link1 = dict(bw=10, delay='5ms')
    link2 = dict(bw=10, delay='10ms')
    link3 = dict(bw=10, delay='15ms')

    topo = CustomTopo(linkopts1 = link1, linkopts2 = link2, linkopts3 = link3, fanout=2) 
    net = Mininet(topo=topo, link=TCLink) #,host=CPULimitedHost,
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    #print "Testing bandwidth between h1 and h4"
    #h1, h4 = net.get('h1', 'h4')
    #net.iperf((h1, h4))
    net.stop()


if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    perfTest()

                    
topos = { 'custom': ( lambda: CustomTopo() ) }
