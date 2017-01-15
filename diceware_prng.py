#!/usr/bin/env python
# -*- coding: utf-8 -*-(PEP 263)

import random
import click
import json

@click.command()
@click.option('--count', default=6, help='Number of words in passphrase')
def passphrase(count):
    r = random.SystemRandom()
    def rand_idx(end, start=0):
        return r.randint(start,end)

    filename = 'wordlist.json'
    with open('wordlist.json') as f:
        wordsl = json.load(f)
    wordsl_last_idx = len(wordsl)-1
    ##### words_df = pd.read_csv(filename, index_col=0)
    def get_passphrase(num_words):
        phrase = []
        for word in range(0,num_words):
            word = wordsl[rand_idx(wordsl_last_idx)]
            phrase.append(word)
        return phrase


    passphrase = get_passphrase(count)
    print('%s' % ' '.join(map(str, passphrase)))

if __name__ == '__main__':
    passphrase()
