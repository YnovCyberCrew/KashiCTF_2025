# The Troll Zone

[libc.so.6](/Pwn/The_Troll_Zone/libc.so.6) given with the chall.
[solve script](/Pwn/The_Troll_Zone/solve.py) :

```console
$ python3 solve.py 
[*] '/home/geoffrey/Documents/Notes/Kashi/Pwn/The_Troll_Zone/chall/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
[+] Opening connection to kashictf.iitbhucybersec.in on port 55668: Done
[*] Switching to interactive mode
$ whoami
root
$ cat /flag.txt
KashiCTF{did_some_trolling_right_there_EZRnYY5N}
$ exit
[*] Got EOF while reading in interactive
$ 
$ 
[*] Closed connection to kashictf.iitbhucybersec.in port 55668
[*] Got EOF while sending in interactive
```
