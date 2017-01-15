diceware_prng.py: Generate strong passphrases without the dice.

Diceware_PRNG uses the excellent, nearly 8000 word strong, collision-free
Diceware dictionary (see: diceware.org) along with python's os.SystemRandom()
which uses the system's cryptographically secure random number generator,
/dev/urandom on most unix-like systems, to generate strong passphrases.

Each additional word in the passphrase adds around 12.5 bits of entropy,
so scale your wordcount accordingly. The recommended minimum wordcount is
6, which yields ~75 bits of entropy. A 10 word passphrase offers ~125 bits
of entropy which should not be brute-forceable in the forseeable future.

Admittedly, this application is somewhat counter to the ideals of
diceware.org, if you really need very high assurance that the random
number generation system used to generate your passphrase has not been
tampered with, you should still use the dice based system described at
diceware.org. This program is intended for  lower security situations
where convenience is more important than strict  operational security.
Also, this code has not been audited by security professionals, so use at
your own risk. The authors of this program disclaim all liability
associated with the use of this software.
