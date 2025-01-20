Installation
============

Prérequis
---------

- **Python 3.8** ou version supérieure (recommandé si vous exécutez le projet localement).
- **Docker** et **docker-compose** installés sur votre machine.
- **Git** pour cloner le projet (optionnel).

Étapes d'installation
---------------------

1. **Cloner le dépôt** (facultatif si vous avez déjà les fichiers) ::

   git clone https://github.com/votre-utilisateur/My-Python-OC-Lettings-FR.git
   cd My-Python-OC-Lettings-FR

2. **Installer les dépendances** si vous exécutez localement sans Docker ::

   pip install -r requirements.txt

3. **Configurer le fichier .env** (optionnel)  
   Vous pouvez définir des variables d'environnement (comme `SECRET_KEY`,
   `DEBUG`, etc.).

4. **(Optionnel) Créer la base de données** si vous lancez en local ::

   python manage.py migrate

