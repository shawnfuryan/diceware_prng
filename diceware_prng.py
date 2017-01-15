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

        Each additional word in the passphrase adds around 12.5 bits of entropy, so scale
        your wordcount accordingly. The recommended minimum wordcount is 6, which yields
        ~75 bits of entropy. A 10 word passphrase offers ~125 bits of entropy which
        should not be brute-forceable in the forseeable future.

        Admittedly, this application is somewhat counter to the ideals of diceware.org,
        if you really need very high assurance that the random number generation system
        used to generate your passphrase has not been tampered with, you should still use
        the dice based system described at diceware.org. This program is intended for 
        lower security situations where convenience is more important than strict 
        operational security.  Also, this code has not been audited by security
        professionals, so use at your own risk. The authors of this program disclaim all
        liability associated with the use of this software.

        *note: If not using one of these Operating Systems, it is up to the user to ensure
        that their system provides a cryptographically secure random number generator
        (usually /dev/urandom) that is compatible with python's os.urandom package. Using
        this script in such an environment may yield insecure passwords. This program
        has not necessarily been tested (recently or ever) on all of the listed Operating
        Systems.

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
        

    wordlist_file = 'wordlist.json'
    with open(wordlist_file) as f:
        wordlist = json.load(f)

    passphrase = get_passphrase(wordcount, wordlist)
    click.echo('%s' % ' '.join(map(str, passphrase)))


if __name__ == '__main__':
    passphrase()
