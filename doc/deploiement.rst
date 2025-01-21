Déploiement
===========

Aperçu
------

Le projet est conçu pour être déployé via **Docker** et **Nginx**, avec
**Gunicorn** comme serveur d'applications Python.

- Conteneur Django/Gunicorn (``myapp``)
- Conteneur Nginx servant de proxy inversé
- Fichiers de configuration (``nginx.conf``, ``Dockerfile``)

Exemple avec Docker Compose
---------------------------

Un exemple de ``docker-compose.yml`` pourrait ressembler à ::

  version: "3"
  services:
    web:
      build: .
      container_name: myapp
      ports:
        - "80:80"
      environment:
        - SECRET_KEY=changeme
        - DEBUG=0
      restart: always

Puis exécutez ::

  docker-compose up -d

Votre application sera alors accessible à l'adresse http://<votre-serveur>:80/.

CI/CD
-----

Vous pouvez mettre en place un pipeline (ex. GitHub Actions) qui :

1. Construit l'image Docker
2. Lance les tests (pytest, coverage, etc.)
3. Pousse l'image sur Docker Hub
4. Déploie automatiquement sur le serveur cible via SSH ou autre méthode.
