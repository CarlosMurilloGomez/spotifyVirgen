from datetime import datetime

from django.core.management.base import BaseCommand
from faker.generator import random

from bdSpotify.models import Usuario, Plan, Lista, ListaCancion, Cancion
from faker import Faker

class Command(BaseCommand):
    help = 'Añadir usuario'

    def handle(self, *args, **kwargs):
        try:
            if not Lista.objects.exists():
                lista = Lista(nombre="ListaDeViajes", usuario=random.choice(list(Usuario.objects.all())), fecha_creacion=datetime.today())
                lista.save()
                self.stdout.write(self.style.SUCCESS(f'Lista ({lista.nombre}) añadida'))

            cancion = ListaCancion(lista=Lista.objects.get(nombre="ListaDeViajes"), cancion=Cancion.objects.get(pk=299))
            cancion.save()
            self.stdout.write(self.style.SUCCESS(f'Cancion ({cancion.cancion.titulo}) insertada en la lista: {lista.nombre}'))
            
            cancion2 = ListaCancion(lista=Lista.objects.get(nombre="ListaDeViajes"), cancion=Cancion.objects.get(pk=299))
            cancion2.save()
            self.stdout.write(self.style.SUCCESS(f'Cancion ({cancion.cancion.titulo}) insertada en la lista: {lista.nombre}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))