// script.js
document.getElementById('message-input').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
      e.preventDefault();
      sendMessage();
  }
});

document.addEventListener('DOMContentLoaded', (event) => {
  convertAllTimestampsToLocal();
});

const socket = io(); 

socket.on('receive_message', function(data) {
  addMessage(data.message, data.time, data.username, data.color);
});

//Funciones
function convertToLocalTime(utcString) {
  const utcDate = new Date(utcString);
  console.log(utcDate.toLocaleTimeString());
  return utcDate.toLocaleTimeString();
}

function convertAllTimestampsToLocal() {
  const messageTimes = document.querySelectorAll('.message-time');
  messageTimes.forEach(span => {
      const utcString = span.getAttribute('data-utc-time');
      span.textContent = '[' + convertToLocalTime(utcString) + ']';
  });
}


function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const message = messageInput.value;
  messageInput.value = '';

  if (message.trim() !== '') {
      socket.emit('send_message', { message: message });
  }
}

function loadInitialMessages() {
  initialMessages.forEach(message => {
      addMessage(message.text, message.timestamp, message.nickname, message.color);
  });
}

function addMessage(message, time, nickname, color) {
  const localTime = convertToLocalTime(time);
  const messagesDiv = document.getElementById('messages');
  const messageElement = document.createElement('div');
  messageElement.innerHTML = `<span class="message-time">[${localTime}]</span> <span style="color: ${color}"><b>${nickname}</b></span>: ${message}`;
  messagesDiv.appendChild(messageElement); 

  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function clearMessages() {
  const messagesDiv = document.getElementById('messages');
  messagesDiv.innerHTML = '';
}

function updateColor(color) {
  fetch('/update_color', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ color: color }),
  })
  .then(response => response.json())
  .then(data => {
      console.log('Color actualizado:', data);
  });
}

