import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib

class EncryptionError(Exception):
    """Custom exception for encryption-related errors."""
    pass

class DecryptionError(Exception):
    """Custom exception for decryption-related errors."""
    pass

class HashingError(Exception):
    """Custom exception for hashing-related errors."""
    pass

def generate_rsa_key_pair(key_size=2048):
    """
    Generates a RSA key pair (private and public keys).

    Parameters:
        key_size (int): Size of the RSA key. Default is 2048 bits.

    Returns:
        tuple: RSA key pair (private key, public key).

    Raises:
        EncryptionError: If RSA key generation fails.
    """
    try:
        key = RSA.generate(key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key
    except Exception as e:
        raise EncryptionError(f"RSA key generation failed: {e}")

def aes_encrypt(plaintext, key):
    """
    Encrypts a plaintext string using AES encryption.

    Parameters:
        plaintext (str): The plaintext string to encrypt.
        key (bytes): The AES key to use for encryption (must be 16, 24, or 32 bytes long).

    Returns:
        bytes: The encrypted data.

    Raises:
        EncryptionError: If encryption fails.
    """
    try:
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        return cipher.iv + ct_bytes
    except Exception as e:
        raise EncryptionError(f"AES encryption failed: {e}")

def aes_decrypt(ciphertext, key):
    """
    Decrypts an AES-encrypted string back to plaintext.

    Parameters:
        ciphertext (bytes): The encrypted data to decrypt.
        key (bytes): The AES key to use for decryption (must be 16, 24, or 32 bytes long).

    Returns:
        str: The decrypted plaintext string.

    Raises:
        DecryptionError: If decryption fails.
    """
    try:
        iv = ciphertext[:AES.block_size]
        ct = ciphertext[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')
    except Exception as e:
        raise DecryptionError(f"AES decryption failed: {e}")

def rsa_encrypt(plaintext, public_key):
    """
    Encrypts a plaintext string using RSA encryption.

    Parameters:
        plaintext (str): The plaintext string to encrypt.
        public_key (bytes): The RSA public key to use for encryption.

    Returns:
        bytes: The encrypted data.

    Raises:
        EncryptionError: If encryption fails.
    """
    try:
        public_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(plaintext.encode('utf-8'))
    except Exception as e:
        raise EncryptionError(f"RSA encryption failed: {e}")

def rsa_decrypt(ciphertext, private_key):
    """
    Decrypts an RSA-encrypted string back to plaintext.

    Parameters:
        ciphertext (bytes): The encrypted data to decrypt.
        private_key (bytes): The RSA private key to use for decryption.

    Returns:
        str: The decrypted plaintext string.

    Raises:
        DecryptionError: If decryption fails.
    """
    try:
        private_key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(ciphertext).decode('utf-8')
    except Exception as e:
        raise DecryptionError(f"RSA decryption failed: {e}")

def sha256_hash(plaintext):
    """
    Hashes a plaintext string using SHA-256.

    Parameters:
        plaintext (str): The plaintext string to hash.

    Returns:
        str: The resulting SHA-256 hash in hexadecimal format.

    Raises:
        HashingError: If hashing fails.
    """
    try:
        return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()
    except Exception as e:
        raise HashingError(f"SHA-256 hashing failed: {e}")

def verify_sha256_hash(plaintext, hash_value):
    """
    Verifies a plaintext string against a given SHA-256 hash.

    Parameters:
        plaintext (str): The plaintext string to verify.
        hash_value (str): The SHA-256 hash to verify against.

    Returns:
        bool: True if the hash matches, False otherwise.

    Raises:
        HashingError: If verification fails.
    """
    try:
        return sha256_hash(plaintext) == hash_value
    except Exception as e:
        raise HashingError(f"SHA-256 hash verification failed: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # AES Encryption/Decryption
        aes_key = get_random_bytes(16)
        plaintext = "This is a secret message."
        ciphertext = aes_encrypt(plaintext, aes_key)
        decrypted_text = aes_decrypt(ciphertext, aes_key)
        print(f"AES Decrypted: {decrypted_text}")

        # RSA Encryption/Decryption
        private_key, public_key = generate_rsa_key_pair()
        rsa_ciphertext = rsa_encrypt(plaintext, public_key)
        rsa_decrypted_text = rsa_decrypt(rsa_ciphertext, private_key)
        print(f"RSA Decrypted: {rsa_decrypted_text}")

        # SHA-256 Hashing/Verification
        hash_value = sha256_hash(plaintext)
        is_verified = verify_sha256_hash(plaintext, hash_value)
        print(f"SHA-256 Verified: {is_verified}")

    except (EncryptionError, DecryptionError, HashingError) as e:
        print(f"An error occurred: {e}")