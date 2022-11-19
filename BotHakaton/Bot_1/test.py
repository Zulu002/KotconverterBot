import requests
def api():
    api_key = "DEMO_KEY"
    params = {"api_key": api_key, "earth_date": "2020-07-01"}
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos", params=params)
    ntf = response.json()
    photos = ntf['photos']
    print("Количество фотографий..", len(photos))
    print(photos[2]["img_src"])

if __name__ == "__main__":
    api()