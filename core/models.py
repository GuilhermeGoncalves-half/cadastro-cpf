from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

cpf_validator = RegexValidator(
    regex=r'^\d{11}$',
    message="CPF deve ter 11 números"
)

class User(AbstractUser):
    cpf = models.CharField(max_length=11,validators=[cpf_validator])
