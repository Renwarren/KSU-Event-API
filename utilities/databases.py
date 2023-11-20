from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()

DATABASE_URL = "mysql+mysqlconnector://admin:Mnas1506$@eventtracker.ctgvnaaozzpy.us-east-2.rds.amazonaws.com/eventtracker"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


