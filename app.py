import sqliteDbComm
from flask import Flask
from flask_socketio import SocketIO, send

DATABASE = '/db/database.sqlite'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketio = SocketIO(app)

data = sqliteDbComm.SqLt('db/database.sqlite')
data.create_table('test', [
    ('id', 'NUMBER'),
    ('description', 'TEXT')
])
data.append('test', [
    ('id', '0'),
    ('description', 'Test 00')
])

#data.drop_table('test')


@app.teardown_appcontext
def close_connection(exception):
    data.close()


@app.route('/')
def root():
    return app.send_static_file("index.html")


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
