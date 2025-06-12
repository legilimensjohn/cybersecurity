# File: /network-traffic-sniffer/network-traffic-sniffer/src/main.py

from sniffer import Sniffer

def main():
    sniffer = Sniffer()
    sniffer.start_sniffing()

if __name__ == "__main__":
    main()