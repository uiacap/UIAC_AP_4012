import random
import math

SEED = 17


def is_prime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False
    

def is_relative_prime(e, phi):
    if math.gcd(e, phi) == 1:
        return True
    else:
        return False
    

def pick_exponent(phi):
    e_found = False
    while not e_found:
        e = random.randint(2, phi - 1)
        if is_relative_prime(e, phi):
            e_found = True
    return e


def public_key(p, q, e):
    n = p * q
    return n, e


def private_key(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    random.seed(SEED)
    k = random.randint(2, phi - 1)
    d = ((k * phi) + 1) // e
    return n, d


p = int(input())
q = int(input())

if is_prime(p) and is_prime(q):
    phi = (p - 1) * (q - 1)
    e = pick_exponent(phi)
    n, e = public_key(p, q, e)
    print(n, e)
    n, d = private_key(p, q, e)
    print(n, d)

else:
    print(False)
