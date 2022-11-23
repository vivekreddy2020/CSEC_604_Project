import binascii
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
x = "vivekflfrmwelnlsnlwlwnclwnlwcwc"
x = pad(bytes(x,"utf-8"),32)
print(x)
y = b'mvevreveveev\x01'
print(unpad(x,32).decode('utf-8'))


