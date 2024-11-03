from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def get_key(length=16):
    # 使用隨機生成的 AES 金鑰
    key = get_random_bytes(length)
    return key


class My_AES_CBC():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, plain_text):
        try:
            # 每次加密生成一個隨機的 IV
            iv = get_random_bytes(AES.block_size)
            cryptor = AES.new(self.key, self.mode, iv)
            encrypted_text = cryptor.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))
            # 將 IV 和加密後的數據一起返回
            return iv + encrypted_text
        except ValueError as e:
            print("加密錯誤:", e)
            return None

    def decrypt(self, encrypted_text):
        try:
            # 分離 IV 和加密數據
            iv = encrypted_text[:AES.block_size]
            encrypted_data = encrypted_text[AES.block_size:]
            cryptor = AES.new(self.key, self.mode, iv)
            plain_text = cryptor.decrypt(encrypted_data)
            plain_text = unpad(plain_text, AES.block_size).decode('utf-8')
            return plain_text
        except (ValueError, KeyError) as e:
            print("解密錯誤:", e)
            return None


if __name__ == '__main__':
    key = get_key()
    pc = My_AES_CBC(key)
    encrypted = pc.encrypt("Pw0900pw")
    decrypted = pc.decrypt(encrypted)
    
    if encrypted:
        print("加密後文本:", encrypted)
    if decrypted:
        print("解密後文本:", decrypted)
