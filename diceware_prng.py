#!/usr/bin/env python
# -*- coding: utf-8 -*-(PEP 263)

import pandas as pd
import random
import pprint

r = random.SystemRandom()
def rand_idx(end, start=0):
    return r.randint(start,end)

filename = 'wordlist.csv'
words_df = pd.read_csv(filename, index_col=0)
def get_passphrase(num_words=6):
    passphrase = []
    for word in range(0,num_words):
        word = words_df['word'][rand_idx(words_df.index[-1])]
        passphrase.append(word)
    return passphrase


passphrase = get_passphrase(10)
print('%s' % ' '.join(map(str, passphrase)))
