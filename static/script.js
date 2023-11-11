// script.js
document.getElementById('message-input').addEventListener('keypress', function (e) {
  if (e.key === 'Enter') {
      e.preventDefault();
      sendMessage();
  }
});

function clearMessages() {
  const messagesDiv = document.getElementById('messages');
  messagesDiv.innerHTML = ''; // Limpiar chat
  localStorage.removeItem('viewedMessages'); // Limpiar LocalStorage
}

function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const message = messageInput.value;
  messageInput.value = ''; // Limpiar input

  fetch('/send', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: message }),
  });
}

const eventSource = new EventSource('/events');
eventSource.onmessage = function (event) {
  const messagesDiv = document.getElementById('messages');
  let viewedMessages = JSON.parse(localStorage.getItem('viewedMessages')) || [];
  const msg = event.data;

  if (!viewedMessages.some(obj => obj.message === msg)) {
      const messageElement = document.createElement('div');
      const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      messageElement.innerHTML = `<span class="message-time">${currentTime}</span>: ${msg}`;
      messagesDiv.appendChild(messageElement);
      viewedMessages.push({ message: msg, time: currentTime });

      // Convertir los objetos a cadenas JSON antes de almacenarlos
      viewedMessages = JSON.stringify(viewedMessages);
      localStorage.setItem('viewedMessages', viewedMessages);

      // Volver a convertir las cadenas JSON a objetos antes de mostrarlos
      viewedMessages = JSON.parse(viewedMessages);
  }
};

window.addEventListener('load', () => {
  const viewedMessages = JSON.parse(localStorage.getItem('viewedMessages')) || [];
  const messagesDiv = document.getElementById('messages');

  viewedMessages.forEach(obj => {
      const messageElement = document.createElement('div');
      messageElement.innerHTML = `<span class="message-time">${obj.time}</span>: ${obj.message}`;
      messagesDiv.appendChild(messageElement);
  });
});
