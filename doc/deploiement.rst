Déploiement
===========

Aperçu
------

Le projet est conçu pour être déployé via **Docker** et **Nginx**, avec
**Gunicorn** comme serveur d'applications Python. L'architecture se
compose généralement de :

- Un conteneur Django/Gunicorn (``myapp``),
- Un conteneur Nginx servant de proxy inversé vers Gunicorn,
- Des configurations (ex. ``nginx.conf``, ``Dockerfile``) pour automatiser le tout.

Exemple d'utilisation avec Docker Compose
-----------------------------------------

Vous pouvez créer un fichier ``docker-compose.yml`` semblable à ::

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

Ensuite ::

  docker-compose up -d

et votre application sera accessible sur http://<votre-serveur>:80/.

CI/CD
-----

Vous pouvez mettre en place un pipeline **GitHub Actions** qui :

1. Construit l'image Docker,
2. Lance les tests (pytest, coverage, etc.),
3. Push l'image sur un registre (Docker Hub par ex.),
4. Déploie automatiquement sur le serveur cible (via SSH ou autre).

