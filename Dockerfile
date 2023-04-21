FROM python:3.8 
# Se especifica el lenguaje y si se desea la versión

WORKDIR /charts
# El directorio
COPY requirements.txt /charts/requirements.txt 
# Copiar, el primer requirements.txt es el archivo en local y el segundo en el contenedor

RUN pip install --no-cache-dir --upgrade -r /charts/requirements.txt
# Correr la instalación de las dependencias y omitiendo el cache

COPY . /charts
# copiar el resto de archivos de la carpeta


CMD bash -c "while true; do sleep 1; done"
# Se deja esta linea para que se mantenga activo ya que necesitamos que el contenedor este disponible