from sqlalchemy import create_engine,  ForeignKey, Column, Integer, String, Text, DateTime, Boolean, Float, CHAR
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
    
    def __repr__(self):
        return "<User(email='%s', password='%s')>" % (
            self.email, self.password)


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(String, primary_key=True)
    full_name = Column(String)
    age = Column(Integer)
    blood_type = Column(String)
    allergies = Column(String)
    weight = Column(Float)
    height = Column(Float)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User", backref=backref('patients', order_by=id))

class Contacts(Base):
    __tablename__ = 'contacts'
    id = Column(String, primary_key=True)
    full_name = Column(String)
    relation = Column(String)
    phone_number = Column(String)
    email = Column(String)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User", backref=backref('contacts', order_by=id))
    
class Hospital(Base):
    __tablename__ = 'hospitals'
    id = Column(String, primary_key=True)
    location = Column(String)
    phone_number = Column(String)
    
class Ambulance(Base):
    __tablename__ = 'ambulances'
    id = Column(String, primary_key=True)
    location = Column(String)
    phone_number = Column(String)
    status = Column(Boolean)
    hospital_id = Column(String, ForeignKey('hospitals.id'))
    hospital = relationship("Hospital", backref=backref('ambulances', order_by=id))
    
class Emergency(Base):
    __tablename__ = 'emergencies'
    id = Column(String, primary_key=True)
    accepted = Column(Boolean)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship("User", backref=backref('emergencies', order_by=id))
    ambulance_id = Column(String, ForeignKey('ambulances.id'))
    ambulance = relationship("Ambulance", backref=backref('emergencies', order_by=id))
    hospital_id = Column(String, ForeignKey('hospitals.id'))
    hospital = relationship("Hospital", backref=backref('emergencies', order_by=id))

engine = create_engine('sqlite:///db.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

import uuid

def create_user(session, email, password):
    id = str(uuid.uuid4())
    if session.query(User).filter(User.email==email).first():
        message = {"message":"User already exists", "status":400}
        return {"message":message}

    else:
        user = User(id=id, email=email, password=password)
        session.add(user)
        session.commit()
        message = {"message":"User created successfully", "status":200}
        
        session = {"user":id, "expires": str(datetime.datetime.now() + datetime.timedelta(days=1))}
    
        return {"message":message, "session":session}

def login_user(session, email, password):
    user = session.query(User).filter(User.email==email).first()
    if user:
        if user.password == password:
            message = {"message":"Login successful", "status":200}
            session = {"user":user.id, "expires": str(datetime.datetime.now() + datetime.timedelta(days=1))}
            return {"message":message, "session":session}
        else:
            message = {"message":"Incorrect password", "status":400}
            return {"message":message}
    else:  
        message = {"message":"This email does not exist", "status":400}
        return {"message":message}
        