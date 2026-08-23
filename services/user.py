from django.db import transaction
from db.models import User


def get_user(user_id: int) -> User:
    return User.objects.get(pk=user_id)


@transaction.atomic
def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    user = User.objects.create_user(
        username=username,
        password=password,
        email=email or "",
        first_name=first_name or "",
        last_name=last_name or ""
    )
    return user


@transaction.atomic
def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    user = get_user(user_id)
    user.username = username if username is not None else (user.username or "")
    user.email = email if email is not None else (user.email or "")
    user.first_name = first_name if first_name is not None else (
        user.first_name or "")
    user.last_name = last_name if last_name is not None else (
        user.last_name or "")

    if password is not None:
        user.set_password(password)

    user.save()
    return user
