from enum import Enum


class Role(Enum):
    STUDENT = "STUDENT_ROLE"
    TEACHER = "TEACHER_ROLE"

    @classmethod
    def as_choices(cls):
        return (
            (cls.STUDENT.value, "Студент"),
            (cls.TEACHER.value, "Учитель")
        )