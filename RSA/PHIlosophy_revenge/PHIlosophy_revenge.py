'''
Challenge Description:
Philosophy might have helped you before, but can you do it again?
'''
from Cryptodome.Util.number import bytes_to_long, getPrime, long_to_bytes

FLAG = b"RVCTF{REDACTED}"

p = getPrime(1024)
q = getPrime(1024)
assert p != q
n = p * q
e = 65537
m = bytes_to_long(FLAG)
phi = (p - 1) * (q - 1)
fake_phi = (p + 1) * (q + 1)
combined = phi * fake_phi

c = pow(m, e, n)

print(f"N = {n}")
print(f"c = {c}")
print(f"combined = {combined}")