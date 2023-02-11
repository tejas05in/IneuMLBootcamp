import multiprocessing
import time
import random
from datetime import datetime

def process_1():
    print("Process 1 start time {}".format(datetime.now()))
    time.sleep(random.randint(1,5))
    print("Process 1 end time {}".format(datetime.now()))

def process_2():
    print("Process 2 start time {}".format(datetime.now()))
    time.sleep(random.randint(1,5))
    print("Process 2 end time {}".format(datetime.now()))

def process_3():
    print("Process 3 start time {}".format(datetime.now()))
    time.sleep(random.randint(1,5))
    print("Process 3 end time {}".format(datetime.now()))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=process_1)
    p2 = multiprocessing.Process(target=process_2)
    p3 = multiprocessing.Process(target=process_3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()