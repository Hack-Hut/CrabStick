# -*- coding: utf-8 -*-
"""CrabStick

Usage:
    crabstick.py (-u <url> |-l <file> | -c <domain>)
                 [-b <file> -w <file>]
                 [-t <n> -r <n>  --os <os> --php --asp]
                 [-f --update --proxy <host:port> --agent <agent> --random-agents --cookies <cookie:value>]
                 [--http-header <value>  --lport <port> --rport <port> ]
                 [-q |-v]

Options:
    Target:
        -u <url>, --url <url>               target url
        -l <file>,  --list-url <file>       list of target url's in a file
    Crawler:
        -c <domain>, --crawl <domain>       domain to crawl [default: False]
        -b <file>, --black-list <file>      black-list urls that start with
        -w <file>, --white-list <file>      white-list urls that start with
    Timing:
        -t <number>, --threads <number>     number of threads [default: 1]
        -r <number>, --rate-limit <number>  limit the number of requests per second [defualt: False]
        --os <os>                           the target operating system (windows, linux) [default: "Unknown"]
        --php                               the target site is running php
        --asp                               the target site is running asp
        --jsp                               the target site is running jsp
    Other:
        -f,  --filter                       perform filter evasion techniques
        --update                            Check if crabsticks is up to date
        --proxy <host:port>                 proxy <host>:<port>
        --agent <agent>                     change user-agents
        --random-agents                     randomize user-agents
        --cookies <cookie:value>            specify cookies
        --http-header <header>                   specify a header
    Shell:
        --lport <port>                      specify a local port for the reverse shell to connect back to (defualt 1234)
        --rport <port>                      specify a remote port for the target to open during shell
    verbose:
        -q --quiet                          SHHHHHHHH!!!!
        -v --verbose                        AHHHHHHHH!!!!

Examples:


"""
from docopt import docopt
import sys
import os
import subprocess

from general_func import GenralFunc
from crab_requests import *


class Domain:
    def __init__(self, docopt, url=False):
        if url == False:
            self.url = docopt["--url"]
        else:
            self.url = url
        self.useragent = docopt["--agent"]
        self.asp = docopt["--asp"]
        self.black_list = docopt["--black-list"]
        self.cookie = docopt["--cookies"]
        self.crawl = docopt["--crawl"]
        self.header = docopt["--http-header"]
        self.lport = docopt["--lport"]
        self.os = docopt["--os"]
        self.php = docopt["--php"]
        self.proxy = docopt["--proxy"]
        self.quiet = docopt["--quiet"]
        self.random_agent = docopt["--random-agents"]
        self.rate_limit = docopt["--rate-limit"]
        self.rport = docopt["--rport"]
        self.thread_count = docopt["--threads"]
        self.verbose = docopt["--verbose"]
        self.white_list = docopt["--white-list"]
        self.filter = docopt["-f"]
        self.get_parameters = None
        GenralFunc.pprint("Target aquired: " + self.url, "underline")
        self.crabrequests = CrabRequests(self.url)

    def start(self):
        if self.crabrequests.test.target_up(self.url) == 1:
            GenralFunc.pprint("Finding GET parameters", "success")
            self.get_parameters = self.crabrequests.test.urlparse(self.url)
            if self.get_parameters != None:
                pass
            else:
                GenralFunc.pprint("Target has no injectable GET parameters", "fail")
        else:
            GenralFunc.pprint("Target connection failed skipping host: " + self.url, "fatal")


def start():
    doc_args = check_env()
    args = parse_cmd_args(doc_args)
    if args:
        return args
    else:
        GenralFunc.pprint("No arguments, something went wrong exiting", "fail")
        exit(-1)

    #test = CrabRequests()
    #test.test.target_up()

def check_env():
    """Checks for relevant python modules, internet connection (proxies), if the project is update"""
    if sys.version_info[0] < 3:
        print("Using python 2 is not supported")
        exit(-1)
    else:
        banner()
        arguments = docopt(__doc__)
        if arguments:
            GenralFunc.pprint("Checking Environment and arguments", "underline")
            GenralFunc.pprint("Using Python 3", "success")
            batcmd="git status"
            try:
                result = subprocess.check_output(batcmd, shell=True).decode().encode('utf-8')
                if b"up-to-date" in result:
                   GenralFunc.pprint("Branch is up to date", "success")
                elif b"not found" in result:
                    pass
                else:
                    GenralFunc.pprint("There is a new version of crabstick available", "warning")
                    GenralFunc.pprint("Update??", "blink")
                    ans = input("N/y:")
                    if "y" in ans.lower():
                        batcmd = "git pull"
                        subprocess.check_output(batcmd, shell=True)
            except Exception as e:
                print(str(e))
                GenralFunc.pprint("Unable to determine if crabstick is up to date", "warning")
                GenralFunc.pprint("try: 'git pull' to check", "warning")
            return arguments
        else:
            GenralFunc.pprint("Looks like we have left to do", "fail")


def banner():
    """Ascii art"""
    GenralFunc.pprint("           ,____,", "bold", symbol=False)
    GenralFunc.pprint("      \)__/\ " "\033[5m" + "oo " + "\033[;0m\033[1m" + "/\__(/", "bold", symbol=False)
    GenralFunc.pprint("        _/\/____\/\_", "bold", symbol=False)
    GenralFunc.pprint("________  /      \_    ___.     _________ __   __        __    ", "bold", symbol=False)
    GenralFunc.pprint("\_   ___\ " + "\033[92m" + "HACK_HUT" + "\033[;0m\033[1m" + " __ \_ |__  /   _____//  |_|__| ____ |  | __", "bold", symbol=False)
    GenralFunc.pprint("/    \  \/\_  __ \__  \ | __ \ \_____  \\   __\  |/ ___\|  |/ /", "bold", symbol=False)
    GenralFunc.pprint("\     \____|  | \// __ \| \_\ \/        \|  | |  \  \___|    < ", "bold", symbol=False)
    GenralFunc.pprint(" \______  /|__|  (______/_____/_________/|__| |__|\_____>__|_ \ ", "bold", symbol=False)
    GenralFunc.pprint("        \/  " + "\033[92m" + " A tool for HTTP file inclusion exploits", "bold", symbol=False)
    GenralFunc.pprint(65 * "_", "underline", symbol=False)
    print(65 * "-")
    GenralFunc.pprint("[!] Remember you need to abide by the \033[91m claw", "bold", symbol=False)
    GenralFunc.pprint(65 * "-", "underline", symbol=False)

def parse_cmd_args(arguments):
    """Reads the commandline args and validates them"""
    #GenralFunc.pprint(str(arguments), "debug")
    GenralFunc.pprint("Success", "success")
    return arguments

if __name__== "__main__":
    args = start()
    if args["-l"]:
        GenralFunc.pprint("List of target mode selected", "underline")
        # Only does this if their is a list of domains
        file = args["-l"]
        with open(file, "r") as f:
            domains = f.readlines()
        domain_class_list = []
        clean = []
        try:
            [clean.append(domains[i].strip()) for i in range(0, len(domains))]
        except Exception:
            GenralFunc.pprint("Looks like their is something wrong with the url list you provided", "fatal")
            exit(-1)
        for i in range(0, len(clean)):
            domain_class_list.append(Domain(args, clean[i]))
    if args["--crawl"] != str(False):
        GenralFunc.pprint("Crawl mode selected", "underline")
        pass
    else:
        # Only does this if their is a single target
        GenralFunc.pprint("Single target mode selected", "underline")
        domain = Domain(args)
        domain.start()

