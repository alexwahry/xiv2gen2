import os

def extract_secret() -> str:
    dir = os.path.dirname(os.path.abspath(__file__))
    path = f"{dir}/secret.txt"

    with open(path, "r") as f:
        secret = f.read().strip()
    
    return secret