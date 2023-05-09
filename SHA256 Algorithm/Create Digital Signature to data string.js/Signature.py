import hashlib
import rsa

message = b'b40eda4711bfaff62d41b38c8a0444a2ae5ee1f14a9a6b4d800c16916fc80096'

# Generate a key pair
(public_key, private_key) = rsa.newkeys(2048)

# Sign the message with the private key to generate a digital signature
signature = rsa.sign(message, private_key, 'SHA-256').hex()

print("Digital signature:", signature)
print("Public key:", public_key.save_pkcs1(format='PEM').decode('utf-8'))
print("Private key:", private_key.save_pkcs1(format='PEM').decode('utf-8'))
