import hashlib

def HMAC_SHA512(data, key_option):

    print(key_option)

    SHA512_1 = hashlib.sha512();
    SHA512_2 = hashlib.sha512();
    block_size = SHA512_1.block_size
    
    key = key_option["key"]
    key_encoding = key_option["encoding"]

    if  key_encoding == "HEX":
        key_bytes = bytearray.fromhex(key)
    if key_encoding == "ASCII":
        key_bytes = bytearray(key, encoding = key_encoding)

# add remaining zeros to the key so that it will have a size of 128 bytes
    for i in range (block_size - len(key_bytes)):
        key_bytes.append(0)

    ipad_bytes = bytearray(block_size)
    opad_bytes = bytearray(block_size)

# set ipad and opad to block size bytes
    for i in range(block_size):
        ipad_bytes[i] = 54
        opad_bytes[i] = 92

    key_bytes_int = int(key_bytes.hex(), 16)
    ipad_bytes_int = int(ipad_bytes.hex(), 16)
    opad_bytes_int = int(opad_bytes.hex(), 16)

    inner_xor = key_bytes_int ^ ipad_bytes_int

    inner_bytes = bytearray.fromhex(hex(inner_xor)[2:])

    data_bytes = bytearray(data, encoding = "ASCII")

    inner_bytes.extend(data_bytes)

    SHA512_1.update(inner_bytes)
    inner_digest = SHA512_1.digest()

    outer_xor = key_bytes_int ^ opad_bytes_int
    outer_bytes = bytearray.fromhex(hex(outer_xor)[2:])

    outer_bytes.extend(inner_digest)

    SHA512_2.update(outer_bytes)

    return SHA512_2.digest().hex()

