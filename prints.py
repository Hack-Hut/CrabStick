BOLD = "\033[1;01m"
RED = "\033[1;031m"
GREEN = "\033[1;032m"
YELLOW = "\033[1;033m"
BLUE = "\033[1;034m"
RESET = "\033[1;00m"


def prints(msg,  code="success", meth="print", endchar=False):
    """
    Pritty prints a message
    :param msg: Thing to print
    :param code: Success error etc
    :param lvl: loud, quiet, normal
    :return: t/f
    """

    if code == "line":
        line = "-" * 63
        print(f"{BOLD}    \t{line}{RESET}")
        return True

    if code == "info":
        code = BLUE
        symbol = "[Info]"

    elif code == "normal":
        code = ""
        symbol = "  "

    elif code == "success":
        code = GREEN
        symbol = "[Good]"

    elif code == "error":
        code = RED
        symbol = "[Fail]"

    elif code == "warning":
        symbol = "[Warn]"
        code = YELLOW

    elif code == "bold":
        symbol = "\n[<-->]"
        code = BOLD
        print(f"{code}{symbol}\t{msg}{RESET}")
        prints("", "line")
        return True
    else:
        prints("You called the prints function wrong with the parameters", "error")
        prints(f"{msg}", "error")
        prints(f"{code}", "error")
        return False
    if meth == "print":
        if endchar:
            print(f"{code}{symbol}{RESET}\t{msg}{RESET}", end="\r")
        else:
            print(f"{code}{symbol}{RESET}\t{msg}{RESET}")
        return True
    elif meth == "input":
        return input(f"{code}{symbol}{RESET}\t{msg}{RESET}")


