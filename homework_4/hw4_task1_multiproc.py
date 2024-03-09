import multiprocessing
import random
import time

el_sum = 0
my_arr = [random.randint(1, 100) for _ in range(101)]
processes = []
start = time.time()


def my_sum(item1):
    global el_sum
    el_sum += item1

def main(my_arr: list):
    for i in my_arr:
        process = multiprocessing.Process(target=None, args=[my_sum(i)])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    main(my_arr)
    print(el_sum)
    print(f'Time: {time.time() - start:2f} sec')
