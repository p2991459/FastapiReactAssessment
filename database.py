from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()


# database
db_url = f"{os.getenv('database')}://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}/{os.getenv('db_name')}"
engine = create_engine(db_url,echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)
Session = session()