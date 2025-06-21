import os
import json
from cryptography.fernet import Fernet
from .crypto.aes import AESEncryptor

class SessionManager:
    def __init__(self, session_name, encryption_key=None):
        self.session_name = session_name
        self.encryptor = AESEncryptor(encryption_key) if encryption_key else None
        self.session_file = f"sessions/{session_name}.session"
        
    async def save_session(self, session_data):
        os.makedirs("sessions", exist_ok=True)
        data = json.dumps(session_data).encode()
        if self.encryptor:
            data = await self.encryptor.encrypt(data)
        with open(self.session_file, "wb") as f:
            f.write(data)
            
    async def load_session(self):
        try:
            with open(self.session_file, "rb") as f:
                data = f.read()
            if self.encryptor:
                data = await self.encryptor.decrypt(data)
            return json.loads(data.decode())
        except FileNotFoundError:
            return None
