from __future__ import annotations
from typing import List

from datetime import datetime

from sqlalchemy.sql.operators import notbetween_op
from app.inventory.models import Inventory

from app.order.models import Events, OrderItems, Orders, TodayEventData, TodaySpecialData, UserOrder, Order
from app.userdata.models import User
from app.baseModel import db

def generateTodaySpecialty() -> List[TodaySpecialData]:
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

def isItemExists(metadata: Order):
    itemList = db.session.query(Inventory).all()
    for itm in itemList:
        if metadata.itemName == itm.name:
            return True
    return False

def processCheckout(metadata: UserOrder):
    usr = db.session.query(User).filter(User.uid == metadata.uid).first()
    if not usr:
        raise Exception("user not registered")
    
    validMenu = list()
    grandTotal = int()
    grandQuantity = int()
    for itm in metadata.orders:
        print(itm)
        if not isItemExists(itm):
            print("item is not valid")
        else:
            validMenu.append(itm)
            grandTotal += itm.total_price
            grandQuantity += itm.quantity

    if len(metadata.orders) != len(validMenu):
        metadata.orders = validMenu
        metadata.total_price = grandTotal
        metadata.total_quantity = grandQuantity
    
    newOrder = Orders(
        done=True,
        uid=metadata.uid,
        grand_price=metadata.total_price,
        quantity=metadata.total_quantity,
        date_created=metadata.date_created
    )
    metadata.order_id = newOrder.insert()

    for itm in metadata.orders:
        newOrderItem = OrderItems(
            order_id=metadata.order_id,
            uid=metadata.uid,
            item_name=itm.itemName,
            quantity=itm.quantity,
            price=itm.price,
            total_price=itm.total_price
        )
        itm.id = newOrderItem.insert()
    
    usr.point += grandTotal/1000
    usr.update()
    metadata.done = True