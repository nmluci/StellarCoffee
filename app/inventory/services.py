from app.inventory.models import Item, Inventory

def registerNewItem(metadata: Item):
    if not metadata.id:
        raise Exception("invalid item id")
    if not metadata.name:
        raise Exception("invalid menu's name")
    if not metadata.price:
        raise Exception("menu's price can't be zero")

    newMenu = Inventory(
        id=metadata.id,
        name=metadata.name,
        price=metadata.price
    )
    newMenu.insert()
