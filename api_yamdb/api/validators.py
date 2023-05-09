from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError

username_validator = UnicodeUsernameValidator()


def validate_user(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Введите другое имя пользователя.'
        )
    return value
