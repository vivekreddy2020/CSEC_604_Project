import hashlib
import base64
from Crypto import Random
from Crypto.Cipher import AES
print(AES.block_size)
key = hashlib.sha256('lol'.encode('utf-8')).digest()
x = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, x)
print(x+cipher.encrypt('vivekkkkk'.encode()))
print(x)
print(x[16:])