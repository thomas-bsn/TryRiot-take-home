import base64
from services.strategies.Interfaces.EncryptionInterface import EncryptionInterface

class Base64Encryption(EncryptionInterface):
    def encrypt(self, value):
        return base64.b64encode(value.encode()).decode()

    def decrypt(self, value):
        return base64.b64decode(value.encode()).decode()
