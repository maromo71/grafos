# Jogo simples estilo "Asteroids" (anos 80) em Python + Pygame
# Autor: ChatGPT (para Maromo)
# Requisitos: Python 3.9+ e pygame (pip install pygame)
#
# Controles:
#   ←/→  : girar a nave
#   ↑    : propulsão (thrust)
#   ESPAÇO: disparar
#   H    : hiperespaco (teleporte seguro, com pequeno risco)
#   P    : pausar
#   ESC  : sair
#
# Recursos:
# - Física simples com dt (delta time)
# - Asteroides se dividem em menores quando atingidos
# - Vida extra a cada 10.000 pontos
# - Piscada de invulnerabilidade ao renascer
# - Wrap de tela (borda para borda)
#
# Observação: este é um projeto didático, com foco em clareza.
# Sinta-se livre para aprimorar (sons, sprites, efeitos, etc.).

import math
import random
import sys
from dataclasses import dataclass
from typing import List, Tuple

import pygame

# --------------------------- Configurações gerais ---------------------------

WIDTH, HEIGHT = 960, 720
FPS = 60

# Cores
WHITE = (240, 240, 240)
GRAY = (140, 140, 140)
DARK = (15, 18, 22)
ACCENT = (80, 200, 255)

# Nave
SHIP_RADIUS = 12
SHIP_THRUST = 220.0      # px/s^2
SHIP_ROT_SPEED = 220.0   # deg/s
SHIP_FRICTION = 0.985    # damping por frame
SHIP_RESPAWN_INVULN = 2.5  # s
SHIP_HYPERSPACE_COOLDOWN = 2.0  # s

# Tiro
BULLET_SPEED = 520.0    # px/s
BULLET_LIFETIME = 1.2   # s
BULLET_CADENCE = 0.22   # s

# Asteroide
AST_SPEED_MIN = 40.0
AST_SPEED_MAX = 120.0
AST_SIZES = {3: 40, 2: 25, 1: 15}  # size->raio
AST_SCORE = {3: 20, 2: 50, 1: 100}

STARTING_LIVES = 3
EXTRA_LIFE_SCORE = 10_000


def wrap(pos: pygame.Vector2) -> pygame.Vector2:
    """Faz o wrap de tela (teletransporte de borda a borda)."""
    x = pos.x % WIDTH
    y = pos.y % HEIGHT
    return pygame.Vector2(x, y)


def rand_unit_vec() -> pygame.Vector2:
    ang = random.uniform(0, math.tau)
    return pygame.Vector2(math.cos(ang), math.sin(ang))


@dataclass
class Bullet:
    pos: pygame.Vector2
    vel: pygame.Vector2
    ttl: float  # time to live (s)

    def update(self, dt: float):
        self.pos += self.vel * dt
        self.pos = wrap(self.pos)
        self.ttl -= dt

    def draw(self, surf: pygame.Surface):
        pygame.draw.circle(surf, WHITE, self.pos, 2)


@dataclass
class Asteroid:
    pos: pygame.Vector2
    vel: pygame.Vector2
    size: int  # 3=grande, 2=medio, 1=pequeno
    angle: float
    ang_vel: float

    @property
    def radius(self) -> float:
        return AST_SIZES[self.size]

    def update(self, dt: float):
        self.pos += self.vel * dt
        self.pos = wrap(self.pos)
        self.angle = (self.angle + self.ang_vel * dt) % 360

    def draw(self, surf: pygame.Surface):
        # Polígono irregular simples
        r = self.radius
        points = []
        spikes = 10
        for i in range(spikes):
            a = (i / spikes) * math.tau + math.radians(self.angle)
            # ligeira variação para dar aspecto rochoso
            rr = r * random.uniform(0.80, 1.05)
            points.append((self.pos.x + math.cos(a) * rr,
                           self.pos.y + math.sin(a) * rr))
        pygame.draw.polygon(surf, WHITE, points, 2)


class Ship:
    def __init__(self, pos: Tuple[float, float]):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0, 0)
        self.angle = -90.0  # apontando para cima
        self.radius = SHIP_RADIUS
        self.can_shoot_in = 0.0
        self.invuln = SHIP_RESPAWN_INVULN
        self.hyper_cooldown = 0.0
        self.alive = True

    def reset(self):
        self.pos.update(WIDTH / 2, HEIGHT / 2)
        self.vel.update(0, 0)
        self.angle = -90.0
        self.can_shoot_in = 0.0
        self.invuln = SHIP_RESPAWN_INVULN
        self.hyper_cooldown = 0.0
        self.alive = True

    def update(self, dt: float, keys: pygame.key.ScancodeWrapper):
        # Rotação
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.angle -= SHIP_ROT_SPEED * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.angle += SHIP_ROT_SPEED * dt

        # Thrust
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            rad = math.radians(self.angle)
            thrust_vec = pygame.Vector2(math.cos(rad), math.sin(rad)) * SHIP_THRUST * dt
            self.vel += thrust_vec

        # Atrito leve
        self.vel *= SHIP_FRICTION

        # Movimento + wrap
        self.pos += self.vel * dt
        self.pos = wrap(self.pos)

        # Timers
        if self.can_shoot_in > 0:
            self.can_shoot_in -= dt
        if self.invuln > 0:
            self.invuln -= dt
        if self.hyper_cooldown > 0:
            self.hyper_cooldown -= dt

    def shoot(self) -> Bullet | None:
        if self.can_shoot_in > 0:
            return None
        rad = math.radians(self.angle)
        dir_vec = pygame.Vector2(math.cos(rad), math.sin(rad))
        muzzle = self.pos + dir_vec * (self.radius + 8)
        bullet_vel = dir_vec * BULLET_SPEED + self.vel * 0.35
        self.can_shoot_in = BULLET_CADENCE
        return Bullet(muzzle, bullet_vel, BULLET_LIFETIME)

    def hyperspace(self):
        if self.hyper_cooldown > 0:
            return
        # Teleporte para posição "segura" aleatória
        # Há um pequeno risco (~10%) de sair em lugar ruim e explodir
        self.pos = pygame.Vector2(random.uniform(0, WIDTH), random.uniform(0, HEIGHT))
        self.vel.update(0, 0)
        self.hyper_cooldown = SHIP_HYPERSPACE_COOLDOWN
        if random.random() < 0.10:  # risco
            self.invuln = 0
            self.alive = False  # vai explodir no check de colisão

    def hit(self) -> bool:
        """Retorna True se foi atingida (considerando invulnerabilidade)."""
        return self.invuln <= 0

    def draw(self, surf: pygame.Surface):
        # Triângulo representando a nave
        rad = math.radians(self.angle)
        dir_vec = pygame.Vector2(math.cos(rad), math.sin(rad))
        left_vec = pygame.Vector2(math.cos(rad + 2.4), math.sin(rad + 2.4))
        right_vec = pygame.Vector2(math.cos(rad - 2.4), math.sin(rad - 2.4))

        tip = self.pos + dir_vec * (self.radius + 6)
        left = self.pos + left_vec * self.radius
        right = self.pos + right_vec * self.radius

        color = ACCENT if (self.invuln > 0 and int(self.invuln * 12) % 2 == 0) else WHITE
        pygame.draw.polygon(surf, color, [tip, left, right], 2)

        # Traço do motor quando acelerando
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            back = self.pos - dir_vec * (self.radius - 2)
            flame_left = back + left_vec * 4
            flame_right = back + right_vec * 4
            tail = self.pos - dir_vec * (self.radius + random.uniform(10, 18))
            pygame.draw.polygon(surf, color, [flame_left, tail, flame_right], 1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids (didático)")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 22)
        self.bigfont = pygame.font.SysFont("consolas", 46, bold=True)

        self.ship = Ship((WIDTH / 2, HEIGHT / 2))
        self.bullets: List[Bullet] = []
        self.asteroids: List[Asteroid] = []
        self.score = 0
        self.lives = STARTING_LIVES
        self.extra_life_threshold = EXTRA_LIFE_SCORE
        self.level = 0
        self.paused = False
        self.game_over = False

        self.start_new_level()

    def start_new_level(self):
        self.level += 1
        self.asteroids.clear()
        count = min(3 + self.level, 10)
        for _ in range(count):
            self.spawn_asteroid(3, avoid_pos=self.ship.pos, min_dist=220)

    def spawn_asteroid(self, size: int, avoid_pos: pygame.Vector2 | None = None, min_dist: float = 180.0):
        # Escolhe um ponto afastado da nave (ao iniciar nível/respawn)
        while True:
            pos = pygame.Vector2(random.uniform(0, WIDTH), random.uniform(0, HEIGHT))
            if avoid_pos is None or pos.distance_to(avoid_pos) > min_dist:
                break
        speed = random.uniform(AST_SPEED_MIN, AST_SPEED_MAX) * (1.0 + self.level * 0.05)
        vel = rand_unit_vec() * speed
        ang = random.uniform(0, 360)
        ang_vel = random.uniform(-50, 50)
        self.asteroids.append(Asteroid(pos, vel, size, ang, ang_vel))

    def split_asteroid(self, ast: Asteroid):
        if ast.size > 1:
            for _ in range(2):
                child = Asteroid(
                    pos=ast.pos.copy(),
                    vel=rand_unit_vec() * random.uniform(AST_SPEED_MIN, AST_SPEED_MAX) * 1.15,
                    size=ast.size - 1,
                    angle=random.uniform(0, 360),
                    ang_vel=random.uniform(-80, 80),
                )
                self.asteroids.append(child)

    def handle_collisions(self):
        # Balas x Asteroides
        new_asteroids: List[Asteroid] = []
        for ast in list(self.asteroids):
            hit = False
            for b in list(self.bullets):
                if ast.pos.distance_to(b.pos) <= ast.radius + 2:
                    hit = True
                    self.bullets.remove(b)
                    self.score += AST_SCORE[ast.size]
                    if self.score >= self.extra_life_threshold:
                        self.lives += 1
                        self.extra_life_threshold += EXTRA_LIFE_SCORE
                    break
            if hit:
                self.asteroids.remove(ast)
                self.split_asteroid(ast)

        # Nave x Asteroides
        if self.ship.alive:
            for ast in self.asteroids:
                if ast.pos.distance_to(self.ship.pos) <= ast.radius + self.ship.radius:
                    if self.ship.hit():
                        self.ship.alive = False
                    break

        # Se a nave "morreu", processa perda de vida e respawn
        if not self.ship.alive:
            self.lives -= 1
            if self.lives < 0:
                self.game_over = True
            else:
                self.ship.reset()
                # Garante que não renasça em cima de asteroide
                safe = False
                for _ in range(120):
                    if all(a.pos.distance_to(self.ship.pos) > a.radius + 160 for a in self.asteroids):
                        safe = True
                        break
                    # tenta nova posição central com jitter
                    jitter = pygame.Vector2(random.uniform(-80, 80), random.uniform(-80, 80))
                    self.ship.pos = wrap(pygame.Vector2(WIDTH / 2, HEIGHT / 2) + jitter)
                if not safe:
                    # como fallback, remove asteroides muito próximos
                    self.asteroids = [a for a in self.asteroids if a.pos.distance_to(self.ship.pos) > a.radius + 160]
                self.ship.alive = True  # volta ao jogo

    def update(self, dt: float):
        if self.paused or self.game_over:
            return

        keys = pygame.key.get_pressed()
        self.ship.update(dt, keys)

        for b in list(self.bullets):
            b.update(dt)
            if b.ttl <= 0:
                self.bullets.remove(b)

        for a in self.asteroids:
            a.update(dt)

        self.handle_collisions()

        # Próximo nível quando limpar todos
        if not self.asteroids and not self.game_over:
            self.start_new_level()

    def draw_hud(self, surf: pygame.Surface):
        score_text = self.font.render(f"SCORE {self.score:06d}   LVL {self.level}", True, WHITE)
        surf.blit(score_text, (16, 12))

        # Vidas como mini naves
        for i in range(max(0, self.lives)):
            x = WIDTH - 24 - i * 20
            y = 20
            r = 6
            ang = -90
            rad = math.radians(ang)
            dir_vec = pygame.Vector2(math.cos(rad), math.sin(rad))
            left_vec = pygame.Vector2(math.cos(rad + 2.4), math.sin(rad + 2.4))
            right_vec = pygame.Vector2(math.cos(rad - 2.4), math.sin(rad - 2.4))
            tip = pygame.Vector2(x, y) + dir_vec * (r + 4)
            left = pygame.Vector2(x, y) + left_vec * r
            right = pygame.Vector2(x, y) + right_vec * r
            pygame.draw.polygon(surf, WHITE, [tip, left, right], 1)

    def draw(self):
        self.screen.fill(DARK)

        # Estrelas de fundo discretas
        for _ in range(24):
            x = random.randrange(0, WIDTH)
            y = random.randrange(0, HEIGHT)
            self.screen.set_at((x, y), GRAY)

        # Entidades
        for a in self.asteroids:
            a.draw(self.screen)
        for b in self.bullets:
            b.draw(self.screen)
        if self.ship.alive:
            self.ship.draw(self.screen)

        self.draw_hud(self.screen)

        if self.paused:
            t = self.bigfont.render("PAUSADO", True, WHITE)
            self.screen.blit(t, t.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        if self.game_over:
            t1 = self.bigfont.render("GAME OVER", True, WHITE)
            t2 = self.font.render("Pressione ENTER para reiniciar ou ESC para sair", True, WHITE)
            self.screen.blit(t1, t1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 24)))
            self.screen.blit(t2, t2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 24)))

        pygame.display.flip()

    def run(self):
        while True:
            dt_ms = self.clock.tick(FPS)
            dt = dt_ms / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if not self.game_over:
                        if event.key == pygame.K_SPACE:
                            b = self.ship.shoot()
                            if b:
                                self.bullets.append(b)
                        elif event.key == pygame.K_h:
                            self.ship.hyperspace()
                        elif event.key == pygame.K_p:
                            self.paused = not self.paused
                    else:
                        if event.key == pygame.K_RETURN:
                            # Reinicia jogo
                            self.__init__()

            if not self.paused:
                self.update(dt)
            self.draw()


if __name__ == "__main__":
    Game().run()
