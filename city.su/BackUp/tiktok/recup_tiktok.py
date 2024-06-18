import re

def extraire_liens(fichier_entree, fichier_sortie):
    # Expression régulière pour trouver les liens commençant par "https://jpg4.su/" et exclure les guillemets
    pattern = r'www\.tiktok\.com/embed/\S+?(?="|\s|$)'
    
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
fichier_entree = 'Test/code_source/code_source.txt'
fichier_sortie = 'Test/tiktok/sortie_tiktok.txt'
extraire_liens(fichier_entree, fichier_sortie)
