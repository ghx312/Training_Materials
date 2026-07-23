from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

FLAG = b"RVCTF{REDACTED}"
m = bytes_to_long(FLAG)

p = getPrime(512)
q_1 = getPrime(512)
q_2 = getPrime(512)
e = 65537
assert p != q_1
assert p != q_2
assert q_1 != q_2

N1 = p * q_1
N2 = p * q_2
tot_N1 = (p - 1) * (q_1 - 1)
tot_N2 = (p - 1) * (q_2 - 1)
d1 = pow(e, -1, tot_N1)
d2 = pow(e, -1, tot_N2)
c1 = pow(m, e, N1)
c2 = pow(m, e, N2)

print(f"{N1 = }")
print(f"{N2 = }")
print(f"{c1 = }")
print(f"{c2 = }")
print(f"{e = }")