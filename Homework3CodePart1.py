from Crypto.Cipher import Salsa20

# Finding the dollar amount that must be put into the message
# My EUID is ckc0133
dollarAmount = ((0 + 1 + 3 + 3) % 8) + 1

# Expected dollar amount to send to Bob using my EUID is $8

# Plaintext message that we want to encrypt in a standard string format
plaintext = "Pay ${}.00 to Bob".format(dollarAmount)

# Now we want to convert the plaintext message into bytes
convertedPlaintext = bytes(plaintext, 'utf-8')

# The secret key
secretKey = b'*Thirty-two byte (256 bits) key*'
# The secret key being converted into hex for print purposes
hex_secretKey = secretKey.hex()

# The cipher that will be made using the secret key given above
cipher = Salsa20.new(key=secretKey)

# Some nonce 
cipherNonce = cipher.nonce

# The cipher text that will be made from the nonce and encryption key
msg = cipherNonce + cipher.encrypt(convertedPlaintext)

# The cipher nonce being converted to hex for print purposes
hex_cipherNonce = cipherNonce.hex()

# The cipher text being converted to hex for print purposes
hex_cipherText = msg.hex()

print("Plaintext: " + str(plaintext))
print("Key: " + str(hex_secretKey))
print("Nonce: " + str(hex_cipherNonce))
print("Ciphertext: " + str(hex_cipherText))

# This is assuming that the ciphertext.txt is in the same directory as this program
f = open("ciphertext.txt", "a")
f.write(str(hex_cipherText))
f.close()
