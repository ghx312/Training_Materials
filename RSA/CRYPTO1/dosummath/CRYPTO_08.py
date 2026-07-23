from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

FLAG = b"RVCTF{REDACTED}"
m = bytes_to_long(FLAG)

p = getPrime(512)
q = getPrime(512)
N = p * q
e = 65537

totn = (p - 1) * (q - 1)
ppq = p + q

c = pow(m, e, N)

print(f"{N = }")
print(f"{c = }")
print(f"{e = }")
print(f"{ppq = }")