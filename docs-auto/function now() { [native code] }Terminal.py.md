### Analyse du fichier `Terminal.py`

#### Rôle du fichier
Le fichier `Terminal.py` est un script Python qui simule un terminal interactif. Il permet à l'utilisateur d'exécuter des commandes système directement depuis l'interpréteur Python.

#### Logique principale
Le script fonctionne en boucle infinie (`while True`), attendant que l'utilisateur entre une commande. Il traite les commandes spécifiques comme `cd` pour changer de répertoire ou `exit` pour quitter le terminal. Pour les autres commandes, il utilise `subprocess.run` pour exécuter la commande système et afficher le résultat.

#### Fonctions importantes
1. **`os.chdir(directory)`** : Change le répertoire de travail courant.
2. **`subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)`** : Exécute une commande système et capture sa sortie standard et d'erreur.

#### Exemple d'utilisation
- **Changer de répertoire** : `cd /chemin/vers/dossier`
- **Exécuter une commande système** : `ls -l`
- **Quitter le terminal** : `exit`

Ce fichier est utile pour créer un environnement interactif de console directement dans un script Python.