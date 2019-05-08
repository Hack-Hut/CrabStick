from .parse_html_content import ParseHTMLContent


class Heuristics:
    """Class used for heuristics for a dictionary attack"""
    def __init__(self, url, payload, crabrequest):
        self.url = url
        self.payload = payload
        self.crabrequest = crabrequest

        self.real = self.Real(self)
        self.fake = self.Fake(self)
        self.normal = self.Normal(self)

        self.guess_via_status_code = self.calc_guess_via_status_code()
        self.parser = ParseHTMLContent(self.real.text, self.normal.text, self.fake.text)

    def calc_guess_via_status_code(self):
        """Used to guess if the payload was successful or not then find the contents of the LFI"""
        # If the real status code is good and the fake one is bad then we
        # have are way of determining if a payload was successful.
        if self.real.status_code != self.fake.status_code:
            if self.real.status_type == "success" or self.real.status_code == "warning":
                if self.fake.status_code == "fail" or self.fake.status_code == "warning":
                    return True
        return False

    def get_file_parser(self):
        return self.parser

    class Normal:
        """Contains information on a normal request that the webservice would receive"""
        def __init__(self, heur):
            self.url = heur.url
            self.payload = heur.payload
            self.crabrequest = heur.crabrequest
            self.response_size = self.get_response_size()
            self.response_time = self.get_response_time()
            self.status_code = self.get_status_code()
            self.text = self.get_text()

        def get_status_code(self):
            return self.payload.initial_status_code

        def get_response_time(self):
            return self.payload.initial_response_time

        def get_response_size(self):
            return self.payload.initial_response_size

        def get_text(self):
            return self.payload.initial_text

        def get_status_type(self):
            return self.payload.initial_status_type

    class Real:
        """Contain information on a real file that was found (previous exploit)"""
        def __init__(self, heur):
            self.url = heur.url
            self.payload = heur.payload
            self.crabrequest = heur.crabrequest
            self.response_size = self.get_response_size()
            self.response_time = self.get_response_time()
            self.status_code = self.get_status_code()
            self.status_type = self.get_status_type()
            self.text = self.get_text()

        def get_status_code(self):
            return self.payload.exploit_status_code

        def get_response_time(self):
            return self.payload.exploit_response_time

        def get_response_size(self):
            return self.payload.exploit_response_size

        def get_text(self):
            return self.payload.exploit_text

        def get_status_type(self):
            return self.payload.exploit_status_type

    class Fake:
        """Contains information on a fake file request"""
        def __init__(self, heur):
            self.url = heur.url
            self.payload = heur.payload
            self.crabrequest = heur.crabrequest
            self.data = self.send_fake()
            self.response_size = self.get_response_size()
            self.response_time = self.get_response_time()
            self.status_code = self.get_status_code()
            self.text = self.get_text()
            self.status_type = self.get_status_type()

        def send_fake(self):
            """Send a request for a non existent file to see the response"""
            fake_file = "/asdf/asd/fas/dfa/sdf/asd/f.txt"
            new_payload = self.payload.new_payload(fake_file)
            new_url = self.payload.weponize(new_payload)
            new_data = self.crabrequest.send_get(new_url)
            return new_data

        def get_status_code(self):
            return self.data.status_code

        def get_response_time(self):
            return self.data.response_time

        def get_response_size(self):
            return len(self.data.text)

        def get_text(self):
            return self.data.text

        def get_status_type(self):
            return self.data.status_type
