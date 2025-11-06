from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)

# -----------------------------
# CORS configuration
# -----------------------------
# Replace this with your frontend URL (Vercel)
FRONTEND_URL = "https://portfolio-sigma-ecru-rijposmiqw.vercel.app"
CORS(app, origins=[FRONTEND_URL])

# -----------------------------
# Mail configuration
# -----------------------------
# Gmail settings (use your email and App Password)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='akashnagarajan001@gmail.com',   # <-- Your Gmail
    MAIL_PASSWORD='kvdiisnuigpmssdc'              # <-- Your Gmail App Password
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
            sender=app.config['MAIL_USERNAME'],        # Use your email as sender
            recipients=[app.config['MAIL_USERNAME']],  # Receive email at your address
            body=f"From: {name} <{email}>\n\n{message}"
        )
        mail.send(msg)
        return jsonify({"message": "Message sent successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Run Flask app
# -----------------------------
if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)
