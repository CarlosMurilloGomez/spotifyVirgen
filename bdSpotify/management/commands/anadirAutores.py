
from django.core.management.base import BaseCommand
from bdSpotify.models import Usuario,Plan
import random
from faker import Faker
class Command(BaseCommand):
    help = 'Usuarios'

    def handle(self, *args, **kwargs):
        faker = Faker()

        if (not Usuario.objects.exists()) and Plan.objects.exists:
            planes = Plan.objects.all()
            for i in range(1,20):
                Usuario.objects.create(email=faker.email(),fecha_nacimiento=faker.date_of_birth(minimum_age=18, maximum_age=70), plan = random.choice(list(planes)))
            self.stdout.write(self.style.SUCCESS('Se han añadidio los usuarios correctamente'))
        else:
            self.stderr.write(self.style.ERROR('Algo falla'))