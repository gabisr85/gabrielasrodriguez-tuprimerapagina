# Guia para mi primer proyecto django

1. creamos una carpeta para guardar el proyecto
2. creamos nuestro archivo README.md a la altura del repositorio
3. creamos el archivo .gitignore con la informacion que nos da la pagina gitignore.io (nunca realizar un commit sin tener listo el archivo) a la altura del repositorio
4. creamos un repositorio en github y seguir los pasos que indica
5. activamos el entorno virtual
6. creamos el requeriments.txt usando el comando pip freeze
7. creamos un proyecto django con el comando django-admin startptoject <nombre_del_proyecto> . (no olvidar el punto final)
8. ejecutamos el proyecto, primero con el comando python manage.py migrate y luego python manage.py runserver
hacemos Ctrl+"clic" en http://127.0.0.1:8000/ y me abre el navegador del proyecto indicando que esta instalado
9. abimos otra terminal, para tener dos asi en una ingresamos los comandos y la anterior nos muestra informacion
10. creamos una aplicacion con el comando python manage.py startapp <nombre_aplicacion>
11. para que el proyecto reconoza la aplicacion, debemos ir al archivo settings.py en la carpeta del proyecto y en la parte de INSSTALLED_APP agregamos la app <nombre_aplicacion>
12. configuramos las url en el archivo urls.py en la carpeta del proyecto. Aqui armamos las ubicacion para acceder a cierto lugar de cada aplicacion (a que pantalla)
13. creamos un archivo urls.py en cada aplicacion (misma informacion que en la urls del proyecto, con import url y vista)
14. creamos la vista en la aplicacion views.py, con import (donde hay retornos)
15. armamos las carpetas de templates. Creamos una carpeta de template a la altura de nuestro proyecto. Tambien creamos otra dentro de cada aplicacion y aqui otra carpeta con el nombre de la aplicacion y ahi va a ser donde se crearan los arhivos html (enonces TEMPLATES > APP > inicio.html). En el settings > TEMPLATES > DIRS indicamos la carpeta <templates>. Y con APP_DIRS true, va a tomar todos los templates de cada aplicacion
16. en views.py del proyecto para saber la ubicacion del archivo html debo indicar esa carptea APP
17. CREAMOS un archivo html. Escribimos ! +  enter, y nos sale la estructura basica o con el comando html:5 tambien
18. por cada vista que creamos debemos
- indicar la url
- crear el template
- replico la navegacion en cada plantilla de la app
19. para cargar informacion se requieren formularios. En el arhcivo models.py creamos la clase e indicamos el import
20. definimos las migraciones que indican que creamos un modelo con el comando python mange.py makemigrations. Luego ejecutamos con python manage.py migrate
21. indicamos los formularios en la plantilla. Alli se determina el metodo de envio de informacion
22. creamos un archivo forms.py en la aplicacion. Importramos y creamos un formulario
23. en views identificamos el metodo de envio de esa informacion, agregamos import
24. luego en la platnilla debo indicar el formulario que debe mostrar {{formulario}} para que muestre lo que cree
25. para seguir creando repetimos los pasos: url, views, template (creo plantilla). Replico y modifico la informacion necesaria para que muestre correctamente la informacion
26. para finalizar y subir la informacion al repositorio
- git add .
- git commit -m 'informacion'
- git push