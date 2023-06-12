"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
SCORE_LIMIT = 100  # Change Mode


def main():
    graphics = BreakoutGraphics(life=NUM_LIVES)
    count = 0
    box_counter = 0

    # Add the animation loop here!
    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()

        graphics.ball.move(vx, vy)
        # 碰到邊緣就反向
        if graphics.ball.x <= 0:
            graphics.set_vx(abs(vx))
        elif graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_vx(-abs(vx))
        if graphics.ball.y <= 0:
            graphics.set_vy(abs(vy))

        graphics.collision()
        if graphics.ball.y + graphics.ball.width >= graphics.window.height:
            graphics.init_ball()

        if graphics.score >= SCORE_LIMIT and count <= 1:
            count += 1
            graphics.king_appear()
            pause(100)
            graphics.minions_draw()
        elif graphics.score >= SCORE_LIMIT:
            box_counter += random.randint(1, 10)
            graphics.minions_move()
            if box_counter % 15 == 0 :
                graphics.box_draw()
            if graphics.box:
                graphics.box_dropping()
                graphics.box_collision()
        if graphics.score == graphics.total_score:
            graphics.game_over("Congratulations !!!")
            break
        if graphics.life == 0:
            graphics.game_over("Game Over")
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
