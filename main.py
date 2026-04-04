from secrets_managment import *
from network_utils import *
from totp import *

totp_secret = extract_secret()
totp_code = totp_decode(totp_secret)

print(totp_code)
send_code_to_xivlauncher(totp_code)