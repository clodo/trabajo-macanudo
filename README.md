Trabajo macanudo
================

Hola Nico Bases

##Instalación

###Clonar repo
    git clone https://github.com/clodo/trabajo-macanudo.git PATH/TO/YOUR/APP

###Instalar dependencias
    sudo apt-get install python-profiler (para que funcione la debugToolbar)
    pip install -r requirements.txt

###Configurar variables de entorno
    export RECAPTCHA_PUBLIC_KEY='key'
    export RECAPTCHA_PRIVATE_KEY='key'
    export TWITTER_CONSUMER_KEY='key'
    export TWITTER_CONSUMER_SECRET='key'
    export TWITTER_TOKEN='key'
    export TWITTER_SECRET='key'

###Crear base de datos
    python manage.py reset

###Ejecutar
    python manage.py run

###Ejecutar tests
    nosetests --rednose
