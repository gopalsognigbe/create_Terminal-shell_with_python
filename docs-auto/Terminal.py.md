### Analyse du fichier Terminal.py

#### Rôle du fichier
Un émulateur de terminal simple qui:
1. Lit des commandes en boucle
2. Exécute ces commandes dans le shell du système
3. Gère quelques cas particuliers comme `cd` et `exit`

#### Logique principale
1. Boucle infinie qui attend des commandes utilisateur
2. Traitement spécial pour:
   - `cd` (changement de répertoire)
   - `exit` (sortie du programme)
3. Pour les autres commandes: exécution via `subprocess.run()`

#### Fonctions importantes
1. `os.chdir()` - Pour le changement de répertoire
2. `subprocess.run()` - Pour exécuter les commandes shell
3. `os.getcwd()` - Affiche le répertoire courant dans le prompt

#### Exemple d'utilisation
```bash
/home/user > ls -la  # Affiche le contenu du dossier
/home/user > cd /tmp  # Change de répertoire
/tmp > exit  # Quitte le terminal
```

Points clés à noter:
- Interface basique mais fonctionnelle
- Gestion minimale des erreurs (juste pour `cd`)
- Capture à la fois stdout et stderr des commandes
- Prompt affiche le répertoire courant