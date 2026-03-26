Analyse du fichier Terminal.py :

**Rôle du fichier** :
- Implémente un terminal interactif simple qui exécute des commandes système.

**Logique principale** :
1. Boucle infinie qui attend des commandes utilisateur
2. Traitement spécial pour la commande `cd` (changement de répertoire)
3. Commande `exit` pour quitter le terminal
4. Exécution des autres commandes via subprocess.run()

**Fonctions importantes** :
- `os.chdir()` : changement de répertoire
- `subprocess.run()` : exécution des commandes système
- Gestion des erreurs pour `cd` (FileNotFoundError)

**Exemple d'utilisation** :
```
/home/user > ls
file1.txt  file2.txt
exit pour sortir

/home/user > cd /tmp
/tmp > pwd
/tmp
exit pour sortir

/tmp > exit
```
(le programme se termine)

Points clés :
- Shell basique avec gestion du répertoire courant
- Affiche stdout et stderr des commandes
- Interface minimale avec invite personnalisée (chemin courant)