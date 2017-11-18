from flask import Flask, render_template, jsonify, request
from peewee import *
from tables import Table

db = SqliteDatabase('save_a_table/db/save_a_table.db')


def before_request_handler():
    database.connect()


def after_request_handler():
    database.close()


Table.create_table(True)

db.connect()


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='<%',
        comment_end_string='%>',
    ))


app = CustomFlask(__name__)

table_data = {
    "floor3": [],
    "floor4": [],
    "floor5": [],
    "floor6": []
}
for table in Table.select():
    table_data[table.floor].append(
        {"name": table.name, "status": table.status})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tableData', methods=["GET"])
def serve_table_data():
    table_data = {
        "floor3": [],
        "floor4": [],
        "floor5": [],
        "floor6": []
    }
    for table in Table.select():
        table_data[table.floor].append(
            {"name": table.name, "status": table.status})
    return jsonify(table_data)


db.close()


@app.route('/update-table', methods=["POST"])
def update_table():
    table = request.get_json()['table']

    # I done messed up. The state is reversed. Sorry.
    if int(table['state']) == 1:
        # Turn it on
        new_status = "Occupied"
    else:
        # turn it off
        new_status = "Vacant"


    table_row = Table.get(Table.name == str("Table " + str(table['number'])) and Table.floor == str("floor" + str(table['floor'])))
    table_row.status = new_status
    table_row.save()
    return "True"

if __name__ == '__main__':
    app.run("0.0.0.0")
