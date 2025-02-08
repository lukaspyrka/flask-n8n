# Oficjalny obraz Playwright z kompatybilnym GLIBC
FROM mcr.microsoft.com/playwright/python:v1.39.0-focal

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie wszystkich plików do kontenera
COPY . /app

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchomienie aplikacji
CMD ["python", "main.py"]
