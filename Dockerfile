# 1. Image officielle Python légère
FROM python:3.11-slim

# 2. Définir le répertoire de travail dans le container
WORKDIR /app

# 3. Copier les fichiers requirements.txt et installer les dépendances
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier tout le code source dans /app
COPY ./app ./app

# 5. Exposer le port 8000
EXPOSE 8000

# 6. Commande pour lancer Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
