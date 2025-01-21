from django.core.management.base import BaseCommand
from bdSpotify.models import Album


class Command(BaseCommand):
    help = 'Borrar Albumes'

    def handle(self, *args, **kwargs):
        try:
            Album.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Albumes borrados con éxito.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
