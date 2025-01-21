from django.core.management.base import BaseCommand
from bdSpotify.models import Cancion, Album

class Command(BaseCommand):
    help = 'Albumes'

    def handle(self, *args, **kwargs):
        try:
            canciones = Cancion.objects.all()
            for c in canciones:
                try:
                    Album.objects.get(nombre=c.album)
                    self.stdout.write(self.style.ERROR(f'El album {c.album} ya está registrado'))
                except Exception as e:
                    Album.objects.create(nombre=c.album)
                    self.stdout.write(self.style.SUCCESS(f'El album {c.album} se ha guardado con éxito'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))