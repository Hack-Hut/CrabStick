# CRABSTICK-2.0.0
![](https://camo.githubusercontent.com/13c4e50d88df7178ae1882a203ed57b641674f94/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667)


![](temp/Header.gif)


## What

Crabstick is a HTTP/HTTPS _security vulnerability_ scanner that find's LFI/RFI (local and remote file inclusion) and try's to escalate this to gain a remote reverse shell.


Crabstick's is designed to handle, look and feel like SQL-map.

### Motivation

The world needed a hacking tool with crab ASCII art, but did't deserve it.  

### Disclaimer 

This tool is not designed to be a web servers _best friend_. Remember you need to abide by the cLAW. Do not use this tool with out multal agreement with the web-servers owners. The developer of this tool accepts no responsibility of the missus of this tool. 

### Who

This tool is aimed at anyone performing web based security analysis. Although this tool is simple to use it is not aimed at script kiddies. 

## Table of Contents
- Intro
    - [What is Crabstick](#What)
    - [Motivation](#Motivation)
    - [Quick discalimer](#Disclaimer)
    - [Who is this tool aimed at?](#Who?)
- Quick start
    - [Installation](#Installation)
    - [Requirements](#Requirements)
    - [Usage](#Usage)
    - [Documentation](#Documentation)
- What can crabstick do?
    - [Host specification](#How)
    - [Optimization](#How)
    - [Advanced Options](#How)
    - [LFI/RFI Payload Generation](#How)
    - [Filter Evasion](#How)
    - [Upgrade local file inclusion to remote code execution](#How)
    - [Dictionary attack on remote file system](#How)
    - [Reverse shells](#How)
- Tested
    - [Tested with](#Tested)
- Other 
    - [Examples](#Examples)
    - [FAQ](#FAQ)
    - [Credits](#Credits)
    - [Licence](#Licence)
    
### Installation 

`$ sudo git clone https://github.com/Hack-Hut/CrabStick`

`$ sudo sh setup.sh`

### Requirements 
1. Requirements are installed with the setup.sh, but if you want to manually do it, you will need the following:
    * Python (Version 3 and above)
    * Scrapy 
    * Beautiful-soup
    * Requests
    * Url-lib
    * Docopt

### Usage 
`python3 src/crabstick.py --help`

## Documentation

(Work in progress)

### How 

1. **Versatile host specification.** 
    * Single URL 
    * List of URL's (Work in progress) 
    * Crawler (Work in progress)
        * White-list
        * Black-list
2. **Plenty of timing optimization.**
    * Os/web-service  specification to target payloads 
    * Threads
    * Rate limiting (Work in progress)
3. **Plenty of advanced options.**
    * Headers (Work in progress)
    * Proxy (Work in progress)
    * User-agents (Work in progress)
    * Randomize user-agents (Work in progress)
    * cookies 
4. **Generate payloads to exploit local and remote file inclusion.**
    * Directory Transferal
    * Null-byte injection
    * Truncation
    * Remote File inclusion
    * Wrappers (Work in progress)
        * php://filter 
        * php://zip 
        * php://data 
        * php://phar 
        * php://expect 
        * php://input     
5. **Filter evasion**
    * Payload encoder
    * Payload double encoder
    * Payload obfuscation 
6. **Upgrade Local file inclusion to remote code execution.** 
    * Log poisioning (Work in progress)
        * Apache
        * Apache2
        * Vsftpd
        * SSHd
        * Mail
    * PHP cookie session injection (Work in progress)
7. **If Crabsick cannot escilate to RCE, a dictionary attack on sensitive file's can be performed.**
    * Use HTTP status codes to find out if the file:(Work in progress)
        * Is readable
        * Is does not exist 
        * Is not readable by the current user 
    * Download these files locally for further inspection 
    * Custom dictionary attacks possible.  
8. **Post exploitation remote reverse shell injector.** 
    * Yeah BABY 
    * Types of shells available (Work in progress)
        * Pentest monkey
        * Metasploit multi-handler 
        * Netcat reverse shell
        * Python reverse shell 
        * Bash reverse shell
        * Perl reverse shell 
        * PHP reverse shell 
        * Ruby reverse shell 
        * Java reverse shell 
        * Xterm reverse shell 
        * Crabstick basic 
9. **Generate file that contain embeded PHP code that can bypass AV dettection.
    * Images (Work in progress)
        * PNG
        * JPEG
        * Gif
    * PDF's  (Work in progress)
    * Audio (Work in progress)
        * MP3
        * Wav
    * Power-Point (Work in progress)
    
 
 ### Tested 
 Tested on Ubuntu 4.15.0-36-generic with python 3.6.6
 
 ### Credit 
 Windows Local-File-Inclusion
 * https://blog.rapid7.com/2016/07/29/pentesting-in-the-real-world-local-file-inclusion-with-windows-server-files/
 
 Local file inclusion cheat-sheets  
 * https://github.com/swisskyrepo/PayloadsAllTheThings/
 * https://highon.coffee/blog/lfi-cheat-sheet/
 
 ### Advanced remote file inclusion demo
 * https://media.blackhat.com/bh-eu-12/Be'ery/bh-eu-12-Be'ery-FYI_you_got_LFI-WP.pdf 
 
