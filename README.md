<snippet>
  <content><![CDATA[
# CrabStick

A tool for automatic local and remote file inclusion exploitation 

## Installation

1.  Cookies
2.  Useragents
3.  Proxies
4.  Payload generator
5.  Automatic mass file retrevial
6.  Spawn reverse netcat connection
7.  Log file posioning to escilate local file inclusion to remote code execution
8.  Spescially craft useragents to escilate local file inclusion to remote code execution
9.  Google dorks
10. Awsome ascii art of crabs

## Aurthor

HackHut
https://www.youtube.com/channel/UC3OAaHAewLkVPu98DL8FR3g

## Installation

Install python requests 
```
pip install requests
```
## Usage
```
Usage: Crab.py [options]

Options:
  -h, --help            show this help message and exit
  -u http://www.somesite.com/index.php?page=, --url=http://www.somesite.com/index.php?page=
                        URL of target
  --crawl               Crawl website enabled
  -v, --verbose         Display more information
  -d, --dork            Search for pages using search engines
  -c CP=H2; Geolocation=Crabland, --cookie=CP=H2; Geolocation=Crabland
                        Cookie for authentication
  -a, --random-agent    Turns random user agents on
  -f /etc/passwd, --file=/etc/passwd
                        File to be included default is /etc/passwd
  -k root:x, --key=root:x
                        Search key for checking if file is included
  -r REMOTE, --remote=REMOTE
                        Enable testing of remote file inclusion
  -s, --stealth         Enable random timing to become more stealthy
  -p http://10.45.16.8:80, --proxy=http://10.45.16.8:80
                        Redirect data through a HTTP proxy
  ```
## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

TODO: Write license
]]></content>
  <tabTrigger>readme</tabTrigger>
</snippet>
