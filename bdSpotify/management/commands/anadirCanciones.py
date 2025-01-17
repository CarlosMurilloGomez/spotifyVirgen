
from django.core.management.base import BaseCommand
from bdSpotify.models import Usuario,Plan, Cancion
import random
from faker import Faker
class Command(BaseCommand):
    help = 'Canciones'

    def handle(self, *args, **kwargs):
        faker = Faker()
        artistas = [
    "María Fernández",
    "Carlos López",
    "Lucía González",
    "Sergio Martínez",
    "Ana Sánchez",
    "Diego Gutiérrez",
    "Carmen Ruiz",
    "Jorge Herrera",
    "Isabel Torres",
    "Miguel Castro",
    "Raquel Morales",
    "Fernando Ortiz",
    "Paula Romero",
    "Adriana Jiménez",
    "Luis Navarro",
    "Beatriz Gil",
    "David Ramos",
    "Sofía Vega",
    "Pablo Méndez",
    "Laura Rivas"
]
        albumnes = [
    "Sueños bajo la luna",
    "Ecos en el viento",
    "Voces del atardecer",
    "Caminos de esperanza",
    "Sombras de la ciudad",
    "Luces en el abismo",
    "Historias nunca contadas",
    "Viaje sin destino",
    "Lágrimas en la lluvia",
    "Horizontes infinitos",
    "Notas del pasado",
    "Ritmos de libertad",
    "Reflejos de la noche",
    "Susurros del bosque",
    "El eco de tu voz",
    "Poesía de medianoche",
    "Luz de un nuevo día",
    "Corazones en llamas",
    "El silencio del mar",
    "Vientos del mañana",
    "Ciclos del tiempo",
    "Sombras en el agua",
    "Fragmentos de memoria",
    "El viaje del alma",
    "La fuerza de la vida",
    "Melodías en el aire",
    "Cielos olvidados",
    "El poder del amor",
    "Nostalgia en el camino",
    "Ríos de luz",
    "La armonía del caos",
    "Sueños de invierno",
    "Energía en movimiento",
    "Misterios del universo",
    "Estrellas en la noche",
    "El amanecer eterno",
    "A través del espejo",
    "Ecos del corazón",
    "La magia del silencio",
    "Vuelo sin fronteras"
]
        generos = ["Pop", "Rock", "Hip-Hop", "Jazz", "Clásica"]

        if (not Cancion.objects.exists()) :


            for i in range(1,300):
                fecha_aleatoria = faker.date_time_between(start_date='-20y', end_date='now')
                fecha_formateada = fecha_aleatoria.strftime('%Y-%m-%d')
                Cancion.objects.create(titulo=faker.sentence(nb_words=6), artista=random.choice(artistas),album=random.choice(albumnes),genero=random.choice(generos),duracion=faker.random_int(min=150, max=600),fecha_lanzamiento=fecha_formateada)
            self.stdout.write(self.style.SUCCESS('Se han añadidio las canciones correctamente'))
        else:
            self.stderr.write(self.style.ERROR('Algo me ha fallado'))