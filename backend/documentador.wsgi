import sys
import os

# Ruta al entorno virtual
activate_this = '/var/www/html/chocolate/backend/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Ruta a la aplicación
sys.path.insert(0, '/var/www/html/chocolate/backend')

from app import app as application