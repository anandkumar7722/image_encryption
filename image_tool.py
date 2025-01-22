from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
import os
import json

def save_key_to_log(key, file_name):
    """Saves the generated key and associated file name to a log file."""
    log_file = "key_log.json"
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                key_log = json.load(f)
        else:
            key_log = {}

        key_log[file_name] = key.hex()

        with open(log_file, 'w') as f:
            json.dump(key_log, f, indent=4)

    except Exception as e:
        print(f"Error saving key to log: {e}")

def get_key_from_log(file_name):
    """Retrieves the key for a given file name from the log file."""
    log_file = "key_log.json"
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                key_log = json.load(f)
                return bytes.fromhex(key_log.get(file_name, ""))
        else:
            return None
    except Exception as e:
        print(f"Error retrieving key from log: {e}")
        return None

def encrypt_image(input_image_path, output_encrypted_path, key):
    """Encrypts an image using AES encryption."""
    try:
        # Read the image data
        with open(input_image_path, 'rb') as f:
            image_data = f.read()

        # Create AES cipher in CBC mode
        cipher = AES.new(key, AES.MODE_CBC)

        # Pad the image data to match the AES block size
        encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

        # Write the initialization vector (IV) and encrypted data to the output file
        with open(output_encrypted_path, 'wb') as f:
            f.write(cipher.iv)  # Write the IV first
            f.write(encrypted_data)

        print(f"Image successfully encrypted and saved to {output_encrypted_path}")

    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(encrypted_image_path, output_image_path, key):
    """Decrypts an encrypted image back to its original form."""
    try:
        # Read the encrypted data
        with open(encrypted_image_path, 'rb') as f:
            iv = f.read(16)  # Read the first 16 bytes (IV)
            encrypted_data = f.read()  # Read the rest (encrypted data)

        # Create AES cipher in CBC mode with the same IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt and unpad the data
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Write the decrypted data back to an image file
        with open(output_image_path, 'wb') as f:
            f.write(decrypted_data)

        print(f"Image successfully decrypted and saved to {output_image_path}")

    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    # Ask for the operation type
    operation = input("Do you want to encrypt or decrypt an image? (1 for encrypt, 2 for decrypt): ").strip()

    if operation == "1":  # Encryption
        # Ask for the image name
        image_name = input("Enter the name of the image file to encrypt (with extension): ").strip()

        # Generate a random 256-bit (32-byte) key
        key = get_random_bytes(32)

        # Define output paths
        encrypted_image_path = image_name + ".enc"

        # Encrypt the image
        encrypt_image(image_name, encrypted_image_path, key)

        # Save the key to the log file
        save_key_to_log(key, encrypted_image_path)

        print(f"Key has been saved securely to the log file.")

    elif operation == "2":  # Decryption
        # Ask for the encrypted file name
        encrypted_image_name = input("Enter the name of the encrypted file (with extension): ").strip()

        # Try to retrieve the key from the log
        key = get_key_from_log(encrypted_image_name)

        if key:
            # Define output paths
            decrypted_image_path = input("Enter the name for the output decrypted image (with extension): ").strip()

            # Decrypt the image
            decrypt_image(encrypted_image_name, decrypted_image_path, key)
        else:
            print("Key not found in log. Decryption cannot proceed.")
    else:
        print("Invalid operation. Please enter '1' for encrypt or '2' for decrypt.")

if __name__ == "__main__":
    main()
