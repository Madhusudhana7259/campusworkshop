"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqd1pmbg5e4khs0lk0-a.oregon-postgres.render.com",
        database="todo_dx7w",
        user="root",
        password="jZL2kvj4oo4bUT3AMTgvSE1gUUaJ4CV7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
