from pynput import mouse
import time
import sys
from contextlib import redirect_stdout

FILEPATH = 'log.txt'

def redirect(filePath, val):
    with open(filePath, 'a') as out:
        with redirect_stdout(out):
            print(val)

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))
    redirect(FILEPATH, 'Pointer moved to {0}'.format((x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    redirect(FILEPATH, '{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:
if __name__ == '__main__':

    # clear the data
    with open('log.txt', 'w') as f:
        f.write('\n')
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()
    while True:
        time.sleep(1)
        if input() == 'q' or 'Q':
            mouse.Listener.stop(listener)
            print('Collect data ends!')
            break

          
