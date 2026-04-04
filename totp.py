import time
import hmac
import hashlib
import base64
import struct

def totp_decode(base32_secret:str, interval:int=30, digits:int=6) -> str:
    key = base64.b32decode(base32_secret.upper())
    c = int(time.time()//interval)
    c_bytes = struct.pack(">Q", c)
    hmac_hash = hmac.new(key, c_bytes, hashlib.sha1).digest()
    offset = hmac_hash[-1] & 0x0F
    
    totp_code = (
        (hmac_hash[offset]&0x7f)<<24|
        (hmac_hash[offset+1]&0xff)<<16|
        (hmac_hash[offset+2]&0xff)<<8 |
        (hmac_hash[offset+3]&0xff)
    )

    return str(totp_code%(10**digits)).zfill(digits)