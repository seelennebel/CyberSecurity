# HMAC RFC2104

from sha512 import HMAC_SHA512
from md5 import HMAC_MD5

import hashlib
import sys

SHA512 = hashlib.sha512()
MD5 = hashlib.md5()

def display_info():
    print("<-------------------------------------------->")
    print("SHA512 block size in bytes:",SHA512.block_size)
    print("SHA512 digest size in bytes:", SHA512.digest_size)
    print("MD5 block size in bytes:", MD5.block_size)
    print("MD5 digest size in bytes:", MD5.digest_size)
    print("<-------------------------------------------->")

if __name__ == "__main__":

# INPUT HANDLING

    args =  sys.argv
    args_length = len(sys.argv)

#available options (only one of hex and ascii must be filled)
    options = {
        "-f" : "",
        "-d" : "",
        "-hex" : "",
        "-ascii" : ""
    }

# if the user just enters the command it will display the help string
    if args_length == 1:
        display_info()

# check if the first option is info or raise an exception
    if args_length == 2 and args[1] == "info":
        display_info()
    else:
        Exception("ERROR, provide valid arguments")

# gather options from the terminal input
    if args_length > 2:

        for i in range(args_length):
            if args[i] in options.keys():
                options[args[i]] = args[i + 1]

# check if -f and -d options are not empty and initializes hash and data variables
        if options["-f"] != "" and options["-d"] != "" and (options["-hex"] != "" or options["-ascii"] != ""):
            hash_function = options["-f"]
            data = options["-d"]
        else:
            raise Exception("ERROR, provide required arguments")

# checks which hash function and key encoding to use

        if hash_function == "sha512":
            if options["-hex"] != "":
                hex_key = options["-hex"]
                print(HMAC_SHA512(data, {"encoding" : "HEX", "key" : hex_key}))
            elif options["-ascii"] != "":
                ascii_key = options["-ascii"]
                print(HMAC_SHA512(data, {"encoding" : "ASCII", "key" : ascii_key}))
            else:
                raise Exception("ERROR: no key is provided or invalid option")
            
        elif hash_function == "md5":
            if options["-hex"] != "":
                hex_key = options["-hex"]
                print(HMAC_MD5(data, {"encoding" : "HEX", "key" : hex_key}))
            elif options["-ascii"] != "":
                ascii_key = options["-ascii"]
                print(HMAC_MD5(data, {"encoding" : "ASCII", "key" : ascii_key}))
            else:
                raise Exception("ERROR: no key is provided or invalid option")
        
        else:
            raise Exception("ERROR: wrong hash function")

