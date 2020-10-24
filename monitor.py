from pynput import mouse, keyboard
import time
import sys
from contextlib import redirect_stdout
from getkey import getkey, keys

FILEPATH = 'mouse_log.txt'
t_start = 0.0
t_end = 0.0
delta_t = 0.0

mouse_time_end = 0.0
mouse_initial = 0.0

action = []  # for keyboard


def redirect(filePath, val):
    with open(filePath, 'a') as out:
        with redirect_stdout(out):
            print(val)


def on_move(x, y):
    global mouse_initial
    mouse_time_end = time.time()
    meas_time = mouse_time_end - mouse_initial
    print(f'{meas_time}, {x}, {y}, Moved')
    redirect(FILEPATH, f'{meas_time}, {x}, {y}, Moved')


def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    global mouse_initial
    mouse_time_end = time.time()
    meas_time = mouse_time_end - mouse_initial
    print('{}, {}, {}, {}'.format(meas_time, x, y,
                                  'Pressed' if pressed else 'Released'))
    redirect(FILEPATH, '{}, {}, {}, {}'.format(meas_time, x, y,
                                               'Pressed' if pressed else 'Released'))
    # if getkey(blocking = False) == 'ESC':
    #     # Stop listener
    #     return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))


def on_press(key):
    global t_start
    try:
        t_start = time.time()
        print('alphanumeric key {0} pressed'.format(key.char))
        action.append('alphanumeric key {0} pressed\n'.format(key.char))
    except AttributeError:
        t_start = time.time()
        print('special key {0} pressed'.format(key))
        action.append('special key {0} pressed\n'.format(key))


def on_release(key):
    global t_end, delta_t
    t_end = time.time()
    delta_t = t_end - t_start
    # print('fuck')
    print('{0} released'.format(key))
    print(f'duration = {delta_t}')
    action.append('{0} released\n'.format(key))
    action.append(f'duration = {delta_t:4f}\n\n')
    if key == keyboard.Key.esc:
        # Stop listener
        with open('keyboard.log', 'w') as fh:
            fh.writelines(action)
        # mouse.Listener.stop(listener)
        print('Collect data ends!')
        return False


# Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# ...or, in a non-blocking fashion:
# if __name__ == '__main__':
def main():
    global mouse_initial
    print('Press letter "S" to start collecting data')
    mouse_initial = time.time()
    # clear the mouse data
    with open('mouse_log.txt', 'w') as f:
        f.write('\n')
    # Collect events until released
    while True:
        k = getkey()
        if k == 's' or 'S':
            break
        # time.sleep(1)

    global listener
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click)
    listener.start()
    # while True:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as key_listener:
        key_listener.join()
        # k = None
        # k = getkey(blocking = True)
        # if keys.name(k) == "ESC":
        #     mouse.Listener.stop(listener)
        #     print('Collect data ends!')
        #     return


main()
