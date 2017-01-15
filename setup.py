from setuptools import setup

setup(
    name='diceware_prng',
    version='0.01',
    py_modules=['diceware_prng'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        diceware_prng=diceware_prng:passhprase
    ''',
)

