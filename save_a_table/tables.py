from peewee import *

db = SqliteDatabase('save_a_table/db/save_a_table.db')

class Table(Model):
    floor = CharField()
    name = CharField()
    # I could use a more efficient data type, but this is a small project
    # and i don't care. The improvement is negligible anyway.
    status = CharField()

    @staticmethod
    def seed():
        db = SqliteDatabase('save_a_table/db/save_a_table.db')

        Table.create_table(True)

        db.connect()

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

        db.close()


    class Meta:
        database = db

if __name__ == '__main__':
    Table.create_table(True)
    Table.seed()
