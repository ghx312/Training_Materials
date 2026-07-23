from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import math
import secrets

FLAG = b"RVCTF{REDACTED:3}"
m = bytes_to_long(FLAG)

p = getPrime(512)
q = getPrime(512)
N = p * q

totn = (p - 1) * (q - 1)
max_d = int((N ** 0.25) / 3)

d = secrets.randbelow(max_d)
while True:
    if d % 2 != 0 and math.gcd(d, totn) == 1:
        break
    d -= 1

e = pow(d, -1, totn)
c = pow(m, e, N)

print(f"{N = }")
print(f"{c = }")
print(f"{e = }")