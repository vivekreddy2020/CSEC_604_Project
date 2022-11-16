import hashlib

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def check(fpath):
    with open(fpath, 'rb') as data:
        fdata = data.read()
    if fdata[16:21] is '0xENC':
        return True
    else:
        return False

def encrypt(key,fpath):
    iv = Random.new().read(AES.block_size)
    
    cipher=AES.new(key, AES.MODE_CBC, iv)
    with open(fpath, 'rb') as data:
        fdata = data.read()
    checksum = hashlib.sha256(fdata.encode('utf-8')).hexdigest()  
    fdata = pad(fdata)
    fdata = iv + '0xENC'+checksum+cipher.encrypt(fdata)
    with open(fpath, 'wb') as data:
        data.write(fdata)
    return True



def decrypt(key, fpath):
    with open(fpath, 'rb') as data:
        fdata = data.read()
    iv = fdata[:16]
    chksum = fdata[16:80]
    fdata = fdata[80:]
    cipher=AES.new(key, AES.MODE_CBC, iv)
    fdata = cipher.decrypt(fdata)
    fdata = unpad(fdata)
    check = hashlib.sha256(fdata.encode('utf-8')).hexdigest()
    if chksum is check:
        with open(fpath, 'wb') as data:
            data.write(fdata)
        return True
    else:
        return False


    