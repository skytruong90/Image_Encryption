from cryptography.fernet import Fernet

# generate a key
key = Fernet.generate_key()

# write the key to a file for later use
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# open the image file to encrypt
with open('image.jpg', 'rb') as image_file:
    image = image_file.read()

# create a Fernet object with the key
fernet = Fernet(key)

# encrypt the image
encrypted_image = fernet.encrypt(image)

# write the encrypted image to a file
with open('encrypted_image.jpg', 'wb') as encrypted_image_file:
    encrypted_image_file.write(encrypted_image)
