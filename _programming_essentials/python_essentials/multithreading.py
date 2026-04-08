import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

#Normal Code
time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()
print(time2-time1)
#Code using threads
time1 = time.perf_counter()

t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()

print(time2-time1)
time1 = time.perf_counter()
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 4)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 1)
        print(future1.result())
        print(future2.result())
        print(future3.result())

poolingDemo()

time2 = time.perf_counter()

print(time2-time1)

















