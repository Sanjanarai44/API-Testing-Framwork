import requests
import logging
from config.config import BASE_URL

logging.basicConfig(
    filename="logs/api_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def get(endpoint):
    url = BASE_URL + endpoint
    logging.info(f"GET request sent to {url}")
    response = requests.get(url)
    return response

def post(endpoint, payload):
    url = BASE_URL + endpoint
    logging.info(f"POST request sent to {url}")
    response = requests.post(url, json=payload)
    return response