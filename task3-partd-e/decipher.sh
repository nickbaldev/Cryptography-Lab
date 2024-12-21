#~!/bin/bash
# K =  00112233445566778899AABBCCDDEEFF 
# IV = 000102030405060708090a0b0c00e0f

# TODO: fill in the code to create plaintext.txt and plaintext-16.txt
echo -n  "123456789" > plaintext.txt
echo -n "1234567891234567" > plaintext.txt


# TODO: fill in the code to create cipher-xxx.txt [xxx = cbc, cfb, ecb, ofb modes]
#       using the commands from the labpage. 

openssl enc -aes-128-cbc -e -in plaintext.txt -out cipher-cbc.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f


openssl enc -aes-128-cfb -e -in plaintext.txt -out cipher-cfb.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f



openssl enc -aes-128-ecb -e -in plaintext.txt -out cipher-ecb.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f


openssl enc -aes-128-ofb -e -in plaintext.txt -out cipher-ofb.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f


# TODO: fill in the code to create cipher-xxx-16.txt [xxx = cbc, cfb, ecb, ofb modes]
#       using the commands from the labpage with input plaintext-16.txt

openssl enc -aes-128-xxx -e -in plaintext-16.txt -out cipher-xxx-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

openssl enc -aes-128-cbc -e -in plaintext-16.txt -out cipher-cbc-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

openssl enc -aes-128-cfb -e -in plaintext-16.txt -out cipher-cfb-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

openssl enc -aes-128-ecb -e -in plaintext-16.txt -out cipher-ecb-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

openssl enc -aes-128-ofb -e -in plaintext-16.txt -out cipher-ofb-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

# TODO: Here is a template for decrypting encrypted cipher-xxx.txt files. Use this
#       template to create plaintext-xxx.txt [xxx = cbc, cfb, ecb, ofb] for these modes.  
openssl enc -aes-128-cbc -d -in <your_ciphertext.txt> -out plaintext-cbc.txt \
              -K \
              -iv 

openssl enc -aes-128-cbc -d -in cipher-cbc.txt -out plaintext-cbc.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

openssl enc -aes-128-cfb -d -in cipher-cfb.txt -out plaintext-cfb.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f

openssl enc -aes-128-ecb -d -in cipher-ecb.txt -out plaintext-ecb.txt \
              -K 00112233445566778899AABBCCDDEEFF 

openssl enc -aes-128-ofb -d -in cipher-ofb.txt -out plaintext-ofb.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f








# TODO: run the decryption with the option -nopad appended at the end of the command 
#       for each of your cipher-xxx-16.txt to create plaintext-xxx-16.txt [xxx = cbc, cfb, ecb, ofb modes]

openssl enc -aes-128-cbc -d -in cipher-cbc-16.txt -out plaintext-cbc-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f -nopad

openssl enc -aes-128-cfb -d -in cipher-cfb-16.txt -out plaintext-cfb-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f -nopad

openssl enc -aes-128-ecb -d -in cipher-ecb-16.txt -out plaintext-ecb-16.txt \
              -K 00112233445566778899AABBCCDDEEFF -nopad

openssl enc -aes-128-ofb -d -in cipher-ofb-16.txt -out plaintext-ofb-16.txt \
              -K 00112233445566778899AABBCCDDEEFF \
              -iv 000102030405060708090a0b0c00e0f -nopad
              