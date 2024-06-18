import re
import os

def extraire_liens(fichier_entree, fichier_sortie):
    # Expression régulière pour trouver les liens commençant par "https://jpg4.su/" et exclure les guillemets
    pattern = r'https://saint2\.su/embed\S+?(?="|\s|$)'
    
    # Lire le contenu du fichier d'entrée avec l'encodage 'utf-8'
    with open(fichier_entree, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    
    # Trouver tous les liens correspondants
    liens = re.findall(pattern, contenu)
    
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
    fichier_sortie = os.path.join(script_directory, 'sortie_saint2.txt')

    # Appeler la fonction avec les chemins relatifs
    extraire_liens(fichier_entree, fichier_sortie)
