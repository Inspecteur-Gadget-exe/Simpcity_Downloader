import requests
from bs4 import BeautifulSoup
import os
import re

def telecharger_images(lien_fichier, dossier_sortie):
    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    # Lire les liens depuis le fichier
    with open(lien_fichier, 'r', encoding='utf-8') as fichier:
        liens = fichier.readlines()
    
    # Pour chaque lien, télécharger l'image
    for lien in liens:
        lien = lien.strip()
        if lien:
            try:
                response = requests.get(lien)
                response.raise_for_status()
                
                # Parser le contenu HTML pour trouver l'image
                soup = BeautifulSoup(response.text, 'html.parser')
                image_tag = soup.find('img', src=re.compile(r'^https://simp6\.host\.church'))
                
                if image_tag:
                    image_url = image_tag['src']
                    
                    # Télécharger l'image
                    image_response = requests.get(image_url)
                    image_response.raise_for_status()
                    
                    # Nom du fichier image basé sur l'URL
                    image_name = os.path.basename(image_url)
                    image_path = os.path.join(dossier_sortie, image_name)
                    
                    # Sauvegarder l'image
                    with open(image_path, 'wb') as image_file:
                        image_file.write(image_response.content)
                    
                    print(f"Téléchargé : {image_url} -> {image_path}")
                else:
                    print(f"Aucune image trouvée pour le lien : {lien}")
            except requests.RequestException as e:
                print(f"Erreur lors de la récupération de {lien} : {e}")

# Exemple d'utilisation
lien_fichier = 'Test/jpg4/sortie_jpg4.txt'
dossier_sortie = 'Test/jpg4/images'
telecharger_images(lien_fichier, dossier_sortie)
