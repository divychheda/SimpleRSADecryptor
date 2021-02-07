

from Crypto.Util.number import *
from factordb.factordb import FactorDB

print("Let's try to decrypt RSA encrypted cipher")
n = int(input("ENTER n : "))
e = int(input("ENTER e : "))
c = int(input("ENTER c : "))


f = FactorDB(n) 
f.get_factor_list()
f.connect()
result=f.get_factor_list()

p = result[0]
q = result[1]

phi = (p-1)*(q-1)

d = inverse(e,phi)

m = pow(c,d,n)

print("The message is :")
print(m)
print("-"*70)
print("The message after long_to_bytes is :")
print(long_to_bytes(m))






