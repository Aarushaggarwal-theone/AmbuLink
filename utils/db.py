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
    
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
    
    def __repr__(self):
        return "<User(email='%s', password='%s')>" % (
            self.email, self.username, self.password)
        
engine = create_engine('sqlite:///db.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

session.query(User).all()
