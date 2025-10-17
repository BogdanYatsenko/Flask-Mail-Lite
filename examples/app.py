from flask import Flask
from flask_mail import Mail, Message

def create_app():
    app = Flask(__name__)
    app.config.update(
        MAIL_SERVER="smtp.example.com",
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME="user",
        MAIL_PASSWORD="pass",
        MAIL_DEFAULT_SENDER=("No-Reply", "no-reply@example.com"),
    )
    mail = Mail(app)

    @app.route("/ping")
    def ping():
        return "ok"

    @app.route("/send-test")
    def send_test():
        msg = Message("Test Email", recipients=["test@example.com"], body="Hello from velza-mail.")
        mail.send(msg)
        return "sent"
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
