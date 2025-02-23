from pwn import *
from AES import pad, decrypt_block, decrypt
import json

# Connect to the server
# p = process(["python3", "server.py"])
p = remote("kashictf.iitbhucybersec.in", 55716)

while True:
    # Read and parse the challenge
    line = p.recvline().strip()
    data = json.loads(line.decode())
    print(f"DEBUG: {data}")

    key = bytes.fromhex(data["key"])  # Extract AES key
    ciphertext = bytes.fromhex(data["ciphertext"])  # Extract ciphertext

    block_1 = ciphertext[:16]

    crib = pad(b"KashiCTF{", 16)
    block_1_x_key = decrypt_block(key, block_1)

    IV_corrupt = xor(crib, block_1_x_key)

    IV = IV_corrupt[:8] * 2

    print(IV.hex())

    print(decrypt(key, ciphertext, IV))

    print(p.recv())
    p.sendline(IV.hex().encode())
    print(p.recvline())
