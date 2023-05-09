import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    """Валидатор для года произведения."""
    if value > dt.date.today().year:
        raise ValidationError(
            f'Год еще не наступил, сейчас {dt.date.today().year}')
    return value
