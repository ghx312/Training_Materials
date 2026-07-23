from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

FLAG = b"RVCTF{REDACTED}"
m = bytes_to_long(FLAG)

p = getPrime(512)
q = getPrime(512)
e = 65537
assert p != q

N = p * q
tot_N = (p - 1) * (q - 1)
d = pow(e, -1, tot_N)
c = pow(m, e, N)

print(f"{N = }")
print(f"{c = }")
print(f"{e = }")
print(f"{p = }")
print(f"{q = }")