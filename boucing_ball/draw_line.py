"""
File: draw_line.py
Name: Charlie chen
------------------------
This file shows that the function of drawing line when we use mouse-click twice.
"""
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 10
x = 0
y = 0
counter = 0
circle_pre = None


def main():
    onmouseclicked(draw_circle)


def draw_circle(mouse):
    """
    當onmouseclicked觸發下，先在觸擊的位置上產生圓，並把位置儲都global的變數 x ,y裡，第二次觸擊時就取
    消上一個圓，同時並根據mouse.x, mouse.y 及global變數 , x ,y來畫線
    :param mouse: onmouseclicked所產生
    :return: None
    """
    global x, y, counter, circle_pre
    # 用來計數點擊次數
    counter += 1
    circle = GOval(SIZE, SIZE)
    window.add(circle, x=mouse.x - circle.width / 2, y=mouse.y - circle.height / 2)
    if counter % 2 == 0:
        line = GLine(x, y, mouse.x, mouse.y)
        window.remove(circle_pre)
        window.remove(circle)
        window.add(line)
    else:
        x = mouse.x
        y = mouse.y
        # 把物件位置存在circle_pre裡，給下一次循環時刪除
        circle_pre = circle


if __name__ == '__main__':
    main()
