import os
import sys
import requests
import multiprocessing
import time

start = time.time()
urls = ['https://images.wallpaperscraft.ru/image/single/mashina_seryj_mokryj_147750_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/mustang_gt_mustang_avtomobil_1191100_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/audi_avtomobil_temnyj_981178_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/chevrolet_camaro_z28_chevrolet_avtomobil_1185511_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/avtomobil_kabriolet_fioletovyj_1185415_1280x720.jpg']
processes = []
def save_img(url):
    pic = requests.get(url)
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    name = 'pictures/mltproc_' + url.split('https://')[1].split('/')[-1]
    with open(name, 'wb') as f:
        f.write(pic.content)

def main():
    for url in urls:
        process = multiprocessing.Process(target=save_img, args=[url])
        processes.append(process)
        process.start()

if __name__ == '__main__':

    urls = [*sys.argv[1:]]
    for process in processes:
        process.join()

    main()
    print(f'Time: {time.time() - start:2f} sec.')
