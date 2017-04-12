#!/usr/bin/python2

from scapy.all import *

conf.ipv6_enabled=False
conf.iface='eno1'
MY_HW_ADDR='10:98:36:fc:8a:1f'
MY_IP_ADDR='192.168.10.1'
HIS_IP_ADDR='192.168.10.2'
HIS_DNS_SERVER='8.8.8.8'


def parse_packet(p):
    if not (p.haslayer(BOOTP) and p.haslayer(DHCP) and p.haslayer(UDP)):
       print '[-] not yet..'
       return

    # Ether / IP / UDP
    e=Ether(src=MY_HW_ADDR, dst=p[BOOTP].chaddr[:6])
    i=IP(src=MY_IP_ADDR, dst='192.168.10.2')
    u=UDP(sport=67, dport=68)
    b=BOOTP(op=2, xid=p[BOOTP].xid, yiaddr=HIS_IP_ADDR, siaddr=MY_IP_ADDR, chaddr=p[BOOTP].chaddr)
    d=DHCP(options=[ ('message-type','offer'), ('server_id', MY_IP_ADDR), ('lease_time', 600), ('subnet_mask', '255.255.255.224'), ('router', MY_IP_ADDR), ('name_server', HIS_DNS_SERVER), 'end'])

    for op in p[DHCP].options:
        if op[0]=='message-type' and op[1]==1:
            d.options[0]=('message-type', 2) # 2=offer
            sendp(e/i/u/b/d)
            return
        if op[0]=='message-type' and op[1]==3:
            d.options[0]=('message-type', 5) # 5=ack
            sendp(e/i/u/b/d)
            return


sniff(filter='udp src port 68', prn=parse_packet)

