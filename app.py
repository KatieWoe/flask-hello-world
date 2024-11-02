from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Kathryn Woessner in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://katie_3308_lab10_user:RV4E0w9kat01p8aZxkf80Yx5hbHGLzkX@dpg-csj511q3esus7380aaf0-a/katie_3308_lab10")
    conn.close()
    return "Database Connection Successful"
