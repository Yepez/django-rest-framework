# Imagen base
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /grupo_mb

# Copiar el archivo de requerimientos
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y graphviz
ENV PATH="/usr/bin/graphviz:${PATH}"

# Copiar el código fuente
COPY ./grupo_mb /grupo_mb

ENV DJANGO_SETTINGS_MODULE=grupo_mb.settings

# Exponer el puerto
EXPOSE 8000

# Ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
