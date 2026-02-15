from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABSE_URL = 'mysql+pymysql://root:Ayan1234%40@localhost:3306/todosapplication'
SQLALCHEMY_DATABSE_URL = 'postgresql://todo_app_a2yc_user:lkh6J8Lt6RsYDnqvMvaUgW2PogXCtc9x@dpg-d68vb6l6ubrc73aa396g-a.singapore-postgres.render.com/todo_app_a2yc'
engine = create_engine(SQLALCHEMY_DATABSE_URL)

# SQLALCHEMY_DATABSE_URL = 'sqlite:///./todosapp.db'
# engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()