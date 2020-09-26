#!/bin/python3

from Crypto.Util.number import *

n = int(input("ENTER n : "))
e = int(input("ENTER e : "))
c = int(input("ENTER c : "))

print("Find out p and q from factordb")

p = int(input("ENTER P : "))
q = int(input("ENTER q : "))

phi = (p-1)*(q-1)

d = inverse(e,phi)

m=pow(c,d,n)

print("The message is :")
print(m)
print("-"*69)
print("The message after long_to_bytes is :")
print(long_to_bytes(m))



