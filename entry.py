from .test_single import TestSingle
from .prints import prints
from .crab_requests import Requests

class Entry:
    def __init__(self, cmd_arguments):
        """Contains all the runtime arguments"""
        self.agent = cmd_arguments['--agent']
        self.black = cmd_arguments['--black']
        self.cookies = cmd_arguments['--cookies']
        self.crawl = cmd_arguments['--crawl']
        self.data = cmd_arguments['--data']
        self.dork = cmd_arguments['--dork']
        self.engine = cmd_arguments['--engine']
        self.follow = cmd_arguments['--follow']
        self.header = cmd_arguments['--http-header']
        self.list = cmd_arguments['--list']
        self.lport = cmd_arguments['--lport']
        self.os = cmd_arguments['--os']
        self.proxy = cmd_arguments['--proxy']
        self.random = cmd_arguments['--random-agents']
        self.rport = cmd_arguments['--rport']
        self.thread = cmd_arguments['--thread']
        self.url = cmd_arguments['--url']
        self.max_depth = cmd_arguments['--max-depth']
        self.local_file = cmd_arguments['--local']
        self.search_term = cmd_arguments['--search']
        self.skip_parameters = self.populate_skips(cmd_arguments["--skip"])
        self.send = Requests(self)

        self.calc_default_settings()
        self.debug = self.get_debug_level(cmd_arguments)
        self.mode = self.get_mode(cmd_arguments)

    def calc_default_settings(self):
        try:
            if self.engine is None:
                self.engine = "Yahoo"

            if self.lport is None:
                self.lport = 1337
            else:
                self.lport = int(self.lport)

            if self.rport is None:
                self.rport = 80
            else:
                self.rport = int(self.rport)

            if self.thread is None:
                self.thread = 10
            else:
                if int(self.thread) <= 20:
                    self.thread = int(self.thread)
                else:
                    prints("Max thread count is 20", "warning")
                    self.thread = 20

            if self.max_depth is None:
                self.max_depth = 10
            else:
                if int(self.max_depth) <= 100:
                    self.max_depth = int(self.max_depth)
                else:
                    prints("Max depth count is 100", "warning")
                    self.max_depth = 100

            if self.local_file is None:
                self.local_file = "/etc/passwd"

            if self.search_term is None:
                self.search_term = "root:x:0:"

        except TypeError:
            prints("Could not parse argument", "error")
            prints("Exiting", "warning")



    @staticmethod
    def populate_skips(skip_list):
        if skip_list is None:
            return list()
        elif "," not in skip_list:
            return list(skip_list)
        else:
            return skip_list.split(",")

    @staticmethod
    def get_debug_level(cmd_args):
        if cmd_args["--verbose"]:
            return "loud"
        if cmd_args["--quiet"]:
            return "quiet"
        return "normal"

    @staticmethod
    def get_mode(cmd_args):
        """Find the mode that crabsticks will run in"""
        if cmd_args["single"]:
            return "single"

        elif cmd_args["list"]:
            return "list"

        elif cmd_args["crawl"]:
            return "crawl"

        elif cmd_args["dork"]:
            return "dork"

        else:
            prints("There was a fatal error in parsing your command line options", "error")
            exit(-1)

    def run(self):
        if self.mode == "single":
            prints("Starting in single target mode")
            test = TestSingle(self)
            test.start()

        if self.mode == "list":
            prints("Starting in list mode")
            # TODO
            pass
        if self.mode == "crawl":
            prints("Starting in crawl mode")
            # TODO
            pass
        if self.mode == "dork":
            prints("Starting in dork mode")
            # TODO
            pass
