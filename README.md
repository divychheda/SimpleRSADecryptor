# SimpleRSADecryptor
Here is an easy way to decrypt simple RSA problems 
I use this tool usually for CTF challenges 

RSA is an asymmetric encryption algorithm which relies on our inability to calculate factors of large numbers efficiently for the security of the data.
This program has its limitations, and may not work for extremely large numbers (whose factors we can't possibly know of). Works fine for CTF challenges or basic RSA encryptions.
To understand RSA better:- https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-1/


## Some stuff needed
To get started, we will need python3 with pip installed.
We then need the following packages. Use sudo if not installing inside a virtualenv.
1) Pycryptodome : Crypto.Util libraries of python 
```
$ pip install pycryptodome
```
2) factordb-pycli : Command Line interface of factorDB, fastest way to get factors of large numbers.
```
$ pip install factordb-pycli
```
With that set-up, one can now use the tool to decrypt.

## Usage
We just input the respective values of 'n', 'e', and 'c'. (n,e) is the public key pair and 'c' is the ciphertext.
FactorDB will find the factors of 'n' as 'p' and 'q', which form the private key pair. 
Euler's Totient Function (phi) is then evaluated.
At this point we just need the private exponent 'd' and the work is done. Some modular exponentiation and **BOOM!!** we get the original message.

The original message is usually a long integer,  we encode it into a byte string to reveal the text :).
