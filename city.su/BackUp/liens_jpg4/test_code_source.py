from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def download_rendered_page(url, filename):
    # Configure les options de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Optionnel: exécute Chrome en mode sans tête (sans interface graphique)
    
    # Remplacez 'path_to_chromedriver' par le chemin vers votre ChromeDriver
    service = Service('/path/to/chromedriver')

    # Initialisez le navigateur
    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Accéder à l'URL spécifiée
        browser.get(url)

        # Attendez que la page soit complètement chargée
        time.sleep(5)  # Ajustez ce délai si nécessaire

        # Obtenez le code HTML rendu
        rendered_html = browser.page_source

        # Sauvegardez le code HTML dans un fichier
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(rendered_html)

        print(f"Le code HTML rendu de la page {url} a été sauvegardé dans le fichier {filename}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement de la page : {e}")
    finally:
        # Fermez le navigateur
        browser.quit()

# Exemple d'utilisation
url = "https://simpcity.su/threads/sofiacrnilovic.67319/"
filename = "Test/liens_jpg4/code_source.txt"
download_rendered_page(url, filename)
