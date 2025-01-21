# **Orange County Lettings**

## **Résumé**
Site web pour la gestion des locations et profils dans le comté d'Orange. Ce projet utilise Django comme base et a été amélioré avec des outils modernes pour une gestion efficace et un déploiement automatisé.

---

## **Fonctionnalités**
- Gestion des profils et des locations.
- Déploiement automatisé via GitHub Actions.
- Conteneurisation avec Docker.
- Documentation hébergée sur Read the Docs.
- Utilisation de Gunicorn comme serveur WSGI.
- Proxy inversé et gestion des requêtes avec Nginx.

---

## **Développement local**

### **Prérequis**
- **Python**: Version 3.8 ou supérieure.
- **Git**: Pour cloner le dépôt.
- **Docker**: Pour construire et exécuter les conteneurs.
- **SQLite**: Préinstallé sur la plupart des systèmes pour la base de données locale.

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
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
```

#### **Exécuter l'application localement**
```bash
python manage.py runserver
```
Accédez au site via `http://localhost:8000`.

---

## **Utilisation de Docker**
L'application peut être exécutée entièrement dans des conteneurs Docker.

### **Construire l'image Docker**
```bash
docker build -t orange-county-lettings .
```

### **Exécuter l'application avec Docker**
```bash
docker run -d -p 8000:8000 orange-county-lettings
```

---

## **Déploiement**

### **Serveur WSGI avec Gunicorn**
L'application utilise **Gunicorn** pour servir le projet Django.

Commandes d'exécution :
```bash
gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
```

### **Proxy inversé avec Nginx**
Le fichier de configuration Nginx (`nginx.conf`) doit être configuré pour gérer les requêtes et proxy vers Gunicorn.

#### Exemple d'une configuration Nginx :
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

## **Intégration Continue**
Le pipeline CI/CD est configuré via **GitHub Actions** pour :
1. Exécuter les tests unitaires avec `pytest`.
2. Effectuer un linting avec `flake8`.
3. Construire et pousser les images Docker si les tests passent.

Fichier de configuration GitHub Actions : `.github/workflows/main.yml`.

---

## **Documentation**
La documentation du projet est hébergée sur **Read the Docs**. Consultez-la pour des détails supplémentaires :
[Documentation sur Read the Docs](https://yourproject.readthedocs.io).

---

## **Base de Données**
### **Utilisation avec SQLite**
- Fichier de base de données : `oc-lettings-site.sqlite3`
- Commandes courantes :
  ```bash
  sqlite3 oc-lettings-site.sqlite3
  .tables
  ```

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
L'application utilise un fichier `.env` pour stocker les variables sensibles :
- **SECRET_KEY** : Clé secrète Django.
- **DATABASE_URL** : URL de connexion à la base de données.
- **SENTRY_DSN** : DSN pour l'intégration Sentry.

Exemple `.env` :
```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///oc-lettings-site.sqlite3
SENTRY_DSN=https://your-sentry-dsn
```

---

## **Contribuer**
1. Forkez le repository.
2. Créez une branche avec vos modifications :
   ```bash
   git checkout -b feature/your-feature
   ```
3. Poussez votre branche et ouvrez une pull request.

---

## **Licence**
Ce projet est sous licence [MIT](LICENSE).
