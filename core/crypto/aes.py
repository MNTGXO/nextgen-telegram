from cryptography.fernet import Fernet
import base64

class AESEncryptor:
    def __init__(self, key: str):
        key = base64.urlsafe_b64encode(key.encode()[:32].ljust(32, b'\0'))
        self.cipher = Fernet(key)
        
    async def encrypt(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)
        
    async def decrypt(self, data: bytes) -> bytes:
        return self.cipher.decrypt(data)
