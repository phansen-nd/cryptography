import random
import math
from dataclasses import dataclass

@dataclass
class RsaPublicKey:
    n: int
    e: int

@dataclass
class RsaPrivateKey:
    p: int
    q: int
    n: int
    d: int

class SimpleRsa:
    def __init__(self, key_length):
        self.key_length = key_length
        self.p, self.q = self.get_two_primes_whose_product_is_of_length()
        self.n = self.p * self.q
        self.m = (self.p - 1) * (self.q - 1)
        self.e = self.find_coprime_with(self.m)
        self.d = pow(self.e, -1, self.m)

        self.public_key = RsaPublicKey(self.n, self.e)
        self.private_key = RsaPrivateKey(self.p, self.q, self.n, self.d)

    def print_keys(self):
        print('public key is {}'.format((self.public_key)))
        print('private key is {}'.format((self.private_key)))

    # Returns a prime n bits in length
    def pick_prime_of_size(self, n) -> int:
        lower = pow(2, n - 1) + 1
        upper = pow(2, n) - 1

        candidate = random.randint(lower, upper)
        while not self.is_prime_FERMAT(candidate):
            candidate = random.randint(lower, upper)
        return candidate

    def is_prime_FERMAT(self, number) -> bool:
        if number < 2: return False
        for _ in range(3):
            randomNumber = random.randint(2, number) - 1
            
            # Test if a^(n-1) = 1 mod n
            if pow(randomNumber, number - 1, number) != 1:
                return False
        
        return True

    def number_of_bits(self, number) -> int:
        # convert number into it's binary and
        # remove first two characters '0b'.
        binary = bin(number)[2:]
        return len(binary)

    def get_two_primes_whose_product_is_of_length(self):
        p = self.pick_prime_of_size(self.key_length / 2 - 1)
        q = self.pick_prime_of_size(self.key_length / 2 + 1)
        return p, q

    def find_coprime_with(self, m) -> int:
        e = random.randint(2, m - 1)
        while math.gcd(e, m) != 1:
            e = random.randint(2, m - 1)
        return e

    @staticmethod
    def encrypt(plaintext, public_key) -> str:
        n, e = public_key.n, public_key.e
    
        encrypted = ''
        for letter in plaintext:
            # Note: we could have also used our rsa_encrypt function here instead
            encrypted = encrypted + chr((ord(letter) ** e) % n)
            
        return encrypted

    @staticmethod
    def decrypt(ciphertext, private_key) -> str:
        n, d = private_key.n, private_key.d
        
        decrypted = ''
        for letter in ciphertext:
            # Note: we could have also used our rsa_decrypt function here instead
            decrypted = decrypted + chr((ord(letter) ** d) % n)

        return decrypted
