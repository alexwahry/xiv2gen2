import requests
import os

dir = os.path.dirname(os.path.abspath(__file__))
path = f"{dir}/error.log"

def send_code_to_xivlauncher(totp_code:str) -> None:
    url = f"http://127.0.0.1:4646/ffxivlauncher/{totp_code}"
    try:
        r = requests.get(url)
        r.raise_for_status()

    except requests.exceptions.RequestException as e:        
        with open(path, "w") as f:
            f.write(str(e))
            print("Error! Please check error.log file")
    else:
        print("Done!")