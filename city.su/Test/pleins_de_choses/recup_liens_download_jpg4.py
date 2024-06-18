import re
import subprocess

def extraire_liens(fichier_entree, fichier_sortie_jpg4, fichier_sortie_saint2, fichier_sortie_tiktok):
    # Expressions régulières pour trouver les liens spécifiques
    pattern_jpg4 = r'https://jpg4\.su/img\S+?(?="|\s|$)'
    pattern_saint2 = r'https://saint2\.su/embed\S+?(?="|\s|$)'
    #pattern_tiktok = r'www\.tiktok\.com/embed/\S+?(?="|\s|$)'

    # Lire le contenu du fichier d'entrée avec l'encodage 'utf-8'
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # Trouver tous les liens correspondants
    liens_jpg4 = re.findall(pattern_jpg4, contenu)
    liens_saint2 = re.findall(pattern_saint2, contenu)
    #liens_tiktok = re.findall(pattern_tiktok, contenu)

    # Filtrer les liens à exclure pour jpg4
    liens_jpg4 = [lien for lien in liens_jpg4 if lien != "https://jpg4.su/img/YnBxSZe"]

    # Écrire les liens trouvés dans les fichiers de sortie avec l'encodage 'utf-8'
    with open(fichier_sortie_jpg4, 'w', encoding='utf-8') as fichier:
        for lien in liens_jpg4:
            fichier.write(lien + '\n')
    
    with open(fichier_sortie_saint2, 'w', encoding='utf-8') as fichier:
        for lien in liens_saint2:
            fichier.write(lien + '\n')
    
    #with open(fichier_sortie_tiktok, 'w', encoding='utf-8') as fichier:
        #for lien in liens_tiktok:
            #fichier.write(lien + '\n')

    # Exécuter le script download_jpg4.py
    subprocess.run(['python', 'Test/jpg4/download_jpg4.py'])

# Exemple d'utilisation
fichier_entree = 'Test/code_source/code_source.txt'
fichier_sortie_jpg4 = 'Test/jpg4/sortie_jpg4.txt'
fichier_sortie_saint2 = 'Test/saint2/sortie_saint2.txt'
fichier_sortie_tiktok = 'Test/tiktok/sortie_tiktok.txt'

extraire_liens(fichier_entree, fichier_sortie_jpg4, fichier_sortie_saint2, fichier_sortie_tiktok)
