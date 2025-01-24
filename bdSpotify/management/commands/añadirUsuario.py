from django.core.management.base import BaseCommand
from faker.generator import random

from bdSpotify.models import Usuario, Plan
from faker import Faker

class Command(BaseCommand):
    help = 'Añadir usuario'

    def handle(self, *args, **kwargs):
        faker=Faker()
        try:
            usuario = Usuario(email=faker.email(), fecha_nacimiento=faker.date_of_birth(minimum_age=10, maximum_age=17), plan=random.choice(list(Plan.objects.all())))
            usuario.save()
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))