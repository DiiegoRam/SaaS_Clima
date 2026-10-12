# Usamos una imagen ligera oficial de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de requerimientos y nuestro código
COPY requirements.txt .
COPY clima_etl.py .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando que se ejecutará cuando despierte el contenedor
CMD ["python", "clima_etl.py"]