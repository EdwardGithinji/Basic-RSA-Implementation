"""
Author: Edward Githinji

This is my python3 code implementing the RSA algorithm for decimal numbers.
"""
import math

message=eval(input('Enter your message as a decimal number: '))

#Created a function called primecheck for checking if numbers entered are prime 
def primecheck(num):
    L=[]
    for i in range(1,num+1):
        if num%i==0:
            L.append(num)
    if len(L)>2:
        return False

#Function enternums used for entering the numbers p and q used in encryption
    
def enternums():
    primep=eval(input("Enter your prime number p: "))
    while primecheck(primep) is False:
        primep=eval(input("Thats not a prime number,enter your prime number p: "))
        primecheck(primep)
    primeq=eval(input("Enter your prime number q: "))
    while primecheck(primeq) is False:
        primeq=eval(input("Thats not a prime number,enter your prime number q: "))
        primecheck(primeq)

    return [primep, primeq]

Primes=[]
for m in enternums():
    Primes.append(m)

#Function modulo obtains the encryption and decryption values used in obtaining public and private keys respectively
def modulo():
    G=[]
    Dec=[]
    prime_n=Primes[0]*Primes[1]         #obtain N
    #prime_n should be larger than the message for RSA to work.
    if prime_n>message:
        phi_n=(Primes[0]-1)*(Primes[1]-1)   #obtain phi(n); (p-1)*(q-1)
        
        #gcd of encryption key and phi(n) should be 1
        for e in range(2,phi_n):
            if math.gcd(e,phi_n)==1:
                G.append(e)
        enc_key=G[0]
        
        #encryption key * decryption key modulus phi(n) should be 1
        for d in range(1,phi_n):
            if (enc_key*d)%phi_n==1:
                Dec.append(d)
        dec_key = Dec[0]
        pub_key=[enc_key,prime_n]
        priv_key=[dec_key,prime_n]
        print('The public key is {}, and the private key is {} '.format(pub_key,priv_key))
        return [pub_key,priv_key]
    else:
        return [0,0]

keys=[]
for e in modulo():
    keys.append(e)
pub_key=keys[0]
priv_key=keys[1]

#Function Eencrypt() encrypts the message producing a ciphertext; Ciphertext=(message^public key) modulus N
def Eencrypt():
    if pub_key==priv_key!=0:
        return -1
    elif pub_key==priv_key==0:
        return 0
    else:
        Ciphertext= (message**pub_key[0])%pub_key[1]    #M^e mod N
        return Ciphertext


#Function Edecrypt() decrypts the message producing plaintext message; message=Ciphertext^private key) modulus N
def Edecrypt():
    if Eencrypt()==-1:
        print('Select Other Prime numbers as encryption will surely be compromised if private and public keys are similar')
    elif Eencrypt()==0:
        print('Choose larger prime numbers.')
    else:
        print('Encrypted message as ciphertext sent is {} '.format(Eencrypt()))
        dmessage=(Eencrypt()**priv_key[0])%priv_key[1]  #C^d mod N
        print('Message obtained from decrypted ciphertext at receivers end is {}'.format(dmessage))

Edecrypt()    


