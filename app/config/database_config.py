import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define operating system ( Windows or Linux )
if os.name == 'nt':
    # Windows
    sqlite_file_name = "../../database/metrics.db"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    url_database = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
else:
    # Linux
    base_dir = "/opt/database/metrics.db"
    url_database = f"sqlite:///{base_dir}"


engine = create_engine(url_database,
                       echo=True,
                       pool_size=10,
                       max_overflow=20,
                       pool_timeout=30)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
