ipad_bytes = bytearray(128)
print(ipad_bytes)
for i in range(128):
    ipad_bytes[i] = 54

print(ipad_bytes.hex().count("36"))