import time
from codecs import encode
from multiprocessing import Queue

def process_a_routine(in_queue: Queue,
                      out_queue: Queue):
    while True:
        if not in_queue.empty():
            message = in_queue.get()
            out_queue.put(message.lower())
            time.sleep(5)


def process_b_routine(in_queue: Queue,
                      out_queue: Queue):
    while True:
        if not in_queue.empty():
            message = in_queue.get()
            out_queue.put(encode(message, "rot_13"))

