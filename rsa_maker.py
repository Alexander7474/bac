from math import gcd
from random import randint
from sympy import randprime
from libnum import invmod
import os

def main(RSAmodule = None, encryptedMessage = None,decryptedMessage = None):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('RSA module saved: '+str(RSAmodule))
    print('Encrypted message saved: '+str(encryptedMessage))
    print('Decrypted message saved: '+str(decryptedMessage))

    print('What to do ?')
    print('1: Make RSA Module')
    print('2: Encrypt a message')
    print('3: Decrypt a message')
    print('4: Exit')
    response = int(input('rp: '))

    if response == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        t = int(input('Give module size t: '))
        RSAmodule = makeModule(t)
        main(RSAmodule,encryptedMessage)
    elif response == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        Message = input('Give the message to encrypt: ')
        os.system('cls' if os.name == 'nt' else 'clear')

        if RSAmodule != None:
            print('There is a saved RSA module: '+str(RSAmodule))
            RSAmoduleSaved = True
        else:
            RSAmoduleSaved = False

        if RSAmoduleSaved:
            print('Do you want to use the saved RSAmodule ?')
            response = input('(y/n): ')
            if response == 'y':
                encryptedMessage = encrypt(Message,RSAmodule[0],RSAmodule[1])
                notSaved = False
            else:
                notSaved = True
        else:
            notSaved = True
        if notSaved:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('1: Make a RSA module')
            print('2: Use public key')
            response  = int(input('rp: '))
            if response == 1:
                t = int(input('Give module size t: '))
                RSAmodule = makeModule(t)
                encryptedMessage = encrypt(Message,RSAmodule[0],RSAmodule[1])
            elif response == 2:
                N = int(input('Give public key N: '))
                e = int(input('Give public key e: '))
                encryptedMessage = encrypt(Message,N,e)
        main(RSAmodule,encryptedMessage,decryptedMessage)
    elif response == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        if encryptedMessage != None:
            print('There is a saved encrypted message: '+encryptedMessage)
            print('Do you want to use the saved encryptred message ?')
            response = input('(y/n): ')
            if response == 'y':
                Message = encryptedMessage
            else:
                Message = input('Give the message to decrypt: ')
        else:
            Message = input('Give the message to decrypt: ')
        os.system('cls' if os.name == 'nt' else 'clear')

        if RSAmodule != None:
            print('There is a saved RSA module: '+str(RSAmodule))
            RSAmoduleSaved = True
        else:
            RSAmoduleSaved = False

        if RSAmoduleSaved:
            print('Do you want to use the saved RSAmodule ?')
            response = input('(y/n): ')
            if response == 'y':
                decryptedMessage = decrypt(Message,RSAmodule[0],RSAmodule[2])
                notSaved = False
            else:
                notSaved = True
        else:
            notSaved = True
        if notSaved:
            os.system('cls' if os.name == 'nt' else 'clear')
            N = int(input('Give private key N: '))
            d = int(input('Give private key d: '))
            decryptedMessage = decrypt(Message,N,d)
        main(RSAmodule,encryptedMessage,decryptedMessage)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

def makeModule(t: int):
    p = randprime(2**(t/2),2**((t+1)/2))
    q = randprime(2**(t/2),2**((t+1)/2))
    prompt = "finding q "
    while p == q:
        os.system('cls' if os.name == 'nt' else 'clear')
        q = randprime(2**(t/2),2**((t+1)/2))
        print(prompt); prompt+='.'
    N = p*q

    EulerN = (p-1)*(q-1)
    e = randint(1,EulerN)
    prompt = "finding e "
    while gcd(e,EulerN) != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        e = randint(1,EulerN)
        print(prompt); prompt+='.'
    d = invmod(e,EulerN)
        
    return (N,e,d)

def encrypt(M,N,e):
    ASCIIencodedMessage = []
    for letters in M:
        ASCIIencodedMessage.append(ord(letters))
    for x in range(len(ASCIIencodedMessage)):
        ASCIIencodedMessage[x] = (ASCIIencodedMessage[x]**e)%N
    encryptedM = ''
    for x in ASCIIencodedMessage:
        encryptedM += chr(x)
    return encryptedM

def decrypt(C,N,d):
    ASCIIencodedMessage = []
    for letters in C:
        ASCIIencodedMessage.append(ord(letters))
    for x in range(len(ASCIIencodedMessage)):
        ASCIIencodedMessage[x] = (ASCIIencodedMessage[x]**d)%N
    decryptedM = ''
    for x in ASCIIencodedMessage:
        decryptedM += chr(x)
    return decryptedM

if __name__ == '__main__':
    main()