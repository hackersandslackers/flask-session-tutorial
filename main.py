"""App entry point."""
from flask_session_tutorial import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082, load_dotenv=True)
