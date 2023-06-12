"""
File: my_drawing.py
Name: Charlie chen
----------------------
This file uses the campy module to
draw on a GWindow object.
"""
"""
Title: stanCode genetic factory

The factory owned by stancode has the capability to produce a large number of minions, 
each of whom can impart their knowledge of Python to us. 
This can be compared to the genetic DNA present in cells, 
which can be obtained from diverse sources and recombined to form various phenotypes.
"""
from campy.graphics.gobjects import GOval, GPolygon, GLabel, GLine, GRect, GArc
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=1000, height=1000, title='DNA molecular')
    phos_group_draw(100, 200, window)
    adenosine_draw(214, 200, window)
    line_ade_to_gua = GLine(215, 326, 107, 427)
    window.add(line_ade_to_gua)
    phos_group_draw(100, 500, window)
    guanine_draw(214, 500, window)
    antisense_phos_group_draw(825, 200, window)
    thymine_antisense_draw(550, 262, window)
    antisense_phos_group_draw(825, 500, window)
    cytosine_antisense_draw(550, 562, window)
    line_thy_to_cyt = GLine(820, 449, 692, 568)
    window.add(line_thy_to_cyt)
    minions_draw(385, 360, window)
    stancode_label(200, 80, window)

def minions_draw(x, y, window):
    head_oval = GOval(70, 60, x=x, y=y)
    head_oval.filled = True
    head_oval.fill_color = 'yellow'
    head_oval.color = 'yellow'
    head_oval_eye = GOval(45, 45, x=x+10, y=y+20)
    head_oval_eye.filled = True
    head_oval_eye.fill_color = 'grey'
    head_oval_eye.color = 'grey'
    head_oval_eye2 = GOval(35, 35, x=x+15, y=y+25)
    head_oval_eye2.filled = True
    head_oval_eye2.fill_color = 'white'
    head_oval_eye2.color = 'white'
    head_rec = GRect(70, 80, x=x, y=y+35)
    head_rec.filled = True
    head_rec.fill_color = 'yellow'
    head_rec.color = 'yellow'
    eyebow = GOval(25, 25, x=x+20, y=y+30)
    eyebow.filled = True
    eyebow.fill_color = 'brown'
    eyebow.color = 'brown'
    eyebow2 = GOval(15, 15, x=x+25, y=y+35)
    eyebow2.filled = True
    eyebow3 = GOval(5, 5, x=x+25, y=y+35)
    eyebow3.filled = True
    eyebow3.fill_color = 'white'
    eyebow3.color = 'white'
    belt = GRect(10, 10, x=x, y=y+35)
    belt.filled = True
    belt2 = GRect(20, 10, x=x+50, y=y+35)
    belt2.filled = True
    pant = GRect(40, 20, x=x+16, y=y+90)
    pant.filled = True
    pant.fill_color = 'lightskyblue'
    pant.color = 'lightskyblue'

    pant2 = GRect(70, 10, x=x, y=y+105)
    pant2.filled = True
    pant2.fill_color = 'lightskyblue'
    pant2.color = 'lightskyblue'

    belt3 = GPolygon()
    belt3.add_vertex((x,y+75))
    belt3.add_vertex((x,y+85))
    belt3.add_vertex((x+25,y+100))
    belt3.add_vertex((x+25,y+90))
    belt3.filled = True
    belt3.fill_color = 'lightskyblue'
    belt3.color = 'lightskyblue'

    belt4 = GPolygon()
    belt4.add_vertex((x+70,y+75))
    belt4.add_vertex((x+70,y+85))
    belt4.add_vertex((x+45,y+100))
    belt4.add_vertex((x+45,y+90))
    belt4.filled = True
    belt4.fill_color = 'lightskyblue'
    belt4.color = 'lightskyblue'

    window.add(head_oval)
    window.add(head_rec)
    window.add(belt)
    window.add(belt2)
    window.add(head_oval_eye)
    window.add(head_oval_eye2)
    window.add(eyebow)
    window.add(eyebow2)
    window.add(eyebow3)
    for i in range(0, 300, 10):
        j = float(i/100)
        mouth = GArc(20, 20, 200, 170, x=x + 30-j, y=y+70-j)
        window.add(mouth)
    window.add(pant)
    window.add(pant2)
    window.add(belt3)
    window.add(belt4)

def phos_group_draw(x, y, window):
    center_x = x
    center_y = y
    phos = GOval(40, 40, x=center_x - 16, y=center_y - 28)
    phos.filled = True
    phos.fill_color = 'red'
    phos_label = GLabel("P", x=center_x, y=center_y)
    oxygen1_label = GLabel("O", x=center_x, y=center_y - 50)
    oxygen2_label = GLabel("O", x=center_x, y=center_y + 50)
    oxygen2_negative_label = GLabel("-", x=center_x + 14, y=center_y + 45)
    oxygen3_label = GLabel("O", x=center_x - 50, y=center_y)
    oxygen4_label = GLabel("O", x=center_x + 50, y=center_y)
    ch_label = GLabel("CH", x=center_x + 90, y=center_y)
    ch_2_label = GLabel("2", x=center_x+115, y=center_y-2)
    ch_2_label.font = '-8'
    # To draw pentose carbohydrate element
    carbon_group = GPolygon()
    carbon_group_center_x = center_x + 94
    carbon_group_center_y = center_y + 90
    carbon_group.add_vertex((carbon_group_center_x, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x + 20, carbon_group_center_y + 35))
    carbon_group.add_vertex((carbon_group_center_x + 60, carbon_group_center_y + 35))
    carbon_group.add_vertex((carbon_group_center_x + 80, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x + 40, carbon_group_center_y - 27.5))
    carbon_group.filled = True
    carbon_group.fill_color = "blue"
    oxygen_in_carbon = GLabel("O", x=carbon_group_center_x+33, y=carbon_group_center_y-25)
    # To draw the link between oxygen and phosphate element
    line_o_to_p_1 = GLine(center_x + 5, center_y - 30, center_x + 5, center_y - 50)
    line_o_to_p_2 = GLine(center_x + 5, center_y + 14, center_x + 5, center_y + 34)
    line_o_to_p_3 = GLine(center_x - 18, center_y - 9, center_x - 38, center_y - 9)
    line_o_to_p_4 = GLine(center_x - 18, center_y - 11, center_x - 38, center_y - 11)
    line_o_to_p_5 = GLine(center_x + 27, center_y - 10, center_x + 47, center_y - 10)
    # To draw the link between oxygen and ch2 group
    line_o_to_ch2 = GLine(center_x + 67, center_y - 10, center_x + 87, center_y - 10)
    # To draw the line between ch2 group and pentose
    line_ch2_to_pentose = GLine(center_x + 94, center_y, center_x + 94, center_y + 90)
    # To draw the line to link pentose to purine or pyrimidine
    line_pentose_to_pp = GLine(center_x + 176, center_y + 90, center_x + 205, center_y + 90)

    window.add(oxygen1_label)
    window.add(oxygen2_label)
    window.add(oxygen3_label)
    window.add(oxygen4_label)
    window.add(ch_label)
    window.add(phos)
    window.add(phos_label)
    window.add(carbon_group)
    window.add(line_o_to_p_1)
    window.add(line_o_to_p_2)
    window.add(line_o_to_p_3)
    window.add(line_o_to_p_4)
    window.add(line_o_to_p_5)
    window.add(line_o_to_ch2)
    window.add(line_ch2_to_pentose)
    window.add(oxygen2_negative_label)
    window.add(line_pentose_to_pp)
    window.add(oxygen_in_carbon)
    window.add(ch_2_label)
# To construct purine backbone
def purine_draw(x, y, window):
    center_x = x
    center_y = y

    carbon_group = GPolygon()
    carbon_group_center_x = center_x + 94
    carbon_group_center_y = center_y + 90
    carbon_group.add_vertex((carbon_group_center_x, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x - 5, carbon_group_center_y - 35))
    carbon_group.add_vertex((carbon_group_center_x + 30, carbon_group_center_y - 50))
    line1 = GLine(carbon_group_center_x - 5, carbon_group_center_y - 37, carbon_group_center_x + 30,
                  carbon_group_center_y - 52)
    carbon_group.add_vertex((carbon_group_center_x + 60, carbon_group_center_y - 25))
    carbon_group.add_vertex((carbon_group_center_x + 40, carbon_group_center_y + 5))
    line2 = GLine(carbon_group_center_x + 57, carbon_group_center_y - 25, carbon_group_center_x + 37,
                  carbon_group_center_y + 5)
    carbon_group.filled = True
    carbon_group.fill_color = "grey"

    carbon_group2 = GPolygon()
    carbon_group2.add_vertex((carbon_group_center_x + 60, carbon_group_center_y - 25))
    carbon_group2.add_vertex((carbon_group_center_x + 40, carbon_group_center_y + 5))
    carbon_group2.add_vertex((carbon_group_center_x + 60, carbon_group_center_y + 30))
    carbon_group2.add_vertex((carbon_group_center_x + 90, carbon_group_center_y + 30))
    carbon_group2.add_vertex((carbon_group_center_x + 110, carbon_group_center_y + 5))
    carbon_group2.add_vertex((carbon_group_center_x + 90, carbon_group_center_y - 25))
    carbon_group2.filled = True
    carbon_group2.fill_color = "grey"

    window.add(carbon_group)
    window.add(line1)
    window.add(line2)
    window.add(carbon_group2)


def adenosine_draw(x, y, window, func=purine_draw):
    carbon_group_center_x = x + 94
    carbon_group_center_y = y + 90
    func(x, y, window)
    line_nh = GLine(carbon_group_center_x + 90, carbon_group_center_y - 25, carbon_group_center_x + 105,
                    carbon_group_center_y - 50)
    nitrogen1_label = GLabel("N", x=carbon_group_center_x + 107, y=carbon_group_center_y - 50)
    line_nh2 = GLine(carbon_group_center_x + 125, carbon_group_center_y - 60, carbon_group_center_x + 145,
                     carbon_group_center_y - 60)
    hydrogen1_label = GLabel("H", x=carbon_group_center_x + 150, y=carbon_group_center_y - 50)
    for i in range(0, 45, 5):
        line_link1 = GLine(carbon_group_center_x + 165 + i, carbon_group_center_y - 60, carbon_group_center_x + 167 + i,
                           carbon_group_center_y - 60)
        window.add(line_link1)
    nitrogen2_label = GLabel("N", x=carbon_group_center_x + 112, y=carbon_group_center_y + 15)
    for i in range(0, 60, 5):
        line_link2 = GLine(carbon_group_center_x + 127 + i, carbon_group_center_y + 5, carbon_group_center_x + 129 + i,
                           carbon_group_center_y + 5)
        window.add(line_link2)
    window.add(line_nh)
    window.add(line_nh2)
    window.add(hydrogen1_label)
    window.add(nitrogen1_label)
    window.add(nitrogen2_label)


def antisense_phos_group_draw(x, y, window):
    center_x = x
    center_y = y
    phos = GOval(40, 40, x=center_x - 16, y=center_y + 172)
    phos.filled = True
    phos.fill_color = 'red'
    phos_label = GLabel("P", x=center_x, y=center_y + 200)
    oxygen1_label = GLabel("O", x=center_x, y=center_y + 150)
    oxygen2_label = GLabel("O", x=center_x, y=center_y + 250)
    oxygen2_negative_label = GLabel("-", x=center_x + 14, y=center_y + 145)
    oxygen3_label = GLabel("O", x=center_x - 50, y=center_y + 200)
    oxygen4_label = GLabel("O", x=center_x + 50, y=center_y + 200)
    ch_label = GLabel("CH", x=center_x - 115, y=center_y + 200)
    ch_2_label = GLabel("2", x=center_x - 91, y=center_y +198)
    ch_2_label.font = '-8'
    # To draw pentose carbohydrate element
    carbon_group = GPolygon()
    carbon_group_center_x = center_x - 190
    carbon_group_center_y = center_y + 90
    carbon_group.add_vertex((carbon_group_center_x, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x + 20, carbon_group_center_y - 27))
    carbon_group.add_vertex((carbon_group_center_x + 60, carbon_group_center_y - 27))
    carbon_group.add_vertex((carbon_group_center_x + 80, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x + 40, carbon_group_center_y + 33))
    carbon_group.filled = True
    carbon_group.fill_color = "blue"
    oxygen_in_carbon = GLabel("O", x=carbon_group_center_x+35, y=carbon_group_center_y+53)
    # To draw the link between oxygen and phosphate element
    # To draw the link between oxygen and phosphate element
    line_o_to_p_1 = GLine(center_x + 5, center_y + 170, center_x + 5, center_y + 150)  # 200
    line_o_to_p_2 = GLine(center_x + 5, center_y + 214, center_x + 5, center_y + 234)
    line_o_to_p_3 = GLine(center_x + 27, center_y + 191, center_x + 47, center_y + 191)
    line_o_to_p_4 = GLine(center_x + 27, center_y + 189, center_x + 47, center_y + 189)
    line_o_to_p_5 = GLine(center_x - 52, center_y + 190, center_x - 82, center_y + 190)
    # To draw the link between oxygen and ch2 group
    line_o_to_ch2 = GLine(center_x - 18, center_y + 190, center_x - 38, center_y + 190)
    # To draw the line between ch2 group and pentose
    line_ch2_to_pentose = GLine(center_x - 110, center_y + 90, center_x - 110, center_y + 180)
    # To draw the line to link pentose to purine or pyrimidine
    line_pentose_to_pp = GLine(center_x - 195, center_y + 90, center_x - 215, center_y + 90)

    window.add(oxygen1_label)
    window.add(oxygen2_label)
    window.add(oxygen3_label)
    window.add(oxygen4_label)
    window.add(ch_label)
    window.add(phos)
    window.add(phos_label)
    window.add(carbon_group)
    window.add(line_o_to_p_1)
    window.add(line_o_to_p_2)
    window.add(line_o_to_p_3)
    window.add(line_o_to_p_4)
    window.add(line_o_to_p_5)
    window.add(line_o_to_ch2)
    window.add(line_ch2_to_pentose)
    window.add(oxygen2_negative_label)
    window.add(line_pentose_to_pp)
    window.add(oxygen_in_carbon)
    window.add(ch_2_label)

# To construct pyrimidine backbone
def pyrimidine_antisense_draw(x, y, window):
    carbon_group_center_x = x
    carbon_group_center_y = y

    carbon_group = GPolygon()
    carbon_group.add_vertex((carbon_group_center_x, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x + 40, carbon_group_center_y))
    carbon_group.add_vertex((carbon_group_center_x + 60, carbon_group_center_y + 30))
    carbon_group.add_vertex((carbon_group_center_x + 40, carbon_group_center_y + 60))
    carbon_group.add_vertex((carbon_group_center_x, carbon_group_center_y + 60))
    carbon_group.add_vertex((carbon_group_center_x - 20, carbon_group_center_y + 30))
    carbon_group.filled = True
    carbon_group.fill_color = "grey"

    window.add(carbon_group)


def thymine_antisense_draw(x, y, window, func=pyrimidine_antisense_draw):
    func(x, y, window)
    carbon_group_center_x = x
    carbon_group_center_y = y
    hydrogen_label = GLabel("H", x=carbon_group_center_x - 55, y=carbon_group_center_y + 42)
    line_hydrogen_to_pp = GLine(carbon_group_center_x - 40, carbon_group_center_y + 30, carbon_group_center_x - 20,
                                carbon_group_center_y + 30)
    oxygen1_label = GLabel("O", x=carbon_group_center_x - 30, y=carbon_group_center_y - 20)
    oxygen_pp_line1 = GLine(carbon_group_center_x - 15, carbon_group_center_y - 26, carbon_group_center_x + 1,
                            carbon_group_center_y - 1)
    oxygen_pp_line2 = GLine(carbon_group_center_x - 17, carbon_group_center_y - 24, carbon_group_center_x - 1,
                            carbon_group_center_y + 1)
    # the oxygen atom above pp
    oxygen2_label = GLabel("O", x=carbon_group_center_x - 30, y=carbon_group_center_y + 110)
    oxygen_pp_line3 = GLine(carbon_group_center_x + 1, carbon_group_center_y + 61, carbon_group_center_x - 19,
                            carbon_group_center_y + 91)
    oxygen_pp_line4 = GLine(carbon_group_center_x - 1, carbon_group_center_y + 59, carbon_group_center_x - 21,
                            carbon_group_center_y + 89)

    window.add(hydrogen_label)
    window.add(line_hydrogen_to_pp)
    window.add(oxygen1_label)
    window.add(oxygen_pp_line1)
    window.add(oxygen_pp_line2)
    window.add(oxygen2_label)
    window.add(oxygen_pp_line3)
    window.add(oxygen_pp_line4)


def guanine_draw(x, y, window, func=purine_draw):
    func(x, y, window)
    carbon_group_center_x = x + 94
    carbon_group_center_y = y + 90
    line_nh = GLine(carbon_group_center_x + 89, carbon_group_center_y - 26, carbon_group_center_x + 104,
                    carbon_group_center_y - 51)
    line_nh1 = GLine(carbon_group_center_x + 91, carbon_group_center_y - 24, carbon_group_center_x + 106,
                     carbon_group_center_y - 49)
    oxygen1_label = GLabel("O", x=carbon_group_center_x + 107, y=carbon_group_center_y - 48)
    line_nh2 = GLine(carbon_group_center_x + 125, carbon_group_center_y + 4, carbon_group_center_x + 145,
                     carbon_group_center_y + 4)
    for i in range(0, 50, 5):
        line_link1 = GLine(carbon_group_center_x + 123 + i, carbon_group_center_y - 60, carbon_group_center_x + 125 + i,
                           carbon_group_center_y - 60)
        window.add(line_link1)
    nitrogen2_label = GLabel("N", x=carbon_group_center_x + 112, y=carbon_group_center_y + 15)
    for i in range(0, 40, 5):
        line_link2 = GLine(carbon_group_center_x + 163 + i, carbon_group_center_y + 4, carbon_group_center_x + 165 + i,
                           carbon_group_center_y + 4)
        window.add(line_link2)
    hydrogen_label = GLabel("H", x=carbon_group_center_x + 147, y=carbon_group_center_y + 15)
    nitrogen3_label = GLabel("N", x=carbon_group_center_x + 107, y=carbon_group_center_y + 80)
    line_nitrogen3 = GLine(carbon_group_center_x + 90, carbon_group_center_y + 30, carbon_group_center_x + 105,
                           carbon_group_center_y + 60)
    line_nh3 = GLine(carbon_group_center_x + 125, carbon_group_center_y + 70, carbon_group_center_x + 145,
                     carbon_group_center_y + 70)
    for i in range(0, 40, 5):
        line_link3 = GLine(carbon_group_center_x + 163 + i, carbon_group_center_y + 70, carbon_group_center_x + 165 + i,
                           carbon_group_center_y + 70)
        window.add(line_link3)
    hydrogen2_label = GLabel("H", x=carbon_group_center_x + 147, y=carbon_group_center_y + 80)

    window.add(line_nh)
    window.add(line_nh1)
    window.add(line_nh2)
    window.add(oxygen1_label)
    window.add(nitrogen2_label)
    window.add(hydrogen_label)
    window.add(nitrogen3_label)
    window.add(line_nitrogen3)
    window.add(line_nh3)
    window.add(hydrogen2_label)


def cytosine_antisense_draw(x, y, window, func=pyrimidine_antisense_draw):
    func(x, y, window)
    carbon_group_center_x = x
    carbon_group_center_y = y
    nitrogen_label = GLabel("N", x=carbon_group_center_x - 35, y=carbon_group_center_y + 42)
    nitrogen2_label = GLabel("N", x=carbon_group_center_x - 30, y=carbon_group_center_y - 20)
    oxygen_pp_line = GLine(carbon_group_center_x - 17, carbon_group_center_y - 24, carbon_group_center_x - 1,
                           carbon_group_center_y + 1)
    hydrogen1_label = GLabel("H", x=carbon_group_center_x - 70, y=carbon_group_center_y - 20)
    # the oxygen atom above pp
    oxygen2_label = GLabel("O", x=carbon_group_center_x - 32, y=carbon_group_center_y + 107)
    oxygen_pp_line3 = GLine(carbon_group_center_x + 1, carbon_group_center_y + 61, carbon_group_center_x - 19,
                            carbon_group_center_y + 91)
    oxygen_pp_line4 = GLine(carbon_group_center_x - 1, carbon_group_center_y + 59, carbon_group_center_x - 21,
                            carbon_group_center_y + 89)
    line_nitrogen_to_hydrogen = GLine(carbon_group_center_x - 55, carbon_group_center_y - 30,
                                      carbon_group_center_x - 35, carbon_group_center_y - 30)

    window.add(nitrogen_label)
    window.add(nitrogen2_label)
    window.add(oxygen_pp_line)
    window.add(hydrogen1_label)
    window.add(oxygen2_label)
    window.add(oxygen_pp_line3)
    window.add(oxygen_pp_line4)
    window.add(line_nitrogen_to_hydrogen)


def stancode_label(x, y, window):
    stan = GLabel("stan", x=x + 185, y=y + 405)
    stan.font = '-30-italic'
    window.add(stan)
    for i in range(0, 500, 10):
        j = float(i)
        code = GLabel("Code", x=x + 260 + j / 100, y=y + 400 + j / 100)
        code.color = 'grey'
        code.font = '-30'
        window.add(code)
    code = GLabel("Code", x=x+259, y=y+400)
    code.color = "red"
    code.font = '-30'
    window.add(code)


if __name__ == '__main__':
    main()
