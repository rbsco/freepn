"""
DNS Blocker Prototype

This will be built using dnslib in py
"""

from dnslib import RR, A, DNSHeader, DNSQuestion, DNSRecord

d = DNSRecord(
    DNSHeader(qr=1, aa=1, ra=1),
    q=DNSQuestion("google.com"),
    a=RR("google.com", rdata=A("0.0.0.0")),
)


def main():
    print(f"I will do {d}")
    while True:
        d


if __name__ == "__main__":
    main()
