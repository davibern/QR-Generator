# Base Python
FROM python:3.9-slim

# Copiamos el directorio de trabajo
WORKDIR /app

# Copiamos los requerimientos
COPY requirements.txt .
COPY . .

# Instalamos dependencias
RUN pip install -r requirements.txt

# Configuramos lanzador app
CMD ["python", "main.py"]