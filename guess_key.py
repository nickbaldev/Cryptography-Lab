#!/usr/bin/python3
from Crypto.Cipher import AES

plaintext = bytearray.fromhex('255044462d312e350a25d0d4c5d80a34')
ciphertext = bytearray.fromhex('d06bf9d0dab8e8ef880660d2af65aa82')
iv = bytearray.fromhex('09080706050403020100A2B2C2D2E2F2')

# read in keys.txt
f = open("keys.txt", "r")


for key in f:
    key = key.strip("/n")
    k = key
    key = bytearray.fromhex(key)
   
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    guess = cipher.encrypt(plaintext)
    if guess == ciphertext:
       # If the key is found print:
       print("Key Cracked!:", k)
       exit(0)

# If the key is not found print:
print("Key Not Found :(")
