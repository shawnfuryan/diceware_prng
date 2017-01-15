#!/usr/bin/env python
# -*- coding: utf-8 -*-(PEP 263)

import random
import click
import json

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

RNG = random.SystemRandom()
def rand_idx(end, start=0):
    return RNG.randint(start,end)

def get_passphrase(num_words, wordlist):
    phrase = []
    wordlist_last_idx = len(wordlist)-1
    for word in range(0,num_words):
        word = wordlist[rand_idx(wordlist_last_idx)]
        phrase.append(word)
    return phrase


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--wordcount', type=int,  prompt=True, help='Number of words in passphrase')
def passphrase(wordcount=6):
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

    if wordcount < 6:
        click.echo('ERROR: Diceware passphrases less than 6 words long are no longer '+ 
                   'considered strong.', err=True)
        click.echo('       Please choose a higher wordcount.', err=True)
        exit() 
    if wordcount > 1000:
        click.echo('ERROR: Your enthusiasm is appreciated, but that many words is on the '+
                   'verge of being difficult to memorize.', err=True)
        click.echo('       Please choose a smaller wordcount.', err=True)
        exit()
        

    filename = 'wordlist.json'
    with open('wordlist.json') as f:
        wordlist = json.load(f)

    passphrase = get_passphrase(wordcount, wordlist)
    #print('%s' % ' '.join(map(str, passphrase)))
    click.echo('%s' % ' '.join(map(str, passphrase)))

    return None

if __name__ == '__main__':
    passphrase()
