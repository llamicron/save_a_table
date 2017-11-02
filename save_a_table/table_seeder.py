from peewee import *
from tables import Table


db = SqliteDatabase('save_a_table.db')


def before_request_handler():
    database.connect()


def after_request_handler():
    database.close()


db.connect()


Table.create_table(True)

table_data = {
    "floor3": [
        {"name": "Table 1", "status": "Occupied"},
        {"name": "Table 2", "status": "Vacant"},
        {"name": "Table 3", "status": "Occupied"},
        {"name": "Table 4", "status": "Vacant"},
        {"name": "Table 5", "status": "Occupied"},
    ],
    "floor4": [
        {"name": "Table 1", "status": "Vacant"},
        {"name": "Table 2", "status": "Vacant"},
        {"name": "Table 3", "status": "Occupied"},
        {"name": "Table 4", "status": "Occupied"},
        {"name": "Table 5", "status": "Vacant"},
    ],
    "floor5": [
        {"name": "Table 1", "status": "Occupied"},
        {"name": "Table 2", "status": "Vacant"},
        {"name": "Table 3", "status": "Vacant"},
        {"name": "Table 4", "status": "Occupied"},
        {"name": "Table 5", "status": "Occupied"},
    ],
    "floor6": [
        {"name": "Table 1", "status": "Vacant"},
        {"name": "Table 2", "status": "Occupied"},
        {"name": "Table 3", "status": "Occupied"},
        {"name": "Table 4", "status": "Vacant"},
        {"name": "Table 5", "status": "Occupied"},
    ]
}

for name, floor in table_data.items():
    for table in floor:
        new_table = Table(floor=name, name=table['name'], status=table['status'])
        new_table.save()
