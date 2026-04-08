document.addEventListener("DOMContentLoaded", () => {
  const chatForm = document.getElementById("chat-form");
  const userInput = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const themeToggle = document.getElementById("theme-toggle");
  const clearChatBtn = document.getElementById("clear-chat");

  // Show welcome message
  addMessage("👋 Welcome! Ask me anything about the college.", "bot");

  // Theme toggle
  themeToggle.addEventListener("click", () => {
    document.body.classList.toggle("dark");
  });

  // Clear chat
  clearChatBtn.addEventListener("click", () => {
    chatBox.innerHTML = "";
    addMessage("👋 Welcome! Ask me anything about the college.", "bot");
  });

  // Form submission
  chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user");
    userInput.value = "";

    showTyping();

    try {
      const response = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
      });

      const data = await response.json();

      hideTyping();

      addMessage(data.response, "bot");

    } catch (error) {
      hideTyping();
      addMessage("⚠️ Error: Could not get a response from the server.", "bot");
    }
  });

  function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message", `${sender}-message`);
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  function showTyping() {
    const typing = document.createElement("div");
    typing.classList.add("message", "bot-message", "typing-indicator");
    typing.id = "typing";
    typing.innerHTML =
      `<span class="dot"></span><span class="dot"></span><span class="dot"></span>`;
    chatBox.appendChild(typing);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  function hideTyping() {
    const typing = document.getElementById("typing");
    if (typing) typing.remove();
  }
});