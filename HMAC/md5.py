import hashlib

def HMAC_MD5(data, key_option):
# initializing MD5 objects and block size variable 
    MD5_1 = hashlib.md5();
    MD5_2 = hashlib.md5();
    block_size = MD5_1.block_size

#initializing the ASCII data to bytes
    data_bytes = bytearray(data, encoding = "ASCII")

# initializing ipad and opad to empty bytes
    ipad_bytes = bytearray(block_size)
    opad_bytes = bytearray(block_size)

# defining the key encoding and the key    
    key = key_option["key"]
    key_encoding = key_option["encoding"]

    if  key_encoding == "HEX":
        key_bytes = bytearray.fromhex(key)
    if key_encoding == "ASCII":
        key_bytes = bytearray(str(key), encoding = key_encoding)

# adding remaining zeros to the key
    for i in range (block_size - len(key_bytes)):
        key_bytes.append(0)

# repeat the values of pads block size times
    for i in range(block_size):
        ipad_bytes[i] = 54
        opad_bytes[i] = 92

# initializing pads and key to integers for the XOR operation
    ipad_bytes_int = int(ipad_bytes.hex(), 16)
    opad_bytes_int = int(opad_bytes.hex(), 16)
    key_bytes_int = int(key_bytes.hex(), 16)

# doing inner xor and then initializing the result to bytearray
    tmp_inner_xor_int = key_bytes_int ^ ipad_bytes_int
    tmp_inner_xor_hex = hex(tmp_inner_xor_int)

# checking if XOR result is 128 and if not it inserts zero to the first place (values remain the same even if 0 is inserted at the beginning of the hex number)
    if len(tmp_inner_xor_hex) == 129:
        inner_xor = "0" + tmp_inner_xor_hex[2:]
        inner_bytes = bytearray.fromhex(inner_xor)
    elif len(tmp_inner_xor_hex) > 128 and (len(tmp_inner_xor_hex) % 2) != 0:
        inner_xor = "0" + tmp_inner_xor_hex[2:]
        inner_bytes = bytearray.fromhex(inner_xor)
    else:
        inner_xor = tmp_inner_xor_int
        inner_bytes = bytearray.fromhex(hex(inner_xor)[2:]) # implement the initialization for ASCII key
    
# appending data to the previous result
    inner_bytes.extend(data_bytes)
    
    MD5_1.update(inner_bytes)
    inner_digest = MD5_1.digest()

    outer_xor = key_bytes_int ^ opad_bytes_int
    outer_bytes = bytearray.fromhex(hex(outer_xor)[2:])

    outer_bytes.extend(inner_digest)

    MD5_2.update(outer_bytes)

# returning in hex format
    return MD5_2.digest().hex()
