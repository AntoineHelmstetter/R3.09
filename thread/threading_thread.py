import threading
import requests
import time

def download_image(img_url):
    img_bytes=requests.get(img_url).content
    img_name=img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

img_urls=['https://pixabay.com/get/g9ea18db98bacb7eac69ffaa965c59d09cf88cab5088bb863bf45c87def3e28f5270a18d7939d3072f20880fda4e25435a57b2a21a949a28315793911c6a7cfae6f313c82f747c77df8aaa7a33fab95de_1920.jpg'
,'https://pixabay.com/get/gf5b466414705d4a688cea66ac0a69925b5df16a86435d2c410e818b57a36765ed70232b628d4ccfbab3df4fdd2958eb346361392504e35f89db9cea9f86b8c878021e0e06aa7ebc7ac00bc48bd11ecbc_1920.jpg'
,'https://pixabay.com/get/gce0b9c9fd06f17ef3612654c93d715171323425ad06fe17856bf35a1300bca4075f7f5012e695322789980a4924f4db353dd762dfacdfc0459c55f38a3fcf9dc12c948175ebca64c312375989b4b8a70_1920.png']


start=time.perf_counter()
t1 = threading.Thread(target=download_image, args=(img_urls[0],))
t1.start()
t2 = threading.Thread(target=download_image, args=(img_urls[1],))
t2.start()
t3 = threading.Thread(target=download_image,args=(img_urls[2],))
t3.start()
t1.join() # j'attends la fin de la thread
t2.join() # j'attends la fin de la thread
t3.join()
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")