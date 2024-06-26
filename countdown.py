import time


def countdown(seconds):
    while True:
        print(seconds, end='\r', flush=True)
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            print("Time's up!")
            break


countdown(10)
