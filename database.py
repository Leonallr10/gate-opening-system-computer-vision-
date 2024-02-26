import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://gate-opening-system-default-rtdb.firebaseio.com/"
})

ref = db.reference('People')

data = {
    "karthie":{
        "name":"karthie krishna",
        "roll":"21327",
        "total_entry": 0,
        "last_entry_time":"2024-02-10 13:54:34"
    },
    "robin":{
        "name":"leonal robin",
        "roll":"21331",
        "total_entry": 0,
        "last_entry_time":"2024-02-10 13:54:34"
    },
    "sai":{
        "name":"sai tharun adhitya",
        "roll":"21325",
        "total_entry": 0,
        "last_entry_time":"2024-02-10 13:54:34"
    }

}

for key,value in data.items():
    ref.child(key).set(value)