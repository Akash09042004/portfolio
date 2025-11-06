from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)

# -----------------------------
# CORS configuration
# -----------------------------
FRONTEND_URL = os.environ.get("portfolio-sigma-ecru-rijposmiqw.vercel.app/", "*")  # Set this on Render to your Netlify URL
CORS(app, origins=FRONTEND_URL)

# -----------------------------
# Mail configuration
# -----------------------------
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get('akashnagarajan001@gmail.com'),  # Gmail address (set as env variable)
    MAIL_PASSWORD=os.environ.get('kvdiisnuigpmssdc')   # Gmail App Password (set as env variable)
)

mail = Mail(app)

# -----------------------------
# Routes
# -----------------------------
@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        # Email content
        msg = Message(
            subject=f"New message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['akashnagarajan001@gmail.com'],  # Change/add recipients if needed
            body=f"From: {name} <{email}>\n\n{message}"
        )
        mail.send(msg)
        return jsonify({"message": "Message sent successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Run Flask app on Render
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
