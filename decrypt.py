from Crypto.Cipher import Salsa20

# Opening the ciphertext.txt file
f = open("ciphertext.txt", "r")
# Reading in the single line from the text file and putting it in a variable
hex_ciphertext = f.readline()
# Closing the file
f.close()

# "Decoding" from hex to byte string
strCiphertext = bytes.fromhex(hex_ciphertext)

# Only gets the part we really need to decode, ignores nonce
useableCiphertext = strCiphertext[8:]

# Secret key from the previous program
secretKey = b'*Thirty-two byte (256 bits) key*'
# Hex version of secret key
hex_secretKey = secretKey.hex()
# Hex nonce from the previous program
hex_nonce = "b291496c5686189a"
# Decoding the hex version of the nonce from the previous program
strNonce = bytes.fromhex(hex_nonce)

# Recreating the cipher using the key and nonce
cipher = Salsa20.new(key=secretKey, nonce=strNonce)

# The plaintext
plaintext = cipher.decrypt(useableCiphertext)

print("Ciphertext: " + hex_ciphertext)
print("Key: " + str(hex_secretKey))
print("Nonce: " + str(hex_nonce))
print("Plaintext: " + str(plaintext))

