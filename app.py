import os
from email_relay import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("FLASK_PORT")),
        debug=True
        )