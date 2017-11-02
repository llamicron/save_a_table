watch:
	sass --watch save_a_table/static/materialize-src/:save_a_table/static/css/

build:
	sass save_a_table/static/materialize-src/:save_a_table/static/css/

run:
	export FLASK_DEBUG=1
	python save_a_table/save_a_table.py

destroy_db:
	rm -rf save_a_table.db

seed:
	python save_a_table/table_seeder.py
