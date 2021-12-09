from __future__ import annotations
from typing import List

from datetime import datetime
from app.inventory.models import Inventory

from app.order.models import Events, TodayEventData, TodaySpecialData
from app.userdata.models import UserData
from app.baseModel import db

def generateTodaySpecialty() -> List[TodayEventData]:
    todaySpecials = db.session.query(Inventory).filter(Inventory.stock != 0).all()
    if not todaySpecials:
        raise Exception("no specials menu today")
    return list(TodaySpecialData(
        item.id,
        item.name,
        item.price
    ).toDict() for item in todaySpecials[:5])

def generateTodayEvents() -> List[TodayEventData]:
    todayDate = datetime.now().date()
    todayEvent = db.session.query(Events).filter((Events.date_start >= todayDate) & (Events.date_end <= todayDate)).all()
    if not todayEvent:
        raise Exception("no events available today")
    return list(TodayEventData(
        event.id, 
        event.name, 
        f"IDR {event.amount}" if event.amount_type == "cash" else f"{event.amount}%").toDict() for event in todayEvent)

def processCheckout(metadata: UserData):
    pass