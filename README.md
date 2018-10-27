# CRABSTICK-2.0.0

![](temp/Header.gif)

## What is crabstick?

Crabstick is a HTTP/HTTPS _security vulnerability_ scanner that find's LFI/RFI (local and remote file inclusion) and try's to escalate this to gain a remote reverse shell.


Crabstick's is designed to handle, look and feel like SQL-map.

### Motivation

The world needed a hacking tool with crab ASCII art, but did't deserve it.  

### Quick disclaimer 

This tool is not designed to be a web servers _best friend_. Remember you need to abide by the cLAW. Do not use this tool with out multal agreement with the web-servers owners. The developer of this tool accepts no responsibility of the missus of this tool. 

### Who is this tool aimed at?

This tool is aimed at anyone performing web based security analysis. Although this tool is simple to use it is not aimed at script kiddies. 

### What can the crab do? 

1. **Versatile host specification.** 
    * Single URL
    * List of URL's 
    * Crawler
        * White-list
        * Black-list
2. **Plenty of timing optimization.**
    * Os/web-service  specification to target payloads 
    * Threads
    * Rate limiting 
3. **Plenty of advanced options.**
    * Headers 
    * Proxy
    * User-agents 
    * Randomize user-agents 
    * cookies 
    * Proxy 
4. **Generate payloads to exploit local and remote file inclusion.**
    * Directory Transferal
    * Null-byte injection
    * Truncation
    * Remote File inclusion
    * Wrappers
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
    * Log poisioning 
        * Apache
        * Apache2
        * Vsftpd
        * SSHd
        * Mail
    * PHP cookie session injection 
7. **If Crabsick cannot escilate to RCE, a dictionary attack on sensitive file's can be performed.**
    * Use HTTP status codes to find out if the file:
        * Is readable
        * Is does not exist 
        * Is not readable by the current user 
    * Download these files locally for further inspection 
    * Custom dictionary attacks possible.  
8. **Post exploitation remote reverse shell injector.** 
    * Yeah BABY 
    * Types of shells available
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
   