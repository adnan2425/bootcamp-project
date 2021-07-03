import hashlib
import binascii

#md5 = hashlib.nev("md5")
md5 = hashlib.md5()
for algo in hashlib.algorithms_available:
    print(algo)

with open("rsa.py", "rb") as fd:
    md5.update(fd.read())
print("MD5 " + md5.hexdigest())

dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
print(binascii.hexlify(dk))