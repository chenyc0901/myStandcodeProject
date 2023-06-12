"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, life=3,
                 title='Breakout'):
        self.ball_radius = ball_radius
        self.minions_body_lists = []
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.brick_spacing = brick_spacing
        self.total_score = BRICK_COLS * BRICK_ROWS + 150
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.minions_x = 0
        self.minions_y = self.window.height / 2 - 35
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width - self.ball.width) / 2, y=window_height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        # Default initialize the king's location
        self.head_oval = None
        # the velocity of minions
        self.minions_dx = 3
        self.minions_dy = 3
        # the bullet
        self.box_counter = 0
        self.box = None
        self.box_list = []
        self.box_size = 10
        # Initialize our mouse listeners
        onmousemoved(self.reset_position)
        onmouseclicked(self.ball_move)
        # Draw bricks
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.bricks_list = []
        for i in range(brick_rows):
            tmp = []
            for j in range(brick_cols):
                self.brick = self.draw_single_bricks()
                tmp.append(self.brick)
            self.bricks_list.append(tmp)
        for i in range(brick_rows):
            for j in range(brick_cols):
                object_draw = self.bricks_list[i][j]
                self.window.add(object_draw, x=j * (brick_width + brick_spacing),
                                y=i * (brick_height + brick_spacing) + brick_offset)
        self.red_brick_list = []
        self.red_brick()
        # life counter

        self.life = life
        ball_size = 20
        self.life_list = []
        for i in range(self.life):
            self.life_o = GOval(ball_size, ball_size, x=self.window.width - ball_size * (i + 1),
                                y=self.window.height - ball_size)
            self.life_o.filled = True
            self.life_o.fill_color = "grey"
            self.life_list.append(self.life_o)
            self.window.add(self.life_list[i])
        # score
        self.score = 0
        # calculator
        self.cal = GLabel("Score:  ")
        self.window.add(self.cal, x=0, y=self.window.height - self.cal.height)
        self.cal_score = GLabel(self.score)
        self.window.add(self.cal_score, x=self.cal.width, y=self.window.height - self.cal.height)

    def king_appear(self):
        """
        小小兵出現的動畫，先出現warning messeage然後繪製小小兵
        """
        for i in range(2):
            rect = GRect(self.window.width, self.window.height, x=0, y=0)
            rect.filled = True
            rect.fill_color = 'red'
            self.window.add(rect)
            label = GLabel("Warning")
            label.font = '-80-bold'
            self.window.add(label, x=(self.window.width - label.width) / 2, y=(self.window.height - label.height) / 2)
            pause(50)
            self.window.remove(rect)
            self.window.remove(label)
        self.__dy *=1.5

    def minions_draw(self):
        """
        繪製小小兵
        """
        self.head_oval = GOval(70, 60, x=self.minions_x, y=self.minions_y)
        self.head_oval.filled = True
        self.head_oval.fill_color = 'yellow'
        self.head_oval.color = 'yellow'
        head_oval_eye = GOval(45, 45, x=self.minions_x + 10, y=self.minions_y + 20)
        head_oval_eye.filled = True
        head_oval_eye.fill_color = 'grey'
        head_oval_eye.color = 'grey'
        head_oval_eye2 = GOval(35, 35, x=self.minions_x + 15, y=self.minions_y + 25)
        head_oval_eye2.filled = True
        head_oval_eye2.fill_color = 'white'
        head_oval_eye2.color = 'white'
        head_rec = GRect(70, 80, x=self.minions_x, y=self.minions_y + 35)
        head_rec.filled = True
        head_rec.fill_color = 'yellow'
        head_rec.color = 'yellow'
        eyebow = GOval(25, 25, x=self.minions_x + 20, y=self.minions_y + 30)
        eyebow.filled = True
        eyebow.fill_color = 'brown'
        eyebow.color = 'brown'
        eyebow2 = GOval(15, 15, x=self.minions_x + 25, y=self.minions_y + 35)
        eyebow2.filled = True
        eyebow3 = GOval(5, 5, x=self.minions_x + 25, y=self.minions_y + 35)
        eyebow3.filled = True
        eyebow3.fill_color = 'white'
        eyebow3.color = 'white'
        belt = GRect(10, 10, x=self.minions_x, y=self.minions_y + 35)
        belt.filled = True
        belt2 = GRect(20, 10, x=self.minions_x + 50, y=self.minions_y + 35)
        belt2.filled = True
        pant = GRect(40, 20, x=self.minions_x + 16, y=self.minions_y + 90)
        pant.filled = True
        pant.fill_color = 'lightskyblue'
        pant.color = 'lightskyblue'

        pant2 = GRect(70, 10, x=self.minions_x, y=self.minions_y + 105)
        pant2.filled = True
        pant2.fill_color = 'lightskyblue'
        pant2.color = 'lightskyblue'

        self.minions_body_lists.append(self.head_oval)
        self.minions_body_lists.append(head_rec)
        self.minions_body_lists.append(belt)
        self.minions_body_lists.append(belt2)
        self.minions_body_lists.append(head_oval_eye)
        self.minions_body_lists.append(head_oval_eye2)
        self.minions_body_lists.append(eyebow)
        self.minions_body_lists.append(eyebow2)
        self.minions_body_lists.append(eyebow3)
        self.minions_body_lists.append(pant)
        self.minions_body_lists.append(pant2)

        for i in self.minions_body_lists:
            self.window.add(i)

    def minions_move(self):
        """
        小小兵的移動
        """
        self.box_counter += 1
        if self.head_oval.x < 0 or self.head_oval.x + 70 >= self.window.width:
            self.minions_dx *= -1
        if self.head_oval.y + 250 > self.window.height or self.head_oval.y < self.brick_spacing:
            self.minions_dy *= -1
        for obj in self.minions_body_lists:
            obj.move(self.minions_dx, self.minions_dy)

    def box_draw(self):
        """
        小小兵射出的攻擊子彈
        """
        self.box = GRect(self.box_size, self.box_size)
        self.box.filled = True
        self.box.fill_color = 'yellow'
        self.window.add(self.box, x=self.head_oval.x + 35, y=self.head_oval.y)
        self.box_list.append(self.box)

    def box_dropping(self):
        """
        攻擊子彈的移動
        """
        for obj in self.box_list:
            if obj.y <= self.window.height - obj.height:
                obj.move(0, 5)
            else:
                self.window.remove(obj)

    def box_collision(self):
        """
        當攻擊子彈撞到paddle的反應，並且在撞到時paddle會變短且會有短暫黃色警示
        """
        switch = False
        for obj in self.box_list:
            for i in range(2):
                x = obj.x + obj.width
                y = obj.y + obj.height + 0.1
                position_obj = self.window.get_object_at(x, y)

                if position_obj is None:
                    continue
                elif position_obj is self.paddle:
                    self.window.remove(obj)
                    if self.paddle.width >= 10:
                        self.paddle_width -= 5
                    else:
                        self.life -= 1
                    x_position = self.paddle.x
                    y_position = self.paddle.y
                    self.paddle.filled = True
                    self.paddle.fill_color = 'yellow'
                    pause(30)
                    self.window.remove(self.paddle)
                    self.paddle = GRect(self.paddle_width, self.paddle_height)
                    self.paddle.filled = True
                    self.window.add(self.paddle, x=x_position, y=y_position)
                    switch = True
                    break
            if switch:
                break

    def red_brick(self):
        """
        隨機產生 red brick
        """
        for i in range(15):
            row = random.randint(0, self.brick_rows - 1)
            col = random.randint(0, self.brick_cols - 1)
            red_object = self.bricks_list[row][col]
            red_object.filled = True
            red_object.fill_color = 'red'
            self.red_brick_list.append(red_object)

    def game_over(self, name):
        """
        最後遊戲結束的動畫
        :param name: ｓｔｒ　；最後顯示的字　可以是ｇａｍｅ　ｏｖｅｒ　ｏｒ　ｙｏｕ　ｌｏｓｅ
        """
        for i in self.minions_body_lists:
            self.window.remove(i)
        for j in self.box_list:
            self.window.remove(j)
        self.window.remove(self.ball)
        onmouseclicked(self.no_function)
        label = GLabel(name)
        label.font = '-40'
        x_position = (self.window.width - label.width) // 2
        self.window.add(label, x=x_position, y=self.window.height)
        for i in range((self.window.height - label.height) // 10):
            label.move(dx=0, dy=-5)
            pause(30)

    def init_ball(self):
        """
        設置初始球
        """
        self.life -= 1
        self.window.remove(self.life_list[self.life])
        self.window.remove(self.ball)
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2, y=self.window.height / 2 - BALL_RADIUS)
        self.__dy = 0
        self.__dx = 0
        onmouseclicked(self.ball_move)
        for obj in self.box_list:
            self.window.remove(obj)

    def ball_move(self, event):
        """
        球的移動
        :param event: onmouseclicked所需
        """
        onmouseclicked(self.no_function)
        if self.score <= 100:
            self.__dy = INITIAL_Y_SPEED
        else:
            self.__dy = INITIAL_Y_SPEED * 2.5
        random_x_speed = random.randint(1, MAX_X_SPEED)
        self.__dx = random_x_speed
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def collision(self):
        """
        當球碰到板子的反應
        """
        switch = False  # 作為開關，如果碰到板子就結速所有點的檢查
        for x in range(2):
            for y in range(2):
                x_position = self.ball.x + self.ball_radius * 2 * x
                y_position = self.ball.y + self.ball_radius * 2 * y
                position_object = self.window.get_object_at(x_position, y_position)

                if position_object is None:
                    continue
                else:
                    if position_object is self.paddle:
                        self.__dy = -abs(self.__dy)
                        random_x_speed = random.randint(1, MAX_X_SPEED)
                        self.__dx = abs(random_x_speed) if self.__dx > 0 else -abs(random_x_speed)
                        switch = True
                        break
                    elif position_object in [self.cal, self.cal_score] or position_object in self.life_list:
                        switch = True
                        break
                    elif position_object in self.minions_body_lists:
                        switch = True
                        break
                    elif position_object in self.box_list:
                        switch = True
                        break
                    elif position_object in self.red_brick_list:
                        self.score += 10
                        position_object.fill_color = 'blue'
                        object_index = self.red_brick_list.index(position_object)
                        self.red_brick_list.pop(object_index)
                        self.__dy = -self.__dy
                        self.__dx = -self.__dx
                        switch = True
                        break
                    else:
                        self.score += 1
                        self.__dy = -self.__dy
                        self.__dx = -self.__dx
                        self.window.remove(position_object)
                        self.window.remove(self.cal_score)
                        self.cal_score = GLabel(self.score)
                        self.window.add(self.cal_score, x=self.cal.width, y=self.window.height - self.cal.height)
                        switch = True
                        break
            if switch:
                break

    def no_function(self, event):
        pass

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_vx(self, reset):
        self.__dx = reset

    def set_vy(self, reset):
        self.__dy = reset

    def reset_position(self, mouse):
        if mouse.x - self.paddle.width / 2 <= 0:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def draw_single_bricks(self):
        bricks = GRect(self.brick_width, self.brick_height)
        return bricks
