import requests
import sys
import os
import random

def download_video(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Vérifie que la requête s'est bien passée
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")
        return

    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # Taille des blocs de téléchargement

    with open(save_path, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded_size = file.tell()
            progress = downloaded_size * 100 // total_size
            print(f"Téléchargé {progress}%")

    print(f"Vidéo téléchargée et sauvegardée dans {save_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python download_video.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    random_number = random.randint(1000, 9999)
    save_path = os.path.join(os.getcwd(), f"{random_number}.mp4")

    download_video(url, save_path)
