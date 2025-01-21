Introduction
============

**My-Python-OC-Lettings-FR** est une application Django permettant la
gestion de locations immobilières. Elle comprend :

- Une base de données SQLite (par défaut) pour stocker les informations,
- Un front-end rendu par Django,
- Une configuration de déploiement basée sur Docker, Nginx et Gunicorn,
- Des conteneurs Docker pour l'application et pour le serveur web.

Objectifs
---------

- Illustrer le fonctionnement d'une application Django conteneurisée
- Utiliser Python 3.8 avec Gunicorn pour la partie serveur d'application
- Mettre Nginx en tant que proxy inversé pour gérer les requêtes HTTP
- Démontrer une intégration CI/CD (GitHub Actions, etc.)
