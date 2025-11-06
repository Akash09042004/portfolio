import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

# ✅ Allow only your Vercel frontend domain
FRONTEND_URL = "https://portfolio-tan-seven-ttnkdyv8m6.vercel.app"
CORS(app, resources={r"/*": {"origins": [FRONTEND_URL]}})

@app.route('/')
def home():
    return jsonify({"message": "Backend running!"})

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        # ✅ Use the SendGrid API key stored in Render environment
        sg = SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

        email_msg = Mail(
            from_email='akashnagarajan001@gmail.com',
            to_emails='akashnagarajan001@gmail.com',
            subject=f'New Portfolio Message from {name}',
            plain_text_content=f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )

        sg.send(email_msg)
        return jsonify({"message": "Message sent successfully!"}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
