from bcrypt import hashpw, gensalt, checkpw
import secrets
import string

def generate_rand_key(len: int = 4):
    characters = string.digits
      
    return ''.join(secrets.choice(characters) for _ in range(len))

def encode_key(key: str) -> str:
    salt = gensalt()
    key: bytes = key.encode()
    
    encode_key = hashpw(key, salt)
    return encode_key.decode()

def check_key(new_key: str, key: str) -> bool:
    new_key: bytes = new_key.encode()
    key: bytes = key.encode()
    
    return checkpw(new_key, key)
