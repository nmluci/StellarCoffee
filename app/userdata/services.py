from __future__ import annotations
from typing import List

from app.baseModel import db
from app.userdata.models import User, UserData

def sortUserByPoint(userData: List[UserData]):
    for i in range(len(userData)):
        for seq, usr in enumerate(userData[:len(userData)-1]):
            if usr.point < userData[seq+1].point:
                temp = userData[seq]
                userData[seq] = userData[seq+1]
                userData[seq+1] = temp

    return list(x.toDict() for x in userData)

def userAddPoint(username: str, point: int):
    usr = db.session.query(User).filter(User.username==username).first()
    if not usr:
        raise Exception("username isn't registered")

    usr.point = point
    usr.update()

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