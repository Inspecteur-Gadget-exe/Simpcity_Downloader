import re
import subprocess
import os

def extraire_liens(fichier_entree, fichier_sortie):
    # Expression régulière pour trouver les liens commençant par "https://jpg4.su/" et exclure les guillemets
    pattern = r'https://jpg4\.su/img/\S+?(?="|\s|$)'
    
    # Lire le contenu du fichier d'entrée avec l'encodage 'utf-8'
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    
    # Trouver tous les liens correspondants
    liens = re.findall(pattern, contenu)
    
    # Filtrer les liens à exclure
    liens = [lien for lien in liens if lien != "https://jpg4.su/img/YnBxSZe"]
    
    # Écrire les liens trouvés dans le fichier de sortie avec l'encodage 'utf-8'
    with open(fichier_sortie, 'w', encoding='utf-8') as fichier:
        for lien in liens:
            fichier.write(lien + '\n')

# Exemple d'utilisation
if __name__ == "__main__":
    # Obtenir le chemin absolu du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construire les chemins relatifs à partir du répertoire du script
    fichier_entree = os.path.join(script_directory, '../code_source/code_source.txt')
    fichier_sortie = os.path.join(script_directory, 'sortie_jpg4.txt')

    # Appeler la fonction avec les chemins relatifs
    extraire_liens(fichier_entree, fichier_sortie)

    # Commande pour exécuter le programme suivant
    # Remplacer 'download_jpg4.py' par le chemin relatif du script à exécuter
    script_a_executer = os.path.join(script_directory, 'download_jpg4.py')
    command = ["python", script_a_executer]

    # Exécution du programme externe
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Sortie du programme externe :\n{result.stdout.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du programme externe :\n{e.stderr.decode()}")
