import os
import string
import random
from pystrich.datamatrix import DataMatrixEncoder
from random_words import RandomWords

WRITE_PATH = os.getenv('WRITE_PATH','/share')

res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
rw = RandomWords()
word = rw.random_word()
encoder = DataMatrixEncoder(word)
encoder.save(WRITE_PATH.strip("/") + '/' + res + '.png')
print(encoder.get_ascii())