from db import session, User
import uuid

def create_user(email, password):
    id = str(uuid.uuid4())
    if session.query(User).filter(User.id==id).first():
    user = User(id=id, email=email, password=password)
    session.add(user)
    session.commit()
    return user