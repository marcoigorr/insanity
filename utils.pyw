import mss
import numpy
import pytesseract


# Question array
question_list = [
    "pisciati",
    "Which two traffic types use the Real-Time Transport Protocol",
    "Which wireless technology has low-power and data rate requirements making it popular",
    "model provides a route to forward messages through an internetwork",
    "Which type of server relies on record types such as A",
    "What are proprietary protocols",
    "What service is provided by DNS",
    "The packet has a destination port number of 110",
    "What command can be used on a Windows PC to see the IP configuration",
    "That printer has been shared so that other computers on the home network can also use the printer",
    "What characteristic describes a virus",
    "The first employee uses a web browser to view a company web page in order to read some announcements",
    "Match the description to the IPv6 addressing component", # tabella
    "If Host1 were to transfer a file to the server",
    "Match the characteristic to the forwarding method", # tabella
    "The IP address of which device interface should be used as the default gateway setting",
    "What service is provided by Internet Messenger",
    "Match the network with the correct IP address and prefix", # tabella
    "Which protocol was responsible for building the table that is shown",
    "A network administrator notices that some newly installed Ethernet cabling is carrying corrupt and distorted data signals",
    "A host is trying to send a packet to a device on a remote LAN segment, but there are currently no mappings in its ARP cache",
    "Which two functions are performed at the MAC sublayer of the OSI Data Link Layer to facilitate Ethernet communication",
    "The packet has a destination port number of 53",
    "The new LAN must support 25 connected devices",
    "What characteristic describes a Trojan horse",
    "What service is provided by HTTPS",
    "A technician with a PC is using multiple applications while connected to the Internet",
    "The new LAN must support 61 connected devices",
    "Match the network with the correct IP address and prefix that ", # duplicata
    "What characteristic describes a DoS attack",
    "Match the application protocols to the correct transport protocols", # tabella
    "What service is provided by SMTP",
    "Which scenario describes a function provided by the transport layer",
    "Host B on subnet Teachers transmits a packet to host D",
    "What does the term",
    "An administrator is trying to configure the switch but receives",
    "Which two protocols operate at the top layer of the",
    "A company has a file server that shares a folder named Public",
    "What three requirements are defined by the protocols used",
    "What are two characteristics of IP",
    "An employee of a large corporation remotely logs into the company",
    "What are two common causes of signal degradation when using",
    "Which subnet would include the address",
    "On the basis of the output",
    "Which two statements describe how to assess traffic flow patterns",
    "What is the consequence of configuring a router",
    "Which three layers of the OSI model map to the application layer of the",
    "If PC1 is sending a packet to PC2",
    "What will happen if the default gateway address",
    "What are two features of ARP",
    "The new LAN must support 90 connected devices",
    "messages that are not present in",
    "The packet has a destination port number of 80",
    "What is an advantage for small organizations of adopting IMAP",
    "Which software utility can the technician use to diagnose the problem",
    "Which two functions are performed at the LLC sublayer",
    "The global configuration command",
    "What happens when the",
    "Match the type of threat with the cause",
    "A disgruntled employee is using some free wireless networking",
    "What service is provided by HTTP",
    "The packet has a destination port number of 67",
    "What are two problems that can be caused by a large number of ARP",
    "When testing the connectivity",
    "During the process of forwarding traffic",
    "What characteristic describes antispyware",
    "A network administrator needs to keep the user ID",
    "What are the two most effective ways to defend against malware",
    "Which type of security threat would be responsible if",
    "Which frame field is created by a source node and used",
    "The new LAN must support 4 connected devices",
    "What service is provided by POP3",
    "What two security solutions are most likely",
    "What characteristic describes antivirus software",
    "What mechanism is used by a router to prevent a received",
    "The packet has a destination port number of 69",
    "An administrator defined a local user account with a secret password",
    "Which two functions are performed at the MAC sublayer of the OSI Data Link Layer to facilitate Ethernet communication", # duplicato
    "An IPv6 enabled device sends a data packet with the destination address",
    "What are the three parts of an IPv6 global",
    "A network administrator is designing the layout of a new wireless network",
    "A new network administrator has been asked to enter a banner message on a Cisco",
    "What method is used to manage contention-based",
    "What is a function of the data link layer",
    "What is the purpose of the TCP sliding window",
    "What characteristic describes spyware",
    "Which switching method drops frames that fail the FCS",
    "Which range of link-local addresses can be assigned to an",
    "What service is provided by FTP",
    "A user is attempting to access",
    "Which two statements accurately describe an advantage or a disadvantage",
    "What would be the interface ID",
    "PC1 issues an ARP request because",
    "What service is provided by BOOTP",
    "What characteristic describes adware",
    "When a switch configuration includes a user-defined error threshold on a per-port basis",
    "Match a statement to the related network model", # tabella
    "What are two primary responsibilities of the Ethernet MAC",
    "What three facts can be determined from the viewable",
    "Match each type of frame field to its function", # tabella
    "What is the subnet ID associated with the",
    "Match the firewall function to the type of threat protection it provides to the network", # tabella
    "Users are reporting longer delays in authentication",
    "How does the service password-encryption",
    "Which two statements are correct in a comparison",
    "A network administrator wants to have the same network mask",
    "What characteristic describes identity theft",
    "The new LAN must support 200 connected devices",
    "What are three commonly followed standards for constructing and installing",
    "What is wrong with the displayed termination",
    "Match the characteristic to the category", # tabella
    "The packet has a destination port number of 143",
    "What are two characteristics shared by TCP",
    "Your answers should waste the fewest addresses",
    "The packet has a destination port number of 21",
    "What attribute of a NIC would place it at the data link",
    "The new LAN must support 10 connected devices",
    "What technique is used with UTP",
    "The network administrator has assigned the LAN",
    "The switches are in their default configuration",
    "Match a statement to the related network model", # duplicato
    "A network engineer has been given the network address",
    "Which connector is used with twisted-pair",
    "The packet has a destination port number of 22",
    "What characteristic describes an IPS",
    "What service is provided by DHCP",
    "Match the header field with the appropriate layer of the OSI model", # tabella
    "The switches have a default configuration",
    "rate requirements making it popular in IoT environments",
    "message types must be permitted through",
    "A client is using SLAAC",
    "Two pings were issued from a host on a local network",
    "An organization is assigned an",
    "What subnet mask is needed if an",
    "If host A sends an IP packet to host B",
    "What is a benefit of using cloud computing in networking",
    "Which two statements are correct about MAC",
    "What is one main characteristic of the data link layer",
    "What are three characteristics of the",
    "Which information does the show",
    "Which two commands can be used on a Windows",
    "What are two functions that are provided by the network layer",
    "Which two statements describe features of an",
    "What characteristic describes a VPN",
    "Why would a Layer 2",
    "Match each description to its corresponding term", # tabella
    "A user sends an HTTP request",
    "What is an advantage to using a protocol that",
    "Data is being sent from a source PC",
    "Match each description with the corresponding TCP", # tabella
    "A company uses the address block",
    "What single subnet mask would be appropriate to use for the three subnetworks",
    "Match each item to the type of topology diagram",
    "What two pieces of information are displayed",
    "A user is complaining that an external web page is taking",
    "Which value",
    "A network technician is researching the use of fiber",
    "description with an appropriate IP address", # tabella
    "A user is executing a tracert to a remote device",
    "Users report that the network access is slow",
    ]


def getScrText():
    pytesseract.pytesseract.tesseract_cmd = '.\\Tesseract-OCR\\tesseract.exe'

    # Screen capture settings
    mon = {'top': 100, 'left': 0, 'width': 1920, 'height': 600}

    with mss.mss() as sct:
        im = numpy.asarray(sct.grab(mon))
        # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(im)
        # cv2.imshow('Image', im)

        return text.replace("\n", " ").replace(" ", "").lower()


def getQuestion(index):
    return question_list[index].lower().replace(" ", "")

# ---------------------- Yanderedev momentum ---------------------

def getAnswer(text):
    if getQuestion(1) in text:
        return("video - voice")    
    elif getQuestion(2) in text:
        return("ZigBee")
    elif getQuestion(3) in text:
        return("internet")
    elif getQuestion(4) in text:
        return("DNS")
    elif getQuestion(5) in text:
        return("protocols developed by organizations")
    elif getQuestion(6) in text:
        return("Resolves domain names")
    elif getQuestion(7) in text:
        return("POP3")
    elif getQuestion(8) in text:
        return("ipconfig")
    elif getQuestion(9) in text:
        return("peer-to-peer (P2P)")
    elif getQuestion(10) in text:
        return("malicious software")
    elif getQuestion(11) in text:
        return("audio conference, financial transactions, web page")
    elif getQuestion(12) in text:
        return("identify subnets -> sub ID; \nby the provider -> global; \nIPv4 -> interface ID")
    elif getQuestion(13) in text:
        return("application, transport, Internet, and network access layers")
    elif getQuestion(14) in text:
        return("always, checks CRC, checks frame -> store-and-frwd; \nhas, may, begins -> cut-through")
    elif getQuestion(15) in text:
        return("R1: G0/0")
    elif getQuestion(16) in text:
        return("An application that allows")
    elif getQuestion(17) in text:
        return("A -> /25; \nB -> /26; \nC -> /27; \nD -> /30")
    elif getQuestion(18) in text:
        return("ARP")
    elif getQuestion(19) in text:
        return("RFI - EMI")
    elif getQuestion(20) in text:
        return("of the default gateway")
    elif getQuestion(21) in text:
        return("integrates Layer 2 flows between 10 - implements CSMA/CD")
    elif getQuestion(22) in text:
        return("DNS")
    elif getQuestion(23) in text:
        return("255.255.255.224")
    elif getQuestion(24) in text:
        return("malicious software")
    elif getQuestion(25) in text:
        return("to secure the exchange of text")
    elif getQuestion(26) in text:
        return("based on the source port number that is used by each application")
    elif getQuestion(27) in text:
        return("255.255.255.192")
    elif getQuestion(28) in text:
        return("A -> /25; \nB -> /26; \nC -> /27; \nD -> /30")
    elif getQuestion(29) in text:
        return("an attack that slows")
    elif getQuestion(30) in text:
        return("FTP, HTTP, SMTP -> TCP \nDHCP, TFTP -> UDP")
    elif getQuestion(31) in text:
        return("Allows clients to send email")
    elif getQuestion(32) in text:
        return("A student has two web browser")
    elif getQuestion(33) in text:
        return("00-00-0c-94-36-ab \n00-00-0c-94-36-bb \n172.16.20.200 \n172.16.10.200")
    elif getQuestion(34) in text:
        return("loss of signal strength as distance")
    elif getQuestion(35) in text:
        return("enter privileged EXEC")
    elif getQuestion(36) in text:
        return("POP - DNS")
    elif getQuestion(37) in text:
        return("authorization")
    elif getQuestion(38) in text:
        return("message size \nmessage encoding \ndelivery options")
    elif getQuestion(39) in text:
        return("does not require - operates independently")
    elif getQuestion(40) in text:
        return("security - quality of service - fault tolerance")
    elif getQuestion(41) in text:
        return("improper termination - low-quality cable or connectors")
    elif getQuestion(42) in text:
        return("192.168.1.64/26")
    elif getQuestion(43) in text:
        return("There are 4 hops - There is connectivity")
    elif getQuestion(44) in text:
        return("Capture traffic during peak - Perform the capture")
    elif getQuestion(45) in text:
        return("The IPv6 enabled router")
    elif getQuestion(46) in text:
        return("application - session - presentation")
    elif getQuestion(47) in text:
        return("remove the Ethernet header")
    elif getQuestion(48) in text:
        return("with hosts in other networks")
    elif getQuestion(49) in text:
        return("If a host is ready to send - If a device receiving an ARP")
    elif getQuestion(50) in text:
        return("255.255.255.128")
    elif getQuestion(51) in text:
        return("Neighbor Solicitation - Router Advertisement")
    elif getQuestion(52) in text:
        return("HTTP")
    elif getQuestion(53) in text:
        return("Messages are kept in the mail servers until")
    elif getQuestion(54) in text:
        return("nslookup")
    elif getQuestion(55) in text:
        return("enables IPv4 and IPv6 \nplaces information in the Ethernet \nhandles communication between \nadds Ethernet control information")
    elif getQuestion(56) in text:
        return("The switch can be remotely managed")
    elif getQuestion(57) in text:
        return("Communication between")
    elif getQuestion(58) in text:
        return("maintence -> poor handling \nenviromental -> temperature extremes \nhardware -> physical damage \nelectrical -> voltage spikes")
    elif getQuestion(59) in text:
        return("reconnaissance")
    elif getQuestion(60) in text:
        return("A basic set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the web")
    elif getQuestion(61) in text:
        return("DHCP")
    elif getQuestion(62) in text:
        return("The ARP request is sent - All ARP request messages must")
    elif getQuestion(63) in text:
        return("ping - ipconfig - nslookup")
    elif getQuestion(64) in text:
        return("switch the packet to the directly")
    elif getQuestion(65) in text:
        return("applications that protect end devices")
    elif getQuestion(66) in text:
        return("SSH")
    elif getQuestion(67) in text:
        return("Update the operating system - Install and update")
    elif getQuestion(68) in text:
        return("Trojan horse")
    elif getQuestion(69) in text:
        return("frame check sequence field")
    elif getQuestion(70) in text:
        return("255.255.255.248")
    elif getQuestion(71) in text:
        return("Retrieves email from the server by downloading")
    elif getQuestion(72) in text:
        return("virtual private networks - intrusion prevention systems")
    elif getQuestion(73) in text:
        return("applications that protect end devices")
    elif getQuestion(74) in text:
        return("It decrements the value of the TTL ")
    elif getQuestion(75) in text:
        return("TFTP")
    elif getQuestion(76) in text:
        return("Configure the IP domain name on the router \nGenerate the SSH keys \nEnable inbound vty SSH sessions")
    elif getQuestion(77) in text:
        return("places information in the Ethernet frame \nintegrates Layer 2 flows between \nimplements trailer with frame \nimplements CSMA/CD \napplies source and destination MAC")
    elif getQuestion(78) in text:
        return("configured routers on the local link")
    elif getQuestion(79) in text:
        return("subnet ID - global - interface ID")
    elif getQuestion(80) in text:
        return("interference - security - coverage area")
    elif getQuestion(81) in text:
        return("Exit privileged EXEC")
    elif getQuestion(82) in text:
        return("CSMA/CA")
    elif getQuestion(83) in text:
        return("provides for the exchange of frames")
    elif getQuestion(84) in text:
        return("to request that a source")
    elif getQuestion(85) in text:
        return("software that is installed on a user")
    elif getQuestion(86) in text:
        return("store-and-forward switching")
    elif getQuestion(87) in text:
        return("FE80::/10")
    elif getQuestion(88) in text:
        return("Allows for data transfers")
    elif getQuestion(89) in text:
        return("DNS server - default gateway")
    elif getQuestion(90) in text:
        return("introduces problems - provides a solution")
    elif getQuestion(91) in text:
        return("1E6F:65FF:FEC2:BDF8")
    elif getQuestion(92) in text:
        return("ARP reply with its MAC address - ARP reply with the PC2 MAC address")
    elif getQuestion(93) in text:
        return("Legacy application that enables")
    elif getQuestion(94) in text:
        return("software that is installed on a user")
    elif getQuestion(95) in text:
        return("store-and-forward")
    elif getQuestion(96) in text:
        return("no dedicated, client and server -> peer-to-peer network \nrequires a specific, a background service -> peer-to-peer aplication")
    elif getQuestion(97) in text:
        return("accessing the media - data encapsulation")
    elif getQuestion(98) in text:
        return("The switch can be remotely managed \nOne device is attached to a physical interface \nThe default SVI has been configured")
    elif getQuestion(99) in text:
        return("error detection -> checks \naddressing -> helps \ntype -> is used \nframe start -> identifies the beginning")
    elif getQuestion(100) in text:
        return("2001:DA48:FC5:A4::/64")
    elif getQuestion(101) in text:
        return("by port number -> application filtering \nbased on ip -> packet filtering \nunsolicited incoming -> stateful packet insp \naccess to websites -> URL filtering")
    elif getQuestion(102) in text:
        return("the network performance baseline")
    elif getQuestion(103) in text:
        return("It encrypts passwords that are stored in router or switch configuration files")
    elif getQuestion(104) in text:
        return("The Source Address field name from - The Time-to-Live field from IPv4")
    elif getQuestion(105) in text:
        return("255.255.255.224")
    elif getQuestion(106) in text:
        return("the use of stolen credentials ")
    elif getQuestion(107) in text:
        return("255.255.255.0")
    elif getQuestion(108) in text:
        return("cable lengths - pinouts - connector types")
    elif getQuestion(109) in text:
        return("The untwisted length of each wire is too long")
    elif getQuestion(110) in text:
        return("Layer 3, into a network, 32 or 128 -> IP address \nLayer 2, OUI, 48 -> MAC address")
    elif getQuestion(111) in text:
        return("IMAP")
    elif getQuestion(112) in text:
        return("port numbering - use of checksum")
    elif getQuestion(113) in text:
        return("208/28 - 224/28")
    elif getQuestion(114) in text:
        return("FTP")
    elif getQuestion(115) in text:
        return("MAC address")
    elif getQuestion(116) in text:
        return("255.255.255.240")
    elif getQuestion(117) in text:
        return("twisting the wires together into pairs")
    elif getQuestion(118) in text:
        return("192.168.10.38 - 255.255.255.248 - 192.168.10.33")
    elif getQuestion(119) in text:
        return("only hosts B, C, and router R1")
    elif getQuestion(120) in text:
        return("no dedicated, client and server -> peer-to-peer network \nrequires a specific, a background service -> peer-to-peer aplication")
    elif getQuestion(121) in text:
        return("200")
    elif getQuestion(122) in text:
        return("RJ 45 (true answer)")
    elif getQuestion(123) in text:
        return("SSH")
    elif getQuestion(124) in text:
        return("a network device that filters")
    elif getQuestion(125) in text:
        return("Dynamically assigns IP")
    elif getQuestion(126) in text:
        return("802.2, FCS, MAC addr -> Layer 2 \nTTL, IP addr -> Layer 3 \nAcknowledge, Destination -> layer 4")
    elif getQuestion(127) in text:
        return("only hosts B, C, and router R1")
    elif getQuestion(128) in text:
        return("Zigbee")
    elif getQuestion(129) in text:
        return("neighbor solicitations - neighbor advertisement")
    elif getQuestion(130) in text:
        return("It must send an ICMPv6 Neighbor")
    elif getQuestion(131) in text:
        return("Security rules are applied")
    elif getQuestion(132) in text:
        return("256")
    elif getQuestion(133) in text:
        return("255.255.255.192")
    elif getQuestion(134) in text:
        return("BB:BB:BB:BB:BB:BB")
    elif getQuestion(135) in text:
        return("Network capabilities are extended")
    elif getQuestion(136) in text:
        return("Destination IP addresses in a packet - Destination and source MAC addresses")
    elif getQuestion(137) in text:
        return("It shields the upper layer protocol")
    elif getQuestion(138) in text:
        return("A device listens and waits until - After detecting a collision - All of the devices on a segment")
    elif getQuestion(139) in text:
        return("the contents of the saved configuration")
    elif getQuestion(140) in text:
        return("route print - netstat -r")
    elif getQuestion(141) in text:
        return("directing data packets to destination - providing end devices")
    elif getQuestion(142) in text:
        return("Directly connected interfaces - If a default static route is configured")
    elif getQuestion(143) in text:
        return("a tunneling protocol that provides")
    elif getQuestion(144) in text:
        return("to enable the switch to be managed remotely")
    elif getQuestion(145) in text:
        return("message encoding -> of converting \nsizing -> of breaking \nencapsulation -> of placing")
    elif getQuestion(146) in text:
        return("the MAC address of the default gateway")
    elif getQuestion(147) in text:
        return("It encourages")
    elif getQuestion(148) in text:
        return("The source port field - UDP segments are - The UDP destination")
    elif getQuestion(149) in text:
        return("number -> window size \nused -> sequence num \nmethod -> retransmission \nreceived -> acknowledgement")
    elif getQuestion(150) in text:
        return("255.255.255.128")
    elif getQuestion(151) in text:
        return("255.255.255.240")
    elif getQuestion(152) in text:
        return("IP addr -> logical topology \n location, path -> physical topology")
    elif getQuestion(153) in text:
        return("IP addresses - Layer 1 statuses")
    elif getQuestion(154) in text:
        return("tracert")
    elif getQuestion(155) in text:
        return("Time-to-Live")
    elif getQuestion(156) in text:
        return("Fiber optic cabling requires different termination - Fiber optic provides higher data ")
    elif getQuestion(157) in text:
        return("link-local -> 169.254 \npublic addr -> 198.133 \nexperimental addr -> 240.2 \nloopback - > 127.0.01")
    elif getQuestion(158) in text:
        return("when the value in the TTL field reaches zero")
    elif getQuestion(159) in text:
        return("worm")

    else:
        return("No answer or question found")

"""
//******/////*******////**********///*//**/////**********//*************//*****/////*************//********/*/********/*******************************
/****/***////*******///**********///**//*//////**********//************///*****/////*************//**********/********/**********//*******************
/********////**/***///***********///***/*//////*********//*************//******/////*********,**///*******************/***********/*******************
/********////**/***///***********///******/////********////***/*/*/(((///*/****/////************///******************//***********/*******************
/*******/////**/***//***********////*****/////*********////(#########%#(###(#(((#######(((#/****///******************/********************************
*******/////******//************/////*//*//////*/****/(####(/(#%#############(((#((##(##((###(####%#*****************/************/************/******
*******/////*****///***********/////*****/////**/#%(/(((%#(#(#######(##%%#%%######%####(##(#((######%###************//********************************
/***/**////******///***********/////***/*//////###((######(###((#((#/((#(######%%%########(##(####%#(#/(##((##((***//*************/************/******
********//******//*****//******///////***/*#((/#(((/######(((#((//(((#((/(((####(#(#%#(###(#######%%(######%%%###(///*********************************
********//*****///**********///////******(*#####(/(/##(((#(((####(#%#(##((*#//((/((#####(#((###############%%####%(#/************/********************
**************////*************////**(%#(/((####%#((((((#(%##(##%%#####((###((((#(((#(##%###%#/(#####%#%#%((%%(#####///**********/*/*/****************
***///////***////////**********/*//#(#%#(#(%%####%#(((((((####%%##((##%#######/##(((,#(%#%%(##(#(((###%#((#%#//(####(/#/#**************************,**
/**///*///****////////////****////#(#(((#####/(##((/(############((#####((((##((####(#(###(###((#(/(###((###(#####((/(/(#/***,**************,,********
***//***////////////////////////(#%%###((((((((((////(/(((((/#/((((/(((///*//////(((((/((#((///((((((#(##%##%#/(#(((((#((((/*****************,********
**///***////////////////////////###(/#(/*,*/,,**,**/*******,**,*******//*,,,***////*//(///(/((((((//((##%%####(/((#(##((###(/****//////////*****/////*
**///***//////////////////////(%#(((((///**,.,*//*,,,,,,,,,,,,,,,,,,,,..........,,,,,,.,,..,**,*/**/////(/(//*/(((((///(/((##(///////////////////////*
**///***////////////////////**/##(#%#((///,,,******,,*,,,,,,,,,,,...........................,,..,.,,*/********////*,*(//(//(#((///////////////////*//*
*////**/////////////////*//////(####(//**,,,,,,,,**,,,,,,,,,,,,,............................,,,,,,,,,,**,*******/**/**///(((((((/////////////////////*
*///***/////////////////*//////#((#((//*,,,..,,***,,,,,,,,,,................................,.,..,,,,,,,,*********/**///*((((#(((/////////////////*//*
*///***//////////////////////*/(#(#(***,,,,..,,***,,,,,,,,........................................,,,,,,,**,*****,*,*/,*//((((#(((////////////////////
*///***///////////////*//(////*##///*/*,,,,,,****,,,,,.,.............................................,,,,,,******,,*,*,***///((((((/////////////////*/
*///***////////////////*/(/////(#(((//*.,,*,,,***,,,,,.,........................ ..................,.,,,,,,******,,,**,**////((#(#((//////////////*///
*/*****///////////////*/*(///*///(//**/**,.,,***,,,,,,................................................,,,,,,,*****,*,,*,*//((((((#((//////////////*/*/
*******///////////////***(///////(//**/,,,,,****,,,,,..................................................,,,,,,*****,*.**,**//(((####((/////////////*///
*******//////////////*/*/(//**///////***,*******,,,,,...................................................,,,,,*******,,,*,*//(((####((////*///////*****
*******//////////////****///*///(((///**********,,,,,,.............        ..... ....... ..............,,,,,,*****/*******//(#((((((////*///////*//*//
*******/////////*///***/**//**///((/////********,,*,,,,,.*,.........                       .......,*,,,,,,,,***/**//////**////((##((////**//////*//**/
*******///////*/*///***/////**/(/(/(////*****,****/*,,**/*(((//(**//,,.....            ....,,*(/////(/(//(//*///*//////////((/((((#(////**//////**/**/
*******///////***//(**(*////(*/(((//////****,,,*//#//(/((/(/(((/(((#(//**,..............,*/(((((((///(//**//(///***/**///*//(/((#((/////***/////******
*******//*//////*///*//**/*(*,*//(//(/**//***,,*////*/**/*,*,,,....,,,,,,,,.........,,,,*****,,,.....,,,****//(/***//*/*//(/////((((////**//////******
*******/**////***//(****////,,,,*///((///****,,*****,,,.,.,//((///***,,.,,*,,......,,,***,,,,**/(///*,,..,,****/*****/////*//,,,((((///****/////******
*******//*///////*/*/***///*,,,.*,,*((#((****,,,,,,,,.,*/(,.,/((/*  ..,..,,,,,,,.,,,***..... .**((//,./(*,,,,*******/*/(//**..,.,(((///***//////*/****
*******//*/////*////****///*,,.,,..,/(#//****,,,,,,,*,,**,,.,.,,.  ..,..,,*,,,,,,,,*****,,,,,,. .,,*,,,***,,,,.,,***/(#/(*,*..,,,(((///***/////*******
*******///////***///***////*,,*,....*((#(****,,,.....,.,......    .....,***,,,,.,,,,******,. ..........,,,,,,,,,,**/((#(,.,,,.*,,(#((///**//////******
******//**/////*////***///**,,*,....*(##/*****,,,,..................,,,,,,,,,,...,,,,,******,,........,....,,,,,**/*/((/,,.,*,,,(###((//***////*******
******////////***///***///***,*,..,,/((((/***,,,,,.........,,,,,,,,.,,,,,,,,,,.....,****,,,,,,,,,,,,,,,,..,.,,,**/*/((((,,.**,,/#(#(#((/***////*******
******///*////**////***///****,,,,,,*(#((/***,,,,,,......,..............,,,,,.......,,,**,,,,....,,,,,,,....,,,,**///((/,.,*,,*(((#((((/***////*******
******///*////**////**////**/*,,,,,,,,/(//***,,,,,.............. ....,,,,,,,.........,,,***,.............,.,,,,,*//(((/*,,,,,,/((#(#((///**////*******
******//**////***//****///**/*,,......,////**,,,,,..................,,,,...,,,,....,,,,,,,,,..........,..,,,,,,**//(/*,,,,,,,*(((##(((//***///********
******///////**/////**////**//*........***//**,,,,,.................,,.....,,,......,,,,,,,,..............,,,,***///,..,,,,,*((((((((///***////*******
*****/****///***///***////**//*,......,,/**/*,,,,,,.................,.,,,,,,,,.....,,***,,,,...............,,***///*.....,,*/(((((((///****///********
*****/***////***///**//*//**///**,..,,.,/**/***,,,,,.................,,,,,,,,,,,,,,,,,,*,,,,,............,,,***////,,,...,,(((((((((///****///********
*****/***///**/*////*////***////*///**,*//*/*,,,,,,,............,,..,.,,.,,.,,**,,,,,,*,,,,,,,.,..........,,***///,..,,,*((((((((((////****/*/*****/*/
*********////****//**////***/////////((((/*/**,,*,,,.......,.,.,,,,,.,,..............,,,.,,,,,,,.........,,****(/((/*/((((((((((((////*****/*/********
**********//****////*///****////*//////(((*/**,,,*,,,...,,...,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,...,,,.,*/***//((((((((((((((((//////******/********
***********/*****////**/****////**///////(///**,.,*,,........,..,,**,/...  .        . ...*/**,,,,,...,.,,,*,**///(((((((((((((((//////******/*********
*****/****//*****///**/*****////*////******///*,,,,,.......,.,....,,***,*,,,,,.,,,,,********,,.,........,**,,///(((((((((((((///***///****************
*****/****/******//*/*/*****///***///******///**,,.*,,...............,,,..............,,,,,,,,,.,,.....,**,**//((((((((///********////****************
,***************//**///******/*************////**,.,,,.....,.........................,,,,.,,,,,,.,....,**,**///(((((((///**********///****************
****************//**/*/******/**************/**/*,,..*,...,...,..........................,,,,,,,.,,,,.*/,**////(((((((//**********////****************
****/***********/*//**/******/**************/**//*,,.,*,,...,,.,,.,,,.....................,,,,,,,,,,,**,**/////((((((///***********/******************
****/************/***///*****/**************//**//*,,,.*,,,,,,,,,.,,,.....................,,*,,,,,,,**,,*///////((((///*******************************
****/************************/***************/***/**,,,.,,*,**,,*,,,.,........   .........,,,,**,,****,**/*/////(((///********************************
*******************/*********/**************,*****/**,,,,,*****,,,,*.,.........    ......,.,,,,****,***/***/,*///////*********************************
*****************//**/*******/**************.,*******,,,,,,,,**,,,,,,............... ....,,,,****,*,,******/..//////**********************************
*****************/////*******/*************,  .,**,,**,,,,,,..,,,*,,,,,.................,,,,**,,,,*********. .,////***********************************
*********************/********************,..   .,,,,,,,,,,.,.,,,,,,*,,,..............,,,,*,,,,,,,***,,*,,  ..,**//***********************************
***/**************////***************//*,,,..     ..,,,,,,,,,,.,..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    ..,,*///**********************************
******************/*****************/****,,.         .,.,.,,,.,.......................,,.,,,,,,,,,,,,,      ..,,**///*********************************
****************/****/******************,,..            ............................,,,,,,,,,,.....         ...,******/*******************************
"""
