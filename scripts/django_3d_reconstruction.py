import datetime
import threading
import time
from termcolor import colored
import signal
import os
import pause

stop = False

def signal_handler(signal, frame):
    global stop
    print_str = '[] Ctrl+C KeyboardInterupt'
    print(colored(print_str, 'yellow', attrs=['bold']))
    stop = True

def job():
    while not stop:
        pause_time = datetime.datetime.now().replace(hour=1, minute=30, second=0, microsecond=0) \
                     + datetime.timedelta(days=1)
        print(pause_time)
        pause.until(pause_time)

        os.system('./generate_and_copy_file_to_django_dir.sh')


if __name__ == '__main__':

    t = threading.Thread(target = job)
    t.start()

    print(colored('[BACKUP LOG] Thread process starts', 'yellow', attrs=['bold']))

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
