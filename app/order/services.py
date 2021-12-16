from __future__ import annotations
from typing import List

from datetime import datetime

from app.inventory.models import Inventory

from app.order.models import Events, OrderItems, Orders, TodayEventData, TodaySpecialData, UserOrder, Order, generalHistory, EventData, Graph
from app.userdata.models import User
from app.baseModel import db

def generateTodaySpecialty() -> List[TodaySpecialData]:
    aliases = ["Espresso", "Cappucino", 
		   "Cafe Latte", "Americano", 
		   "Vanilla Latte", "French Fries", 
		   "Croissant", "Deluxe Burger",
		   "Potato Wedges", "Cheese Burger",
		   "Lemon Tea", "Taro Latte", "Chocolate Latte", "Lychee Tea", "Matcha Latte"]

    g = Graph(15, aliases)
    g.graph =	[
		[ 0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ],
		[ 0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ],
		[ 1 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ],
		[ 1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ],
		[ 1 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ], 
		[ 1 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ],
		[ 0 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ],
		[ 1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ],
		[ 1 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ],
		[ 1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ],
		[ 1 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ],
		[ 1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ],
		[ 1 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0 ],
		[ 0 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ],
		[ 1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ],
    ]

    allSpeciality = g.graphColouring(5)
    for key in allSpeciality.keys():
        detailed = list()
        for itm in allSpeciality[key]:
            print(itm)
            specialItem = db.session.query(Inventory).filter(Inventory.name==itm).first()
            detailed.append(TodaySpecialData(
                item_id=specialItem.id,
                name=specialItem.name,
                price=specialItem.price,
                path=specialItem.path_picture
            ))
        allSpeciality[key] = detailed

    return allSpeciality

def generateTodayEvents() -> List[TodayEventData]:
    todayDate = datetime.now().date()
    todayEvent = db.session.query(Events).filter((Events.date_start <= todayDate) & (Events.date_end >= todayDate)).all()
    if not todayEvent:
        raise Exception("no events available today")
    return list(TodayEventData(
        event_id=event.id, 
        name=event.name,
        coupon_code=event.coupon_code,
        disc_amount=f"IDR {event.amount}").toDict() for event in todayEvent)

def generateAllValidEvents() -> List[TodayEventData]:
    todayDate = datetime.now().date()
    allEvent = db.session.query(Events).filter((Events.date_end >= todayDate)).all()
    if not allEvent:
        raise Exception("no events available yet")
    return list(TodayEventData(
        event_id=event.id, 
        name=event.name,
        coupon_code=event.coupon_code,
        disc_amount=f"IDR {event.amount}").toDict() for event in allEvent)

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

def insertEvents(metadata: EventData):
    events = db.session.query(Events).filter(Events.coupon_code==metadata.coupon).all()
    if events:
        print(list(x.coupon_code for x in events))
        raise Exception("event already listed")
    
    newEvent = Events(
        name=metadata.name,
        amount=metadata.amount,
        coupon_code=metadata.coupon,
        date_start=metadata.date_start,
        date_end=metadata.date_end,
    )
    newEvent.insert()

    metadata.id = newEvent.id

def getUserGeneralHistoryCheckout(metadata: str) -> List[generalHistory]:
    res = []
    allOrders = db.session.query(Orders).all()

    for order in allOrders:
        if order.uid == int(metadata):
            userHistory = generalHistory(
                order_id=order.id,
                date_created=order.date_created,
                grand_total=order.grand_price,
                total_item=order.quantity,
                status=order.done
            )
            res.append(userHistory.toDict())
    return res
