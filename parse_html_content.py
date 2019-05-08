from .prints import prints
from bs4 import BeautifulSoup

class ParseHTMLContent:
    """Class used to parse HTML so that we can try and find the content of the Local File Inclusion"""
    def __init__(self, real_text, normal_text, fake_text):
        # Get the raw HTML
        self.real_text = real_text
        self.fake_text = fake_text
        self.normal_text = normal_text

        # Parse the text out of it
        self.real_soup = self.parse_html(real_text)
        self.fake_soup = self.parse_html(fake_text)
        self.normal_soup = self.parse_html(normal_text)

        # Find the best way to split the text
        self.split_char = self.find_split()

        # Convert it to a set
        self.real_set = self.split(self.real_soup)
        self.fake_set = self.split(self.fake_soup)
        self.normal_set = self.split(self.normal_soup)

        # etc/passwd is always the first payload
        self.etc_passwd = self.find_file_contents()

        # Do the math
        #self.file_content = self.find_file_contents(self.real_text)
        self.error_content = self.find_error_message()
        self.static_content = self.find_static_content()


    @staticmethod
    def parse_html(text):
        return BeautifulSoup(text, 'lxml').text

    def find_split(self):
        """Looks for the correct split in the real payload"""
        temp_one = self.real_soup.split("\n")
        temp_two = self.real_soup.split("\n\n")
        one_count = 0
        two_count = 0
        for line in temp_one:
            if ":x:" in line:
                one_count += 1

        for line in temp_two:
            if ":x:" in line:
                two_count += 1

        if one_count < two_count:
            return "\n"

        elif two_count < one_count:
            return "\n\n"

        else:
            # TODO add a better return for failure
            return "\n"

    def split(self, text):
        return set(text.split(self.split_char))

    def new_real(self, text):
        self.real_soup = self.parse_html(text)
        self.real_set = self.split(self.real_soup)

    def find_file_contents(self):
        file_content = self.real_set - self.fake_set - self.normal_set
        return file_content

    def find_error_message(self):
        error_message = self.fake_set - self.real_set - self.normal_set
        return error_message

    def find_static_content(self):
        static_content = self.fake_set & self.real_set & self.normal_set
        return static_content


