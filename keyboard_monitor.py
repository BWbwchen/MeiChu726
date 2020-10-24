from pynput import keyboard
import time

t_start = 0.0
t_end = 0.0
delta_t = 0.0

action = []


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
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
