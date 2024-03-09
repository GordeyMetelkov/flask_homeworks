import random
import asyncio
import time


my_arr = [random.randint(1, 100) for _ in range(10001)]
el_sum = 0
start = time.time()


async def my_sum(item1):
    global el_sum
    el_sum += item1

async def main(arr: list):
    for i in arr:
        await my_sum(i)

if __name__ == '__main__':
    asyncio.run(main(my_arr))
    print(f'Time: {time.time() - start:2f} sec')
    print(el_sum)