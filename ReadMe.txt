Como correr el proyecto usando conda (Es analogo a usar un environment normal de python)

- Usar Anaconda Promp (Consola de anaconoda) o CMD (Simbolo de sistema) en caso de python.
- Activar Environment de Django: conda activate django (o con django/activate sin conda)
- Dejar ruta de consola en la carpeta del proyecto, en mi caso: cd desktop/pagweb/locallibrary
- Correr Server con: python manage.py runserver
- Abrir una pestaña de navegador con url http://127.0.0.1:8000/

--- Upgrade 27/12 ----
Cambie la tabla usando Jquery Datatables con la DB que viene con django (sqlite3)
para agregar un deportista meterse a 127.0.0.1:8000/admin
user: skill
pass: ramoqlmalo

si quieren hacerse un admin, antes de correr el server, escribir python manage.py createsuperuser 







Ayudas: https://developer.mozilla.org/es/docs/Learn/Server-side/Django

