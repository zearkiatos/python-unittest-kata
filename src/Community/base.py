from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.config.config import Config

config = Config()
sqlite_connection_string = config.get_config()['SQLITE_CONNECTION_STRING']

engine = create_engine(sqlite_connection_string)
Session = sessionmaker(bind=engine)
Base = declarative_base()

