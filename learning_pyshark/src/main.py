import pyshark
import time

# Reading a captured file
capturedFile = pyshark.FileCapture("../pcap_files/captura1.pcap")

for packet in capturedFile:
    try:
        src_addr = packet.ip.src
        dst_addr = packet.ip.dst
        print("IP src: %s -> IP dst: %s" % (src_addr, dst_addr))
    except AttributeError:
        pass





# Sniff from interface
# capture = pyshark.LiveCapture(interface="enp0s3")

# Getting packets summaries
# for packet in capture:
#     # adjusted output
#     try:
#         # get timestamp
#         localtime = time.asctime(time.localtime(time.time()))

#         # get packet content
#         protocol = packet.transport_layer  # protocol type
#         src_addr = packet.ip.src  # source address
#         src_port = packet[protocol].srcport  # source port
#         dst_addr = packet.ip.dst  # destination address
#         dst_port = packet[protocol].dstport  # destination port

#         # output packet info
#         print(
#             "IP %s:%s <-> %s:%s (%s)"
#             % (src_addr, src_port, dst_addr, dst_port, protocol)
#         )
#     except AttributeError as e:
#         # ignore packets other than TCP, UDP and IPv4
#         pass
#     print(" ")
