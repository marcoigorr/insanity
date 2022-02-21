import mss
import numpy
import pytesseract


# Question array
question_list = [
    "pisciati",
    "Which component is designed to protect against unauthorized communications to and from a computer",
    "Which command will block login attempts on RouterA for a period of 30 seconds if there are 2 failed login attempts within 10 seconds",
    "What is the purpose of the network security accounting function",
    "What type of attack may involve the use of tools such as nslookup and fping?",
    "Match each weakness with an example",
    "Match the type of information security threat to the scenario",
    "Which example of malicious code would be classified as a Trojan horse",
    "What is the difference between a virus and a worm",
    "Which attack involves a compromise of data that occurs between two end points",
    "Which type of attack involves an adversary attempting to gather information about a network to identify vulnerabilities",
    "Match the description to the type of firewall filtering",
    "What is the purpose of the network security authentication function",
    "Which firewall feature is used to ensure that packets coming into a network are legitimate responses to requests initiated from internal hosts",
    "When applied to a router, which command would help mitigate brute-force password attacks against the router",
    "Identify the steps needed to configure a switch for SSH",
    "What feature of SSH makes it more secure than Telnet for a device management connection",
    "What is the advantage of using SSH over Telnet",
    "What is the role of an IPS",
    "A user is redesigning a network for a small company and wants to ensure security at a reasonable price. The user deploys a new application-aware firewall with intrusion detection capabilities on the ISP connection",
    "What is an accurate description of redundancy?",
    "A network administrator is upgrading a small business network to give high priority to real-time applications traffic. What two types of network services is the network administrator trying to accommodate",
    "What is the purpose of a small company using a protocol analyzer utility to capture network traffic on the network segments where the company is considering a network upgrade",
    "Refer to the exhibit. An administrator is testing connectivity to a remote device with the IP address 10.1.1.1. What does the output of this command indicate",
    "Which method is used to send a ping message specifying the source address for the ping",
    "A network engineer is analyzing reports from a recently performed network baseline. Which situation would depict a possible latency issue",
    "Which statement is true about Cisco IOS ping indicators",
    "A user reports a lack of network connectivity. The technician takes control of the user machine and attempts to ping other computers on the network and these pings fail. The technician pings the default gateway and that also fails. What can be determined for sure by the results of these tests?",
    "tracert -6 www.cisco.com command on a Windows PC. What is the purpose of the -6 command option",
    "Why would a network administrator use the tracert utility",
    "A ping fails when performed from router R1 to directly connected router R2. The network administrator then proceeds to issue the show cdp neighbors command. Why would the network administrator issue this command if the ping failed between the two routers?",
    "A network engineer is troubleshooting connectivity issues among interconnected Cisco routers and switches. Which command should the engineer use to find the IP address information, host name, and IOS version of neighboring network devices?",
    "What information about a Cisco router can be verified using the show version command",
    "Which command should be used on a Cisco router or switch to allow log messages to be displayed on remotely connected sessions using Telnet or SSH",
    "Which command can an administrator issue on a Cisco router to send debug messages to the vty lines",
    "By following a structured troubleshooting approach, a network administrator identified a network issue after a conversation with the user. What is the next step that the administrator should take",
    "Users are complaining that they are unable to browse certain websites on the Internet. An administrator can successfully ping a web server via its IP address, but cannot browse to the domain name of the website. Which troubleshooting tool",
    "An employee complains that a Windows PC cannot connect to the Internet. A network technician issues the ipconfig command on the PC and is shown an IP address of 169.254.10.3. Which two conclusions can be drawn",
    "Refer to the exhibit. Host H3 is having trouble communicating with host H1. The network administrator suspects a problem exists with the H3 workstation and wants to prove that there is no problem with the R2 configuration. What tool could the network administrator use on router R2",
    "Refer to the exhibit. Baseline documentation for a small company had ping round trip time statistics of 36/97/132 between hosts H1 and H3. Today the network administrator checked connectivity by pinging between hosts H1 and H3 that resulted in a round trip time of 1458/2390/6066",
    "Which network service automatically assigns IP addresses to devices on the network",
    "Which command can an administrator execute to determine what interface a router will use to reach remote networks",
    "On which two interfaces or ports can security be improved by configuring executive timeouts",
    "When configuring SSH on a router to implement secure network management, a network engineer has issued the login local and transport input ssh line vty commands. What three additional configuration actions have to be performed to complete the SSH configuration",
    "What is considered the most effective way to mitigate a worm attack",
    "Which statement describes the ping and tracert commands",
    "A technician is to document the current configurations of all network devices in a college, including those in off-site buildings. Which protocol would be best to use to securely access the network devices",
    "Which command has to be configured on the router to complete the SSH configuration",
    "An administrator decides to use WhatAreyouwaiting4 as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use pR3s!d7n&0 as the password on a newly installed router. Which statement applies to the password choice", #uguale
    "An administrator decides to use 5$7*4#033 as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use pR3s!d7n&0 as the password on a newly installed router. Which statement applies to the password choice", #uguale
    "An administrator decides to use 12345678! as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use admin as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use Feb121978 as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use password as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use RobErT as the password on a newly installed router. Which statement applies to the password choice",
    "An administrator decides to use Elizabeth as the password on a newly installed router. Which statement applies to the password choice",
    "A network technician is troubleshooting an issue and needs to verify the IP addresses of all interfaces on a router. What is the best command to use to accomplish the task",
    "Students who are connected to the same switch are having slower than normal response times. The administrator suspects a duplex setting issue. What is the best command to use to accomplish the task",
    "A user wants to know the IP address of the PC. What is the best command to use to accomplish the task",
    "A student wants to save a router configuration to NVRAM. What is the best command to use to accomplish the task",
    "A support technician needs to know the IP address of the wireless interface on a MAC. What is the best command to use to accomplish the task",
    "A network technician is troubleshooting an issue and needs to verify all of the IPv6 interface addresses on a router. What is the best command to use to accomplish the task",
    "A teacher is having difficulties connecting his PC to the classroom network. He needs to verify that a default gateway is configured correctly. What is the best command to use to accomplish the task",
    "Only employees connected to IPv6 interfaces are having difficulty connecting to remote networks",
    "An administrator is troubleshooting connectivity issues and needs to determine the IP address of a website. What is the best command to use to accomplish the task",
    "Only employees connected to IPv6 interfaces are having difficulty connecting to remote networks",
    "What is a characteristic of UDP",
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