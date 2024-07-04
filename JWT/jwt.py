from sha512_bytes import HMAC_SHA512_bytes
import base64

payload = '{"sub":"1234567890","name":"John Doe","admin":true,"iat":1516239022}'

header = '''{"alg":"HS512","typ":"JWT"}'''

# return base64url encoded string
def generate_BASE64URL_string(string):
    utf8_bytes = bytearray(string, "utf-8")
    base64_bytes = base64.urlsafe_b64encode(utf8_bytes)
    base64_str = base64_bytes.decode()
    while(base64_str[-1] == "="):
        base64_str = base64_str[:-1]

    return base64_str

def generate_BASE64URL_bytes(input):
    base64_bytes = base64.urlsafe_b64encode(input)
    base64_str = base64_bytes.decode()
    while(base64_str[-1] == "="):
        base64_str = base64_str[:-1]

    return base64_str

def generate_JWT(payload, key):
    header = '{"alg":"HS512","typ":"JWT"}'
    JWT = ""
    JWT += generate_BASE64URL_string(header)
    JWT += "."
    JWT += generate_BASE64URL_string(payload)
    hmac_bytes = HMAC_SHA512_bytes(JWT, {"key" : key, "encoding" : "ASCII"})
    JWT += "."
    JWT += generate_BASE64URL_bytes(hmac_bytes)
    return JWT

def validate_JWT(jwt, key):
    jwt_split = jwt.split(".")
    signing_input = jwt_split[0] + "." + jwt_split[1]
    hmac_bytes = HMAC_SHA512_bytes(signing_input, {"key" : key, "encoding" : "ASCII"})
    hmac_string = generate_BASE64URL_bytes(hmac_bytes)
    if hmac_string == jwt_split[2]:
        return True
    else:
        return False