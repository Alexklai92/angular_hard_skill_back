from .base_view import BaseView
from modules.databases.hard_skill import HardSkill
from errors.agent import ApiErrorNotYetSkill, ApiError, BackendError
from flask import jsonify, request, abort
from lib.util import login_required, RestToken
import json


# TODO: Сделать нормальный логин реквайред
#       Или переделать динамический роутинг
# TODO: заюзать logger, после того
#        как вебка будет работать
class SkillApi(BaseView):
    @property
    def initial_view(self):
        self._endpoint = "api"
        self._rule = "/api/v0/skills/"
        self.get_alloweds = []

        # TODO: вынести на уровень ниже
        self.table = "hardskill_table"

    @property
    def get_methods(self):
        return [
            self.get,
            self.post,
            self.patch,
            self.delete,
            self.get_token,
            self.get_by_id,
        ]

    def get(self) -> dict or list:
        hr = HardSkill()
        return jsonify(hr.get_all(self.table))

    def get_by_id(self, skill_id):
        hr = HardSkill()
        result = hr.get(skill_id)

        return jsonify(result)

    def post(self) -> dict:
        try:
            skill = self.get_skill
        except ApiErrorNotYetSkill as e:
            print(e)
            return jsonify({"errcode": 1, "data": "Not yet Skill"})
        except ApiError as e:
            print(e)
            return jsonify({"errcode": 1, "data": "Invalid Skill object"})

        hr = HardSkill()
        token = skill.get("token", "")
        print(token)
        try:
            result = hr.create(skill, token=token)
        except BackendError as e:
            print(e)
            abort(401)

        return jsonify(result)

    def patch(self) -> dict:
        try:
            skill = self.get_skill
        except ApiErrorNotYetSkill as e:
            print(e)
            return jsonify({"errcode": 1, "data": "Not yet Skill"})
        except ApiError as e:
            print(e)
            return jsonify({"errcode": 1, "data": "Invalid Skill object"})
        except json.decoder.JSONDecodeError as e:
            print(e)
            abort(403)

        hr = HardSkill()
        token = skill.get("token", "")
        try:
            result = hr.update(skill, token=token)
        except BackendError as e:
            print(e)
            abort(401)

        return jsonify(result)

    def delete(self, skill_id) -> bool:
        token = request.args.get("auth")

        hr = HardSkill()
        try:
            result = hr.delete(skill_id, token=token)
        except BackendError as e:
            print(e)
            abort(401)

        return jsonify(result)

    def get_token(self):
        user = request.data
        user = json.loads(user.decode())

        email = user["email"]
        password = user["password"]

        if not email or not password:
            abort(403)

        return jsonify({"token": RestToken.get(email, password)})

    @property
    def get_skill(self) -> dict or Exception:
        skill = request.data
        skill = json.loads(skill.decode())
        skill.update({"token": request.args.get("auth")})

        if not skill:
            raise ApiErrorNotYetSkill("Not yet Skill object")
        elif type(skill) != dict:
            raise ApiError("Invalid Skill object")
        return skill

