# 📞 Twilio Incoming Call Handler

**Description:**  
This project demonstrates how to use **Twilio's Voice API** to receive and handle incoming calls programmatically. The project uses **Flask** as the web framework to manage incoming call webhooks, allowing custom responses (like playing messages or forwarding the call) when someone calls your **Twilio virtual number**.

---

## 🌟 Features:
- **Receive Incoming Calls:** Handle incoming calls to your Twilio virtual number and respond with a custom message.
- **Call Forwarding:** Forward incoming calls to another number (optional).
- **Status Callback:** Track the status of the incoming call in real-time, such as completed or in-progress.
- **Environment Variable Management:** Securely manage Twilio credentials via `.env` file.

---

## 🚀 Quick Start

### Prerequisites:
- [Twilio Account](https://www.twilio.com/)
- Python 3.x
- Flask framework
- Twilio Python SDK (`twilio` package)
- `dotenv` for environment variables

### 1. Clone the Repository
```bash
git clone https://github.com/MeghanaKiran77/Twilio_call_functionality.git
cd Twilio_call_functionality
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory and add your Twilio credentials:
```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

### 4. Run the Flask Server
```bash
python app.py
```

### 5. Expose Localhost to the Internet using Ngrok
Since you are handling incoming calls, you need to expose your local server to the internet using Ngrok:
```bash
ngrok http 5000
```
Copy the generated Ngrok URL and add it to your Twilio console under the **Voice & Fax** settings for your Twilio phone number as a webhook URL (e.g., `https://your-ngrok-url/incoming-call`).

---

## 💻 Main Functionality

### `app.py`
- **Incoming Call Handling:** When someone calls your Twilio number, the app responds with a voice message and can optionally forward the call to a second number.
- **Status Callback:** Logs call status updates (such as completed, ringing, or failed) to the console.

---

## 📞 How It Works

1. **Incoming Call Flow:**
   - When someone calls your Twilio virtual number, Twilio sends a webhook request to your Flask server.
   - The server responds with a custom message (e.g., "Good Afternoon Authorities, We are Team Drona") or forwards the call to another number.

2. **Status Callback:**
   - The call status is tracked using the `/status-callback` route. This logs the call status (e.g., completed or in-progress) to the console.

---

## 🔐 Security

- **Environment Variables**: Your Twilio credentials are stored securely in a `.env` file. Be sure to add the `.env` file to `.gitignore` so that sensitive information is not pushed to version control.

---

## 🛠 Troubleshooting

### Common Issues:
1. **Ngrok URL Change:** Make sure to update the Ngrok URL in your Twilio console every time you restart Ngrok.
2. **Environment Variables Not Loading:** Check your `.env` file formatting and ensure that `python-dotenv` is properly installed.

---

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
