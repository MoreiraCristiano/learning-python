import pyshark
import json

# Reading a captured file
capturedFile = pyshark.FileCapture("../pcap_files/captura1.pcap")

# Load the conference file
with open("../data/conferenceData.json") as conference_file:
    data = json.load(conference_file)

# Simple print json
print(data)

# Print formatted JSON
print(json.dumps(data, indent=2))

# Iteration in all packets of pcap file
for packet in capturedFile:
    try:
        protocol = packet.transport_layer
        src_addr = packet.ip.src
        src_port = packet[protocol].srcport
        dst_addr = packet.ip.dst
        dst_port = packet[protocol].dstport

        if protocol == "TCP":
            print(
                f"Src IP: {src_addr}:{src_port}\nDst IP: {dst_addr}:{dst_port}\nProtocol: {protocol} \n"
            )

    except AttributeError:
        print("Something went wrong")
