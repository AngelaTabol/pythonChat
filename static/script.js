// script.js
document.getElementById('message-input').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
      e.preventDefault();
      sendMessage();
  }
});

const socket = io(); 

// Modifica la función socket.on para incluir los datos adicionales
socket.on('receive_message', function(data) {
  addMessage(data.message, data.time, data.nickname, data.color);
});

//Funciones
function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const message = messageInput.value;
  messageInput.value = '';

  socket.emit('send_message', { message: message });
}

function addMessage(message, time, nickname, color) {
  const messagesDiv = document.getElementById('messages');
  const messageElement = document.createElement('div');
  messageElement.innerHTML = `<span class="message-time">${time}</span> <span style="color: ${color}">${nickname}</span>: ${message}`;
  messagesDiv.appendChild(messageElement); 
}



function clearMessages() {
  const messagesDiv = document.getElementById('messages');
  messagesDiv.innerHTML = '';
}

