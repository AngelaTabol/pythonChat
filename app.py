from flask import Flask, flash, render_template, request, jsonify, redirect, url_for
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from config import SQLALCHEMY_DATABASE_URI
from config import IP
from config import PORT
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['IP'] = IP
app.config['PORT'] = PORT

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Modelo de Usuario
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'chat'}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(7))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#Modelo de Mensajes
class Message(db.Model):
    __tablename__ = 'messages'
    __table_args__ = {'schema': 'chat'}
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('chat.users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return f'<Message {self.id}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Autenticación
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas. Por favor, inténtalo de nuevo.')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        nickname = request.form.get('nickname')
        color = request.form.get('color')

        #Por hacer: Validación de los datos

        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            new_user = User(
                username=username,
                nickname=nickname,
                color=color
            )
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('index'))

        flash('El nombre de usuario ya existe. Elige otro.')

    return render_template('register.html')


socketio = SocketIO(app)

@app.route('/update_color', methods=['POST'])
@login_required
def update_color():
    data = request.json
    current_user.color = data['color']
    db.session.commit()
    return jsonify({'status': 'success', 'message': 'Color actualizado'})

@app.route('/')
@login_required
def index():
    last_messages = Message.query.order_by(Message.timestamp.desc()).limit(20).all()
    last_messages = last_messages[::-1]

    messages_with_user_info = [{
        'text': message.message,
        'timestamp': message.timestamp,
        'nickname': message.user.nickname,
        'color': message.user.color
    } for message in last_messages]

    return render_template('chat.html', messages=messages_with_user_info)


@socketio.on('send_message')
@login_required
def handle_send_message_event(data):
    message_text = data.get('message')
    if message_text:
        message = Message(message=message_text, user_id=current_user.id)
        db.session.add(message)
        db.session.commit()

        emit('receive_message', {
            'message': message_text,
            'time': message.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
            'username': current_user.nickname,
            'color': current_user.color
        }, broadcast=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, host=IP, port=PORT, debug=True)
