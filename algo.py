w, h = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

nod = gcd(w, h)

ans = set()

for i in range(1, int(nod**0.5) + 1):
    if nod % i == 0:
        if i != 1:
            ans.add(i)
        if nod // i > 1:
            ans.add(nod // i)

print(len(ans))
print(*sorted(ans))
