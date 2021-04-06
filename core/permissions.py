from django.http import Http404

from core.models import Role


def user_is(user, role):
    return user.role == role


def check_user_role(user, roles):
    return user.is_authenticated and any(map(lambda role: user_is(user, role), roles))


def user_role_decorator(roles):
    def deco(fn):
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if check_user_role(user, roles):
                return fn(request, *args, **kwargs)
            else:
                raise Http404("Invalid role")
        return _wrapped
    return deco


is_student = user_role_decorator([Role.STUDENT.value])
is_teacher = user_role_decorator([Role.TEACHER.value])
