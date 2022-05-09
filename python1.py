import curses, random

screen  = curses.initscr()
width   = screen.getmaxyx()[1]
height  = screen.getmaxyx()[0]
size    = width*height
b       = 0

curses.curs_set(0)
curses.start_color()
curses.init_pair(1,0,0)
curses.init_pair(2,7,0)
screen.clear

while 1:
    try:
        b = (b + 1)%2
        screen.addstr(  (random.randint(0,height))%height,
                        (random.randint(0,width))%width,
                        '■',
                        curses.color_pair(b))

        screen.timeout(10)
        screen.refresh()
        if (screen.getch()!=-1):
            break
    except:
        pass

curses.endwin()
