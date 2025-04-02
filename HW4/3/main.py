from multiprocessing import Queue, Process
from process_routines import process_a_routine, process_b_routine
from datetime import datetime
import select
import sys

if __name__ == "__main__":
    in_queue_a = Queue()
    in_queue_b = Queue()
    in_queue_main = Queue()

    process_a = Process(target=process_a_routine, args=(in_queue_a, in_queue_b))
    process_b = Process(target=process_b_routine, args=(in_queue_b, in_queue_main))

    process_a.start()
    process_b.start()

    try:
        while True:
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                message = input()
                if message == "quit":
                    break
                print(f"{datetime.now()}: Main process got stdin input: {message}")
                in_queue_a.put(message)

            if not in_queue_main.empty():
                encoded_message = in_queue_main.get()
                print(f"{datetime.now()}: Main process got encoded message: {encoded_message}")
    except EOFError:
        print("Main process got stdin EOF")
    finally:
        process_a.terminate()
        process_b.terminate()
