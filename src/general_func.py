"""This class is used for genral functionality of such as pretty printing"""

from time import gmtime, strftime

class GenralFunc:
    def __init__(self):
        pass

    def pprint(text, mode, symbol=True):
        debug = '\033[94m'
        success = '\033[92m'
        blink = '\033[5m'
        warning = '\033[93m'
        fail = '\033[91m'
        bold = '\033[1m'
        underline = '\033[4m'
        reset = "\033[;0m"
        dim = "\033[2m"
        fatal = "\033[101m"

        if symbol == False:
            if mode == "debug":
                code = debug
                print(code + text + reset)
            if mode == "success":
                code = success
                print(code + text + reset)
            if mode == "blink":
                code = blink
                print(code + text + reset)
            if mode == "bold":
                code = bold
                print(code + text + reset)
            if mode == "underline":
                code = underline
                print(code + text + reset)
            if mode == "warning":
                code = warning
                print(code + text + reset)
            if mode == "fail":
                code = fail
                print(code + text + reset)
            if mode == "normal":
                print(text)
            return

        time = dim +  "[{0}]". format(strftime("%H:%M:%S", gmtime())) +  reset

        if mode == "debug":
            code = debug
            print("[" + code + "D" + reset + "]"  +  time  + "[" + code + "DEBUG" + reset + "]\t" + code + text + reset)
        if mode == "success":
            code = success
            print("[" + code + "+" + reset + "]"  +  time +  "[" + code + "OK" + reset + "]\t" + code + text + reset)
        if mode == "blink":
            code = blink
            print("[ ]"  +  time + code + text + reset)
        if mode == "bold":
            code = bold
            print("[ ]"  +  time + code + text + reset)
        if mode == "underline":
            code = underline
            print("-"* 65 + "\n[" + code + "*" + reset + "]"  +  time  + code + "----" + text + reset)
        if mode == "warning":
            code = warning
            print("[" + code + "-" + reset + "]" +  time  + "[" + code + "WARNING" + reset + "]" +  code + text + reset)
        if mode == "fail":
            code = fail
            print("[" + code + "!" + reset + "]" +  time  + "[" + code + "FAILURE" + reset + "]" + code + text + reset)
        if mode == "fatal":
            code = fatal
            print("[" + fail + "!" + reset + "]" +  time  + "[" + fail   + "FATAL" + reset + "]\t" + code + text + reset)
        if mode == "normal":
            print("[ ]"  +  time + "[INFO]\t" + text)
