from io import BytesIO
from PIL import Image
import requests

target_url = "https://pokeapi.co/api/v2/"

def get_poke_info(num):
    url = f"{target_url}pokemon/{num}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Bu sayıyla bir pokemon yok, Hata Kodu: {response.status_code}")


def get_poke_img(sprite_url):
    try:
        response = requests.get(sprite_url)
        if response.status_code == 200:
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            return img
        else:
            return None
    except Exception as e:
        print(f"Resim yüklenirken bir hata oluştu: {e}")
        return None