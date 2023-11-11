# Python Chat

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/en/3.0.x/)
[![Kafka](https://img.shields.io/badge/Kafka-3.6.0-red.svg)](https://kafka.apache.org/)

Una aplicación simple de chat creada con Python, usando Flask, Kafka y WebSockets para mensajería en tiempo real.

## Tecnologías utilizadas

- Python 
- Flask
- Kafka
- WebSocket
- HTML/CSS
- JavaScript

## Features

- Chat en tiempo real usando WebSockets. [In progress]
- Los mensajes se envían y reciben usando Apache Kafka como broker de mensajería
- Gestión de caché de mensajes en LocalStorage
- Limpiar historial de chat con un click


## Requisitos

- **Kafka**: Debes tener Apache Kafka instalado y configurado correctamente. Puedes descargarlo [aquí](https://kafka.apache.org/downloads) y seguir las instrucciones de instalación.
- **Python**: Debes tener Python instalado en tu sistema. Puedes descargarlo [aquí](https://www.python.org/downloads/).
- **Flask**: Flask es un framework de Python para construir aplicaciones web. Puedes instalarlo utilizando `pip`: ```pip install Flask```
- **kafka-python**: Esta librería te permitirá interactuar con Apache Kafka desde Python. Puedes instalarla con `pip`: ```pip install kafka-python```


## Como funciona la aplicación?

- Introduce tu mensaje en el campo de texto y pulsa "ENTER" o haz click en el botón "Enviar" para enviar un mensaje.
- Dicho mensaje enviado se visualizará en la parte superior, indicando un timestamp y tu mensaje enviado.
- Puedes hacer click en el botón de la papelera para borrar el historial de chat.


