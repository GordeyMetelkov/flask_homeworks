import random
import threading
import time


my_arr = [random.randint(1, 100) for _ in range(10001)]
threads = []
el_sum = 0
start = time.time()
print(my_arr)
def my_sum(item1):
    global el_sum
    el_sum += item1

def main(arr: list):
    for i in arr:
        thread = threading.Thread(target=my_sum, args=[i])
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()

if __name__ == '__main__':
    main(my_arr)
    print(el_sum)
    print(f'Time: {time.time() - start:2f} sec')