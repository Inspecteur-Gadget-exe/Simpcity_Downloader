import os

# Fonction pour modifier le lien
def modifier_lien(lien):
    # Vérifier que le lien commence bien par le préfixe attendu
    prefixe_ancien = "https://saint2.su/d/"
    prefixe_nouveau = "https://simp2.saint2.su/api/download.php?file="
    
    if lien.startswith(prefixe_ancien):
        # Remplacer le préfixe
        lien_modifie = lien.replace(prefixe_ancien, prefixe_nouveau)
        # Supprimer le symbole '=' à la fin du lien
        lien_modifie = lien_modifie.rstrip('=')
        return lien_modifie
    else:
        raise ValueError("Le lien ne commence pas par le préfixe attendu.")

if __name__ == "__main__":
    # Obtenir le chemin absolu du script en cours d'exécution
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construire les chemins relatifs à partir du répertoire du script
    chemin_sortie_lien = os.path.join(script_directory, 'sortie_lien.txt')
    chemin_sortie_lien_modifie = os.path.join(script_directory, 'sortie_lien_modifie.txt')

    try:
        # Lire le fichier 'sortie_lien.txt'
        with open(chemin_sortie_lien, 'r', encoding='utf-8') as fichier:
            lien_original = fichier.readline().strip()
            print(f"Lien original : {lien_original}")

        # Modifier le lien
        lien_modifie = modifier_lien(lien_original)
        print(f"Lien modifié : {lien_modifie}")

        # Écrire le lien modifié dans un nouveau fichier ou écraser l'ancien
        with open(chemin_sortie_lien_modifie, 'w', encoding='utf-8') as fichier_modifie:
            fichier_modifie.write(lien_modifie + '\n')

        print(f"Le lien modifié a été enregistré dans '{chemin_sortie_lien_modifie}'.")

    except FileNotFoundError:
        print(f"Le fichier '{chemin_sortie_lien}' n'a pas été trouvé.")
    except ValueError as e:
        print(f"Erreur : {e}")
