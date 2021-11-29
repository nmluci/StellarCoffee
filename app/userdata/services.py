from app.baseModel import db
from app.userdata.models import User, UserData

def addPoint(username:str, amount: int):
    usr = db.session.query(User).filter(User.username==username).first()
    if not usr:
        raise Exception("username isn't registered")
    
    usr.point += amount
    usr.update()

def usePoint(username: str, amount: int):
    pass

def getUserData(metadata: UserData):
    usr = db.session.query(User).filter(User.username==metadata.username).first()
    if not usr:
        raise Exception("username isn't registered")
    
    metadata.uid = usr.uid
    metadata.firstname = usr.firstname
    metadata.lastname = usr.lastname
    metadata.point = usr.point
    metadata.password = usr.password
    