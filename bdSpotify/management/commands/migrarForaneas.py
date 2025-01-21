'''
recorrer los objetos album_temp comparando con los ids de los objetos canciones y añadiendo la foranea de album al objeto cancion
'''

from django.core.management.base import BaseCommand
from bdSpotify.models import Cancion, Album, Album_Temp

class Command(BaseCommand):
    help = 'Migrar foraneas'

    def handle(self, *args, **kwargs):
        try:
            albumes_temp = Album_Temp.objects.all()

            for at in albumes_temp:
                try:
                    a = Album.objects.get(id=at.id_album)
                    c = Cancion.objects.get(id=at.id_cancion)
                    c.album = a
                    c.save()
                    self.stdout.write(self.style.SUCCESS(f'Foranea de album añadida a la cancion {c.titulo}'))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error al encontrar la cancion: {e}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))