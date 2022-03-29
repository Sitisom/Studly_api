from enum import Enum


class Role(Enum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"

    @classmethod
    def as_choices(cls):
        return (
            (cls.STUDENT.value, "Студент"),
            (cls.TEACHER.value, "Учитель")
        )