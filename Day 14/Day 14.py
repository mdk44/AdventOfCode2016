import hashlib

salt = 'abc'
salt = 'qzyelonm'

def md5(salt, int):
    inp = salt + str(int) 
    code = hashlib.md5(inp.encode())
    print(code.hexdigest())

md5('abc', 18)