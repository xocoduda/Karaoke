Para comenzar con la instalación del proyecto, hará falta descargar python desde su página oficial 
o la de microsoft, el entorno de desarrollo (Visual Studio Code) en este caso, e instalar la 
extensión de python para Visual Studio.

Para preparar el entorno virtual de trabajo con django, se ejecuta el siguiente código en la consola:
	-python –m venv nombre_carpeta

Una vez dentro de la carpeta del proyecto, se activa el entorno virtual:
	.\Scripts\activate

Se instala django:
	django-admin startproject nombre_proyecto .

Y ya estaría listo para ejecutarse en modo debug el servidor:
	python manage.py runserver

Si se quiere crear una aplicación, el comando sería:
	python manage.py startapp nombre

Para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes en Python, se instalará
"Pillow", una biblioteca adicional:
	pip install pillow
Para el despliegue, se ha utilizado un servidor temporal "Ngrok" que proporciona 1Gb gratis. Su 
funcionamiento se basa en abrir una cmd en el directorio en el que se encuentra el archivo, ejecutar:
	ngrok http 8000
y sustituir la direccion de red que te proporciona en settings.py, mas concretamente en:
- ALLOWED_HOSTS = ['30d8-79-145-125-227.ngrok-free.app', 'localhost', '127.0.0.1']
- CORS_ALLOWED_ORIGINS = ["https://30d8-79-145-125-227.ngrok-free.app",]
- CSRF_TRUSTED_ORIGINS = ['https://30d8-79-145-125-227.ngrok-free.app',]