from .prints import prints
import requests
import time
import urllib3

OK = ()
ERROR = ()

STATUS_CODE_LIST = "other/http_status_codes.csv"

class Requests:
    """Just a wrapper for sending requests with the correct user runtime options"""
    def __init__(self, cmd_args):
        self.agent = cmd_args.agent
        self.cookies = self.validate_cookies(cmd_args.cookies)
        self.http_header = cmd_args.header
        self.proxy = cmd_args.proxy

        self.code_dict = self.populate_code_dict()

        self.last_request = None
        self.last_response = None
        self.time_taken = None

    def validate_agent(self):
        # TODO
        pass

    def random_agent(self):
        # TODO
        pass

    def validate_cookies(self, cookies):
        """Validates the cmdline cookies passed to crabsticks"""
        validated_cookies = dict()
        if cookies is None:
            return validated_cookies
        try:
            pairs = cookies.split(";")
            for pair in pairs:
                validated_cookies[pair.split("=")[0]] = pair.split("=")[1]
            return validated_cookies
        except IndexError:
            prints(f"Could not validate cookies {cookies}", "error")
            prints(f'Example:\t cookies="security=low; PHPSESSID=ac342fa8793966be6d0732dc872ca0c9"', "info")
        exit()

    def validate_header(self):
        # TODO
        pass

    def validate_proxy(self):
        # TODO
        pass

    @staticmethod
    def populate_code_dict():
        """Creates a dictionary containing information about status codes"""
        list_of_dicts = []
        with open(STATUS_CODE_LIST, "r") as f:
            for line in f.readlines():
                clean = line.strip("\n")
                data = clean.split(",")
                if "Code" in data[0]:
                    continue
                list_of_dicts.append({"Code": data[0].strip(" "),
                                      "Name": data[1].strip(" "),
                                      "Type": data[2].strip(" "),
                                      "Info": data[3]
                                      })
        return list_of_dicts

    def send_get(self, url):
        """
        Sends a HTTP request
        :param url: URL to send it too
        :return: Returns the request
        """
        start = time.time()
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            r = requests.get(url, headers={'User-Agent': "tettra_"}, cookies=self.cookies, proxies=self.proxy, verify=False)
            self.time_taken = time.time() - start
            self.last_request = r
            return self.get_data()
        except requests.exceptions.ConnectionError as e:
            print()
            prints(str(e), "error")
            print()
            return False
        except requests.exceptions.MissingSchema:
            prints("")

    def get_data(self):
        return self.Status(self.last_request, self.code_dict, self.time_taken)

    class Status:
        """Quick way of getting all the information about a request, if it failed etc"""
        def __init__(self, last_request, code_dict, time_taken):
            self.code_dict = code_dict
            self.last_request = last_request
            self.results = self.parse_status()

            self.response_time = time_taken
            self.status_code = self.results["Code"]
            self.status_name = self.results["Name"]
            self.status_type = self.results["Type"]
            self.status_info = self.results["Info"]
            self.text = last_request.text

        def parse_status(self):
            """
            Calculates the type of status code the last request responded with then uses this to search through the CSV
            dict to grab all the info about that type of request
            :return:
            """
            last_status = self.last_request.status_code
            for dicts in self.code_dict:
                if int(dicts["Code"]) == last_status:
                    return dicts
            prints(f"Status Code not found {self.last_request.status_code}", "error")
            return False

class Request_interface:
    """Dependency injection to allow calling the Requeset class,
    whithout having to have an object with attributes"""
    def __init__(self, agent, cookie, header, proxy):
        self.agent = agent
        self.cookie = cookie
        self.header = header
        self.proxy = proxy

    def get_interface(self):
        return self
