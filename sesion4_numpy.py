import pygame
import sys
import numpy as np

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 4 - Movimiento con NumPy")

class Agente:

    def __init__(self, x, y):
        # posición como vector numpy
        self.pos = np.array([x, y], dtype=float)

        # dirección inicial
        self.dir = np.array([1.0, 0.0])

        self.velocidad = 3

        self.tamano = 40

        self.vertices_locales = np.array([
            [0, -self.tamano],
            [-self.tamano/2, self.tamano/2],
            [self.tamano/2, self.tamano/2]
        ])

    def mover(self):

        teclas = pygame.key.get_pressed()

        direccion = np.array([0.0, 0.0])

        if teclas[pygame.K_LEFT]:
            direccion[0] -= 1
        if teclas[pygame.K_RIGHT]:
            direccion[0] += 1
        if teclas[pygame.K_UP]:
            direccion[1] -= 1
        if teclas[pygame.K_DOWN]:
            direccion[1] += 1

        # normalización para velocidad constante
        magnitud = np.linalg.norm(direccion)

        if magnitud != 0:
            direccion = direccion / magnitud

        self.pos += direccion * self.velocidad

    def dibujar(self, superficie):

        vertices = []

        for v in self.vertices_locales:
            vx = self.pos[0] + v[0]
            vy = self.pos[1] + v[1]
            vertices.append((vx, vy))

        pygame.draw.polygon(superficie, (0,200,255), vertices)


agente = Agente(400,300)

corriendo = True

while corriendo:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill((0,0,0))

    agente.mover()
    

    agente.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
sys.exit()
