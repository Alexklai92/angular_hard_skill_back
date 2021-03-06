import time

from errors.agent import BackendError
from lib.util import validation

from .base import BackendMixin


class HardSkill(BackendMixin):
    @property
    def default_fields(self):
        return [
            "id",
            "title",
            "author",
            "created",
            "updated",
            "finished",
            "description",
            "link_approve_first",
            "link_approve_second",
            "type",
        ]

    @validation
    def create(self, skill: dict, **kwargs) -> dict:
        con = self._con
        cursor = con.cursor()
        try:
            cursor.execute(
                """insert into hardskill_table (title, author, created, type) VALUES (
                    %(title)s, %(author)s, %(created)s, %(type)s
                ) returning *; """,
                dict(
                    title=skill.get("title"),
                    author=skill.get("author"),
                    created=time.time(),
                    type=skill.get("type", "programming")
                ),
            )
        except Exception as e:
            print(e)
            self._con.close()
            return False

        result = cursor.fetchone()
        con.commit()
        con.close()
        return self.to_dict(result, True)

    @validation
    def update(self, skill: dict, **kwargs) -> dict:
        con = self._con
        cursor = con.cursor()

        try:
            cursor.execute(
                """update hardskill_table set
                    title=%(title)s, author=%(author)s,
                    created=%(created)s, updated=%(updated)s,
                    finished=%(finished)s, description=%(description)s,
                    link_approve_first=%(link_approve_first)s,
                    link_approve_second=%(link_approve_second)s,
                    type=%(type)s
                   where id=%(id)s returning *;
                """,
                dict(**skill),
            )
        except Exception as e:
            print(e)
            con.close()
            return False

        result = cursor.fetchone()
        con.commit()
        con.close()
        return self.to_dict(result, True)

    @validation
    def delete(self, skill_id: int, **kwargs) -> bool:
        if not skill_id:
            raise BackendError("Invalid Skill Object")

        con = self._con
        cursor = con.cursor()
        try:
            cursor.execute(
                "delete from hardskill_table where id=%(skill_id)s",
                dict(skill_id=skill_id),
            )
        except Exception as e:
            print(e)
            self._con.close()
            return False

        con.commit()
        con.close()
        return True

    def get(self, skill_id: int) -> dict:
        if not skill_id:
            raise BackendError("Invalid Skill Object")

        cursor = self._cursor
        try:
            cursor.execute(
                "select * from hardskill_table where id=%(skill_id)s",
                dict(skill_id=skill_id),
            )
        except Exception as e:
            print(e)
            self._con.close()
            return
        result = cursor.fetchone()
        self._con.commit()
        self._con.close()
        return self.to_dict(result, True) if result else None
