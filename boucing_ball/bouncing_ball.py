"""
File: bouncing_ball.py
Name: Charlie chen
------------------------
This file demonstrates that the motion of the ball dropping to the ground  when mouse is clicked
After three times click, the mouse function was deactivated
"""
from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# 設置窗口和球的初始位置及其大小
window = GWindow(width=800, height=500)
X_START = 0
Y_START = 20
SIZE = 10

# 設置球的加速度
GRAVITY = 19800
VX = 100
# 設置球的衰減系數
REDUCE = 0.9

# 設置間隔(單位)時間
DELAY = 0.001

ball_start = GOval(SIZE, SIZE, x=X_START, y=Y_START)
ball_end = None
counter = 0   # 用來計算滑鼠指令的次數


def main():
    ball_start.filled = True
    window.add(ball_start)
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    """
    用來繪製動畫，作為onmouseclicked的function，當點蠕時預設球為消失，並且產生一個跳動的球。
    在執行三次後就會使onmouseclicked的功能失效
    """
    global counter, ball_end
    counter += 1
    window.remove(ball_start)
    window.remove(ball_end)
    x = X_START
    y = Y_START
    velocity_y = 0
    # 用來防止在程式進行中滑鼠的指令影響
    onmouseclicked(do_nothing)
    while True:
        # 繪製球
        ball = GOval(SIZE, SIZE)
        ball.filled = True
        window.add(ball, x=x, y=y)
        # 設定速度公式  速度 = 加速度 * 單位時間
        velocity_y += GRAVITY * DELAY
        # 設定y軸位移 = 速度 * 單位時間 + 1/2 * 重力加速度 * 單位時間的平方
        y += velocity_y * DELAY + 0.5 * GRAVITY * DELAY ** 2
        # 設定x軸位移 = 速度 * 單位時間 (等速)
        x += VX * DELAY
        # 如果球碰到地面，進行彈性碰撞
        if y + SIZE >= window.height:
            y = window.height - SIZE  # 迫使球不會掉到底下
            # 在彈性碰撞時速度產生衰減
            velocity_y *= -REDUCE

        pause(DELAY * 1000)

        # 移除上一顆的球和軌跡
        window.remove(ball)
        print(velocity_y)
        # 如果球超出範圍就重新製造一顆新球，並且終止此循環
        if x + SIZE >= window.width:
            ball_end = GOval(SIZE, SIZE, x=X_START, y=Y_START)
            ball_end.filled = True
            window.add(ball_end)
            # 重新啟動滑鼠指令
            onmouseclicked(bouncing_ball)
            break
    # 若執行超過三次，就使onmouseclicked function失效 (即放入沒有功用的function)
    if counter >= 3:
        onmouseclicked(do_nothing)
    # 移除最後一幀的球和軌跡
    window.remove(ball)


# 定義一個沒有功用的function
def do_nothing(mouse):
    pass


if __name__ == '__main__':
    main()
