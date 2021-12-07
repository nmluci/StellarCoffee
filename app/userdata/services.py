from __future__ import annotations
from typing import List

from app.baseModel import db
from app.userdata.models import User, UserData

def sortUserByPoint(userData: List[UserData]):
    return list(x.toDict() for x in userData)

def getUserData(metadata: UserData):
    usr = db.session.query(User).filter(User.username==metadata.username).first()
    if not usr:
        raise Exception("username isn't registered")
    
    metadata.uid = usr.uid
    metadata.firstname = usr.firstname
    metadata.lastname = usr.lastname
    metadata.point = usr.point
    metadata.password = usr.password
    
def getLeaderboard(usrCount: int):
    users = db.session.query(User).all()
    sortedUser = sortUserByPoint(list(UserData(
        username=usr.username,
        uid=usr.uid,
        point=usr.point
    ) for usr in users))
    return sortedUser[:int(usrCount)]