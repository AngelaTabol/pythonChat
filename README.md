# Python Chat

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/en/3.0.x/)

Una aplicación simple de chat creada con Python, usando Flask, WebSockets y PostgreSQL para tener mensajería en tiempo real y persistencia.

## Tecnologías utilizadas

- Python
- Flask
- WebSocket
- HTML/CSS
- JavaScript

## Features

- Chat en tiempo real usando WebSockets. [In progress]
- Los mensajes se persisten en una base de datos de PostgreSQL
- Limpiar historial de chat con un click
- Gestión de usuarios y autenticación
- Customización de usuario (Nickname, color de chat)

## Requisitos

- **Python**: Debes tener Python instalado en tu sistema. Puedes descargarlo [aquí](https://www.python.org/downloads/).
- **Flask**: Flask es un microframework de Python para construir aplicaciones web. Puedes instalarlo utilizando `pip`: 
```bash pip install Flask```
- **Flask-SocketIO**: Proporciona capacidades de Socket.IO para aplicaciones Flask, usada para la comunicación en tiempo real.** ```bash pip install Flask```
- **Flask-SQLAlchemy**: Un ORM para Python, usado para interactuar con bases de datos.
```bash pip install Flask-SQLAlchemy```
- **Werkzeug**: Una biblioteca WSGI para aplicaciones web en Python. Se utiliza para funciones de seguridad como la generación y verificación de hashes de contraseñas.
```bash pip install Werkzeug```
- **Flask-Login**: Proporciona gestión de sesiones de usuario para Flask, utilizada para manejar la autenticación de usuarios.
```bash pip install Flask-Login```

## Como funciona la aplicación?

- Introduce tu mensaje en el campo de texto y pulsa "ENTER" o haz click en el botón "Enviar" para enviar un mensaje.
- Dicho mensaje enviado se visualizará en la parte superior, indicando un timestamp y tu mensaje enviado.
- Puedes hacer click en el botón de la papelera para borrar el historial de chat.


