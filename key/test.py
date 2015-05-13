#coding=utf-8
import os
import rsa
ss = 'mlli5mKd58KlKBNOp5h5MsvuIYy/zzMGXUiemc4ge3gWkIg3oC1S+LSwoaTvRw3PyBZQ4f77E9NiE7m/2f3RlKZ0QmrmUH4TzWEokwzv4kUSByLNYf6VmgTrA1Y/9zKnEiPcyASXT2l8ZRsqXkA0TF49klS+HH+Ej/RJlf98s6o='
privkey = rsa.PrivateKey.load_pkcs1(open('./id_rsa').read())
print rsa.decrypt(ss,privkey)
