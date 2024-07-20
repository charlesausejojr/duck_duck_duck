import re
import random
import requests

class Utilities:
    def __init__(self) -> None:
        self.word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        self.response  = requests.get(self.word_site)
        self.words     = self.response.content.splitlines()

    def get_random_word(self):
        rand_word = str(random.choice(self.words))
        return re.findall("'([^']*)'", rand_word)[0]

    def get_random_words(self, num_words : int = 5):
        rand_words = []
        for _ in range(num_words):
            rand_words.append(self.get_random_word())
        return rand_words
