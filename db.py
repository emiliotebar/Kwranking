from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Crea el engine indicando la cadena de conexión a la base de datos
engine = create_engine('sqlite:///keywords.sqlite')

# Crea el objeto para manejar la sesión de base de datos
Session = sessionmaker(bind = engine)
session = Session()

# Crea la clase base de la que hereden los modelos de la aplicación
Base = declarative_base()