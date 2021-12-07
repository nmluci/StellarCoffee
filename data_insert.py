import requests
from requests.api import head

baseHeader = {
    "SC-API-TOKEN": "KyaanDameNakaWaZettaiDameeDaaa",
    "Super-Secret-Key": "IyaaNakaWaZettaiDameDaaa",
    "Content-Type": "application/json"
}

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

for usr in data:
    res = requests.post("http://127.0.0.1:6969/api/auth/register", headers=baseHeader, json=usr)
    print(usr["username"], res.status_code)