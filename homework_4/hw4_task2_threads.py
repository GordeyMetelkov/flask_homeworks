import os
import sys
import time
import requests
import threading


start = time.time()
urls = ['https://images.wallpaperscraft.ru/image/single/mashina_seryj_mokryj_147750_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/mustang_gt_mustang_avtomobil_1191100_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/audi_avtomobil_temnyj_981178_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/chevrolet_camaro_z28_chevrolet_avtomobil_1185511_1280x720.jpg',
        'https://images.wallpaperscraft.ru/image/single/avtomobil_kabriolet_fioletovyj_1185415_1280x720.jpg']
threads = []
def save_img(url):
    pic = requests.get(url)
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    name = 'pictures/thrds_' + url.split('https://')[1].split('/')[-1]
    with open(name, 'wb') as f:
        f.write(pic.content)

def main():
    for url in urls:
        thread = threading.Thread(target=save_img, args=[url])
        threads.append(thread)
        thread.start()

if __name__ == '__main__':

    for thread in threads:
        thread.join()

    urls = [*sys.argv[1:]]
    main()
    print(f'Time: {time.time() - start:2f} sec.')
