#!/usr/bin/python3
import socket
from binascii import hexlify, unhexlify

# XOR two bytearrays
def xor(first, second):
   return bytearray(x^y for x,y in zip(first, second))

class PaddingOracle:

    def __init__(self, host, port) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

        ciphertext = self.s.recv(4096).decode().strip()
        self.ctext = unhexlify(ciphertext)

    def decrypt(self, ctext: bytes) -> None:
        self._send(hexlify(ctext))
        return self._recv()

    def _recv(self):
        resp = self.s.recv(4096).decode().strip()
        return resp 

    def _send(self, hexstr: bytes):
        self.s.send(hexstr + b'\n')

    def __del__(self):
        self.s.close()


if __name__ == "__main__":
    oracle = PaddingOracle('10.9.0.80', 5000)

    # Get the IV + Ciphertext from the oracle
    iv_and_ctext = bytearray(oracle.ctext)

    # This assumes that the oracle is returning three 
    # blocks of ciphertext: the IV, C1 and C2. 
    # TODO: Your task is to figure out how many blocks are 
    # returned by the oracle.ctext command and then 
    # assign it to the ciphertexts. 
    IV    = iv_and_ctext[00:16]
    C1    = iv_and_ctext[16:32]  # 1st block of ciphertext
    C2    = iv_and_ctext[32:48]  # 2nd block of ciphertext
    print("C1:  " + C1.hex())
    print("C2:  " + C2.hex())

    ###############################################################
    # In the experiment, we need to iteratively modify CC1
    # We will send this CC1 to the oracle, and see its response.
    CC1 = bytearray(16)

    CC1[0]  = 0x00
    CC1[1]  = 0x00
    CC1[2]  = 0x00
    CC1[3]  = 0x00
    CC1[4]  = 0x00
    CC1[5]  = 0x00
    CC1[6]  = 0x00
    CC1[7]  = 0x00
    CC1[8]  = 0x00
    CC1[9]  = 0x00
    CC1[10] = 0x00
    CC1[11] = 0x00
    CC1[12] = 0x00
    CC1[13] = 0x00
    CC1[14] = 0x00
    CC1[15] = 0x00

    ###############################################################
    # In each iteration, we focus on one byte of CC1.  
    # We will try all 256 possible values, and send the constructed
    # ciphertext CC1 + C2 (plus the IV) to the oracle, and see 
    # which value result in a valid padding. 
    # As long as our construction is correct, there will be 
    # one valid value. This value helps us get one byte of the encrypted output (D2) 
    # Repeating the method for 16 times, we get all the 16 bytes of D2. 

    P2 = bytearray(0x0 for i in range(16))

    # TODO: K is the 15th byte that we are trying to crack in the example
    #       below. Your task is to generalize this to crack all indices
    #       15th -> 0th byte. 
    K = 1
    for i in range(256):
          CC1[16 - K] = i
          status = oracle.decrypt(IV + CC1 + C2)
          if status == "Valid":
              print("Valid: i = 0x{:02x}".format(i))
              print("CC1: " + CC1.hex())
    # TODO: Find the value of P2[K] if we get a valid padding. 
    # TODO: Setup CCI to decipher P2[K-1]

    ###############################################################

    # Once you get all the 16 bytes of P2 print it out
    print("P2:  " + P2.hex())
