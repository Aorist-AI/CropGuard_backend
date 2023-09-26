import requests


def get(ip: str):
    _ip = ip.strip()
    res = requests.get(f'http://ip-api.com/json/{_ip}').json()

    return res
