def encode(s):
    print(s)
    a=[]
    c=ord(s[0])
    for i in s:
        if ord(i)!=c:
            if c>=ord('A') and c<=ord('Z'): c+=32
            else: c-=32
            a.append(chr(c))
            c=ord(i)
    if c>=ord('A') and c<=ord('Z'): c+=32
    else: c-=32
    a.append(chr(c))
    ans=""
    while len(a)!=0:
        ans+=a.pop()
    print(ans)

encode('SuDin')
encode('aaaaEEeeecccCCCGEExffe')


def prime(n):
    no=n
    i=2
    p=True
    while i*i<=n:
        if n%i==0:
            p=False
            break
        i+=1

    if p and no!=1: print(no,"is prime")
    else: print(no,"is not prime")

prime(1)
prime(2)
prime(3455665)
prime(998244353)