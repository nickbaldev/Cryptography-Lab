# !/usr/bin/python3

def xor(bit_str1, bit_str2):

    result = []
    for i in range(min(len(bit_str1), len(bit_str2))):
           result.append(bit_str1[i] ^ bit_str2[i])

    return bytearray(result)

P1_str = "This is a known message!"
C1_str = "a469b1c502c1cab966965e50425438e1bb1b5f9037a4c159"


P1 = bytes(P1_str, 'utf-8')
C1 = bytearray.fromhex(C1_str)

C2_str = "bf73bcd3509299d566c35b5d450337e1bb175f903fafc159"
C2 = bytearray.fromhex(C2_str)



#TODO: Use XOR to find P2:
key = xor(C1, P1)
P2  = xor(C2, key)

print(P2)
