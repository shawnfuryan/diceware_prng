#!/usr/bin/env python
# -*- coding: utf-8 -*-(PEP 263)

import random
import click
import json

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
#@click.option('--count', default=6, help='Number of words in passphrase')
@click.option('--wordcount', type=int,  prompt=True, help='Number of words in passphrase')
def passphrase(wordcount):
    """
        diceware_prng.py: Generate strong passphrases without the dice.

        Diceware_PRNG uses the excellent, nearly 8000 word strong Diceware dictionary
        (see: diceware.org) and the cryptographically secure random number genrator
        provided by many operating systems* (like Mac OSX, Windows 7+, Debian/Unbuntu/Mint,
        Redhat/Fedora/CentOS, Arch/Manjaro, BSD, Solaris) to generate strong passphrases.

        Each additional word int he passphrase adds 12.5 bits of entropy, so scale your
        wordcount appropriately. The recommended minimum wordcount is 6, which yields
        ~75 bits of entropy. A 10 word passphrase offers ~125 bits of entoropy which
        should not be brute-forceable in the forseeable future.

        *note: If not using one of these Operating Systems, it is up to the user to ensure
        that their system provides a cryptographically secure random number generator
        (usually /dev/urandom) that is recognized by python's os.urandom package. Using
        this script in such an environment may yield insecure passwords. 

    """
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


    passphrase = get_passphrase(wordcount)
    print('%s' % ' '.join(map(str, passphrase)))

if __name__ == '__main__':
    passphrase()
