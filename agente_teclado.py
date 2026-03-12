import pygame
import sys

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Agente controlado con teclado")

# -------- Clase Agente --------
class Agente:
    """
    Representa un agente que puede moverse dentro del entorno.
    La estructura está preparada para agregar comportamientos inteligentes
    en futuras sesiones.
    """

    def __init__(self, x, y, tamano=30):
        self.x = x
        self.y = y
        self.tamano = tamano
        self.velocidad = 5

    def mover(self, teclas):
        """Mueve el agente según las flechas del teclado"""

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad

        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad

        if teclas[pygame.K_UP]:
            self.y -= self.velocidad

        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad

    def rebotar(self):
        """Evita que el agente salga de la pantalla"""

        if self.x < self.tamano:
            self.x = self.tamano

        if self.x > ANCHO - self.tamano:
            self.x = ANCHO - self.tamano

        if self.y < self.tamano:
            self.y = self.tamano

        if self.y > ALTO - self.tamano:
            self.y = ALTO - self.tamano

    def dibujar(self, superficie):
        """Dibuja el agente en la pantalla"""
        pygame.draw.circle(superficie, (0, 200, 255), (int(self.x), int(self.y)), self.tamano)


# -------- Crear agente --------
agente = Agente(400, 300)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:

    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    agente.mover(teclas)
    agente.rebotar()

    pantalla.fill((0, 0, 0))

    agente.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
sys.exit()