import re
import subprocess
import os

def extraire_liens(fichier_entree, fichier_sortie_jpg4, fichier_sortie_saint2):
    # Expressions régulières pour trouver les liens spécifiques
    pattern_jpg4 = r'https://jpg4\.su/img\S+?(?="|\s|$)'
    pattern_saint2 = r'https://saint2\.su/embed\S+?(?="|\s|$)'

    # Lire le contenu du fichier d'entrée avec l'encodage 'utf-8'
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()

    # Trouver tous les liens correspondants
    liens_jpg4 = re.findall(pattern_jpg4, contenu)
    liens_saint2 = re.findall(pattern_saint2, contenu)

    # Filtrer les liens à exclure pour jpg4
    liens_jpg4 = [lien for lien in liens_jpg4 if lien != "https://jpg4.su/img/YnBxSZe"]

    # Écrire les liens trouvés dans les fichiers de sortie avec l'encodage 'utf-8'
    with open(fichier_sortie_jpg4, 'w', encoding='utf-8') as fichier:
        for lien in liens_jpg4:
            fichier.write(lien + '\n')
    
    with open(fichier_sortie_saint2, 'w', encoding='utf-8') as fichier:
        for lien in liens_saint2:
            fichier.write(lien + '\n')

    # Commande pour exécuter le programme suivant
    # Remplacer 'download_jpg4.py' par le chemin relatif du script à exécuter
    script_a_executer = os.path.join(script_directory, '../jpg4/download_jpg4.py')
    command = ["python", script_a_executer]

    # Exécution du programme externe
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Sortie du programme externe :\n{result.stdout.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du programme externe :\n{e.stderr.decode()}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Obtenir le chemin absolu du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construire les chemins relatifs à partir du répertoire du script
    fichier_entree = os.path.join(script_directory, '../code_source/code_source.txt')
    fichier_sortie_jpg4 = os.path.join(script_directory, '../jpg4/sortie_jpg4.txt')
    fichier_sortie_saint2 = os.path.join(script_directory,'../saint2/sortie_saint2.txt')

    # Appeler la fonction avec les chemins relatifs
    extraire_liens(fichier_entree, fichier_sortie_jpg4, fichier_sortie_saint2)
