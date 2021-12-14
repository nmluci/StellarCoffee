from __future__ import annotations
from typing import List

from app.baseModel import db
from app.userdata.models import User, UserData

def partition(userData: List[UserData], low: int, high: int):
    pivot = low
    batas_bawah = low + 1

    for i in range(low + 1, high):
        if userData[i].point > userData[pivot].point:
            # Swap
            temp = userData[batas_bawah]
            userData[batas_bawah] = userData[i] 
            userData[i] = temp

            batas_bawah += 1
    temp = userData[pivot]
    userData[pivot] = userData[batas_bawah - 1]
    userData[batas_bawah - 1] = temp
    return batas_bawah

def quick_sort(userData: List[UserData], low: int, high: int):
    if (low >= high) :
        return
    new_high = partition(userData, low, high)
    quick_sort(userData, low, new_high - 1)
    quick_sort(userData, new_high, high)
    return

def sortUserByPoint(userData: List[UserData]):
    length_data = len(userData)
    temp_userData = userData.copy()
    quick_sort(temp_userData, 0, length_data)
    return list(x.toDict() for x in temp_userData)

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