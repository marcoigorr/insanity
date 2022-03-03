import mss
import numpy
import pytesseract


# Question array
question_list = [
    "pisciati",
    "A client packet is received by a server. The packet has a destination port number of 22",
    "What does the value of the window size specify",
    "To which TCP port group does the port 414 belong",
    "An administrator is trying to configure the switch but receives the error message that is displayed in the exhibit",
    "What is a user trying to determine when issuing a ping 10.1.1.1",
    "What is a characteristic of a switch virtual interface",
    "Match the descriptions to the terms",
    "What happens when a switch receives a frame and the calculated CRC",
    "Two network engineers are discussing the methods used to forward frames through a switch",
    "Which two issues can cause both runts and giants in Ethernet networks",
    "Which two functions are performed at the LLC sublayer",
    "Which two commands could be used to check if DNS name resolution",
    "A small advertising company has a web server that provides critical business service",
    "Only employees connected to IPv6 interfaces are having difficulty connecting to remote networks",
    "A network administrator is connecting a new host to the Registrar LAN",
    "Match the command with the device mode at which the command is entered",
    "A router boots and enters setup mode",
    "What service is provided by POP3",
    "Two students are working on a network design project",
    "Which command is used to manually query a DNS server to resolve a specific host name",
    "Which PDU is processed when a host computer is de-encapsulating a message at the transport layer",
    "Which two OSI model layers have the same functionality as two layers of the",
    "Which three layers of the OSI model are comparable in function to the application layer of the",
    "What task might a user be trying to accomplish by using the ping",
    "Which two ICMP messages are used by both IPv4",
    "A network technician types the command ping 127.0.0.1",
    "why is it no longer necessary",
    "What does a router do when it receives a Layer 2 frame over the network medium",
    "Which two acronyms represent the data link sublayers that Ethernet",
    "A network team is comparing topologies for connecting on a shared media",
    "Given network 172.18.109.0",
    "Three devices are on three different subnets. Match the network address and the broadcast address",
    "What type of address is 198.133.219.162",
    "What does the IP address 192.168.1.15",
    "Why is NAT not needed in IPv6",
    "What routing table entry has a next hop address associated with a destination",
    "Which term describes a field in the IPv4 packet header that contains a unicast",
    "If the default gateway is configured incorrectly on the host",
    "Which is the compressed format of the IPv6 address",
    "Which IPv6 address is one of the link-local addresses of the workstation",
    "What type of IPv6 address is represented by",
    "Which statement describes network security",
    "Which two devices would be described as intermediary devices",
    "What characteristic describes spyware",
    "The exhibit shows a small switched network and the contents of the MAC address",
    "Which destination address is used in an ARP request frame",
    "PC1 issues an ARP request because it needs to send a packet to PC3",
    "A network administrator is issuing the login block-for 180 attempts 2 within 30 command on a router",
    "Which statement describes the characteristics of packet-filtering and stateful firewalls as they relate",
    "What are two ways to protect a computer from malware",
    "The employees and residents of Ciscoville cannot access the Internet or any remote",
    "Which two statements describe the characteristics of",
    "What OSI physical layer term describes the measure of the transfer of bits across a medium",
    "What is the maximum possible throughput between the PC and the server",
    "Match the description with the media",
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
        return("SSH")
    
    elif getQuestion(2) in text:
        return("the amount of data that can be sent before an acknowledgment is required")

    elif getQuestion(3) in text:
        return("well-known")

    elif getQuestion(4) in text:
        return("The administrator must first enter privileged EXEC mode before issuing the command.")

    elif getQuestion(5) in text:
        return("if there is connectivity with the destination device")

    elif getQuestion(6) in text:
        return("An SVI is created in software and requires a configured IP address and a subnet mask in order to provide remote access to the switch")

    elif getQuestion(7) in text:
        return("CLI - Users interact; GUI - enables the user to interact; KERNEL - The part of the OS; SHELL - the part of the operating") # Tabella

    elif getQuestion(8) in text:
        return("The switch drops the frame.")

    elif getQuestion(9) in text:
        return("Packets can be relayed with errors when fast-forward switching is used.")

    elif getQuestion(10) in text:
        return("half-duplex operations - a malfunctioning NIC")

    elif getQuestion(11) in text:
        return("enables IPv4 - places information in the Ethernet - handles communication between upper layer - adds Ethernet control information") 

    elif getQuestion(12) in text:
        return("nslookup cisco.com - ping cisco.com")

    elif getQuestion(13) in text:
        return("DSL line to another ISP")

    elif getQuestion(14) in text:
        return("show running-config")

    elif getQuestion(15) in text:
        return("192.168.235.234")

    elif getQuestion(16) in text:
        return("R1(config)# - service;\n R1> - enable;\n R1# - copy;\n R1(config-line)# - login;\n R1(config-if)# - ip address") # Tabella

    elif getQuestion(17) in text:
        return("NVRAM")

    elif getQuestion(18) in text:
        return("Retrieves email from ")

    elif getQuestion(19) in text:
        return("peer-to-peer")

    elif getQuestion(20) in text:
        return("nslookup")

    elif getQuestion(21) in text:
        return("segment")

    elif getQuestion(22) in text:
        return("network - transport")

    elif getQuestion(23) in text:
        return("presentation - application - session")

    elif getQuestion(24) in text:
        return("connectivity to the internet")

    elif getQuestion(25) in text:
        return("protocol unreachable - route redirection")

    elif getQuestion(26) in text:
        return("testing the integrity")

    elif getQuestion(27) in text:
        return("the use of full-duplex capable Layer 2 switches")

    elif getQuestion(28) in text:
        return("de-encapsulates the frame")

    elif getQuestion(29) in text:
        return("LLC - MAC")

    elif getQuestion(30) in text:
        return("extended star")

    elif getQuestion(31) in text:
        return("255.255.255.192")

    elif getQuestion(32) in text:
        return(".64 - sub 1 net num;\n .19 - sub 2 broad addr;\n .32 sub 3 net num;\n .79 - sub 1 broad addr;\n .16 - sub 2 net num;\n .39 - sub 3 broad addr ") # Tabella

    elif getQuestion(33) in text:
        return("public")

    elif getQuestion(34) in text:
        return("broadcast address")

    elif getQuestion(35) in text:
        return("Any host or user can get a public IPv6 ")

    elif getQuestion(36) in text:
        return("remote routes")

    elif getQuestion(37) in text:
        return("destination IPv4 address")

    elif getQuestion(38) in text:
        return("unable to communicate with hosts on remote networks")

    elif getQuestion(39) in text:
        return("fe80::220:b3f:f0e0:29")

    elif getQuestion(40) in text:
        return("fe80::30d0:115:3f57:fe4c/128")

    elif getQuestion(41) in text:
        return("loopback")

    elif getQuestion(42) in text:
        return("It ensures sensitive corporate")

    elif getQuestion(43) in text:
        return("wireless LAN controller \n IPS")

    elif getQuestion(44) in text:
        return("software that is installed on a user device")

    elif getQuestion(45) in text:
        return("to all ports except port 4.")

    elif getQuestion(46) in text:
        return("FFFF.FFFF.FFFF")

    elif getQuestion(47) in text:
        return("RT1 will send an ARP reply with its own Fa0/0 MAC address")

    elif getQuestion(48) in text:
        return("a user who is trying to guess a password to access the router")

    elif getQuestion(49) in text:
        return("A packet-filtering firewall typically can filter up to the transport layer, whereas a stateful firewall can filter up to the session layer")

    elif getQuestion(50) in text:
        return("Use antivirus software \n Keep software up to date")

    elif getQuestion(51) in text:
        return("DoS")

    elif getQuestion(52) in text:
        return("Fiber-optic cabling does not conduct electricity \n Fiber-optic cabling is primarily used as backbone cabling")

    elif getQuestion(53) in text: 
        return("throughput")

    elif getQuestion(54) in text: 
        return("128 kb/s")

    elif getQuestion(55) in text: 
        return("STP - industrial \n wireless - most mobility options \n optical fiber - high transmission speed \n coaxial - for television") # Tabella
    
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
