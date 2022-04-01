import curses
from curses import wrapper


# stdscr stands for STD screen, which is
# `Standard Output Screen`
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr(0, 0, "Hello World !", curses.color_pair(1))
    stdscr.refresh()
    key = stdscr.getkey()
    print(key)


wrapper(main)
