from .prints import prints
import urllib.parse as urlparse
from .gen_payload_interface import GenPayloadInterface as LocalPayloads

TOKEN = "%%PAYLOAD%%"

class SetupURL:
    """Controls the logic for the single target testing"""
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.skip_parameters = args.skip_parameters

        self.parameters_dictionary = []
        self.tokenized_objects = []
        self.payloads = []
        self.parameters = None
        self.scheme = None
        self.netloc = None
        self.path = None
        self.crab_req = args.send
        self.exploit_list = []
        self.initial_request_data = None
        # TODO test if page is dynamic

    def parse(self):
        parsed_url = urlparse.urlparse(self.url)

        self.netloc = parsed_url.netloc
        self.parameters = parsed_url.query
        self.path = parsed_url.path
        self.scheme = parsed_url.scheme

        prints(f"query: {self.parameters}", "info")
        prints(f"path: {self.path}", "info")
        prints(f"netloc: {self.netloc}", "info")
        prints(f"scheme: {self.scheme}", "info")
        return self.validate_parse()

    def validate_parse(self, get=True):
        """Makes sure that the URL is formatted that crabstricks can understand"""
        if self.netloc is None:
            prints("Malformed URL missing network location ie:", "error")
            prints("www.test.com", "info")
            return False
        if self.scheme == "":
            prints("Malformed URL missing schema ie:", "error")
            prints("https://", "info")
            return False
        if get and self.parameters == "":
            prints("Could not find any parameters to inject ie", "error")
            prints("?file=test.txt", "info")
            return False
        else:
            return True

    def is_target_online(self):
        """
        Display's intial connection information and quality
        :return: True or False
        """
        prints(f"Testing connection to {self.url}")
        if self.crab_req.send_get(self.url):
            self.initial_request_data = self.crab_req.get_data()
        else:
            return False
        if self.initial_request_data.status_type == "fail":
            prints(f"Connection to {self.url} failed horribly :(", "error")
            self.display_info(self.initial_request_data, "error")
            return False

        elif self.initial_request_data.status_type == "warning":
            prints(f"Connection to {self.url} had minor issues :(", "warning")
            self.display_info(self.initial_request_data, "warning")
            return True

        elif self.initial_request_data.status_type == "success":
            prints(f"Connection to {self.url} seems good to me.")
            self.display_info(self.initial_request_data, "success")
            return True

        else:
            prints("Crabsticks could not handle this, look at it in a debugger", "error")

    def display_info(self, data, code="success"):
        prints(f"code:\t{data.status_code}", "info")
        prints(f"name:\t{data.status_name}", "info")
        prints(f"Info:\t{data.status_info}", "info")
        prints(f"Type:\t{data.status_type.upper()}", code)
        self.response_time(data.response_time)

    @staticmethod
    def response_time(rep_time):
        if rep_time < 0.5:
            prints("Response time is good")
        elif rep_time < 1:
            prints("Response time is not the best", "warning")
        else:
            prints("Response time is very slow", "error")
        prints(f"Time: {rep_time}Ms", "info")

    def get_parameters(self):
        return self.parameters_dictionary

    def get_scheme(self):
        return self.scheme

    def get_netloc(self):
        return self.netloc

    def get_path(self):
        return self.path

    def find_injection_points(self):
        """
        Finds all injectable parameters, for example
        "q=asdf&id=1" = [{"param1": "q", "Data": "asdf"}]
        :return: True False
        """
        # Multiple parameters
        if "&" in self.parameters:
            param_and_data = self.parameters.split("&")
            for param in param_and_data:
                param_dict = self.split_injection_points(param)
                if not self.add_parm_to_dict(param_dict):
                    return False
        else:
            param_dict = self.split_injection_points(self.parameters)
            if not self.add_parm_to_dict(param_dict):
                return False
        return True

    @staticmethod
    def split_injection_points(param):
        """
        Splits up parameters into param:value
        :param param: GET parameters and  Value
        :return: dictionary Name:Value
        """
        if param.count("=") == 1:
            param_spit = param.split("=")
            parameter = param_spit[0]
            parameter_value = param_spit[1]
            prints(f"parameter: {parameter}\t value:\t {parameter_value}")
            param_dict = {"Name": parameter, "Value": parameter_value}
            return param_dict
        else:
            prints(f"It looks like the parameter in {param} is malformed", "error")
            prints(f"Crabsticks will not test this parameter", "warning")
            return False

    def add_parm_to_dict(self, param_dict):
        """Checks if the parameter was parsed successfully, then if it was we will add it to the dictionary"""
        param_name = param_dict["Name"]
        if not param_dict:
            return False
        elif param_name in self.skip_parameters:
            prints(f"User requested that the parameter {param_name} is skipped", "info")
            return True
        else:
            self.parameters_dictionary.append(param_dict)
        return True

    def test_parameter(self):
        for parameter in self.parameters_dictionary:
            self.tokenized_objects.append(self.TestParameter(self, parameter))

    def get_payload_list(self, local_file, search_term, max_tran_depth):
        payloads = LocalPayloads(local_file, search_term, max_tran_depth)
        payloads.gen_all()
        self.payloads = payloads.get_payload_list()
        return self.payloads

    def get_tokenized_objects(self):
        return self.tokenized_objects
    

    class TestParameter:
        """
        Class used for testing parameters of a GET request
        """
        def __init__(self, target, parameter):
            # URL
            self.target = target
            self.parameter_name = parameter["Name"]
            self.parameter_value = parameter["Value"]
            self.original_url = target.url
            self.token_url = self.tokenize()
            
            # Initial data
            self.initial_response_time = target.initial_request_data.response_time
            self.initial_status_code = target.initial_request_data.status_code 
            self.initial_status_name = target.initial_request_data.status_name 
            self.initial_status_type = target.initial_request_data.status_type 
            self.initial_status_info = target.initial_request_data.status_info 
            self.initial_text = target.initial_request_data.text 
            
        def tokenize(self):
            """Finds the parameter location and then tokenizes to allow the payload to be injected into that spot"""
            before = self.parameter_name + "=" + self.parameter_value
            after = self.parameter_name + "=" + TOKEN
            return self.original_url.replace(before, after)
        

