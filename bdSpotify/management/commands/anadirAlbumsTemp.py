from django.core.management.base import BaseCommand
from bdSpotify.models import Cancion, Album, Album_Temp


class Command(BaseCommand):
    help = 'Albumes_Temp'

    def handle(self, *args, **kwargs):
        try:
            canciones = Cancion.objects.all()

            for c in canciones:
                try:
                    album = Album.objects.get(nombre=c.album)
                    Album_Temp.objects.create(
                        id_album=album.id,
                        id_cancion=c.id
                    )
                    self.stdout.write(f'Cancion: {str(c.titulo)}, {str(c.id)} -- Album: {str(album.nombre)}, {str(album.id)}')
                    self.stdout.write(self.style.SUCCESS(f'Album_Temp se ha guardado con éxito'))

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error al encontrar el album: {e}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))