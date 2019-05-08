def yes_no(response, recomended):
    """Chooses between True and False based on user response to a runtime question"""
    first_char = response[0].lower()
    if first_char == "y":
        return True
    if first_char == "N":
        return False
    if first_char is None:
        return yes_no
    else:
        return yes_no(recomended, "a")


def get_number(response, ans_range):
    try:
        response = int(response)
    except ValueError:
        print("returning 1")
        return 1
    options = []
    [options.append(x) for x in range(1, ans_range + 1)]
    if response in options:
        return options.index(response) + 1
    else:
        return 1