from modules.databases.hard_skill import HardSkill
from flask import Flask
from config import PORT, HOST, DEBUG

app = Flask(__name__)


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)