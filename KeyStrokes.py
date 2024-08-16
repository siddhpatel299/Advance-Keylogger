from pynput.keyboard import Key, Listener

sentence = []
count = 0
def ON_PRESS(key):
    global sentence
    global count

    if key == Key.backspace: count+=1
    elif count!=0:
        sentence.append(str(count) + ' * Backspaces')
        count = 0
    else: 
        if key == Key.space: sentence.append(" ")
        elif key == Key.enter: sentence.append("\n")
        else: sentence.append(key)
        
def ON_RELEASE(key):
    if key == Key.esc:
        return False
    
    
    print(sentence)
    
with Listener(on_press=ON_PRESS, on_release=ON_RELEASE) as listner:
    listner.join()