from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import sympy

FLAG = b"RVCTF{REDACTED}"
m = bytes_to_long(FLAG)

p = getPrime(512)
q = getPrime(512)
N = p * q
e = 3

totn = (p - 1) * (q - 1)

d = pow(e, -1, totn)
c = 8228907262615805960296232646024624600898133677406586770572969912905595231422698060028631034961240821863712686667071375225600622584091542889578635603480307209409425894945125

print(f"{N = }")
print(f"{c = }")
print(f"{e = }")