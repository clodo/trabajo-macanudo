Trabajo macanudo
================

Hola Nico Bases

##Instalación

###Clonar repo
    git clone https://github.com/clodo/trabajo-macanudo.git PATH/TO/YOUR/APP

###Instalar dependencias
    sudo apt-get install python-profiler (para que funcione la debugToolbar)
    pip install -r requirements.txt

###Crear base de datos
    python manage.py reset

###Ejecutar
    python manage.py run

###Ejecutar tests
    nosetests --rednose
