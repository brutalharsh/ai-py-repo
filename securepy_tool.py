import os
import hashlib
import base64
import logging
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SecurePy:
    """A utility class providing encryption, decryption, hashing, and secure password storage functionalities."""

    @staticmethod
    def generate_random_key(length: int = 32) -> bytes:
        """
        Generate a secure random key.

        :param length: Length of the key in bytes (default is 32).
        :return: Secure random key.
        :raises ValueError: If length is not a positive integer.
        """
        if length <= 0:
            raise ValueError("Key length must be a positive integer.")
        key = get_random_bytes(length)
        logger.info(f"Generated random key of length {length}")
        return key

    @staticmethod
    def encrypt_data(data: bytes, key: bytes) -> bytes:
        """
        Encrypt data using AES (CBC mode) with the provided key.

        :param data: Data to be encrypted.
        :param key: Encryption key.
        :return: Encrypted data (IV + ciphertext).
        :raises ValueError: If data or key is empty.
        """
        if not data or not key:
            raise ValueError("Data and key must not be empty.")
        
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv

        # Padding data to be multiple of AES block size
        padding_length = AES.block_size - len(data) % AES.block_size
        data += bytes([padding_length]) * padding_length

        try:
            ciphertext = cipher.encrypt(data)
            logger.info("Data encrypted successfully")
            return iv + ciphertext
        except Exception as e:
            logger.exception("Encryption failed")
            raise

    @staticmethod
    def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
        """
        Decrypt data using AES (CBC mode) with the provided key.

        :param encrypted_data: Data to be decrypted (IV + ciphertext).
        :param key: Decryption key.
        :return: Decrypted data.
        :raises ValueError: If encrypted data or key is empty, or if padding is incorrect.
        """
        if not encrypted_data or not key:
            raise ValueError("Encrypted data and key must not be empty.")
        if len(encrypted_data) < AES.block_size:
            raise ValueError("Invalid encrypted data.")
        
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)

        try:
            data = cipher.decrypt(ciphertext)
            # Remove padding
            padding_length = data[-1]
            if padding_length > AES.block_size:
                raise ValueError("Invalid padding length.")
            data = data[:-padding_length]
            logger.info("Data decrypted successfully")
            return data
        except Exception as e:
            logger.exception("Decryption failed")
            raise

    @staticmethod
    def hash_data(data: bytes) -> str:
        """
        Generate a SHA-256 hash of the provided data.

        :param data: Data to be hashed.
        :return: SHA-256 hash of the data.
        :raises ValueError: If data is empty.
        """
        if not data:
            raise ValueError("Data must not be empty.")
        
        try:
            hash_object = hashlib.sha256(data)
            hash_hex = hash_object.hexdigest()
            logger.info("Data hashed successfully")
            return hash_hex
        except Exception as e:
            logger.exception("Hashing failed")
            raise

    @staticmethod
    def generate_salt(length: int = 16) -> bytes:
        """
        Generate a secure random salt.

        :param length: Length of the salt in bytes (default is 16).
        :return: Secure random salt.
        :raises ValueError: If length is not a positive integer.
        """
        if length <= 0:
            raise ValueError("Salt length must be a positive integer.")
        
        try:
            salt = get_random_bytes(length)
            logger.info(f"Generated salt of length {length}")
            return salt
        except Exception as e:
            logger.exception("Salt generation failed")
            raise

    @staticmethod
    def hash_password(password: str, salt: bytes, length: int = 32, N: int = 2**14, r: int = 8, p: int = 1) -> str:
        """
        Hash a password with a salt using scrypt.

        :param password: Password to be hashed.
        :param salt: Salt to be used in hashing.
        :param length: Desired length of the hash (default is 32 bytes).
        :param N: CPU/memory cost parameter (default is 2^14).
        :param r: Block size parameter (default is 8).
        :param p: Parallelization parameter (default is 1).
        :return: Hashed password.
        :raises ValueError: If password, salt, or length are invalid.
        """
        if not password or not salt:
            raise ValueError("Password and salt must not be empty.")
        if length <= 0:
            raise ValueError("Hash length must be a positive integer.")
        
        try:
            hashed_password = scrypt(password.encode(), salt, length, N=N, r=r, p=p)
            hashed_password_base64 = base64.b64encode(hashed_password).decode('utf-8')
            logger.info("Password hashed successfully")
            return hashed_password_base64
        except Exception as e:
            logger.exception("Password hashing failed")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        # Generate a random key
        key = SecurePy.generate_random_key()

        # Encrypt data
        data = b"Secret Data"
        encrypted_data = SecurePy.encrypt_data(data, key)
        logger.info(f"Encrypted Data: {base64.b64encode(encrypted_data).decode('utf-8')}")

        # Decrypt data
        decrypted_data = SecurePy.decrypt_data(encrypted_data, key)
        logger.info(f"Decrypted Data: {decrypted_data.decode('utf-8')}")

        # Hash data
        data_hash = SecurePy.hash_data(data)
        logger.info(f"Data Hash: {data_hash}")

        # Generate a salt
        salt = SecurePy.generate_salt()

        # Hash password
        password = "StrongPassword!"
        hashed_password = SecurePy.hash_password(password, salt)
        logger.info(f"Hashed Password: {hashed_password}")

    except Exception as e:
        logger.exception("An error occurred")