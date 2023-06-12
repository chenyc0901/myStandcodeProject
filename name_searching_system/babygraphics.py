"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    line_interval = (width - 2*GRAPH_MARGIN_SIZE)/len(YEARS)
    return GRAPH_MARGIN_SIZE + line_interval*int(year_index)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH,index)
        canvas.create_line(x, 0, x,CANVAS_HEIGHT , width=LINE_WIDTH)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,anchor=tkinter.NW, text=YEARS[index])


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    y_unit = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/(1000-1)
    counter = 0
    for name in lookup_names:
        color = COLORS[counter % len(COLORS)]
        counter += 1
        if name in name_data:
            # 一次處理兩年，並把第一年的文字處理在圖上
            for index in range(len(YEARS)-1):
                year1 = str(YEARS[index])
                year2 = str(YEARS[index+1])
                if year1 in name_data[name]:
                    x1 = get_x_coordinate(CANVAS_WIDTH, index)
                    y1 = GRAPH_MARGIN_SIZE + (int(name_data[name][year1])-1)*y_unit \
                        if int(name_data[name][year1]) < 1000 else GRAPH_MARGIN_SIZE + 999*y_unit
                    canvas.create_text(x1, y1, fill=color, anchor=tkinter.SW, text=f'{name} {name_data[name][year1]}')
                else:
                    x1 = get_x_coordinate(CANVAS_WIDTH, index)
                    y1 = GRAPH_MARGIN_SIZE + 999*y_unit
                    canvas.create_text(x1, y1, fill=color, anchor=tkinter.SW, text=f'{name} *')
                if year2 in name_data[name]:
                    x2 = get_x_coordinate(CANVAS_WIDTH, index+1)
                    y2 = GRAPH_MARGIN_SIZE + (int(name_data[name][year2]) - 1) * y_unit \
                        if int(name_data[name][year2]) < 1000 else GRAPH_MARGIN_SIZE + 999 * y_unit
                else:
                    x2 = get_x_coordinate(CANVAS_WIDTH, index+1)
                    y2 = GRAPH_MARGIN_SIZE + 999 * y_unit
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
                # 處理最後一年的文字問題
                if int(year2) == YEARS[-1] and year2 in name_data[name] and int(name_data[name][year2]) < 1000:
                    canvas.create_text(x2, y2, fill=color, anchor=tkinter.SW, text=f'{name} {name_data[name][year2]}')
                elif int(year2) == YEARS[-1]:
                    canvas.create_text(x2, y2, fill=color, anchor=tkinter.SW, text=f'{name} *')


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
