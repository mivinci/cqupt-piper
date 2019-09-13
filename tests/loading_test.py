from sys import stdout
from time import sleep


frames = ['[=   ]', '[ =  ]', '[  = ]', '[   =]']

def loading_print(msg: str):
    for frame in frames:
        print(frame, msg)
        stdout.write("\033[F")  # Cursor up one line
        sleep(0.5)


loading_print("login")
