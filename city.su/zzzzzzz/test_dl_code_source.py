import requests

def save_webpage_source(url, file_path):
    try:
        # Effectuer la requête GET pour récupérer le contenu de la page
        response = requests.get(url)
        
        # Vérifier que la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Enregistrer le contenu de la page dans un fichier
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Le code source de la page a été enregistré dans le fichier {file_path}.")
        else:
            print(f"Erreur lors de la requête HTTP : {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
url = "https://saint2.su/embed/IzQUdh728Kl"
file_path = "source_page.html"
save_webpage_source(url, file_path)
