from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import SQLALCHEMY_DATABASE_URI
import os

# Configuración inicial de la aplicación Flask y SocketIO
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Modelo de mensajes
class Message(db.Model):
    __tablename__ = 'message'
    __table_args__ = {'schema': 'chat'}
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.id}>'

socketio = SocketIO(app)

@app.route('/')
def index():
    last_messages = Message.query.order_by(Message.timestamp.desc()).limit(10).all()
    last_messages = last_messages[::-1]
    return render_template('chat.html', messages=last_messages)


@socketio.on('send_message')
def handle_send_message_event(data):
    message_text = data.get('message')
    if message_text:
        #Crear y almacenar el mensaje en la base de datos
        message = Message(message=message_text)
        db.session.add(message)
        db.session.commit()

        #Emitir el mensaje a todos los clientes conectados
        time_stamp = message.timestamp.strftime('%H:%M:%S')
        emit('receive_message', {'message': message_text, 'time': time_stamp}, broadcast=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
