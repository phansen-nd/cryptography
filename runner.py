#!/usr/bin/python3

from simple_term_menu import TerminalMenu

from Algorithm import *

if __name__ == '__main__':
    print('\nWelcome to the Cryptultimate!\n')

    key_length_options = ['16', '32', '64', '128', '256']
    menu = TerminalMenu(key_length_options, title='Pick a length (in bits) for your key: ')
    index = menu.show()
    length = int(key_length_options[index])
    rsa = SimpleRsa(length)
    rsa.print_keys()

    message = input('Enter a message to be encrypted: ')

    encrypted = SimpleRsa.encrypt(message, rsa.public_key)
    print('encrypted: {}'.format(encrypted))

    decrypted = SimpleRsa.decrypt(encrypted, rsa.private_key)
    print('decrypted: {}'.format(decrypted))

