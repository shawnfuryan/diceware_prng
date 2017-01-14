#!/usr/bin/env python
# -*- coding: utf-8 -*-(PEP 263)

import pandas as pd
import random
import click

@click.command()
@click.option('--count', default=6, help='Number of words in passphrase')
def passphrase(count):
    r = random.SystemRandom()
    def rand_idx(end, start=0):
        return r.randint(start,end)

    filename = 'wordlist.csv'
    words_df = pd.read_csv(filename, index_col=0)
    def get_passphrase(num_words):
        phrase = []
        for word in range(0,num_words):
            word = words_df['word'][rand_idx(words_df.index[-1])]
            phrase.append(word)
        return phrase


    passphrase = get_passphrase(count)
    print('%s' % ' '.join(map(str, passphrase)))

if __name__ == '__main__':
    passphrase()
