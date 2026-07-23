from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime

FLAG = b"RVCTF{REDACTED}"
m = bytes_to_long(FLAG)

p_lst = [getPrime(64) for _ in range(10)]
e = 65537

N = 1
for i in range(len(p_lst)):
    N *= p_lst[i]

tot_N = 1
for i in range(len(p_lst)):
    tot_N *= p_lst[i] - 1

d = pow(e, -1, tot_N)
c = pow(m, e, N)

print(f"{N = }")
print(f"{c = }")
print(f"{e = }")