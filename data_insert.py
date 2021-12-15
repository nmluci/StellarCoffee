import requests
from requests.api import head

baseHeader = {
    "SC-API-TOKEN": "KyaanDameNakaWaZettaiDameeDaaa",
    "Super-Secret-Key": "IyaaNakaWaZettaiDameDaaa",
    "Content-Type": "application/json"
}

inv = [
    {
        "menuId": 1,
        "namaMenu": "Espresso",
        "hargaMenu": 16000,
        "pathGambar": "/assets/img/menu/espresso.jpg"
    },
    {
        "menuId": 2,
        "namaMenu": "Americano",
        "hargaMenu": 24000,
        "pathGambar": "/assets/img/menu/americano.jpg"
    },
    {
        "menuId": 3,
        "namaMenu": "Cappucino",
        "hargaMenu": 25000,
        "pathGambar": "/assets/img/menu/cappucino.jpg"
    },
    {
        "menuId": 4,
        "namaMenu": "Vanilla Latte",
        "hargaMenu": 27000,
        "pathGambar": "/assets/img/menu/vanilla-latte.jpg"
    },
    {
        "menuId": 5,
        "namaMenu": "Cafe Latte",
        "hargaMenu": 25000,
        "pathGambar": "/assets/img/menu/cafe-latte.jpg"
    },
    {
        "menuId": 6,
        "namaMenu": "Lemon Tea",
        "hargaMenu": 17000,
        "pathGambar": "/assets/img/menu/lemon-tea.jpg"
    },
    {
        "menuId": 7,
        "namaMenu": "Lychee Tea",
        "hargaMenu": 20000,
        "pathGambar": "/assets/img/menu/lychee-tea.jpg"
    },
    {
        "menuId": 8,
        "namaMenu": "Taro Latte",
        "hargaMenu": 20000,
        "pathGambar": "/assets/img/menu/taro-latte.jpg"
    },
    {
        "menuId": 9,
        "namaMenu": "Matcha Latte",
        "hargaMenu": 25000,
        "pathGambar": "/assets/img/menu/matcha-latte.jpg"
    },
    {
        "menuId": 10,
        "namaMenu": "Chocolate Latte",
        "hargaMenu": 25000,
        "pathGambar": "/assets/img/menu/chocolate-latte.jpg"
    },
    {
        "menuId": 11,
        "namaMenu": "French Fries",
        "hargaMenu": 17000,
        "pathGambar": "/assets/img/menu/french-fries.jpg"
    },
    {
        "menuId": 12,
        "namaMenu": "Potato Wedges",
        "hargaMenu": 20000,
        "pathGambar": "/assets/img/menu/potato-wedges.jpg"
    },
    {
        "menuId": 13,
        "namaMenu": "Croissant",
        "hargaMenu": 25000,
        "pathGambar": "/assets/img/menu/croissant.jpg"
    },
    {
        "menuId": 14,
        "namaMenu": "Cheese Burger",
        "hargaMenu": 45000,
        "pathGambar": "/assets/img/menu/cheese-burger.jpg"
    },
    {
        "menuId": 15,
        "namaMenu": "Deluxe Burger",
        "hargaMenu": 50000,
        "pathGambar": "/assets/img/menu/deluxe-burger.jpg"
    }
]

data = [
    {
        "username": "fuwuna",
        "password": "fyn177013",
        "first_name": "Lynne",
        "last_name": "Fuyuna"
    },
    {
        "username": "pangpang",
        "password": "kompng132",
        "first_name": "Kompiang Gede",
        "last_name": "Sukadharma"
    },
        {
        "username": "ddiahhh",
        "password": "dhl4h",
        "first_name": "Diah",
        "last_name": "Pramesti"
    },
        {
        "username": "yauww",
        "password": "jyf100",
        "first_name": "James Yauw Fang",
        "last_name": "Dwiharta"
    },
        {
        "username": "audyyy",
        "password": "ady1822",
        "first_name": "Audy",
        "last_name": "Cipta"
    },
        {
        "username": "ngaknnnn",
        "password": "ngkn1241",
        "first_name": "Ngakan",
        "last_name": "Widyasprana"
    }
]
points = [600, 500, 231, 421, 800, 142]

events = [
    {
        "name": "Christmas Sale",
        "code": "XMAS20SL",
        "date_start": "2021-12-01",
        "date_end": "2021-12-27",
        "amount": 20000
    },
    {
        "name": "New Year Sale", 
        "code": "NY35SL",
        "date_start": "2021-12-27",
        "date_end": "2022-01-03",
        "amount": 35000
    },
    {
        "name": "StellarCoffee Anniversary Sale", 
        "code": "STELLARCOFFEE60",
        "date_start": "2021-12-17",
        "date_end": "2021-12-19",
        "amount": 60000
    },
]

print("Inserting Userdata")
for point, usr in zip(points, data):
    res = requests.post("http://127.0.0.1:5000/api/auth/register", headers=baseHeader, json=usr)
    
    if res.status_code == 200:
        print(usr["username"])
    else:
        print(res.json())
    res = requests.post(f"http://127.0.0.1:5000/api/user/{usr['username']}?add_point={point}", headers=baseHeader, json=usr)
    
    if res.status_code == 200:
        print(f"{usr['username']} point added: {point}")
    else:
        print(res.json())

print("Inserting Inventory Data")
for itm in inv:
    res = requests.post("http://127.0.0.1:5000/api/inventory", headers=baseHeader, json=itm)
    if res.status_code == 200:
        print(f"{itm['namaMenu']} added (id: {itm['menuId']})", res.status_code)
    else:
        print(res.json())

print("Inserting Events Data")
for itm in events:
    res = requests.post("http://127.0.0.1:5000/api/order/events", headers=baseHeader, json=itm)
    if res.status_code == 200:
        print(f"{itm['name']} added (code: {itm['code']})", res.status_code)
    else:
        print(res.json())
