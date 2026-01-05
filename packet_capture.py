from scapy.all import sniff, IP, TCP
import pandas as pd

def process_packet(packet):
    if IP in packet:
        features = {
            "packet_length": len(packet),
            "protocol": packet.proto,
            "src_port": packet[TCP].sport if TCP in packet else 0,
            "dst_port": packet[TCP].dport if TCP in packet else 0
        }
        return pd.DataFrame([features])

def start_capture(callback):
    sniff(prn=lambda pkt: callback(process_packet(pkt)), store=False)
