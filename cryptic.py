import binascii
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def check(fpath):
    with open(fpath, 'rb') as data:
        fdata = data.read()
    fdata = fdata.decode('utf-8')
    if fdata[32:37] == '0xENC':
        return True
    else:
        return False

def encrypting(key,fpath):
    iv = Random.new().read(16)
    with open("testdata2.txt", 'wb') as data:
        data.write("while encrypting ".encode('utf-8'))
        data.write(str(iv).encode('utf-8'))
    
    cipher=AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    with open(fpath, 'rb') as data:
        fdata = data.read()
    checksum = hashlib.sha256(fdata).hexdigest()  
    
    fdata = pad(fdata.decode('utf-8'))
 
    fdata = ((binascii.hexlify(iv)).decode('utf-8'))+ '0xENC'+checksum+"--"+(binascii.hexlify(cipher.encrypt(fdata.encode('utf-8')))).decode('utf-8')
    with open(fpath, 'wb') as data:
        data.write(fdata.encode('utf-8'))
    return True



def decrypting(key, fpath):
    with open(fpath, 'rb') as data:
        fdata = (data.read())
    fdata = fdata.decode('utf-8')
    iv = binascii.unhexlify(bytes(fdata[:32],"utf-8"))
    with open("testdata3.txt", 'wb') as data:
        data.write("while decrypting".encode('utf-8'))
        data.write(str(iv).encode('utf-8'))

   
    chksum = fdata[37:101]
    fdata = fdata[103:]
 
   
    cipher=AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    fdata = cipher.decrypt(binascii.unhexlify(bytes(fdata,"utf-8")))

    fdata= binascii.hexlify(fdata)
   
    fdata = unpad((binascii.unhexlify(fdata)).decode('utf-8'))
   
  
    check = hashlib.sha256(fdata.encode('utf-8')).hexdigest()
  
    if chksum == check:
        with open(fpath, 'wb') as data:
            data.write(fdata.encode('utf-8'))
        return True
    else:
        return False


    