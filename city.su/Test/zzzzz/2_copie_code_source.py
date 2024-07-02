import requests
import os

def save_webpage_source(url, filename):
    try:
        # Effectuer une requête GET pour obtenir le code source de la page
        response = requests.get(url)
        response.raise_for_status()  # Vérifier s'il y a eu des erreurs de requête
        
        # Ouvrir un fichier en mode écriture
        with open(filename, 'w', encoding='utf-8') as file:
            # Écrire le contenu de la page dans le fichier
            file.write(response.text)
        
        print(f"Le code source de {url} a été sauvegardé dans {filename}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la page : {e}")

# Utilisation du script
script_directory = os.path.dirname(os.path.abspath(__file__))

url = 'https://saint2.su/embed/IzQUdh728Kl'  # Remplacer par l'URL de la page que vous souhaitez récupérer
filename = os.path.join(script_directory, '2_sortie_code_source.txt')  # Nom du fichier où le code source sera sauvegardé

save_webpage_source(url, filename)