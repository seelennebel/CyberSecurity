# HMAC RFC2104

import hashlib
import sys

SHA512 = hashlib.sha512()
MD5 = hashlib.md5()

key = 0x1A6
data = "some text"

ipad_str = "0X36"
opad_str = "0x5C"

def display_info():
    print("<-------------------------------------------->")
    print("SHA512 block size in bytes:",SHA512.block_size)
    print("MD5 block size in bytes:", MD5.block_size)
    print("<-------------------------------------------->")

def HMAC_SHA512(hash_function, block_size, ipad_str, opad_str):
    key = "0x1A6"
    data = "hello"
    key_size = sys.getsizeof(key, 16)
    if key_size < block_size:
        remaining_zeros = block_size - key_size
    for i in range(remaining_zeros):
        key += "0"

    for i in range(SHA512.block_size - 1):
        ipad_str += "36"

    inner_xor = int(key, 16) ^ int(ipad_str, 16)
    print(inner_xor)
    print(hex(ord(data)))

def HMAC_MD5(ipad_str, opad_str):
    for i in range(MD5.block_size - 1):
        ipad_str += "36"
    print(hex(int(ipad_str, 16)))

if __name__ == "__main__":
    args_length = len(sys.argv)
    args =  sys.argv
    if args_length == 2:
        if args[1] == "info":
            display_info()
        if args[1] == "sha512":
            HMAC_SHA512(SHA512, SHA512.block_size, ipad_str, opad_str)
        if args[1] == "md5":
            HMAC_MD5(ipad_str, opad_str)
        

