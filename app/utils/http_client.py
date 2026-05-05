# app/utils/http_client.py
import requests

def get_request(url: str):
    return requests.get(url, timeout=5)