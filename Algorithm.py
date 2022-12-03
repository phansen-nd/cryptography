import random

class SimpleRsa:
    def pick_base_primes(self) -> int:
        print()

def fermat_primality_test(number) -> bool:
    if number < 2: return False
    for time in range(3):
        randomNumber = random.randint(2, number) - 1
        
        # Test if a^(n-1) = 1 mod n
        if pow(randomNumber, number - 1, number) != 1:
            return False
    
    return True
