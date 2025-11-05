from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='akashnagarajan001@gmail.com',
    MAIL_PASSWORD='kvdiisnuigpmssdc'
)

mail = Mail(app)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    msg = Message(
        subject=f"New message from {name}",
        sender=app.config['MAIL_USERNAME'],
        recipients=['akashnagarajan001@gmail.com'],
        body=f"From: {name} <{email}>\n\n{message}"
    )
    mail.send(msg)
    return jsonify({"message": "Message sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
