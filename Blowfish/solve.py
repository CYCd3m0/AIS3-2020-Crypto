from base64 import b64decode, b64encode
from pwn import *
import pickle

with open('user.pickle', 'rb') as f :
    data = pickle.load(f)
origin = pickle.dumps(data)

data[0]['admin'] = True
forgery = pickle.dumps(data)

r = remote('60.250.197.227', 12001)
r.recvuntil('Your token:')
s = r.recvline()
c = b64decode(s)

payload = b''
for i in range(len(origin)) :
    payload += bytes([origin[i] ^ forgery[i] ^ c[i]])

r.sendlineafter('username', 'maojui')
r.sendlineafter('password', 'SECRET')
r.sendlineafter('TOKEN', b64encode(payload))
r.interactive()

# flag = AIS3{ATk_BloWf1sH-CTR_by_b1t_Flipping_^_^}