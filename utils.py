import time
import cv2
import mss
import numpy
import pytesseract
import keyboard
import webbrowser
import os
import webview


question_list = [
    "pisciati",
    "Which action is performed by a client when establishing communication with a server via the use of UDP at the transport layer",
    "Which transport layer feature is used to guarantee session establishment",
    "What is the complete range of TCP and UDP well-known ports",
    "What is a socket",
    "A PC is downloading a large file from a server. The TCP window is 1000 bytes",
    "Which factor determines TCP window size",
    "What does a client do when it has UDP datagrams to send",
    "Which three fields are used in a UDP segment header",
    "What are two roles of the transport layer in data communication on a network",
    "What information is used by TCP to reassemble and reorder received segments",
    "What important information is added to the TCP/IP transport layer header",
    "Which two characteristics are associated with UDP sessions",
    "A client application needs to terminate a TCP communication session with a server",
    "Which flag in the TCP header is used in response to a received FIN",
    "Which protocol or service uses UDP for a client-to-server",
    "What is a characteristic of UDP",
    "What kind of port must be requested from IANA in order to be used with",
    "Which three application layer protocols use TCP",
    "Which three statements characterize UDP",
    "Which two fields are included in the TCP header but not in the UDP header",
    "Which field in the TCP header indicates the status of the three-way handshake process",
    "Why does HTTP use TCP as the transport layer protocol",
    "Which two types of applications are best suited for UDP",
    "How are port numbers used in the TCP/IP encapsulation process",
    "In what two situations would UDP be better than TCP as the preferred",
    "What are three responsibilities of the transport layer",
    "Which three statements describe a DHCP Discover message",
    "Which two protocols may devices use in the application process that sends email",
    "What is true about the Server Message Block protocol",
    "What is the function of the HTTP GET message",
    "Which OSI layer provides the interface between the applications used to communicate",
    "Which networking model is being used when an author uploads one",
    "What do the client/server and peer-to-peer network models have in common",
    "In what networking model would eDonkey, eMule, BitTorrent, Bitcoin",
    "What is a common protocol that is used with peer-to-peer applications",
    "What is a key characteristic of the peer-to-peer networking model",
    "The application layer of the TCP/IP model performs the functions of what",
    "What is an example of network communication that uses the client",
    "Which layer in the TCP/IP model is used for formatting, compressing",
    "What is an advantage of SMB over FTP",
    "A manufacturing company subscribes to certain hosted services from its ISP",
    "Which application layer protocol uses message types such as GET, PUT, and POST",
    "What type of information is contained in a DNS MX record",
    "Which three protocols operate at the application layer of the TCP/IP model",
    "Which protocol is used by a client to communicate securely with a web server",
    "Which applications or services allow hosts to act as client and server at the same time",
    "What are two characteristics of peer-to-peer networks",
    "Which scenario describes a function provided by the transport layer",
    "Which three layers of the OSI model provide similar network services to",
    "web server acknowledge after it has received two packets of data from the PC",
    "will the web server acknowledge after it has received three packets of data from the PC",
    "server acknowledge after it has received four packets of data from the PC",
    "The client is requesting TFTP service",
    "The client is requesting FTP service",
    "The client is requesting SSH service",
    "The client is requesting HTTP service",
    "The client is requesting POP3 service",
    "The client is requesting telnet service",
    "The client is requesting SNMP service",
    "The client is requesting SMTP service",
    "The client is requesting HTTPS service",

    ]

def getQuestion(index):
    return question_list[index].lower().replace(" ", "")

def destroy(window):
    while True:
        if keyboard.read_key() == 'x':
            try:
                window.destroy()
            except:
                pass
        else:
            pass
    

def createWindow(answer):
    f = open("text.txt", "a+")
    f.write(answer)
    f.close()
    window = webview.create_window(answer, 'text.txt', width=100, height=50, y=1080)
    webview.start(destroy, window)
    os.remove("text.txt")

# +----------------------------------------------------------------+
# +---------------------- Yanderedev momentum ---------------------+
# +----------------------------------------------------------------+

def giveAnswer(text):
    if getQuestion(1) in text:
        createWindow("The client randomly selects a source port number.")
    
    elif getQuestion(2) in text:
        createWindow("TCP 3-way handshake")

    elif getQuestion(3) in text:
        createWindow("0 to 1023")

    elif getQuestion(4) in text:
        createWindow("the combination of a source IP address")

    elif getQuestion(5) in text:
        createWindow("10 segments")

    elif getQuestion(6) in text:
        createWindow("the amount of data the destination can process at one time")

    elif getQuestion(7) in text:
        createWindow("It just sends the datagrams")

    elif getQuestion(8) in text:
        createWindow("Length, Source Port, Checksum")

    elif getQuestion(9) in text:
        createWindow("identifying, tracking")

    elif getQuestion(10) in text:
        createWindow("sequence numbers")

    elif getQuestion(11) in text:
        createWindow("destination and source port numbers")

    elif getQuestion(12) in text:
        createWindow("Destination devices receive traffic with minimal delay, Received")

    elif getQuestion(13) in text:
        createWindow("FIN;ACK;FIN;ACK")

    elif getQuestion(14) in text:
        createWindow("ACK")

    elif getQuestion(15) in text:
        createWindow("DNS")

    elif getQuestion(16) in text:
        createWindow("UDP reassembles the received datagrams")

    elif getQuestion(17) in text:
        createWindow("registered port")

    elif getQuestion(18) in text:
        createWindow("SMTP FTP HTTP")

    elif getQuestion(19) in text:
        createWindow("provides basic; relies on application; is a low overhead")

    elif getQuestion(20) in text:
        createWindow("window, sequence number")

    elif getQuestion(21) in text:
        createWindow("control bits")

    elif getQuestion(22) in text:
        createWindow("because HTTP requires reliable delivery")

    elif getQuestion(23) in text:
        createWindow("that handle; that can")

    elif getQuestion(24) in text:
        createWindow("If multiple conversations")

    elif getQuestion(25) in text:
        createWindow("when a faster delivery; when applications do not need")

    elif getQuestion(26) in text:
        createWindow("meeting; multiplexing; identifying")

    elif getQuestion(27) in text:
        createWindow("255.255.255.255; a client seeking an IP address; but only a DHCP server replies")

    elif getQuestion(28) in text:
        createWindow("SMTP DNS")

    elif getQuestion(29) in text:
        createWindow("Clients establish a long term connection to servers")

    elif getQuestion(30) in text:
        createWindow("to request an HTML page from a web server")

    elif getQuestion(31) in text:
        createWindow("application")

    elif getQuestion(32) in text:
        createWindow("client/server")

    elif getQuestion(33) in text:
        createWindow("Both models support.")

    elif getQuestion(34) in text:
        createWindow("peer-to-peer")

    elif getQuestion(35) in text:
        createWindow("Gnutella")

    elif getQuestion(36) in text:
        createWindow("resource sharing")

    elif getQuestion(37) in text:
        createWindow("session presentation application")

    elif getQuestion(38) in text:
        createWindow("www.cisco.com")

    elif getQuestion(39) in text:
        createWindow("application")

    elif getQuestion(40) in text:
        createWindow("SMB clients can establish a long-term")

    elif getQuestion(41) in text:
        createWindow("FTP HTTP SMTP")

    elif getQuestion(42) in text:
        createWindow("HTTP")

    elif getQuestion(43) in text:
        createWindow("the domain name mapped to")

    elif getQuestion(44) in text:
        createWindow("FTP POP3 DHCP")

    elif getQuestion(45) in text:
        createWindow("HTTPS")

    elif getQuestion(46) in text:
        createWindow("P2P applications")

    elif getQuestion(47) in text:
        createWindow("decentralized resources, resource sharing")

    elif getQuestion(48) in text:
        createWindow("A student has two web browser windows open in order to access two web sites")

    elif getQuestion(49) in text:
        createWindow("session layer; application layer; presentation layer")

    elif getQuestion(50) in text:
        createWindow("3001")

    elif getQuestion(51) in text:
        createWindow("4501")

    elif getQuestion(52) in text:
        createWindow("6001")

    elif getQuestion(53) in text: # 60 in itexamanswers.net
        createWindow("69")

    elif getQuestion(54) in text: # 61 in itexamanswers.net
        createWindow("21")

    elif getQuestion(55) in text: # 62 in itexamanswers.net
        createWindow("22")

    elif getQuestion(56) in text: # 63 in itexamanswers.net
        createWindow("80")

    elif getQuestion(57) in text: # 64 in itexamanswers.net
        createWindow("110")

    elif getQuestion(58) in text: # 65 in itexamanswers.net
        createWindow("23")

                                  # skipped 66

    elif getQuestion(59) in text: # 67 in itexamanswers.net 
        createWindow("161")

    elif getQuestion(60) in text: # 68 in itexamanswers.net
        createWindow("25")

    elif getQuestion(61) in text: # 69 in itexamanswers.net
        createWindow("443")    

    else:
        createWindow("No answer or question found")

"""
,,,,,,,,,,,,,...........,,,,,,,,,,,,,,.............,,,,,,.........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,.........,,,,,,,,,,,,,,,,**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,***,,,,,.,,,,,.....,.,,,.,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,......,,,,,,,,,,,,,,,,***,,***,,,***,........,,,,*********,***,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,........,.,,.......,,****,**,,*,,**,.......,***,,,*************,*,,,................,.....,
.,,,.,,,,.............,...,,,******,,,,,.........,,,,,,***************,*,,*,*,,,...........,..,.....
.........................,****//*,,*,,,,.............,,,,,,****/*,**,***,,*,,,*,....................
.......................,*/***/*,******,, ..... . .....,,,,,,,*******/,**,/,,,..,....................
......................*,***/**/***/(*/.....*..... ...,*.. ..,*.,,*,,*,*,,,,*,..     ................
.....................,,***/*****/////*,,,/,.***,,..,*,.....,,....,..,,,,,,.,,,.  ..  .....#(/.(.#.#,
.....................,,*,*,,*,*/(,(**,**/**/*/****/*...,,,*, .       ... ,., ....  , ....*###/,,/,#(
.....................,,,**,,**/#*(****((*(///**/*/**,,**,*...,    ..... ..,...  .. .................
....................,,****,,,*(*(***/((/((((///*/********.,,*.....,., ....,. .  ,,....,..../...,(#.#
..................,*,***********(/**##((((((/(/***////******,*******,..,,,,*.,,..***,,*,...#,(.#*#.*
..................****,***,/**/(//*(##((((#((/**//////////******,*****,*,*,**.,*,*////**,...........
..................**/*****//*/(#(((##((((((#///////*///(///*//***////**,*/*//,,/**/*/*/**...(/......
.................,,*,**//*///(##//#%(((((##///(#((///((////(%##%(///##(/#(//(/*//*/(,,,/,...,.,./.*.
.................,*..,////((/(#(**/(%%%%%(//#%##(#####(/%#((###((######%%%#((//((////*..,.........*.
....................,*/*/(((((##((&&&&&#/(#%&&@@@@&&&@@@@@@@&%&@@@@@%%#&&&%#((//((/*/**. ...***,,*,.
...................,**,/((((/(#%%%&@@@@@@@@@@@@@&&%%%&@@@@@@@@@@@@@%%##&&%%#//(//(//,*,,....#.,(.(/.
....................,,,/////((#&###%@@@@@@@@@@@@#/**/#&@@@@@@@@@@@%##@&&####/((/(//*,,..............
.....................,***/*/((#%%%%####%%%##%&%//**,**/#%#((###(((((##%%####((//,/***.......,*,**/*,
.....................,///,((((##%%#(////////((///*****/////********//(####(((/(/*,((,...............
.....................,/(///((((((###(///**//(((//*,,**/////********//((##((((/((//((*........*#/#/.,
......................*(((//((##((((((//////(////*,,**/**(//******///((((((((((//(((,...............
......................*((/(/#(######(((((///(((%#(((/(((/(**/////////(/((((/((#/(((/,...............
......................,/(((/##((######((/////%%(**/(///(///*/*////(////((((###((((/,................
......................,,///(#######((#((/***/***,**/**/***//***////////((((#((//*,,,................
........................,,///((###%#(#(,,,/((((/((*///////(#(****////////*****,,,,..................
........................,,,,,**/(#&%#/,,.,(((#((/*/////((((//,,*//((/(//*****,,,,,..................
.........................,,,,,***/&@%#*,,,///###%%&&%%##(////,,,*(((((&@/***,,,,....................
..........................,,,,,*(@@@@%/*/*(((//////**//////((////####(@@@@#,,,,.....................
............................,,,,@@@@@(/*****##(///((((/////(#**,*/*/(%@@@@@/,.......................
.............................,,#@@@@@((/******//&##########****/#%###@@@@@&*........................
.............................,,#@@@/*/**,*********&@@@@@*****/(%%%#(#@@@@&&#........................
..............................,,@@//**/*************/&***,,**(&%%%##%@@@&&&#........................
..............................%/****************/******/,**/%%%#####%%&&@@&&&.......................
........................,#&&&**************************//*#&%%##(((#&&@@@@&&&&%,....................
.................(&&&&@@&@@///*,,**********************//(&&%#((((#@@@@@@&&&&&&&&%,.................
...........*&&&&&&@&@@@@@@@&(//**********************////%%#(((((&@@@@@@@@&&&&&&&&&&&&&#,...........
....,%&&&&&&&&&&&&@@@@@@@@@@////********************////(%#(((((@@@@@@@@&&&&&@&&&&&&&&&&&&&&&@* ....
&&&@&&&&&&@@@&&&@@@@@@@@@@@@@#//************************(%((/(&@@@@@@@@@@@@@@&@@@&&@@@@@&&&&&&&&&&&&
&&&&@&&&@@@@@&&@@@@@@@@@@@@@@@#/********,***************###&&@@@@@@@@@@@@@@@&&@&@@@@&&&&&&&&&&&&&&&&
&&@@@@@@@@@@@@@&@@@@@@@@@&@@@@@%(//*******,******(((((((((@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&@@@
"""