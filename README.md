# dhcp-scapy-server
Simple scapy script that listen for DHCP discover/requests and set an IP address

Everything on the script is hardcoded. Anyone could adapt it to argv (yeah I'm lazy).

If you're lazy too just change these variables:

    conf.iface='eno1'              # your interface name (type /sbin/ifconfig -a to verify)
    MY_HW_ADDR='aa:aa:aa:aa:aa:aa' # your interface MAC address
    MY_IP_ADDR='192.168.10.1'      # your interface IP address
    HIS_IP_ADDR='192.168.10.2'     # client's IP address
    HIS_DNS_SERVER='8.8.8.8'       # DNS server to use (thank you Google)

In the most cases you'll just need to change `MY_HW_ADDR` variable.
