from django.core.exceptions import ValidationError


def validate_musician_name_start_from_capital(value):
    if value[0].isupper():
        return value
    else:
        raise ValidationError('Start from capital letter')
