import hashlib


def sha256_hash(text: str) -> str:
    """Возвращает SHA-256 хеш сроки в виде шестнадцатеричной строки"""
    
    text_bytes = text.encode('utf-8')
    
    hash_object = hashlib.sha256(text_bytes)
    
    return hash_object.hexdigest()