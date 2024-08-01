from sqlalchemy import create_engine,  ForeignKey, Column, Integer, String, Text, DateTime, Boolean, Float, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_name = Column(String)
    password = Column(String)
    
    def __init__(self, id, email, user_name, password):
        self.id = id
        self.email = email
        self.user_name = user_name
        self.password = password
    
    def __repr__(self):
        return "<User(email='%s', username='%s', password='%s')>" % (
            self.email, self.username, self.password)
        
