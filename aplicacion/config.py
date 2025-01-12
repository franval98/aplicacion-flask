import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = False # En despliegue esto pasa a FALSE # En desarrollo podemos cambiar a True
SQLALCHEMY_DATABASE_URI =  os.getenv('DATABASE_URL', 'sqlite:///{}/dbase.db'.format(PWD))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:password@localhost/base_datos'
#SQLALCHEMY_TRACK_MODIFICATIONS=False

