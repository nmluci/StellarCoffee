from app.inventory.models import Item, Inventory

def registerNewItem(metadata: Item):
    if not metadata.id:
        return Exception("invalid item id")
    if not metadata.name:
        return Exception("invalid menu's name")
    if not metadata.stock:
        metadata.stock = 0
    if not metadata.price:
        return Exception("menu's price can't be zero")

    newMenu = Inventory(
        id=metadata.id,
        name=metadata.name,
        stock=metadata.stock,
        price=metadata.price
    )
    newMenu.insert()
