import math

def encrypt(p,q,m):
    n = p*q
    pqless1 = (p-1)*(q-1)
    e = 2
    while math.gcd(e,pqless1) != 1:
        e+=1
        print('finding e')
    c = (m**e)%n
    d = 1
    while (e*d)%pqless1 != 1:
        d+=1
        print('finding d')
    return [n,d,c]

def decrypt(n,d,c):
    return (c**d)%n

print('What to do ?')
print('1: encrypt')
print('2: decrypt')
response = int(input('rp: '))

if response == 1:
    p = int(input('donnez p: '))
    q = int(input('donnez q: '))
    m = int(input('donnez m: '))
    result = (encrypt(p,q,m))
    print('n: '+str(result[0]) +'\nd: '+str(result[1]) +'\nc: '+str(result[2]))
elif response == 2:
    n = int(input('donnez n: '))
    d = int(input('donnez d: '))
    c = int(input('donnez c: '))
    print('le nombre était: ' +str(decrypt(n,d,c)))
    