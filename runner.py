#!/usr/bin/python3

from Algorithm import *

if __name__ == '__main__':
    print('\nWelcome to the Cryptultimate!\n')

    count = 2
    p = 0
    q = 0
    for i in range(99999980, 999999800):
        if fermat_primality_test(i):
            print('{} is prime? {}'.format(i, fermat_primality_test(i)))

            count -= 1
            if count == 0: break
    
        