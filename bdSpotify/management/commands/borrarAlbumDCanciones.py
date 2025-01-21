from django.core.management.base import BaseCommand
from bdSpotify.models import Cancion


class Command(BaseCommand):
    help = 'Borrar Campo Album de Canciones'

    def handle(self, *args, **kwargs):
        try:
            canciones = Cancion.objects.all()

            for c in canciones:
                c.album = 1
                c.save()
                self.stdout.write(self.style.ERROR(f'Campo album modificado..'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))