"""This class is used for sending the HTTP requests and handling multi-threading"""

import requests
from general_func import GenralFunc
import urllib.parse as urlparse
import pyspeedtest

class CrabRequests:
    def __init__(self, url):
        self.url = url
        self.test = self.TestConect(url)
        pass

    class TestConect:
        """Class used for testing init requests"""
        def __init__(self, url):
            self.url = url
            pass

        def urlparse(self, url):
            """
            Parse the URL to get the GET parameters
            :param url: URL to parse
            :return: A dictionary of parameters
            """
            print(type(urlparse.urlparse(url)))
            return urlparse.urlparse(url)


        def target_up(self, url):
            """
            Is the target Up?
            :param url: url to test
            :return: No | yes
            """
            try:
                r = requests.head(url)
            except requests.ConnectionError:
                GenralFunc.pprint("Connection Error: \t" + url, "fail")
                return -1
            except requests.exceptions.MissingSchema:
                GenralFunc.pprint("Malformed URL:\t" + url , "fail")
                return -1

            GenralFunc.pprint("Recived HTTP status code " + str(r.status_code), "normal")
            if r.status_code == 200:
                GenralFunc.pprint(url + "\treturned " + str(200), "success")
                return 1
            else:
                status_code = str(r.status_code)
                try:
                    with open("../Other/HTTP_status_codes", "r") as file:
                        collection = file.readlines()
                except {FileExistsError, FileNotFoundError}:
                    GenralFunc.pprint("It looks like the file located at Crabstick-2.0.0/Other/HTTP_status_codes", "fail")
                    GenralFunc.pprint("Try and update Crabstrick")
                    return -1
                for codes in collection:
                    try:
                        if status_code in codes.split("%%")[0].lower():
                            code = str(codes.split("%%")[0].lower()).strip()
                            name = str(codes.split("%%")[1].lower()).strip()
                            description = str(codes.split("%%")[3].lower()).strip()
                            succ_fail_warning = str(codes.split("%%")[2].lower()).strip()
                            if "success" in succ_fail_warning.lower():
                                GenralFunc.pprint("HTTP_STATUS CODE: " + code, "success")
                                GenralFunc.pprint("NAME: " + name, "success")
                                GenralFunc.pprint("DESCRIPTION: " + description, "success")
                                return 1
                            elif "warning" in succ_fail_warning.lower():
                                GenralFunc.pprint("HTTP_STATUS CODE: " + code, "warning")
                                GenralFunc.pprint("NAME: " + name, "warning")
                                GenralFunc.pprint("DESCRIPTION: " + description, "warning")
                                return 1
                            elif "fail" in succ_fail_warning.lower() :
                                GenralFunc.pprint("HTTP_STATUS CODE: " + code, "fatal")
                                GenralFunc.pprint("NAME: " + name, "fatal")
                                GenralFunc.pprint("DESCRIPTION: " + description, "fatal")
                                return -1
                    except IndexError as e:
                        GenralFunc.pprint("Crabsticks could not understand the HTTP_Status code", "fail")
                        return -1
                return -1

        def connection_quality(self):
            """Tests the quality of the connection"""
            #
            #   DO THE REST
            #
            GenralFunc.pprint("Testing networking connection quality", "normal")
            GenralFunc.pprint("Connection quality OK", "success")
            pass

        def find_tech(self):
            """Finds what background technology is running on the server (php, asp, jsp ... etc)"""
            pass




    class Cookies:
        """Sends payload via cookie"""
        def __init__(self):
            pass

    class Post:
        """Sends payload via a POST request"""
        def __init__(self):
            pass

    class Get:
        """Sends payload via a GET request"""
        def __init__(self):
            pass

    class Crawler:
        """Class used for crawlers"""
        def __init__(self):
            pass

        def send(self):
            pass
