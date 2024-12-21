#!/bin/env python3

# XOR two bytearrays
def xor(first, second):
    # TODO: complete this function to produce a bitwise XOR
    result = []
    for i in range(min(len(first), len(second))):
           result.append(first[i] ^ second[i])

    return bytearray(result)
# TODO: Get these values from the oracle
IV_BOB  = "486e7f5bbac1ebc3fc09bb30dc4f5417"
IV_BOB_byte = bytearray.fromhex(IV_BOB)

IV_NEXT = "3a1082a6bac1ebc3fc09bb30dc4f5417"
IV_NEXT_byte = bytearray.fromhex(IV_NEXT)

#YES XOR IV_BOB = ATTACK XOR IV_NEXT
#(YES XOR IV_BOB) XOR IV_NEXT = ATTACK


# Construct the guess (with the padding)
YES = b"Yes" + bytes("\x0d"*13, 'utf-8')
NO  = b"No"  + bytes("\x0e"*14, 'utf-8')



# TODO: provide an input plaintext that will recreate the 
#  input Bob might have put in (you'll have to guess either 
#   a "Yes" or "No")
# HINT: Think carefully about the series of XOR operations 
#      that it would take to generate the same ciphertext as
#      Bob, (thereby confirming the same plaintext). Remember
#      that we have a different IV for our encryption block. 
plaintext_guess = xor( xor(YES, IV_BOB_byte), IV_NEXT_byte)

# Print the plaintext in hex, and use this as input to the oracle.
print(plaintext_guess.hex())

