# TO DO
# implement the initialization for ASCII key

import hashlib

# size of key = 128 bytes max
# size of key with added zeros = 128 bytes
# size of pads = 128 bytes

def HMAC_SHA512(data, key_option):

    print("debug:")

# initializing sha512 objects and block size variable 
    SHA512_1 = hashlib.sha512();
    SHA512_2 = hashlib.sha512();
    block_size = SHA512_1.block_size

    print("block size:", block_size)
#initializing the ASCII data to bytes
    data_bytes = bytearray(data, encoding = "ASCII")

# initializing ipad and opad to 128 empty bytes
    ipad_bytes = bytearray(block_size)
    opad_bytes = bytearray(block_size)

# defining the key encoding and the key    
    key = key_option["key"]
    key_encoding = key_option["encoding"]

    if  key_encoding == "HEX":
        key_bytes = bytearray.fromhex(key)
    if key_encoding == "ASCII":
        key_bytes = bytearray(str(key), encoding = key_encoding)

    print("key", key_bytes.hex())

# adding remaining zeros to the key so that it will have a size of 128 bytes
    for i in range (block_size - len(key_bytes)):
        key_bytes.append(0)
    print("size of key after apending", len(key_bytes))
    print(len(key_bytes.hex()))
# repeat the values of pads block size times
    for i in range(block_size):
        ipad_bytes[i] = 54
        opad_bytes[i] = 92

    print("ipad size:", len(ipad_bytes))
    print("opad size:", len(opad_bytes))

# initializing pads and key to integers for the XOR operation
    ipad_bytes_int = int(ipad_bytes.hex(), 16)
    opad_bytes_int = int(opad_bytes.hex(), 16)
    key_bytes_int = int(key_bytes.hex(), 16)

# doing inner xor and then initializing the result to bytearray
    tmp_inner_xor_int = key_bytes_int ^ ipad_bytes_int
    tmp_inner_xor_hex = hex(tmp_inner_xor_int)

# checking if XOR result is 256 and if not it inserts zero to the first place (values remain the same even if 0 is inserted at the beginning of the hex number)
    if len(tmp_inner_xor_hex) == 255:
        inner_xor = "0" + tmp_inner_xor_hex[2:]
        inner_bytes = bytearray.fromhex(inner_xor)
        print("\n")
        print(hex(tmp_inner_xor_int))
        print(inner_xor)
        print("\n")
    else:
        inner_xor = tmp_inner_xor_int
        inner_bytes = bytearray.fromhex(hex(inner_xor)[2:]) # implement the initialization for ASCII key
    
    print("size after first XOR:", len(inner_bytes))
# appending data to the previous result
    inner_bytes.extend(data_bytes)
    
    SHA512_1.update(inner_bytes)
    inner_digest = SHA512_1.digest()

    outer_xor = key_bytes_int ^ opad_bytes_int
    outer_bytes = bytearray.fromhex(hex(outer_xor)[2:])

    outer_bytes.extend(inner_digest)

    SHA512_2.update(outer_bytes)

# returning in hex format
    return SHA512_2.digest().hex()
