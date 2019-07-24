from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MinLengthValidator

class Role(Group):
    description = models.TextField(max_length=500)

    @staticmethod
    def get_roles():
        try:
            queryset = Role.objects.all()
            return queryset
        except Role.DoesNotExist:
            return None

class User(AbstractUser):
    id_card = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(8, 'Mínimo 8 dígitos')])
    address = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True, related_name='usuario')
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
    	return self.get_full_name()
