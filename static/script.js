function typeWriter(text, element, delay) {
  let index = 0;
  element.innerHTML = ''; 

  function type() {
      if (index < text.length) {
          element.innerHTML += text.charAt(index);
          index++;
          setTimeout(type, delay);
      }
  }
  type();
}

function displayMessage(message, sender) {
  const chatArea = document.getElementById('chatArea');
  const messageElement = document.createElement('div');
  messageElement.className = `message ${sender}-message`;
  
  if (sender === 'user') {
      messageElement.innerHTML = `<p>${message}</p>`;
      chatArea.appendChild(messageElement);
  } else {
      const paragraphElement = document.createElement('p');
      messageElement.appendChild(paragraphElement);
      chatArea.appendChild(messageElement);
      typeWriter(message, paragraphElement, 15);
  }

  chatArea.scrollTop = chatArea.scrollHeight;
}

document.getElementById('uploadButton').addEventListener('click', () => {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];

  if (file) {
      const formData = new FormData();
      formData.append('file', file);

      fetch('/upload', {
          method: 'POST',
          body: formData,
      })
      .then(response => response.json())
      .then(data => {
          if(data.explanation){
              displayMessage(data.explanation, 'bot');
          }
          else{
              displayMessage('Error: Could not analyze the report.', 'bot');
          }
      })
      .catch(error =>{
          console.error('Error:', error);
          displayMessage('Error occurred while uploading the file.', 'bot');
      });
  }
  else {
      alert('Please select a file to upload');
  }
});

document.getElementById('sendButton').addEventListener('click', () => {
  const messageInput = document.getElementById('messageInput');
  const message = messageInput.value.trim();

  if (message) {
    displayMessage(message, 'user');

    messageInput.value = '';

    let botResponse;

    if (message.toLowerCase().includes('hi') || message.toLowerCase().includes('hello') || message.toLowerCase().includes('hey')) {
        botResponse = "Hello! Welcome to the blood report analysis assistant. How can I help you today?";
    } else if (message.toLowerCase().includes('explain it') || message.toLowerCase().includes('explain') || message.toLowerCase().includes('give explaination')) {
        document.getElementById('uploadButton').click();
        return; // Exit the function as the upload will handle the response
    } else if (message.toLowerCase().includes('how does this work')) {
        botResponse = "I can analyze your blood report for you. Just upload a file or type 'explain it' to get started.";
    } else if (message.toLowerCase().includes('what can you do') || message.toLowerCase().includes('can you help me in my blood report')) {
        botResponse = "I can help you understand your blood test results. I can explain various parameters and provide general insights about your health based on the report.";
    } else if (message.toLowerCase().includes('upload')) {
        botResponse = "To upload your blood report, click on the 'Choose File' button, select your report file, and then click 'Upload'. I'll analyze it for you.";
    } else if (message.toLowerCase().includes('thank you') || message.toLowerCase().includes('thanks')) {
        botResponse = "You're welcome! Is there anything else I can help you with regarding your blood report?";
    } else if (message.toLowerCase().includes('bye') || message.toLowerCase().includes('goodbye')) {
        botResponse = "Goodbye! If you need any more help with blood report analysis in the future, don't hesitate to ask.";
    } else {
        botResponse = "I'm here to help with blood report analysis. Please type 'explain it' to get the blood report explanation, or upload a blood report file. If you're unsure, ask 'How does this work?'";
    }

    // Display bot response
    displayMessage(botResponse, 'bot');
  }
});

// New chat button event listener
document.getElementById('new-chat-btn').addEventListener('click', resetChat);

function resetChat() {
  const chatArea = document.getElementById('chatArea');
  chatArea.innerHTML = `
      <div class="message bot-message">
          <p>Hello, how can I assist you today?</p>
      </div>
      <div class="message bot-message">
          <p>Please upload your blood report.</p>
      </div>
  `;
}

// Initialize chat on page load
document.addEventListener('DOMContentLoaded', resetChat);