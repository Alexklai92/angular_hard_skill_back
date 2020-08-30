from modules.databases.hard_skill import HardSkill
from flask import Flask
from config import PORT, HOST, DEBUG
from modules.views.skill import SkillApi

app = Flask(__name__)
api = SkillApi()


for method in api.get_methods:
    if method.__name__ == 'get_token':
        # TODO: убрать костыль
        app.add_url_rule(
            (api.get_rule + method.__name__),
            ("skill_" + method.__name__),
            method,
            methods=["GET"],
        )
        continue

    app.add_url_rule(
        (api.get_rule + method.__name__),
        ("skill_" + method.__name__),
        method,
        methods=[method.__name__],
    )


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
