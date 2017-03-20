# CrabStick

A small python tool for automatic local and remote file inclusion exploitation.

. 
![alt text](https://i.gyazo.com/1c8ea2caf7d25124f60635654f6eced6.png "Logo Title Text 1")

## Installation

pip install requests

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

## To Do !

1. Dorks 
2. Base64 
3. Beautiful soup 
4. Comment code 
5. Documentation 

### Author

HackHut

https://www.youtube.com/channel/UC3OAaHAewLkVPu98DL8FR3g

Created as a small project to help me learn






