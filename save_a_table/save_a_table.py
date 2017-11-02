from flask import Flask, render_template, jsonify
from peewee import *
from tables import Table


db = SqliteDatabase('save_a_table.db')

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


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tableData', methods=["GET"])
def serveTableData():
    table_data = {
        "floor3": [],
        "floor4": [],
        "floor5": [],
        "floor6": []
    }
    for table in Table.select():
        table_data[table.floor].append({"name": table.name, "status": table.status})
    return jsonify(table_data)

db.close()


if __name__ == '__main__':
    app.run()
