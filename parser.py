from tkinter.tix import Tree
import requests
from bs4 import BeautifulSoup as BS
import os


file1 = open("linqs.txt", "r")
count = 0
while True:
    line = file1.readline()
    if not line:
        break
    req = requests.get(line.strip(), stream=True)
    if req.status_code==200:
        with open(f'dowloadsImages/tree.{count}.jpg','wb') as imgfile:
            imgfile.write(req.content)
    count +=1
    print(count)
print("FINISHED")
file1.close

#page = 0

#file = open('linqs.txt', 'w')

#while page != 50:
    #r = requests.get(f"https://ru.wallpaper.mob.org/gallery/tag=derevya/{page}/")
    #html = BS(r.content, 'html.parser')
    #for el in html.select('.image-gallery-image__inner'):
        #file.write(el.select('img')[0]['src'] + '\n')
        #print(el.select('img')[0]['src'])
    #page += 1
#file.close()



#while page != 6:
#    r = requests.get(
#       f"https://www.kartinki24.ru/kartinki/derevya/fotopage/{page}/")
#    html = BS(r.content, 'html.parser')
#    for el in html.select('.imgcat'):
#        imgLinq = el.select('.imgcat > a')
#        img = imgLinq[0].select('img')[0]
#        print(f"https://www.kartinki24.ru{img['src']}")   #https://www.kartinki24.ru/uploads/gallery/thumb/366/kartinki24_ru_trees_190.jpg
#    page += 1