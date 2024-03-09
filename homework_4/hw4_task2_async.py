import asyncio
import os.path
import sys
import aiohttp
import time

start = time.time()
urls = ['https://images.wallpaperscraft.ru/image/single/mashina_seryj_mokryj_147750_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/mustang_gt_mustang_avtomobil_1191100_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/audi_avtomobil_temnyj_981178_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/chevrolet_camaro_z28_chevrolet_avtomobil_1185511_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/avtomobil_kabriolet_fioletovyj_1185415_1280x720.jpg']


async def save_img(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pic = await response.content.read()
            if not os.path.exists('pictures'):
                os.mkdir('pictures')
            name = 'pictures/async_' + url.split('https://')[1].split('/')[-1]
            with open(name, 'wb') as f:
                f.write(pic)


async def main():
    global urls
    tasks = []
    for url in urls:
        task = asyncio.create_task(save_img(url))
        tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':

    urls = [*sys.argv[1:]]
    asyncio.run(main())
    print(f'Time: {time.time() - start:2f} sec.')