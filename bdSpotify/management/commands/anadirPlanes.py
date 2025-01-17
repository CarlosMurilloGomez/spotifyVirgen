
from django.core.management.base import BaseCommand
from bdSpotify.models import Plan
class Command(BaseCommand):
    help = 'Planes'

    def handle(self, *args, **kwargs):
        if not Plan.objects.exists():
            Plan.objects.create(nombre='Normal',precio=12.99)
            Plan.objects.create(nombre='Estudiante', precio=9.99)
            Plan.objects.create(nombre='Jubilado', precio=11.00)
            self.stdout.write(self.style.SUCCESS('Se han añadidio los planes correctamente'))
        else:
            self.stderr.write(self.style.ERROR('Los planes ya están añadidos'))

