import curses, random

screen  = curses.initscr()
width   = screen.getmaxyx()[1]
height  = screen.getmaxyx()[0]
size    = width*height
char    = [" ", "■"]
b       = []

curses.curs_set(0)
curses.start_color()
curses.init_pair(1,0,0)
curses.init_pair(2,7,0)
screen.clear

for i in range(size+width+1): b.append(0)

while 1:
        for i in range(int(width/9)):
            b[int((random.random()*width)+width*(height-1))]=65
        
        
        for i in range(size):
                b[i]=int((b[i]+b[i+1]+b[i+width]+b[i+width+1])/4)
                color=(0 if b[i]>1 else b[i])
                if(i<size-1):
                    screen.addstr(  int(i/width),
                                    i%width,
                                    char[(1 if b[i]>1 else b[i])],
                                    curses.color_pair(color))
        
        screen.refresh()
        screen.timeout(30)
        if (screen.getch()!=-1): break

curses.endwin()
