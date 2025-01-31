# **Orange County Lettings**

## **Résumé**
Site web pour la gestion des locations et profils dans pour "Orange county". Ce projet utilise Django comme base et a été amélioré avec une **architecture conteneurisée** et un **pipeline CI/CD** pour une gestion et un déploiement automatisé.

---

## **Fonctionnalités**
- Gestion des profils et des locations.
- Déploiement automatisé via **GitHub Actions**.
- **Conteneurisation complète avec Docker**.
- Documentation technique hébergée sur **Read the Docs**.
- Utilisation de **Gunicorn** comme serveur WSGI.
- Proxy inversé et gestion des requêtes avec **Nginx**.
- Intégration de la surveillance des erreurs avec **Sentry**.

---

## **Développement local**

### **Prérequis**
- **Python**: Version 3.8 ou supérieure.
- **Git**: Pour cloner le dépôt.
- **Docker**: Pour construire et exécuter les conteneurs.

### **Installation et Exécution**

#### **Cloner le repository**
```bash
git clone https://github.com/Your-Username/Your-Repository.git
cd Your-Repository
```

#### **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
.env\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

#### **Exécuter l'application localement**
```bash
python manage.py runserver
```
Accédez au site via `http://localhost:8000`.

---

## **Utilisation de Docker**

### **Construire et Exécuter avec Docker**
L'application est entièrement conteneurisée et peut être exécutée via Docker.

#### **Construire l'image Docker**
```bash
docker build -t orange-county-lettings .
```

#### **Exécuter l'application avec Docker**
```bash
docker run -d -p 8000:8000 orange-county-lettings
```

---

## **Pipeline CI/CD**

Un pipeline **CI/CD** est configuré avec **GitHub Actions** pour automatiser les étapes suivantes :

### **Étapes du pipeline :**
1. **Build et Test :**
   - Linting avec `flake8`.
   - Tests unitaires avec `coverage`.
   - Validation de la couverture des tests (minimum 80%).
   - Création d'une image Docker de test.
2. **Build et Push de l'image finale :**
   - Une fois les tests réussis, une image Docker finale est créée et poussée vers Docker Hub.
3. **Déploiement :**
   - L'image finale est déployée sur un serveur (Droplet) avec Docker.
   - Le conteneur en cours d'exécution est remplacé par le nouveau.

### **Configuration GitHub Actions**
Le pipeline CI/CD est défini dans `.github/workflows/ci-cd-pipeline.yml`. Il inclut :
- La configuration pour Docker Buildx.
- Le déploiement via SSH sur un Droplet avec la commande `docker run`.

---

## **Déploiement**

### **Serveur WSGI avec Gunicorn**
L'application est servie via **Gunicorn**. Commande d'exécution :
```bash
gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
```

### **Proxy inversé avec Nginx**
Exemple de configuration Nginx pour la mise en production :
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /path/to/staticfiles/;
    }
}
```

---

## **Surveillance avec Sentry**
L'intégration de Sentry permet de surveiller les erreurs en production.

### **Configurer Sentry**
1. Ajouter votre **DSN Sentry** dans le fichier `.env` :
   ```env
   SENTRY_DSN=https://your-sentry-dsn
   ```
2. Les exceptions non gérées apparaîtront sur votre tableau de bord Sentry.

---

## **Tests**
### **Exécuter les tests unitaires**
```bash
pytest
```

### **Linting**
```bash
flake8
```

---

## **Variables d'environnement**
L'application utilise un fichier `.env` pour les variables sensibles :
- **SECRET_KEY** : Clé secrète Django.
- **SENTRY_DSN** : DSN pour Sentry.

Exemple `.env` :
```env
SECRET_KEY=your-secret-key
SENTRY_DSN=https://your-sentry-dsn
```
