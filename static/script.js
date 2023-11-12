// script.js
document.getElementById('message-input').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
      e.preventDefault();
      sendMessage();
  }
});

const socket = io(); 

socket.on('receive_message', function(data) {
  addMessage(data.message, data.time);
});

//Funciones
function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const message = messageInput.value;
  messageInput.value = '';

  socket.emit('send_message', { message: message });
}

function addMessage(message, time) {
  const messagesDiv = document.getElementById('messages');
  const messageElement = document.createElement('div');
  messageElement.innerHTML = `<span class="message-time">${time}</span>: ${message}`;
  messagesDiv.appendChild(messageElement); 
}

function clearMessages() {
  const messagesDiv = document.getElementById('messages');
  messagesDiv.innerHTML = '';
}

