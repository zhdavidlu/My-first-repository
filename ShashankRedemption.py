import hashlib
import os
wkdir = os.path.abspath(os.path.dirname(__file__))

whereToThonk = wkdir + "/" + raw_input("Filename: ")
thonkPower = int(raw_input("Bytes to Read: "))

turnk = hashlib.sha256()

with open(whereToThonk,'rb') as file:
    thonk = 0
    while thonk != b'':
        thonk = file.read(thonkPower)
        turnk.update(thonk)
SHA1result = turnk.hexdigest()
print(SHA1result)
