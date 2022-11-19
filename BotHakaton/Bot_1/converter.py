import requests


def convert(message):
    api_key = "048572a9a42e7b7a0574d1487ad5a059"
    headers = {f'{"apikey": {api_key}, "file": "{message}", "outputformat": "docx"}'}
    response = requests.get("http://api.convertio.co/convert", headers=headers)
    print(response)
