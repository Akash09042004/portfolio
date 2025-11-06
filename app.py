# refreshed
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)

FRONTEND_URL = "https://portfolio-sigma-ecru-rijposmiqw.vercel.app"
CORS(app, origins=[FRONTEND_URL])

# ----------------------------
# Flask-Mail Config
# ----------------------------
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='akashnagarajan001@gmail.com',
    MAIL_PASSWORD='kvdiisnuigpmssdc'  # your app password
)

mail = Mail(app)

@app.route('/contact', methods=['POST', 'OPTIONS'])
def contact():
    if request.method == 'OPTIONS':
        # Handle CORS preflight
        return jsonify({'message': 'Preflight OK'}), 200

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'All fields required'}), 400

    msg = Message(
        subject=f"Portfolio Message from {name}",
        sender='akashnagarajan001@gmail.com',
        recipients=['akashnagarajan001@gmail.com'],
        body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )

    try:
        mail.send(msg)
        return jsonify({'message': 'Message sent successfully!'}), 200
    except Exception as e:
        print("Mail error:", e)
        return jsonify({'error': 'Failed to send message'}), 500

if __name__ == '__main__':
    app.run(debug=True)

