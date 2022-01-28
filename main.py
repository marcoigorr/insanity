import time
import cv2
import mss
import numpy
import pytesseract
import keyboard
import webbrowser
import os
import subprocess
import webview


def createWindow(answer):
    f = open("text.txt", "a+")
    f.write(answer)
    f.close()
    window = webview.create_window(answer, 'text.txt', width=100, height=50)
    webview.start()
    time.sleep(1)
    os.remove("text.txt")

# Yanderedev momentum
def giveAnswer(text):
    if "What is the prefix length notation for the subnet mask 255.255.255.224" in text:
        createWindow("/27") # Answer

    elif "How many valid host addresses are available on an IPv4 subnet that is" in text:
        createWindow("62")

    elif "Which subnet mask would be used if 5 host bits are available" in text:
        createWindow("255.255.255.224")

    elif "A network administrator subnets the 192.168.10.0/24 network into subnets with /26" in text:
        createWindow("4")

    elif "Match the subnetwork to a host address that would be included within the subnetwork." in text:
        createWindow("1.32 - 1.48; 1.64 - 1.68; 1.96 - 1.121")

    elif "An administrator wants to create four subnetworks from the network address" in text:
        createWindow("subnetwork 192.168.1.64 subnet mask 255.255.255.192")

    elif "How many bits must be borrowed from the host portion of an address to accommodate" in text:
        createWindow("three")

    elif "How many host addresses are available on the 192.168.10.128/26 network" in text:
        createWindow("62")

    elif "How many host addresses are available on the network 172.16.128.0 with a subnet mask" in text:
        createWindow("1022")

    elif "Match each IPv4 address to the appropriate address category." in text:
        createWindow("192.168.100.161/25 203.0.113.100/24 hostAddr; 10.10.10.128/25 172.110.12.64/28 netAddr; 192.168.1.191/26 10.0.0.159/27 broadAddr")

    elif "What three blocks of addresses are defined by RFC 1918 for private network use" in text:
        createWindow("10.0.0.0/8; 172.16.0.0/12; 192.168.0.0/16")

    elif "Refer to the exhibit. An administrator must send a message to everyone on the router A" in text:
        createWindow("172.16.19.255")

    elif "A site administrator has been told that a particular network at the site must" in text:
        createWindow("255.255.255.128")

    elif "Refer to the exhibit. Considering the addresses already used and having to remain" in text:
        createWindow("10.16.10.64/27")

    elif "What is the usable number of host IP addresses on a network that has a /26 mask" in text:
        createWindow("62")

    elif "Which address prefix range is reserved for IPv4 multicast?" in text:
        createWindow("224.0.0.0 – 239.255.255.255")

    elif "Refer to the exhibit. Match the network with the correct IP address and prefix that will" in text:
        createWindow("A-25 B-26 C-27 D-30")

    elif "A high school in New York (school A) is using videoconferencing technology to" in text:
        createWindow("This is a private IP address.")

    elif "Which three addresses are valid public addresses" in text:
        createWindow("198.133.219.17; 128.107.12.117; 64.104.78.227")

    elif "A message is sent to all hosts on a remote network. Which type of message is it" in text:
        createWindow("directed broadcast")

    elif "A company has a network address of 192.168.1.64 with a subnet mask of" in text:
        createWindow("192.168.1.64/27; 192.168.1.96/28")

    elif "Which address is a valid IPv6 link-local unicast address" in text:
        createWindow("FE80::1:4545:6578:ABC1")

    elif "3FFE:1044:0000:0000:00AB:0000:0000:0057?" in text:
        createWindow("3FFE:1044:0:0:AB::57")

    elif "A network administrator has received the IPv6 prefix 2001:DB8::/48 for subnetting" in text:
        createWindow("65536")

    elif "Given IPv6 address prefix 2001:db8::/48, what will be the last subnet that is created if" in text:
        createWindow("2001:db8:0:f000::/52")

    elif "Consider the following range of addresses:" in text:
        createWindow("/60")

    elif "What type of IPv6 address is FE80::1" in text:
        createWindow("link-local")

    elif "Refer to the exhibit. A company is deploying an IPv6 addressing scheme for its" in text:
        createWindow("16")

    elif "What is used in the EUI-64 process" in text:
        createWindow("the MAC address of the IPv6 enabled interface")

    elif "What is the prefix for the host address 2001:DB8:BC15:A:12AB::1/64" in text:
        createWindow("2001:DB8:BC15:A")

    elif "An IPv6 enabled device sends a data packet with the destination address of FF02::1" in text:
        createWindow("all IPv6 enabled devices on the local link or network")

    elif "Match the IPv6 address with the IPv6 address type" in text:
        createWindow("2001:DB8::BAF... global unicast; FF02::1 all node multicast; ::1 loopback; FF02::1:FFAE.. solicited node multicast")

    elif "Which IPv6 prefix is reserved for communication between devices on the same link" in text:
        createWindow("FE80::/10")

    elif "Which type of IPv6 address refers to any unicast address that is assigned to multiple" in text:
        createWindow("anycast")

    elif "What are two types of IPv6 unicast addresses" in text:
        createWindow("loopback link-local")

    elif "Which service provides dynamic global IPv6 addressing to end devices without using" in text:
        createWindow("SLAAC")

    elif "Which protocol supports Stateless Address Autoconfiguration (SLAAC) for dynamic" in text:
        createWindow("ICMPv6")

    elif "Three methods allow IPv6 and IPv4 to co-exist" in text:
        createWindow("IPv4 dual stack; The IPv6 tunneling; IPv6 translation")

    elif "A technician uses the ping 127.0.0.1 command" in text:
        createWindow("the TCP/IP stack on a network host")

    elif "An administrator is trying to troubleshoot connectivity between" in text:
        createWindow("R1")

    elif "Which protocol is used by the traceroute command to send and receive echo-requests" in text:
        createWindow("ICMP")

    elif "Which ICMPv6 message is sent when the IPv6 hop limit" in text:
        createWindow("time exceeded")

    elif "A user executes a traceroute over IPv6" in text:
        createWindow("when the value of the Hop Limit field reaches zero")

    elif "What is the purpose of ICMP messages" in text:
        createWindow("to provide feedback of IP packet transmissions")

    elif "What source IP address does a router use by default when the traceroute command" in text:
        createWindow("the IP address of the outbound interface")

    elif "Match each description with an appropriate IP address" in text:
        createWindow("private - 172; loopback - 127; experim - 240.2; TEST-NET - 192.0; linklocal - 169.254")

    elif "A user issues a ping 192.135.250.103 command" in text:
        createWindow("host unreachable")

    elif "Which subnet would include the address 192.168.1.96" in text:
        createWindow("192.168.1.64/26")

    elif "Open the PT Activity" in text:
        createWindow("2001:DB8:1:1::1 - 2001:DB8:1:2::1 - 2001:DB8:1:3::2")

    elif "A host is transmitting a broadcast" in text:
        createWindow("all hosts in the same subnet")

    elif "A host is transmitting a unicast" in text:
        createWindow("one specific host")

    elif "includes a code of 3" in text:
        createWindow("address unreachable")

    elif "A host is transmitting a multicast" in text:
        createWindow("a specially defined group of hosts")

    elif "A host is transmitting a broadcast" in text:
        createWindow("all hosts in the same subnet")

    elif "2001:0db8:0000:0000:0000:a0b0:0008:0001" in text:
        createWindow("2001:db8::a0b0:8:1")

    elif "fe80:09ea:0000:2200:0000:0000:0fe0:0290" in text:
        createWindow("fe80:9ea:0:2200::fe0:290")

    elif "2002:0042:0010:c400:0000:0000:0000:0909" in text:
        createWindow("2002:42:10:c400::909")

    elif "2001:0db8:0000:0000:0ab8:0001:0000:1000" in text:
        createWindow("2001:db8::ab8:1:0:1000")

    elif "2002:0420:00c4:1008:0025:0190:0000:0990" in text:
        createWindow("2002:420:c4:1008:25:190::990")

    elif "includes a code of 2" in text:
        createWindow("beyond scope of the source address")

    elif "a code of 1" in text:
        createWindow("host unreachable")

    elif "includes a code of 3" in text:
        createWindow("address unreachable")

    elif "code of 0" in text:
        createWindow("network unreachable")

    elif "includes a code of 4" in text:
        createWindow("port unreachable")

    else:
        createWindow("No answer or question found")

# Importazione Pytesseract esterno; da sistemare
pytesseract.pytesseract.tesseract_cmd = '.\\Tesseract-OCR\\tesseract.exe'
# Oppure 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Dimensione della cattura
mon = {'top': 10, 'left': 0, 'width': 1920, 'height': 600}

with mss.mss() as sct:
    while True:
        if keyboard.read_key() == 'p':

            im = numpy.asarray(sct.grab(mon))
            # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(im)
            # cv2.imshow('Image', im)

            new_text = text.replace("\n", " ")

            giveAnswer(new_text)

            # Press "0" to quit
            if cv2.waitKey(25) & 0xFF == ord('0'):
                cv2.destroyAllWindows()
                break
