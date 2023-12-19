import requests


def download_map_image(lat, lon, zoom, api_key):
    print("Downloading Image")
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size=400x400&key={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        with open("map_image.png", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download image, status code: {response.status_code}")


# Replace with your actual values
latitude = "85.3475465"
longitude = "23.3499754"
zoom_level = "20"
api_key = "AIzaSyBQKl4etvsGI452JeNyWEsVxQX299qI28E"

download_map_image(latitude, longitude, zoom_level, api_key)
