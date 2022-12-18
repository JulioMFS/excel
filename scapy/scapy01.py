from scapy.all import *
from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Ether

Layer2 = Ether()
Layer2.show()
Layer3 = IP()
Layer3.show()
MyIPv6 = IPv6()
MyIPv6.show()

Layer2 = Ether(src="01:02:03:04:05:06")
Layer2.show()

Layer3=IP(dst="192.168.1.249")
Layer3.show()

send=sendp(Layer2/Layer3)