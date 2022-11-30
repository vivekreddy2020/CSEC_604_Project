import binascii
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import codecs
from Crypto.Util.Padding import pad
from os.path import exists

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def check(fpath):

    try:
        with open(fpath, 'rb') as data:
            fdata = data.read()
        fdata = codecs.decode(fdata)
        if fdata[32:37] == '0xENC':
            return True
    except:
        return False


def encrypting(key,fpath):
    iv = Random.new().read(16)
    
    cipher=AES.new(codecs.encode(key), AES.MODE_CBC, iv)
    with open(fpath, 'rb') as data:
        fdata = data.read()
    checksum = hashlib.sha256(fdata).hexdigest()  
    
    try: 
        fdata = pad(fdata,16)
  
 
        fdata = (codecs.decode((binascii.hexlify(iv))))+ '0xENC'+checksum+codecs.decode(binascii.hexlify(cipher.encrypt(fdata)))
        with open(fpath, 'wb') as data:
            data.write(codecs.encode(fdata))
        return True
    except: 
        return False



def decrypting(key, fpath):
    with open(fpath, 'rb') as data:
        fdata = (data.read())
    fdata = codecs.decode(fdata)
    iv = binascii.unhexlify(bytes(fdata[:32],'utf-8'))


   
    chksum = fdata[37:101]
    fdata = fdata[101:]
 
   
    cipher=AES.new(codecs.encode(key), AES.MODE_CBC, iv)
    fdata = cipher.decrypt(binascii.unhexlify(bytes(fdata,"utf-8")))

    fdata= binascii.hexlify(fdata)
    fdata = unpad(binascii.unhexlify(fdata))
 
   
  
    check = hashlib.sha256(fdata).hexdigest()
  
    if chksum == check:
        with open(fpath, 'wb') as data:
            data.write(fdata)
        return True
    else: 
        return False


    