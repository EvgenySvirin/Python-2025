from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import math
from integrate import integrate

if __name__ == "__main__":
    cpu_num = 16
    with open("../artifacts/2/bench_executors.txt", "w") as file:
        for executor_class in (ThreadPoolExecutor, ProcessPoolExecutor):
            for n_jobs in range(1, 2 * cpu_num + 1):
                file.write(f"Start bench {executor_class.__name__} n_jobs = {n_jobs}\n")

                executor = executor_class(n_jobs)
                start_time = time.time()
                result = integrate(f=math.cos, a=0, b=math.pi / 2, executor=executor, n_jobs=n_jobs)
                end_time = time.time()
                executor.shutdown()

                exact_value = 1.0
                eps = 0.005
                diff = abs(result - exact_value)
                if eps < diff:
                    file.write(f"ERROR: calculation went wrong, difference is too big: {diff}\n")
                file.write(f"End bench  {end_time - start_time:.4f} sec, result = {result:.4f}\n")


