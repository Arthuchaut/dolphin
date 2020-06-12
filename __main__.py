from typing import List
import time
import os
from sprites import sprites, background

SPEED: float = 0.1
DISTANCE: int = 30


def invert(sprite: str) -> str:
    return (
        '\n'.join([line[::-1] for line in sprite.split('\n')])
        .replace(')@(', '(@)')
        .replace(')-(', '(-)')
        .replace('<>', '><')
    )


def translate(sprite: str, sp: int) -> str:
    return '\n'.join(
        [' '.join(['' for __ in range(sp)]) + _ for _ in sprite.split('\n')]
    )


def draw(sprite: str, bg: str, v: float) -> None:
    print(sprite + bg)
    time.sleep(v)
    os.system('clear')


def animate(
    *, sprites: List[str], background: str, speed: float, distance: int
) -> None:
    i: int = 0
    j: int = 0
    k: int = 0
    sprite: str = None
    inv: bool = False

    while True:
        i = i % len(sprites)
        j = j % distance
        inv = not inv if not j else inv
        sprite = sprites[i] if inv else invert(sprites[i])
        sprite = translate(sprite, k)

        draw(sprite, background, speed)

        j += 1
        i += 1
        k += 1 if inv else -1


if __name__ == '__main__':
    animate(
        sprites=sprites, background=background, speed=SPEED, distance=DISTANCE
    )
