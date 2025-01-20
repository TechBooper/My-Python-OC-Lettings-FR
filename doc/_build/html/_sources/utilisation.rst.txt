Utilisation
===========

Exécution en local (sans Docker)
--------------------------------

1. Démarrez le serveur Django ::

   python manage.py runserver

2. Ouvrez votre navigateur à l'adresse :
   http://127.0.0.1:8000/

3. (Optionnel) Créez un utilisateur admin ::

   python manage.py createsuperuser

Exécution avec Docker
---------------------

1. **Construire l'image Docker** ::

   docker build -t myapp:latest .

2. **Lancer le conteneur** sur le port 80 (si libre) ::

   docker run -d -p 80:80 --name myapp myapp:latest

3. Rendez-vous sur http://localhost/ pour vérifier l'application.

4. **Logs** ::

   docker logs myapp

