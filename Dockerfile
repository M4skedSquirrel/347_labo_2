# Stage de base commun
FROM python:3.9-slim as base

WORKDIR /app

# Installation des dépendances communes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers communs
COPY models.py .
COPY templates/ templates/
COPY app.py .

# Stage de développement
FROM base as development
ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1

# Copie des fichiers spécifiques au développement
COPY addDataDevDb.py .

# Exposer le port
EXPOSE 5000

# Commande pour le développement
CMD ["sh", "-c", "python addDataDevDb.py && python app.py"]

# Stage de production
FROM base as production
ENV FLASK_ENV=production
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=0
ENV PYTHONUNBUFFERED=1

# Copie des fichiers spécifiques à la production
COPY addDataProdDb.py .

# Exposer le port
EXPOSE 5000

# Commande pour la production
CMD ["sh", "-c", "python addDataProdDb.py && python app.py"] 