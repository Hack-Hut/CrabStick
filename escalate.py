from .heuristics import Heuristics
from .lfi_dictionary_attack import DictionaryAttack
from .prints import prints

SMALL_DICK = "other/small_log_poision"
BIG_DICK = "other/sensitive_files"

class Escalate:
    """Used for handling escilation"""
    def __init__(self, url, payload, request):
        """
        :param url: URL object
        :param payload: Successful payload object
        :param request: Crab request method
        """
        self.url = url
        self.payload = payload
        self.request = request
        self.heuristic = Heuristics(self.url, self.payload, self.request)
        self.parser = self.get_heuristics_parser()
        self.start_escilation()

    def start_escilation(self):
        dictionary_attack = DictionaryAttack(self.request, self.parser, self.payload)
        dictionary_attack.log_poison_dictionary_attack()
        dictionary_attack.large_dictionary_attack()

    def get_heuristics_parser(self):
        """Try and figure out the type of responses a web server will give us"""
        return self.heuristic.get_file_parser()

    def get_status_code_success_check(self):
        return self.heuristic.guess_via_status_code

