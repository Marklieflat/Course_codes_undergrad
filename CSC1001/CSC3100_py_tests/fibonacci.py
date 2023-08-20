def Fibonaaci(n):
    return additiveSequence(n, 1, 1)

def additiveSequence(n, t0, t1):
    if n == 0: return t0
    if n == 1: return t1
    return additiveSequence(n - 1, t1 % mod, (t0 + t1) % mod)

if __name__ == "__main__":
    n = int(input())
    mod = 998244353
    print(Fibonaaci(n))