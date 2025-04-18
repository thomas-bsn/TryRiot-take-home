from abc import ABC, abstractmethod

class EncryptionInterface(ABC): #Interface pour le service d'encryption
    @abstractmethod
    def encrypt(self, value): 
        pass

    @abstractmethod
    def decrypt(self, value):
        pass
