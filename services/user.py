from django.db import transaction
from db.models import User
from django.contrib.auth import get_user_model


def get_user(user_id: int) -> User:
    user_model = get_user_model()
    return user_model.objects.get(pk=user_id)


@transaction.atomic
def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> User:
    user = User.objects.create_user(username=username,
                                    password=password,
                                    email=email,
                                    first_name=first_name,
                                    last_name=last_name
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
    user.username = username if username is not None else user.username
    user.email = email if email is not None else user.email
    user.first_name = first_name if first_name is not None else user.first_name
    user.last_name = last_name if last_name is not None else user.last_name
    user.save()
    return user
