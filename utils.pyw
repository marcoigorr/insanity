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

# DA MODIFICARE LE RISPOSTE
def getAnswer(text):
    if getQuestion(1) in text:
        return("firewall")
    
    elif getQuestion(2) in text:
        return("30 attempts 2 within 10")

    elif getQuestion(3) in text:
        return("to keep track of the actions of a user")

    elif getQuestion(4) in text:
        return("reconnaissance attack")

    elif getQuestion(5) in text:
        return("configuration weakness - when implementing an access; technological weakness - A network engineer is examinating; security policy weakness -  The network administrator did not") #tabella

    elif getQuestion(6) in text:
        return("information theft - obtaining trade secret illegally; identity theft - pretending to be someone else; data loss - installing virus code; disruption of service - preventing users from accessing") #tabella

    elif getQuestion(7) in text:
        return("written to look like a video game")

    elif getQuestion(8) in text:
        return("Worms self-replicate but viruses do not")

    elif getQuestion(9) in text:
        return("man-in-the-middle attack")

    elif getQuestion(10) in text:
        return("reconnaissance")

    elif getQuestion(11) in text:
        return("based on the port numbers - application filtering; based on whether the traffic is in response - stateful packet inspection; based on web addresses or keywords - URL filtering; based on the IP or MAC - packet filtering ") #tabella

    elif getQuestion(12) in text:
        return("to require users to prove who they are")

    elif getQuestion(13) in text:
        return("stateful packet inspection")

    elif getQuestion(14) in text:
        return("login block-for 60 attempts 5 within 60")

    elif getQuestion(15) in text:
        return("Non mettere 'login command' e 'password cisco'") #tabella

    elif getQuestion(16) in text:
        return("login information and data encryption")

    elif getQuestion(17) in text:
        return("SSH provides secure communications to access hosts")

    elif getQuestion(18) in text:
        return("detecting and blocking of attacks in real time")

    elif getQuestion(19) in text:
        return("layered")

    elif getQuestion(20) in text:
        return("multiple paths between switches to ensure there is no single point of failure")

    elif getQuestion(21) in text:
        return("voice-video")

    elif getQuestion(22) in text:
        return("to document and analyze network traffic requirements on each network segment")

    elif getQuestion(23) in text:
        return("A router along the path did not have a route to the destination")

    elif getQuestion(24) in text:
        return("without specifying a destination IP address")

    elif getQuestion(25) in text:
        return("an increase in host-to-host ping response times")

    elif getQuestion(26) in text:
        return("'U' may indicate that a router along the path did not contain a route to the destination address and that the ping was unsuccessful")

    elif getQuestion(27) in text:
        return("Nothing can be determined for sure at this point")

    elif getQuestion(28) in text:
        return("It forces the trace to use IPv6")

    elif getQuestion(29) in text:
        return("to identify where a packet was lost or delayed on a network")

    elif getQuestion(30) in text:
        return("verify Layer 2 connectivity")

    elif getQuestion(31) in text:
        return("show cdp neighbors detail")

    elif getQuestion(32) in text:
        return("the value of the configuration register")

    elif getQuestion(33) in text:
        return("terminal monitor")

    elif getQuestion(34) in text:
        return("terminal monitor")

    elif getQuestion(35) in text:
        return("Establish a theory of probable causes")

    elif getQuestion(36) in text:
        return("nslookup")

    elif getQuestion(37) in text:
        return("PC cannot-PC is configured")

    elif getQuestion(38) in text:
        return("extended ping")

    elif getQuestion(39) in text:
        return("time delay")

    elif getQuestion(40) in text:
        return("DHCP")

    elif getQuestion(41) in text:
        return("ip route")

    elif getQuestion(42) in text:
        return("console-vty")

    elif getQuestion(43) in text:
        return("RSA-IP-Create")

    elif getQuestion(44) in text:
        return("Download security updates from the operating system vendor and patch all vulnerable systems")

    elif getQuestion(45) in text:
        return("Tracert shows each hop, while ping shows a destination reply only")

    elif getQuestion(46) in text:
        return("SSH")

    elif getQuestion(47) in text:
        return("transport input ssh")

    elif getQuestion(48) in text:
        return("It is strong because it uses a passphrase")

    elif getQuestion(49) in text:
        return("uses a minimum of 10 numbers, letters and special characters") #domanda uguale alla 51

    elif getQuestion(50) in text:
        return("it contains 10 numbers and special characters")

    elif getQuestion(51) in text:
        return("uses a minimum of 10 numbers, letters and special characters") #domanda uguale alla 49

    elif getQuestion(52) in text:
        return("uses a series of numbers or letters")

    elif getQuestion(53) in text: 
        return("It is weak because it is often the default password on new devices")

    elif getQuestion(54) in text: 
        return("uses easily found personal information")

    elif getQuestion(55) in text: 
        return("weak because it is a commonly used password")

    elif getQuestion(56) in text: 
        return("It is weak since it uses easily found personal information")

    elif getQuestion(57) in text:   
        return("weak because it uses easily found personal information")

    elif getQuestion(58) in text: 
        return("show ip interface brief")

    elif getQuestion(59) in text:
        return("show interfaces")

    elif getQuestion(60) in text:
        return("ipconfig")

    elif getQuestion(61) in text: 
        return("copy running-config startup-config")    

    elif getQuestion(62) in text: 
        return("ipconfig getifaddr en0")   

    elif getQuestion(63) in text: 
        return("show ipv6 interface")

    elif getQuestion(64) in text: 
        return("ipconfig")

    elif getQuestion(65) in text: 
        return("show running-config")

    elif getQuestion(66) in text: 
        return("nslookup")

    elif getQuestion(67) in text: 
        return("show running-config")

    elif getQuestion(68) in text: 
        return("UDP reassembles the received datagrams in the order they were received")    

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