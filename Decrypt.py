from cryptography.fernet import Fernet

# read the key from the file
with open('key.key', 'rb') as key_file:
    key = key_file.read()

# open the encrypted image file
with open('encrypted_image.jpg', 'rb') as encrypted_image_file:
    encrypted_image = encrypted_image_file.read()

# create a Fernet object with the key
fernet = Fernet(key)

# decrypt the image
decrypted_image = fernet.decrypt(encrypted_image)

# write the decrypted image to a file
with open('decrypted_image.jpg', 'wb') as decrypted_image_file:
    decrypted_image_file.write(decrypted_image)
