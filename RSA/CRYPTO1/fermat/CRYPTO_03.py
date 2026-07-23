from Crypto.Util.number import getPrime, isPrime, bytes_to_long

FLAG = b"RVCTF{REDACTED}"
e = 65537

def gen_pq():
    while True:
        p = getPrime(512)
        if isPrime(p + 2):
            return p, p + 2
        
p, q = gen_pq()
N = p * q   
print(N)
print(pow(bytes_to_long(FLAG), e, N))
print(e)    