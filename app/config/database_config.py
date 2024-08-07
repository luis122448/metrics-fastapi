import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../../database/metrics.db"
base_dir = os.path.dirname(os.path.abspath(__file__))

url_database = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(url_database, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
