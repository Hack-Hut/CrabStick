# -*- coding: utf-8 -*-
"""CrabStick:
           .____.
      \)__/\ oo \/\__(/
        _/\/_~__\/\_
________ _/      \_    __.     _________ __   __        __
\_   ___\ HACK_HUT __ \_ |__  /   _____//  |_|__| ____  |  | __
 |   \  \/\_  __ \__  \ | __ \ \_____  \\   __\  |/ ___\|  |/ /
 |   \_____|  | \// __ \| \_\ \/        \|  | |  \  \___|    <
 \______  /|__|  (______/_____/_________/|__| |__|\_____>__|_ \

        \/  A tool for HTTP file inclusion exploits

Usage:
    crabsticks.py single --url=<url>
                  [--thread=<n> ,--request=<n>, --os=<os>]
                  [--data=<data, --proxy=<host:port>, --agent=<agent>, --random-agents]
                  [--cookies <cookie:value>, --http-header=<header>]
                  [--skip=<parameter>, --max-depth=<n>,]
                  [(--local=<file>, --search=<term>)]
                  [(--lport=<port>, --rport <port>)]
                  [-q, | -v]
                  [--help]
    crabsticks.py list --list=<list.txt>
                  [--thread=<n> ,--request=<n>, --os=<os>]
                  [--proxy=<host:port>, --agent=<agent>, --random-agents]
                  [--cookies <cookie:value>, --http-header=<header>]
                  [--skip=<parameter>, --max-depth=<n>,]
                  [(--lport=<port>, --rport=<port>)]
                  [(--local=<file>, --search=<term>)]
                  [-q, | -v]
                  [--help]
    crabsticks.py crawl --url=<url>
                  [--follow, --black=<list.txt>]
                  [--thread=<n> ,--request=<n>, --os=<os>]
                  [--proxy=<host:port>, --agent=<agent>, --random-agents]
                  [--cookies <cookie:value>, --http-header=<header>]
                  [--skip=<parameter>, --max-depth=<n>,]
                  [(--local=<file>, --search=<term>)]
                  [(--lport=<port>, --rport <port>)]
                  [-q, | -v]
                  [--help]
    crabsticks.py dork --dork=<url>
                  [--thread=<n> ,--request=<n>, --os=<os>]
                  [--proxy=<host:port>, --agent=<agent>, --random-agents]
                  [--cookies <cookie:value>, --http-header=<header>]
                  [--skip=<parameter>, --max-depth=<n>,]
                  [(--local=<file>, --search=<term>)]
                  [(--lport=<port>, --rport <port>)]
                  [-q, | -v]
                  [--help]
Options:
    Single:
        --url <url>                         Url to test.
    List:
        --list <list.txt>                   A text file containing a list of urls to test, separated by new line
                                            characters.
    Crawl:
        --crawl <url>                       A URL to crawl.
        -f, --follow                        Follow external links.
        --black <list.txt>                  A text file containing black listed URL's separated by new lines.
    Dork:
        --dork <dork>                       A dork for the search engine to use (defaults to Yahoo)
        --engine <engine>                   Select a different search engine (Google, Bing, Yahoo)

    Timing:
        -t <number>, --threads <number>     Number of threads [default: 1]
        -r <number>, --rate-limit <number>  Limit the number of requests per second
        --os <w|l>                          The target operating system (Windows, Linux), defaults to Linux

    Connection Settings:
        --data=<data>                       POST data, instead of GET request
        --proxy=<host:port>                 Proxy <host>:<port>
        --agent=<agent>                     Change user-agents
        --random-agents                     Randomize user-agents
        --cookies=<cookie:value>            Specify cookies e.g "Name=Admin; PHPSESSID="1"
        --http-header=<header>              Specify a header

    Payload:
        --skip=<file, id>                   List of GET parameters not to test
        --max-depth=<n>                     Maximum number of directories to transverse
        --local=<file>                      Local file (default: "/etc/passwd")
        --search=<term>                     File search term  (default: "root:x:0:")

    Shell Settings:
        --lport=<port>                      Specify a local port for the reverse shell to connect back to (default 1234)
        --rport=<port>                      Specify a remote port for the target to open during shell

    Verbose:
        -q --quiet                          SHHHHHHHH!!!!
        -v --verbose                        AHHHHHHHH!!!!

    Other:
        -h, --help                          Shows this help page.
"""
from docopt import docopt

from src.entry import Entry
from src.prints import prints


def banner():
    prints("          .____.", "normal")
    prints("     \)__/\ \033[1;032moo\033[1;00m \/\__(/", "normal")
    prints("       _/\/_~__\/\_", "normal")
    prints("_______ _/      \_    __.     _________ __   __        __", "normal")
    prints("_   ___\ \033[1;032mHACK_HUT\033[1;00m __ \_ |__  /   _____//  |_|__| ____  |  | __", "normal")
    prints(" |   \  \/\_  __ \__  \ | __ \ \_____  \\   __\  |/ ___\|  |/ /", "normal")
    prints(" |   \_____|  | \// __ \| \_\ \/        \|  | |  \  \___|    <", "normal")
    prints(" \______  /|__|  (______/_____/_________/|__| |__|\_____>__|_ \\", "normal")
    prints("        \/  ", "normal")
    prints("            \033[1;032mA tool for HTTP file inclusion exploits\033[1;00m", "normal")
    prints("Usage:", "normal")
    prints("python3 crabstick.py --help", "normal")
    prints("", "normal")
    prints("", "line")
    prints("", "normal")


if __name__ == "__main__":
    arguments = docopt(__doc__)
    banner()
    start = Entry(arguments)
    try:
        start.run()
    except KeyboardInterrupt:
        print("")
        prints("Exiting")
