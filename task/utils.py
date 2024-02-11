from django.core.exceptions import ValidationError

def validate_min_length(value, min_length):

    if len(value) < min_length:
        raise ValidationError(f"El campo debe tener al menos {min_length} caracteres.")
