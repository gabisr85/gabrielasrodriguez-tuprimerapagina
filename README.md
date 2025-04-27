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

# ENTREGA FINAL
27. importante: cuando tenemos creada una clase en modelo.py, por cada modificacion se debe realizar un migrate
28. cuando creamos un campo fecha en models, es recomendable que pueda estar vacio por si hay datos previos <models.DateField(null=True)>. En forms realizamos las modificaciones necesarias como un <wigdet> para que podamos seleccionar la fecha y en views indicamos el campo fecha.
29. creamos un superusuario "admin" <python manage.py createsuperuser> que sera el administrador que vera toda la informacion de la pagina. en el archivo admin.py le pedimos que regstre el modelo de nuestra app para poder ver un modificar informacion.
30. modificaciones CRUD: lectura,modificacion y borrado del objeto creado. primero en la URL creamos el acceso, a que vista lleva los datos, y el campo variable que traiga el identificador (como es un valor numerico indicamos el int). en views definimos esa vista pidiendo que los datos se obtengan por el id, y retornar al template nuevo (que vamos a crear). en dicho template agregar un ancla que utiliza info de la url.
31. si la vista la definimos como clase hay que importar la vista a heredar, indicamos el modelo a utilizar y el template. En la url lleva datos diferentes a una <def>como un <pk> para identificador. el modelo es la variable que utilizara el template. (dato: variable plural indica el camino desde el listado)
32. cuando cramos una clase de edicion se utiliza un formulario, el atriburo succes_url indica a donde va la info que se edito. Se indica como "form".
33. Herencia de templates: se crea uno base en la carpeta template a la altura del proyecto y con <{% block contenido %}{% endblock contenido %}> indico que es lo que quiero que agregue, este tiene las anclas de navegacion. en los otros templates extiendo con {% extend base.html %}.
34. creamos una aplicacion <python manage.py startapp usuarios> para login y logut (realizamos las conexiones al crear app)
35. seguimos los pasos de creacion de app: url con sus import como login y logut. Views, definimos <def> login y <class> logout. creamos el template: <template/usuarios>.
36. LOGIN: al ser formulario de autenticacion en views importamos <AuthenticationForm(request, data=request.POST)> que valida si un usuario existe. importamos <login as django_login> permite que el usuartio quede conectado. url import <login>.
37. LOGOUT: en url import <LogoutView> porque es una clase basada en vistas. ene l path indicamos el template logout. En el template base agregamos un boton armamos un formulario de seguridad <csrf_token>
38. REGISTRO: determinar url import <registro>. creamos en views <def registro> utilizando formulario, importamos <UserCreationForm>. Creamos template. agregamos el ancla en el base.
39. en REGISTRO, el formulario modelform, permite guardar los datos <formulario.save()>
40. para modificar el formato por defecto, creamos un formulario <FormularioModificarRegistro>. Este se crea en <forms.py>, importamos <UserCreationForm> entonces <FormularioModificarRegistro(UserCreationForm)>
41. creamos una subclase <class Meta> para poder cambiar informacion que no tiene el formulario que se hereda de model form. Aqui usamos el models <User>, lo importamos (para cambiar por ejemplo los textos de ayuda o dejarlos vacios)
42. para limitar que un usuario pueda hacer modificaciones debo asegurar que este logueado. Se utiliza el clase MIXINS. En views se importa <LoginRequiredMixin> (lo indicamos en la clase como primera herencia)
* en el Setting indicamos <LOGIN_URL = "/usuarios/login/"> para que cuando no estoy logueado y quiero modificar algo, me lleve al login.
43. DECORADOR permite englobar funcionalidades. import <login_required> y se indica antes de la funcion <@loguin_required>
44. crear Edicion de usuario: en views <UserChangeForm> y lo importamos. determinamos la url y lo indicamos en template base. Creamos el template editar_usuario
45. creadmos <FormularioEdicionPerfil> en forms para cambiar el formato. al igual que modificar perfil, creamos la subclase <class Meta> lo importamos en vista
* le indicamos al formulario <FormularioEdicionPerfil(instance=requets.user)>, se lo agregamos a todos los formularios de la clase, instance=requets.user
46. AVATAR. a un modelo se le agrega el campo imagen, se importa libreria, se editan los formularios, la informacion que se les pasa a los formulario n las vistas y en los termplates se agrega en las etiquetes form para que acepte trabajar con imagenes
47. en models.py creamos un modelo aparte sobre impormacion extra al model User. importamso y creamos una clase <Infoextra(models.Model)>
48. el campo extra en este caso es AVATAR pero para trabajar con imagenes enecesito instalar pip instal pillow, actualizar requeriments y migramos
49. agregamos el campo de imagen en editar perfil, se modifica el modelo agregando el campo. para que reconoza imagenes un formulario se debe agregar <regest.FILES>
* indico al fomulario que guarde la informacion del InfoExtra relacionandolo con el Usuario
49. en el tempalate de editar perfil pasar <enctype="multipart/fomr-data"> 
50. IMPORTANTE: en settings agregar MEDIA_URL = /media/". primero import os luego MEDIA_ROOT = os.path.join(BASE_DIR, "media")
51. en url del proyecto agrego al final <+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)> e importamos settings
52. IMPORTANTE: cuando un usuario se loguea, se le cree un user y un infoextra.
* en vista importamos el modelo InfoExtra y en el mismo login agregamos <InfoExtra.objects.get_or_create(user=usuario)>
* para mostar la imagen en editar perfil, indicar formulario de editar perfil un <initial={ 'avatar' : infoextra.avatar },>
# 53 Agregar campo en Usuarios
* se crearon dos campos: Sports y Hobbies
* los agregamos en forms.py
* en models.py en el Infoextra ya que el modelo User no los incluye
* agrego tambien en views.py en el formulario editar perfil
# 54 Agregar imagen en productos
* agregar en el template base al ancla de listado de porductos la imagen
* en forms importar Models y Producto, y agrego la imagen en clase y subclase
* models agregar la imagen con los armugentos para subir imagen y que pueda estar vacia)
* template en  agregar_producto indicar request.FILES, en clase Modificar Producto agregar la imagen
* se agrega en los templates eliminar y y modificar agrego enctype="multipart/form-data", en detalle producto el en campo imagen
# 55 Crear Perfil
* en views.py creo un def perfil_usuario teniendo en cuenta los datos de infoextra y los datos del modelo user. agrego @loguin_required
* en url y definimos el path
* creamos el template, tambien tenemos en cuenta los atriburos de user y info_extra. En infoextra indicamos mensaje si esta vacio.
* incorporamos en el template base el ancla d perfil
# 56 Start Bootstrap
* descargamos plantilla de html. se crea una carpeta llamada Static
* copiamos la info de html y la pegamos en nuestro templante Base y modificamos para incorporar nuestros codigos con la estetica del bootstrap
57. para finalizar realizamos el git push