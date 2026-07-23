from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime, isPrime
import math
import sympy as sp
import secrets

FLAG = b"RVCTF{REDACTED}"
m = bytes_to_long(FLAG)

p = getPrime(1024)
q = getPrime(1024) 

assert isPrime(p)

N = p * q
e = 65537

c = pow(m, e, N)

print(f"{N = }")
print(f"{e = }")
print(f"{c = }")
