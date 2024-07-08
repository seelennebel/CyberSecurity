# HMAC-SHA512 / HMAC-MD5
### In this project, we implemented SHA512 and MD5 Hash-based Message Authentication Codes

## Installation
### Requirements:
- Python 3

no additional libraries are required

```
git clone https://github.com/seelennebel/CyberSecurity.git
cd CyberSecurity/HMAC
```

## Generating HMACs
### Program flags and input
- "-f" flag is used to specify the desired hash function to use in HMAC generation. In our case, it is either sha512 or md5
- "-d" flag is used to specify the data for HMAC generation. Please, put the data into double quotes (also see the usage examples)
- "-ascii" or "-hex" flags are used to specify the type of the key. It can be either a hexadecimal number or an ASCII string. Please, also put ASCII string into double quotes. The hex number should be written in the following notation:

Do not use 0x or 0X in front of the hex number!!! Also, the hex number should have an even number of hex characters

Following the notation (please also see the usage examples):

0x1 should be -> 01

0xFF should be -> FF or 00FF

We ask to follow this notation because Python bytes objects (used in the implementation) perceive the information in octets and give errors if the hex number has an odd count of hex characters. Also, this gives you full control over the input.

### Examples
Generate HMAC for "Hi There" using sha512 with the key "Jefe"
```
python hmacutil.py -d "Hi There" -f sha512 -ascii "Jefe"
```

Generate HMAC for "Hi There" using sha512 with the key 0x874FA (using the notation specified above)
```
python hmacutil.py -d "Hi There" -f sha512 -hex 0874FA 
```

Generate HMAC for "MD is better than SHA =)" using md5 with the key "But md has smaller digest size =(" 
```
python hmacutil.py -d "MD is better than SHA =)" -f md5 -ascii "But md has smaller digest size =("
```

Generate HMAC for "I like MD" using md5 with the key 0x7ED5 (again, we shouldn't forget about the special notation)
```
python hmacutil.py -d "I like MD" -f md5 -hex 7ED5   
```

## Input limitations

For the ASCII key:
- please do not use characters that the shell can perceive as special characters, like "!"
