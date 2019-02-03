import pygame

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
running = True
v = 20
ind = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            radius = 0
            x, y = event.pos
            ind = True
    screen.fill(pygame.Color('blue'))
    if ind:
        pygame.draw.circle(screen, pygame.Color('yellow'), (x, y), int(radius))
        radius += v * clock.tick() / 1000
    pygame.display.flip()
    clock.tick()
while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()
