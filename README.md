# Python Chat

Una aplicación simple de chat creada con Python, usando Flask, Kafka y WebSockets para mensajería en tiempo real.

## Features

- Chat en tiempo real usando WebSockets. [In progress]
- Los mensajes se envían y reciben usando Apache Kafka como broker de mensajería
- Limpiar historial de chat con un click
- Gestión de caché de mensajes en LocalStorage

## Requisitos del Proyecto

- **Python**: Debes tener Python instalado en tu sistema. Puedes descargarlo desde [Python's official website](https://www.python.org/downloads/).
- **Flask**: Flask es un framework de Python para construir aplicaciones web. Puedes instalarlo utilizando `pip`: pip install Flask
- **Kafka**: Debes tener Apache Kafka instalado y configurado. Puedes descargarlo desde [Kafka's official website](https://kafka.apache.org/downloads) y seguir las instrucciones de instalación.
- **kafka-python**: Esta librería te permitirá interactuar con Apache Kafka desde Python. Puedes instalarla con `pip`: pip install kafka-python
- **WebSocket Library**: Necesitarás una biblioteca de WebSocket para habilitar la comunicación en tiempo real en tu aplicación. Puedes usar una librería como `Flask-SocketIO`.

## Como funciona la aplicación?

- Introduce tu mensaje en el campo de texto y pulsa "ENTER" o haz click en el botón "Enviar" para enviar un mensaje.
- Dicho mensaje enviado se visualizará en la parte superior, indicando un timestamp y tu mensaje enviado.
- Puedes hacer click en el botón de la papelera para borrar el historial de chat.


## Tecnologías utilizadas

- Python
- Flask
- Kafka
- WebSocket
- HTML/CSS
- JavaScript
